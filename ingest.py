from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

with open("meetings.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()


meetings = raw_text.split("\n\n---\n\n")

documents = []

for meeting in meetings:
    if "Transcript:" not in meeting:
        continue

    documents.append(Document(page_content=meeting.strip()))

print(f"Total meetings loaded: {len(documents)}")


splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

docs = splitter.split_documents(documents)

print(f"Total chunks before filtering: {len(docs)}")

filtered_docs = []

for doc in docs:
    text = doc.page_content.strip()

 
    if len(text) < 100:
        continue

    if text.lower().startswith("transcript:") and len(text) < 150:
        continue

    filtered_docs.append(doc)

docs = filtered_docs

print(f"Chunks after filtering: {len(docs)}")


# print(f"Using chunks: {len(docs)}")


print("\nSAMPLE CHUNK:\n")
print(docs[0].page_content[:500])


embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2",
    encode_kwargs={"batch_size": 32}
)

print("\nStarting embedding...")

db = Chroma.from_documents(
    docs,
    embedding,
    persist_directory="db"
)

print("\nStored successfully in Chroma DB")