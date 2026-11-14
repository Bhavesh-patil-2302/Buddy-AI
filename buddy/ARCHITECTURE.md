# Buddy AI Architecture

## Principles

- One module = One responsibility
- Modular design
- Reusable functions

--------------------------------

main.py

Responsible for

- Program flow
- Menus
- Calling modules

--------------------------------

storage_manager.py

Responsible for

- save_json()
- load_json()

Never knows about users.

--------------------------------

user_memory.py

Responsible for

- save_user_data()
- load_user_data()

Never opens files directly.

--------------------------------

settings_manager.py

Responsible for

- load_settings()
- save_settings()

Only handles settings.

--------------------------------

scanner/

Responsible for

- File scanning

--------------------------------
notes/

- notes_manager.py - handles notes logic such as create, view ,update ,delete and searching queries
- notes_cli - interacts with user ,acts as interface 
- notes.json - notes are saved here in json format with creation time , id , title , content and tags of notes

---------------------------------

## File Manager Module (v1.4.0)

The File Manager is responsible for filesystem operations within Buddy AI.

It provides a modular interface for managing files and directories while separating user interaction, filesystem operations, scanning, filtering, and Trash management.

### Module Structure

```text
buddy/
└── file_manager/
    ├── __init__.py
    ├── file_manager.py
    ├── file_operations.py
    ├── file_scanner.py
    ├── file_filters.py
    ├── trash_manager.py
    └── file_manager_cli.py
```

### Module Responsibilities

| Module | Responsibility |
|---|---|
| `file_manager.py` | Coordinates File Manager functionality |
| `file_operations.py` | Handles copying, moving, renaming, and folder creation |
| `file_scanner.py` | Scans directories and collects file metadata |
| `file_filters.py` | Handles file categorization, filtering, and sorting |
| `trash_manager.py` | Manages Trash, restoration, and permanent deletion |
| `file_manager_cli.py` | Provides the File Manager command-line interface |

### File Operations

The File Manager uses Python's filesystem libraries:

- `pathlib` for path handling.
- `shutil` for copying and moving files and directories.
- `os` for filesystem operations and directory scanning.

Filesystem operations return standardized status values through Buddy's existing status management system.

### File Scanning and Filtering

The scanner collects structured information about directory entries, including:

- Filename
- Path
- File or directory type
- Extension
- Size
- Creation timestamp
- Modification timestamp

The filtering module provides predefined file categories, custom extension filtering, and sorting functionality.

### Trash Architecture

The Trash system separates stored files from their metadata.

```text
buddy/
└── data/
    └── file_manager/
        ├── trash/
        │   └── files/
        └── trash_index.json
```

The Trash index maintains:

- Unique item IDs
- Original file paths
- Stored filenames
- Deletion timestamps
- Next available ID

The Trash Manager handles moving items into Trash, listing stored items, restoring items, and permanent deletion.

### Storage and Error Handling

The File Manager reuses the existing storage manager for JSON persistence.

It also uses the centralized path configuration and status definitions.

Storage validation and filesystem error handling help maintain consistency when operations fail.

### Design Principles

- Separation of concerns.
- Reusable filesystem operations.
- Centralized path management.
- Structured metadata.
- Consistent status reporting.
- Safe handling of destructive operations.
- Minimal coupling between CLI interaction and filesystem logic.