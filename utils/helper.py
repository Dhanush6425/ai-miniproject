import re
def clean_response(raw):
    cleaned = []

    for line in raw.split("\n"):
        line = line.strip()

        # Remove only leading bullets/numbers
        line = re.sub(r"^[-•\d+.\s]+", "", line)

        if line:
            cleaned.append(line)

    return cleaned