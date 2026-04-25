import pandas as pd

INPUT_FILE = "test_df.csv"
OUTPUT_FILE = "meetings.txt"

df = pd.read_csv(INPUT_FILE)
df.columns = df.columns.str.strip()

print("Columns:", df.columns)

documents = []

for _, row in df.iterrows():
    transcript = str(row.get("Transcript", "")).strip()

    if transcript == "" or transcript.lower() == "nan":
        continue

    transcript = transcript.replace("\n", " ")
    transcript = " ".join(transcript.split())

    meeting_id = row.get("Meeting_UID", "Unknown")
    date = row.get("Date", "Unknown")

    text = f"""
Transcript:
{transcript}

Meeting ID: {meeting_id}
Date: {date}
"""

    documents.append(text)

print(f"Documents created: {len(documents)}")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n\n---\n\n".join(documents))

print("Saved successfully!")