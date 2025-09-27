# 💬 LangGraph Chatbot

An AI-powered chatbot built with **Streamlit**, **FastAPI**, and **LangGraph** that supports:  
✅ Conversational chat with memory  
✅ Uploading documents (**TXT, PDF**) and summarizing them  
✅ Gemini API integration for responses

---

## 🚀 Features
- Interactive chat interface with history (Streamlit)
- Chat state management with **LangGraph**
- Backend powered by **FastAPI**
- Upload and summarize documents (PDF / TXT)
- **Gemini Flash model** integration for fast responses
- Memory support (conversations stay in context)

---

## 🛠️ Tech Stack
- **Frontend**: [Streamlit](https://streamlit.io/)  
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)  
- **AI Model**: Google Gemini (via `google-generativeai`)  
- **Orchestration**: [LangGraph](https://python.langchain.com/docs/langgraph)  
- **Document Parsing**: PyPDF2 (for PDFs), built-in text reader  

---

## 📂 Project Structure
```
📦 langgraph-chatbot
 ┣ 📂 backend
 ┃ ┣ 📜 main.py        # FastAPI entrypoint
 ┃ ┣ 📜 graph.py       # LangGraph + Gemini model integration
 ┣ 📂 frontend
 ┃ ┣ 📜 app.py        # FastAPI entrypoint
 ┣ 📜 requirements.txt # Python dependencies
 ┣ 📜 README.md        # Project documentation
```

---

## ⚙️ Installation

### 1. Clone repo
```bash
git clone https://github.com/your-username/langgraph-chatbot.git
cd langgraph-chatbot
```

### 2. Create virtual environment
```bash
python -m venv .venv
# Activate virtual environment
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root:
```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Running the Project

### 1. Start Backend (FastAPI)
```bash
python -m uvicorn backend.main:app --reload
```

### 2. Start Frontend (Streamlit)
```bash
streamlit run frontend.py
```

---

## 💡 Usage
- Open the Streamlit UI (usually at [http://localhost:8501](http://localhost:8501))  
- Type messages in the chat input to talk with the bot  
- Click the **+ button** to upload TXT/PDF documents  
- The bot will summarize the document and add the summary to chat  

---

## 📦 Requirements
Example `requirements.txt`:
```
streamlit
fastapi
uvicorn
requests
pydantic
langgraph
google-generativeai
PyPDF2
python-dotenv
```



## 📸 Screenshots (Optional)
