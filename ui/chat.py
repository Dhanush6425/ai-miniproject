# ui/chat.py

import streamlit as st

def save_bookmark(entry):
    st.session_state.bookmarks.append(entry)


def render_chat(chat_history):
    for idx, entry in enumerate(chat_history):

        already = any(
            b["question"] == entry["question"]
            for b in st.session_state.bookmarks
        )

        st.markdown(f"**Question: {entry['question']}**")
        st.markdown("\n".join(entry["answer"]))
        st.caption(entry["timestamp"])

        st.button(
            "✅" if already else "🔖",
            key=f"bookmark_{idx}",
            on_click=save_bookmark,
            args=(entry,),
            disabled=already
        )

        st.divider()