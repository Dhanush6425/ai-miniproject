import hashlib
from core.meeting_store import process_and_store_meeting
from data.metadata import save_metadata

def handle_meeting_save(file_bytes, meeting_name, db, session):

    file_hash = hashlib.md5(file_bytes).hexdigest()

    if "file_meeting_map" not in session:
        session.file_meeting_map = {}

    if "meeting_names" not in session:
        session.meeting_names = {}

    # REPLACE
    if file_hash in session.file_meeting_map:
        meeting_id = session.file_meeting_map[file_hash]

        db._collection.delete(where={"meeting_id": meeting_id})

    else:
        meeting_id = f"Meeting_{len(session.meetings) + 1}"
        session.meetings.append(meeting_id)

    process_and_store_meeting(
        file_bytes.decode("utf-8"),
        db,
        meeting_id
    )

    session.file_meeting_map[file_hash] = meeting_id
    session.meeting_names[meeting_id] = meeting_name

    save_metadata(session.meeting_names)

    return meeting_id, file_hash