from buddy.core.status import Status
from buddy.memory.storage_manager import save_json, load_json
from buddy.core.settings_metadata import SETTINGS_METADATA


DEFAULT_SETTINGS = {
    "show_version": True,
    "show_time": True,
    "auto_greet": True
}
SETTINGS_FILE="buddy/data/settings.json"

# create default settings file if it doesn't exist
def create_default_settings():
    save_json(SETTINGS_FILE, DEFAULT_SETTINGS)

# load settings function
def load_settings():
    settings = load_json(SETTINGS_FILE)
    if settings is None:
        create_default_settings()
        settings = DEFAULT_SETTINGS
    return settings

# save settings function
def save_settings(settings):
    save_json(SETTINGS_FILE, settings)
    return Status.SUCCESS.value


# change setting function
def change_setting(key, value):
    settings = load_settings()
    if key not in settings:
        return Status.INVALID_KEY.value

    expected_type = SETTINGS_METADATA.get(key, {}).get("type")
    if expected_type is None:
        return Status.INVALID_KEY.value

    if not isinstance(value, expected_type):
        print("sahi data type daal ")
        return Status.INVALID_TYPE.value

    if settings.get(key) == value:
        print("pehle se vahi setting hai bhai 🙄")
        return Status.NO_CHANGE.value

    settings[key] = value
    save_json(SETTINGS_FILE, settings)
    return Status.SUCCESS.value