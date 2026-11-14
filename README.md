# Buddy AI Assistant
#  Buddy AI

Buddy AI is my personal AI assistant project built from scratch using Python.

##  Goals

- Learn Python
- Learn Automation
- Build an AI Assistant
- Learn Software Engineering
- Learn AI Integration



## Settings System (v1.2.0)

Buddy AI includes a Settings System that allows users to customize application behaviour through configurable preferences.

### Features

- **Load Settings:** Load user preferences from `settings.json`.
- **Modify Settings:** Change individual settings.
- **Persistent Configuration:** Automatically save modified settings to JSON.
- **Default Values:** Use default settings when preferences are unavailable.
- **Settings Metadata:** Maintain metadata for supported settings.
- **Modular Design:** Keep settings management separate from the main application logic.

### Configurable Settings

| Setting | Description |
|---|---|
| `show_version` | Controls whether the application version is displayed in the startup banner. |
| `show_time` | Controls whether Buddy displays the current time during startup. |

### Storage Structure

Settings are stored in a dedicated JSON file:

```text
buddy/
├── core/
│   ├── defaults.py
│   └── settings_metadata.py
│
├── data/
│   └── settings.json
│
└── memory/
    └── settings_manager.py
```

### Settings Data Example

```json
{
    "show_version": true,
    "show_time": true
}
```

### Technical Implementation

- `settings_manager.py` handles loading and modifying settings.
- `storage_manager.py` provides JSON persistence.
- `defaults.py` maintains default configuration values.
- `settings_metadata.py` maintains settings-related metadata.
- `main.py` applies preferences during application startup.

### Goal

The Settings System provides a foundation for customizable application behaviour and makes it easier to introduce additional preferences in future versions.

## Notes System (v1.3.0)

Buddy AI includes a dedicated Notes System that allows users to create, manage, and search personal notes directly through the CLI.

### Features

- **Create Notes:** Create notes with a title, content, and tags.
- **View Notes:** Display saved notes with their details.
- **Update Notes:** Modify existing notes using their IDs.
- **Delete Notes:** Delete notes using their unique IDs.
- **Search Notes:** Search notes by title or content.
- **Tags:** Organize notes using comma-separated tags.
- **Timestamps:** Store the creation date and time of each note.
- **Persistent Storage:** Store notes in a dedicated JSON file.

### Notes Menu

The Notes System provides the following operations:

| Option | Operation |
|---|---|
| 1 | Create Note |
| 2 | View Notes |
| 3 | Delete Note |
| 4 | Update Note |
| 5 | Search Notes |
| 6 | Return to Main Menu |

### Storage Structure

Notes are stored separately from user information and application settings.

```text
buddy/
└── notes/
    ├── notes_manager.py
    ├── notes_cli.py
    └── notes.json
```

### Note Data Structure

Each saved note contains:

```json
{
    "id": 1,
    "title": "My First Note",
    "body": "This is my note content.",
    "tags": [
        "Testing",
        "New-Feature"
    ],
    "created_at": "2026-11-08T15:47:47"
}
```

The `notes.json` file also maintains a `next_id` value for assigning IDs to newly created notes.

## File Manager (v1.4.0)

Buddy AI includes a dedicated File Manager that allows users to manage files and directories through the CLI.

### Features

- **Copy:** Copy files and directories to another location.
- **Move:** Move files and directories.
- **Rename:** Rename files and directories.
- **Create Folders:** Create new directories.
- **File Scanning:** Scan directories and retrieve file information.
- **Sorting:** Sort files by name, size, creation date, and modification date.
- **Filtering:** Filter files by category or custom extensions.
- **Trash System:** Move deleted files and directories into Buddy's Trash instead of permanently deleting them.
- **Restore:** Restore trashed items to their original locations.
- **Permanent Deletion:** Permanently delete selected items from Trash with confirmation.
- **Path Handling:** Support a default workspace and browsing other accessible directories.
- **Filesystem Safety:** Validate paths and handle filesystem errors to protect user data.

### File Categories

The File Manager supports the following predefined categories:

| Category | Supported file types |
|---|---|
| Images | JPG, JPEG, PNG, GIF, BMP, WEBP, SVG, ICO |
| Documents | PDF, DOC, DOCX, TXT, MD, PPT, PPTX, XLS, XLSX, CSV, ODT |
| Code | PY, CPP, C, H, JAVA, JS, TS, HTML, CSS, JSON, SQL, SH, BAT |
| Videos | MP4, MKV, AVI, MOV, WMV, FLV, WEBM |
| Audio | MP3, WAV, FLAC, AAC, OGG, M4A |
| Archives | ZIP, RAR, 7Z, TAR, GZ |

Custom extension filtering is also supported.

### Sorting Options

| Option | Description |
|---|---|
| `name` | Sort alphabetically by filename |
| `size` | Sort by file size |
| `created` | Sort by creation date |
| `modified` | Sort by modification date |

Sorting supports ascending and descending order.

### Trash System

The File Manager uses a dedicated Trash system to protect users from accidental deletion.

- Deleted items are moved into Buddy's Trash.
- Original file paths and deletion timestamps are recorded.
- Each trashed item receives a unique ID.
- Items can be restored using their IDs.
- Permanent deletion requires explicit confirmation.
- Trash metadata is stored separately from trashed files.

### CLI Menu

The File Manager provides the following operations:

| Option | Operation |
|---|---|
| 1 | Copy a file or folder |
| 2 | Move a file or folder |
| 3 | Rename a file or folder |
| 4 | Create a folder |
| 5 | Delete (move to Trash) |
| 6 | View Trash |
| 7 | Restore from Trash |
| 8 | Delete permanently from Trash |
| 9 | List files (sort / filter) |
| 10 | Return to Main Menu |

### Storage Structure

The File Manager uses dedicated storage for Trash files and their metadata.

```text
buddy/
├── file_manager/
│   ├── file_manager.py
│   ├── file_operations.py
│   ├── file_scanner.py
│   ├── file_filters.py
│   ├── trash_manager.py
│   └── file_manager_cli.py
│
└── data/
    └── file_manager/
        ├── trash/
        ├── trash_index.json
        └── operation_history.json
```

The exact storage paths are managed through Buddy's core path configuration.

### Goal

The File Manager provides a foundation for filesystem management within Buddy AI, with an emphasis on modularity, usability, and protecting user data.