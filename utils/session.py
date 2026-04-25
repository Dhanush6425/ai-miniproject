import streamlit as st

def init_session():
    defaults = {
        "history": [],
        "chat_history": [],
        "query": "",
        "bookmarks": [],
        "query_count": 0,
        "uploaded_meetings": {},
        "selected_meeting": "All Meetings",
        "upload_mode": False,
        "current_query": None,
        "last_processed_query": None,
        "last_response": None
    }

    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val