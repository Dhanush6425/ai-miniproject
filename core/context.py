from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def get_uploaded_context(query, selected, meetings, k):

    if selected == "All Meetings":
        combined = "\n\n---\n\n".join(meetings.values())
    else:
        combined = meetings.get(selected, "")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=150
    )

    docs = splitter.split_documents([Document(page_content=combined)])

    docs = [d for d in docs if len(d.page_content.strip()) >= 100]

    if not docs:
        return combined[:3000]

    query_words = set(query.lower().split())

    def score(doc):
        return len(query_words & set(doc.page_content.lower().split()))

    ranked = sorted(docs, key=score, reverse=True)

    return "\n\n".join(d.page_content for d in ranked[:k])