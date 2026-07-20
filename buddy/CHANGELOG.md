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