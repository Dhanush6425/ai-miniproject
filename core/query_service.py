from core.engine import run_query
from utils.helper import clean_response
from datetime import datetime

def handle_query(query, query_type, top_k, db, llm, session):

    selected = session.selected_meeting

    if selected == "ALL":
        # Fetch from ALL indexed meetings — no filter
        retriever = db.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": top_k,
                "fetch_k": 20,
            }
        )
    else:
        # Fetch only from the selected meeting
        retriever = db.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": top_k,
                "fetch_k": 10,
                "filter": {"meeting_id": selected}
            }
        )

    raw_response, context = run_query(
        query, query_type, top_k, retriever, llm, session
    )

    cleaned = clean_response(raw_response)

    entry = {
        "question": query,
        "answer": cleaned,
        "context": context,
        "query_type": query_type,
        "timestamp": datetime.now().strftime("%I:%M %p"),
        "meeting_id": selected
    }

    return entry