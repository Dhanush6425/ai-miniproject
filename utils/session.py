import streamlit as st

def init_session():
    defaults = {
        "history": [],
        "meeting_names": {},   # meeting_id → meeting_name
        "chat_history": [],
        "query": "",
        "bookmarks": [],
        "meetings": [],
        "query_count": 0,
        "uploaded_meetings": {},
        "selected_meeting": "ALL",   # "ALL" or a specific meeting_id
        "upload_mode": False,
        "current_query": None,
        "last_processed_query": None,
        "last_response": None,
        "file_meeting_map": {},
        "saved_hashes": set()
    }

    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val