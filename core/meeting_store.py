from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
import streamlit as st


def process_and_store_meeting(raw_text, db, meeting_id):

    # ---------- SPLITTER ----------
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200,
        chunk_overlap=150
    )

    chunks = splitter.split_text(raw_text)

    # ---------- CREATE DOCUMENTS ----------
    docs = [
        Document(
            page_content=chunk,
            metadata={"meeting_id": meeting_id}
        )
        for chunk in chunks
        if len(chunk.strip()) > 50
    ]

    # ---------- BATCH INSERT (FIX) ----------
    BATCH_SIZE = 500  # safe size

    total = len(docs)

    if total == 0:
        return

    # Optional progress bar (nice UX)
    progress = st.progress(0)

    for i in range(0, total, BATCH_SIZE):
        batch = docs[i:i + BATCH_SIZE]

        db.add_documents(batch)

        # update progress
        progress.progress((i + len(batch)) / total)

    progress.empty()