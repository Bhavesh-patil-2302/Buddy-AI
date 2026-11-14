# Buddy AI Architecture

## Principles

- One module = One responsibility
- Modular design
- Reusable functions

--------------------------------

main.py

Responsible for

- Program flow
- Menus
- Calling modules

--------------------------------

storage_manager.py

Responsible for

- save_json()
- load_json()

Never knows about users.

--------------------------------

user_memory.py

Responsible for

- save_user_data()
- load_user_data()

Never opens files directly.

--------------------------------

settings_manager.py

Responsible for

- load_settings()
- save_settings()

Only handles settings.

--------------------------------

scanner/

Responsible for

- File scanning

--------------------------------
notes/

- notes_manager.py - handles notes logic such as create, view ,update ,delete and searching queries
- notes_cli - interacts with user ,acts as interface 
- notes.json - notes are saved here in json format with creation time , id , title , content and tags of notes