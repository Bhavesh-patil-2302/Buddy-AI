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
