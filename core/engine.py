# core/engine.py

from core.context import get_uploaded_context

def run_query(query, query_type, top_k, retriever, llm, session):
    
    # ---------- CONTEXT ----------
    if session.get("upload_mode") and session.get("uploaded_meetings"):
        context = get_uploaded_context(
            query,
            session.get("selected_meeting", "All Meetings"),
            session.get("uploaded_meetings"),
            top_k
        )
    else:
        docs = retriever.invoke(query)
        context = "\n\n".join([d.page_content for d in docs])

    # ---------- PROMPT ----------
    prompt = f"""
You are an AI assistant for meeting analysis.

IMPORTANT:
- If the question is casual → respond normally
- If meeting-related → use ONLY context

Query Type: {query_type}

Rules:
- Action items → bullet points
- Summary → topics + decisions + actions
- Decisions → list only
- Do NOT hallucinate

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content, context