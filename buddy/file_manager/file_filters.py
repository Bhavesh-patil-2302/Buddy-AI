FILE_CATEGORIES = {
    "images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".ico"},
    "documents": {".pdf", ".doc", ".docx", ".txt", ".md", ".ppt", ".pptx",
                  ".xls", ".xlsx", ".csv", ".odt"},
    "code": {".py", ".cpp", ".c", ".h", ".java", ".js", ".ts", ".html",
             ".css", ".json", ".sql", ".sh", ".bat"},
    "videos": {".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm"},
    "audio": {".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"},
    "archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
}

SORT_OPTIONS = ["name", "size", "created", "modified"]


def filter_by_extensions(entries, extensions):
    # accepts "py" or ".py", in any upper/lower case
    wanted = set()
    for ext in extensions:
        ext = ext.lower()
        wanted.add(ext if ext.startswith(".") else "." + ext)
    return [e for e in entries if e["extension"] in wanted]


def filter_by_category(entries, category):
    return filter_by_extensions(entries, FILE_CATEGORIES[category])


def sort_entries(entries, sort_by="name", descending=False):
    keys = {
        "name": lambda e: e["name"].lower(),
        "size": lambda e: e["size"],
        "created": lambda e: e["created"],
        "modified": lambda e: e["modified"],
    }
    return sorted(entries, key=keys[sort_by], reverse=descending)