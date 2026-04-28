import json
import os

META_FILE = "meetings.json"

def load_metadata():
    if os.path.exists(META_FILE):
        with open(META_FILE, "r") as f:
            return json.load(f)
    return {}

def save_metadata(data):
    with open(META_FILE, "w") as f:
        json.dump(data, f)