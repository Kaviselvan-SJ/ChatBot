from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from backend.graph import chat_app
from PyPDF2 import PdfReader
import io
import google.generativeai as genai
import os

# Configure Gemini
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-2.0-flash-lite")

app = FastAPI()

# ---------- Chat Endpoint ----------
class ChatRequest(BaseModel):
    user_message: str
    thread_id: str

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(req: ChatRequest):
    state = {"messages": [req.user_message]}
    result = chat_app.invoke(state, config={"configurable": {"thread_id": req.thread_id}})
    return ChatResponse(response=result["messages"][-1])


# ---------- Upload & Summarize ----------
@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    content = await file.read()
    text = ""

    # Handle TXT files
    if file.filename.endswith(".txt"):
        text = content.decode("utf-8", errors="ignore")

    # Handle PDF files
    elif file.filename.endswith(".pdf"):
        reader = PdfReader(io.BytesIO(content))
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

    else:
        return {"summary": "⚠️ Unsupported file type."}

    if not text.strip():
        return {"summary": "⚠️ No readable text found in document."}

    # Summarize with Gemini (safe truncate to 6000 chars)
    try:
        response = model.generate_content(f"Summarize this document:\n\n{text[:6000]}")
        summary = response.text.strip()
    except Exception as e:
        summary = f"⚠️ Error: {str(e)}"

    return {"summary": summary}
