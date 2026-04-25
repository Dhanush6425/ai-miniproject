import re


def parse_meetings_from_text(raw_text: str) -> dict:

    # 1️⃣ Try clean separator
    parts = raw_text.split("\n\n---\n\n")

    # 2️⃣ Fallback: flexible dash separator
    if len(parts) == 1:
        parts = re.split(r"\n\s*-{3,}\s*\n", raw_text)

    # 3️⃣ Fallback: detect "Meeting" keywords
    if len(parts) == 1:
        parts = re.split(r"\n(?=Meeting\s+\d+)", raw_text)

    # 4️⃣ Fallback: speaker/timestamp-based split
    if len(parts) == 1:
        parts = re.split(r"\n(?=Speaker\s+\d+:|\d{2}:\d{2})", raw_text)

    meetings = {}

    for i, part in enumerate(parts):
        part = part.strip()
        if not part:
            continue

        meetings[f"Meeting {i+1}"] = part

    # 5️⃣ Final fallback
    if not meetings:
        return {"Full Document": raw_text}

    return meetings