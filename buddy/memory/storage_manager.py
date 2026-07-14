#saving files created in user_memory.py
import json

def save_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f)

# save_json("buddy/data/user.json", {"name": "Bhavesh", "age": 18})
