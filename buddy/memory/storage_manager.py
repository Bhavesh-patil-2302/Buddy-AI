#saving files created in user_memory.py
import json

#save user data function
def save_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f , indent=4)



# 6354721377 RNGPIT

#load user data function
def load_json(file_path):
    try:
        with open(file_path, "r") as user_data:
            return json.load(user_data)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None
    
