from buddy.notes.notes_manager import create_note, view_note, delete_note, update_note, search_note




def notes_manager_menu():
    print("Notes Manager Menu:")
    print("1. Create a new note")
    print("2. View existing notes")
    print("3. Delete a note")
    print("4. Update a note")
    print("5. Search notes")
    print("6. Return to main menu")

    choice = input("Please enter the number of your choice: ")

    if choice == "1":
        title = input("enter the title of the note: ")
        body = input("enter the content of the note: ")
        tags = input("enter the tags for the note (comma-seperated): ").split(",")
        status =create_note(title, body, tags)
        print(f"Note creation status: {status.value}")
        
        
    elif choice == "2":
        view_note()
        
    elif choice == "3":
        note_id = int(input("Enter the ID of the note to delete: "))
        status = delete_note(note_id=note_id)
        print(f"Note deletion status: {status.value}")
        
    
    elif choice == "4":
        note_id = int(input("Enter the ID of the note to update: "))
        title = input("Enter the new title of the note: ")
        body = input("Enter the new content of the note: ")
        tags = input("Enter the new tags for the note (comma-separated): ").split(",")
        status = update_note(note_id=note_id, title=title, body=body, tags=tags)
        print(f"Note update status: {status.value}")
        
    elif choice == "5":
        query = input("Enter the search query: ")
        search_note(query)
        
    elif choice == "6":
        print("Returning to main menu...")
        return  # Exit the notes manager menu and return to the main menu
    else:
        print("Invalid choice. Please select a valid option from the menu.")