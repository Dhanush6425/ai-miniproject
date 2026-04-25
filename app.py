import streamlit as st
from core.models import load_models
from core.engine import run_query
from utils.session import init_session
from utils.helper import clean_response
from ui.sidebar import render_sidebar
from ui.style import apply_styles
from ui.chat import render_chat
from core.upload_mode import handle_upload_ui
from datetime import datetime

# ---------- INIT ----------
st.set_page_config(page_title="Meeting Summarizer", layout="wide")
init_session()
apply_styles()

# ---------- SIDEBAR ----------
query_type, top_k, show_context, query_count_placeholder = render_sidebar()

# ---------- MODELS ----------
db, llm = load_models()
retriever = db.as_retriever(
    search_type="mmr",
    search_kwargs={"k": top_k, "fetch_k": 10}
)

# ---------- UI ----------
st.title("🎙️ Meeting Summarizer")
handle_upload_ui()

# ---------- INPUT ----------
query_input = st.chat_input("Ask something...")

if query_input:
    st.session_state.current_query = query_input
elif st.session_state.get("query"):
    st.session_state.current_query = st.session_state.query
    st.session_state.query = ""

query = st.session_state.get("current_query")

if not query:
    st.info("👋 Ask a question or use quick queries")
    st.stop()

# ---------- RUN QUERY ----------
if query != st.session_state.get("last_processed_query"):

    raw_response, context = run_query(
        query, query_type, top_k, retriever, llm, st.session_state
    )

    cleaned = clean_response(raw_response)

    timestamp = datetime.now().strftime("%I:%M %p")

    entry = {
        "question": query,
        "answer": cleaned,
        "context": context,
        "query_type": query_type,
        "timestamp": timestamp
    }

    st.session_state.last_response = entry

    st.session_state.chat_history.append(entry)
    st.session_state.last_processed_query = query
    st.session_state.query_count += 1

    query_count_placeholder.metric("Queries", st.session_state.query_count)

# ---------- DISPLAY ----------
render_chat(st.session_state.get("chat_history", []))

# ---------- CONTEXT ----------
last = st.session_state.get("last_response")

if show_context and last:
    with st.expander("📄 Source Context Used"):
        st.write(last["context"])