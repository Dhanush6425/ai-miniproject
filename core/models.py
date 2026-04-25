from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # go to project root
DB_PATH = BASE_DIR / "db"
load_dotenv(dotenv_path=BASE_DIR / ".env", override=True)

@st.cache_resource
def load_models():
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    db = Chroma(
    persist_directory=str(DB_PATH),
    embedding_function=embedding
    )

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        api_key=api_key
    )

    return db, llm