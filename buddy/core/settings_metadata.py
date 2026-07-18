# settings metadata\descriptions  is stored here for future use, but it can be useful for providing descriptions or metadata for settings in the future.
"""
settings_metadata.py

Contains metadata for Buddy AI settings.

This module stores information ABOUT each setting
(display names, descriptions, types, etc.).

It does NOT store user preferences.
User preferences are stored in settings.json.

Responsibilities:
- Display names
- Descriptions
- Data types

This metadata is used by the Settings UI.
"""

SETTINGS_METADATA = {
    "show_version": {
        "display_name": "Show Version",
        "description": "Display the current Buddy AI version during startup.",
        "type": bool,
    },

    "show_time": {
        "display_name": "Show Time",
        "description": "Display the current system time during startup.",
        "type": bool,
    },

    "auto_greet": {
        "display_name": "Auto Greet",
        "description": "Automatically greet the user when Buddy AI starts.",
        "type": bool,
    },
}