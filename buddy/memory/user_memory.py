# user data is stored here
from buddy.memory.storage_manager import save_json


def save_user_data(name, age):
    user_data = {
        "name": name,
        "age": age
    }
    save_json("buddy/data/user.json", user_data)