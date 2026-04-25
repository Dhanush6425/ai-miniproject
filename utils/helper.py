def clean_response(raw):
    cleaned = []

    for line in raw.split("\n"):
        line = line.strip("-•1234567890. ").strip()
        if line:
            cleaned.append(line)

    return cleaned