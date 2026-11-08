"""
notes manager functions with
creater
viewer
deletor 
modifier 
searcher
"""
#imports
import copy
from datetime import datetime
from buddy.core.defaults import DEFAULT_NOTES
from buddy.core.paths import NOTES_FILE  
from buddy.memory.storage_manager import save_json , load_json
from buddy.core.status import NoteStatus



#for creating notes

def create_note(title,body,tags=None):
    data = load_json(NOTES_FILE)
    if not data:
        data = copy.deepcopy(DEFAULT_NOTES)
        
    now=datetime.now().isoformat(timespec="seconds")
    
    note = {
        "id" : data["next_id"],
        "title" : title,
        "body" : body,
        "tags" : tags,
        "created_at" : now
    }
    data["notes"].append(note)
    data["next_id"] += 1
    save_json(NOTES_FILE, data)
    return NoteStatus.NOTE_CREATED

#for viewing notes
def view_note():
    data = load_json(NOTES_FILE)
    if not data or not data["notes"]:
        print("No notes found , Wanna Create One ??")
    for note in data["notes"]:
        print(f"ID: {note['id']}")
        print(f"Title: {note['title']}")
        print(f"Body: {note['body']}")
        print(f"Tags: {', '.join(note['tags']) if note['tags'] else 'No tags'}")
        print(f"Created At: {note['created_at']}")
        print("-" * 40)
        
        
#for deleting notes
def delete_note(note_id=None):
    data = load_json(NOTES_FILE)
    if not data or not data["notes"]:
        print("no notes found !")
        return NoteStatus.NOTE_NOT_FOUND
    for note in data["notes"]:
        if note["id"] == note_id:
            data["notes"].remove(note)
            save_json(NOTES_FILE, data)
            return NoteStatus.NOTE_DELETED
        return NoteStatus.NOTE_NOT_FOUND
    
    
    
#for updating notes
def update_note(note_id=None , new_title=None, new_body=None, new_tags=None):
    data = load_json(NOTES_FILE)
    if not data or not data["notes"]:
        print("No notes found!")
        return NoteStatus.NOTE_NOT_FOUND
    for note in data["notes"]:
        if note["id"] == note_id:
            if new_title:
                note["title"] = new_title
            if new_body:
                note["body"] = new_body
            if new_tags is not None:
                note["tags"] = new_tags
            save_json(NOTES_FILE, data)
            return NoteStatus.NOTE_UPDATED

    
    
# for searchng notes
def search_note(query):
    data = load_json(NOTES_FILE)
    if not data or not data["notes"]:
        print("No notes found!")
        return NoteStatus.NOTE_NOT_FOUND
    query=query.lower()
    results=[]
    for note in data["notes"]:
        if query in note["title"].lower() or query in note["body"].lower() or query in [tag.lower() for tag in note["tags"]]:
            results.append(note) 
    if results:
        for note in results:
            print("-" * 40)
            print(f"ID: {note['id']}")
            print(f"Title: {note['title']}")
            print(f"Body: {note['body']}")
            print(f"Tags: {', '.join(note['tags']) if note['tags'] else 'No tags'}")
            print(f"Created At: {note['created_at']}")
            print("-" * 40)
    else:
        print("No notes found matching the search query.")