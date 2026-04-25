import streamlit as st
from core.parser import parse_meetings_from_text


def handle_upload_ui():
    """Handles upload UI + session state + mode badge"""

    st.markdown("### 📁 Upload Transcript")

    uploaded_file = st.file_uploader("Upload .txt file", type=["txt"])

    # -------- PROCESS FILE --------
    if uploaded_file is not None:
        raw_text = uploaded_file.read().decode("utf-8")
        parsed = parse_meetings_from_text(raw_text)

        if parsed:
            st.session_state.uploaded_meetings = parsed
            st.session_state.upload_mode = True
            st.success(f"Loaded {len(parsed)} meeting(s)")
        else:
            st.warning("No meetings detected")

    # -------- CLEAR BUTTON --------
    if st.session_state.get("upload_mode"):
        if st.button("❌ Clear Upload"):
            st.session_state.upload_mode = False
            st.session_state.uploaded_meetings = {}
            st.session_state.selected_meeting = "All Meetings"
            st.rerun()

    # -------- MODE BADGE --------
    if st.session_state.get("upload_mode"):
        scope = st.session_state.get("selected_meeting", "All Meetings")

        st.markdown(
            f'<span class="upload-badge">🟢 Upload Mode · {scope}</span>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<span class="badge">🔵 Database Mode</span>',
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)