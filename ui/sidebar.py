import streamlit as st

def render_sidebar():
    with st.sidebar:

        # ---------- HEADER ----------
        st.markdown("""
            <div class="sidebar-header">
                <div class="sidebar-icon">🎙️</div>
                <div class="sidebar-title">Meeting Summarizer</div>
                <div class="sidebar-subtitle">
                    Your intelligent meeting companion
                </div>
            </div>
        """, unsafe_allow_html=True)

        # ---------- MEETING SELECT (TOP) ----------
        meetings = st.session_state.get("meetings", [])

        if meetings:
            meeting_names = st.session_state.get("meeting_names", {})

            # Build display options with "All Meetings" at top
            named_options = [meeting_names.get(m, m) for m in meetings]
            options = ["🗂️ All Meetings"] + named_options

            selected_name = st.selectbox("📂 Select Meeting", options)

            if selected_name == "🗂️ All Meetings":
                st.session_state.selected_meeting = "ALL"
            else:
                # Map display name → meeting_id
                selected_id = [
                    m for m in meetings
                    if meeting_names.get(m, m) == selected_name
                ][0]
                st.session_state.selected_meeting = selected_id

        else:
            st.info("📥 Upload a meeting to begin")

        st.divider()

        # ---------- SETTINGS ----------
        st.markdown("### ⚙️ Settings")

        query_type = st.selectbox(
            "Query Mode",
            ["Auto", "Summary", "Action Items", "Decisions"],
            key="query_type"
        )

        top_k = st.slider(
            "Context Depth",
            1, 10, 3,
            key="top_k"
        )

        show_context = st.toggle(
            "Show Source Context",
            value=False,
            key="show_context"
        )

        st.divider()

        # ---------- QUICK QUERIES ----------
        st.markdown("### ⚡ Quick Queries")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("📌 Actions", use_container_width=True):
                st.session_state.query = "What are the action items?"

            if st.button("📋 Decisions", use_container_width=True):
                st.session_state.query = "What decisions were made?"

        with col2:
            if st.button("📊 Summary", use_container_width=True):
                st.session_state.query = "Summarize the meeting"

            if st.button("👥 Owners", use_container_width=True):
                st.session_state.query = "Who are the owners of each action item?"

        st.divider()

        # ---------- STATS ----------
        st.markdown("### 📈 Session Stats")

        col1, col2 = st.columns(2)
        query_count_placeholder = col1.empty()
        col2.metric("Bookmarks", len(st.session_state.get("bookmarks", [])))

        query_count_placeholder.metric(
            "Queries",
            st.session_state.get("query_count", 0)
        )

        st.divider()

        # ---------- BOOKMARKS ----------
        bookmarks = st.session_state.get("bookmarks", [])

        if bookmarks:
            st.markdown("### 🔖 Bookmarks")

            for i, bm in enumerate(bookmarks):
                with st.expander(f"Q: {bm['question'][:40]}…"):
                    for line in bm["answer"]:
                        st.markdown(f"- {line}")

                    if st.button("🗑️ Remove", key=f"del_bm_{i}"):
                        st.session_state.bookmarks.pop(i)
                        st.rerun()

        # ---------- RESET ----------
        if st.button("🗑️ Reset Everything", use_container_width=True):
            st.session_state.clear()
            st.rerun()

    return query_type, top_k, show_context, query_count_placeholder