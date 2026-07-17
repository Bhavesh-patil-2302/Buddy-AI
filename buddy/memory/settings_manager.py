from buddy.memory.storage_manager import save_json, load_json


DEFAULT_SETTINGS = {
    "show_version": True,
    "show_time": True,
    "auto_greet": True
}
SETTINGS_FILE="buddy/data/settings.json"

def create_default_settings():
    save_json(SETTINGS_FILE, DEFAULT_SETTINGS)

def load_settings():
    settings = load_json(SETTINGS_FILE)
    if settings is None:
        create_default_settings()
        settings = DEFAULT_SETTINGS
    return settings
