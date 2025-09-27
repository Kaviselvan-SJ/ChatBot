import streamlit as st
import requests
import uuid

st.set_page_config(page_title="LangGraph Chatbot", layout="centered")
st.title("💬 LangGraph Chatbot")

# Store chat history in session
if "history" not in st.session_state:
    st.session_state["history"] = []
if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = str(uuid.uuid4())

# ---------- Chat Input + Upload ----------
col1, col2 = st.columns([8, 1])  # Wide text input, small + button

with col1:
    user_input = st.chat_input("Type your message...")

with col2:
    with st.popover("+"):  # Acts like a plus button with popup
        uploaded_file = st.file_uploader("Upload document", type=["txt", "pdf"])

# ---------- Handle Chat ----------
if user_input:
    st.session_state["history"].append(("You", user_input))

    resp = requests.post(
        "http://127.0.0.1:8000/chat",
        json={"user_message": user_input, "thread_id": st.session_state["thread_id"]}
    )
    bot_reply = resp.json()["response"]

    st.session_state["history"].append(("Bot", bot_reply))

# ---------- Handle File Upload ----------
if uploaded_file is not None:
    with st.spinner("Summarizing document..."):
        resp = requests.post(
            "http://127.0.0.1:8000/upload",
            files={"file": (uploaded_file.name, uploaded_file.getvalue())}
        )
        summary = resp.json()["summary"]
        st.session_state["history"].append(("Bot", f"📄 Document Summary:\n\n{summary}"))

# ---------- Display Chat ----------
for sender, msg in st.session_state["history"]:
    with st.chat_message("user" if sender == "You" else "assistant"):
        st.markdown(msg)
