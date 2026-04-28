import hashlib
import streamlit as st
from core.models import load_models
from utils.session import init_session
from ui.sidebar import render_sidebar
from ui.style import apply_styles
from ui.chat import render_chat
from ui.popup import meeting_popup
from data.upload_service import handle_meeting_save
from core.query_service import handle_query
from data.metadata import load_metadata

# INIT
st.set_page_config(page_title="Meeting Summarizer", layout="wide")
init_session()
apply_styles()

# LOAD METADATA
data = load_metadata()
st.session_state.meetings = list(data.keys())
st.session_state.meeting_names = data

# SIDEBAR
query_type, top_k, show_context, query_count_placeholder = render_sidebar()

# MODELS
db, llm = load_models()

st.title("🎙️ Meeting Summarizer")

# UPLOAD
uploaded_file = st.file_uploader("📁 Upload Meeting (.txt)", type=["txt"])

if uploaded_file:
    file_bytes = uploaded_file.getvalue()
    file_hash = hashlib.md5(file_bytes).hexdigest()

    already_saved = file_hash in st.session_state.get("saved_hashes", set())
    already_pending = (
        st.session_state.get("temp_hash") == file_hash
        and st.session_state.get("open_dialog")
    )

    if not already_saved and not already_pending:
        st.session_state.temp_file = file_bytes
        st.session_state.temp_hash = file_hash
        st.session_state.open_dialog = True

# POPUP
name, save_clicked, cancel_clicked = meeting_popup(
    st.session_state.get("open_dialog")
)

if save_clicked and name:
    meeting_id, file_hash = handle_meeting_save(
        st.session_state.temp_file, name, db, st.session_state
    )

    if "saved_hashes" not in st.session_state:
        st.session_state.saved_hashes = set()
    st.session_state.saved_hashes.add(st.session_state.temp_hash)

    st.toast(f"✅ {name} added")
    st.session_state.open_dialog = False
    st.rerun()

if cancel_clicked:
    if "saved_hashes" not in st.session_state:
        st.session_state.saved_hashes = set()
    if st.session_state.get("temp_hash"):
        st.session_state.saved_hashes.add(st.session_state.temp_hash)
    st.session_state.open_dialog = False
    st.rerun()

# QUERY
# ---------- INPUT (CHAT + QUICK QUERY) ----------
chat_query = st.chat_input("Ask something...")

if chat_query:
    st.session_state.current_query = chat_query

elif st.session_state.get("query"):
    st.session_state.current_query = st.session_state.query
    st.session_state.query = ""   # clear after use

query = st.session_state.get("current_query")

if query:
    entry = handle_query(query, query_type, top_k, db, llm, st.session_state)

    st.session_state.chat_history.append(entry)
    st.session_state.query_count += 1

    query_count_placeholder.metric("Queries", st.session_state.query_count)

# DISPLAY — show all history when ALL selected, else filter by meeting
selected = st.session_state.get("selected_meeting", "ALL")

if selected == "ALL":
    filtered_chat = st.session_state.chat_history
else:
    filtered_chat = [
        c for c in st.session_state.chat_history
        if c["meeting_id"] == selected
    ]

render_chat(filtered_chat)