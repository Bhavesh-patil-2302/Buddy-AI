# Changelog

## v1.1.1

Released:
July 2026

### Added

- Persistent User Memory
- JSON storage
- Returning user detection

### Improved

- Startup flow
- Error handling

### Fixed

- JSONDecodeError crash


---------------------

## v1.0.0

### Added

- Greeting
- Time
- Chrome Launcher
- Universal App Launcher
- Folder Scanner


# Changelog

All notable changes to Buddy AI will be documented in this file.

---

## [v1.2.0] - 20-07-2026

###  Added
- Interactive Settings Menu.
- Dynamic settings display using `SETTINGS_METADATA`.
- Automatic menu numbering with `enumerate()`.
- Dynamic "Back" option.
- Boolean setting toggle support.
- Status-based feedback using the `Status` enum.
- Metadata-driven architecture for settings UI.

###  Architecture
- Moved Settings Menu into `assistants.py`.
- Separated UI from business logic.
- `change_setting()` is now the single API responsible for updating settings.
- Improved dependency direction between modules.
- Settings menu now generates automatically from metadata instead of hardcoded options.

### ⚙ Settings
Current configurable settings:
- Show Version
- Show Time
- Auto Greet

### 🛠 Improved
- Cleaner menu formatting.
- Dynamic mapping between menu options and setting keys.
- Simplified toggle logic.
- Better project modularity.

### 🐞 Fixed
- Fixed setting update logic in `change_setting()`.
- Fixed metadata type lookup.
- Fixed current value comparison.
- Fixed update/save flow.
- Fixed return status handling.
- Fixed menu navigation ("Back" option).
- Fixed function naming issues after refactoring.

### 📂 Project Structure
Settings system now consists of:

```
main.py
    │
    ▼
settings_menu()        (assistants.py)
    │
    ▼
change_setting()       (settings_manager.py)
    │
    ▼
storage_manager.py
    │
    ▼
settings.json
```

---

# v1.3.0 — Notes System
**Release date:** 08 November 2026

### Added
- Introduced a dedicated Notes System.
- Added note creation with title, body, and tags.
- Added functionality to view saved notes.
- Added functionality to update existing notes.
- Added functionality to delete notes using their IDs.
- Added note searching by title and body.
- Added automatic note ID assignment.
- Added creation timestamps for notes.
- Added JSON-based note persistence using `notes.json`.
- Added a dedicated Notes CLI menu.
- Added `NoteStatus` enum to represent note operation results.

### Technical
- Created `buddy/notes/notes_manager.py` for note management.
- Created `buddy/notes/notes_cli.py` for CLI interaction.
- Reused the existing JSON storage manager.
- Added a dedicated notes data file.

### Project
- Completed the v1.3.0 Notes System milestone.

# Changelog

## [1.4.0] - 2026-11-14 - 8.35 PM

### Added
- Introduced a dedicated File Manager module.
- Added file and directory copying.
- Added file and directory moving.
- Added file and directory renaming.
- Added directory creation.
- Added structured directory scanning.
- Added file information retrieval.
- Added sorting by name, size, creation date, and modification date.
- Added predefined file categories for filtering.
- Added custom extension filtering.
- Introduced a dedicated Trash system.
- Added Trash listing functionality.
- Added file and directory restoration.
- Added permanent deletion from Trash with confirmation.
- Added unique Trash item IDs.
- Added original path and deletion timestamp tracking.
- Added dedicated File Manager CLI menu.

### Improved
- Improved filesystem path validation.
- Improved error handling for filesystem operations.
- Improved handling of directory and symbolic-link operations.
- Improved Trash metadata validation and persistence.
- Added safeguards against unsafe directory operations.
- Improved recovery and consistency handling for Trash operations.

### Technical
- Created dedicated modules for file operations, scanning, filtering, Trash management, and CLI interaction.
- Reused the existing status and storage management systems.
- Centralized file categories and sorting options.
- Separated filesystem operations from CLI interaction.

### Project
- Completed the v1.4.0 File Manager milestone.

---

[Previous releases](#)
