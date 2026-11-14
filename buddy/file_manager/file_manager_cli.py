from buddy.file_manager.file_operations import copy_file, move_file, rename_file, create_folder
from buddy.file_manager.trash_manager import trash_item, list_trash, restore_item, delete_permanently


def show_trash(items):
    if not items:
        print("Trash is empty.")
        return
    for item in items:
        print(f"[{item['id']}] {item['original_path']}")
        print(f"     deleted: {item['deleted_at']}")
        print()


def file_manager_menu():
    while True:
        print()
        print("File Manager Menu:")
        print("1. Copy a file or folder")
        print("2. Move a file or folder")
        print("3. Rename a file or folder")
        print("4. Create a folder")
        print("5. Delete (move to Trash)")
        print("6. View Trash")
        print("7. Restore from Trash")
        print("8. Delete permanently from Trash")
        print("9. Return to main menu")

        choice = input("Please enter the number of your choice: ")

        if choice == "1":
            source = input("Path to copy: ").strip('"')
            destination = input("Copy to (folder or new path): ").strip('"')
            print(copy_file(source, destination).value)

        elif choice == "2":
            source = input("Path to move: ").strip('"')
            destination = input("Move to (folder or new path): ").strip('"')
            print(move_file(source, destination).value)

        elif choice == "3":
            path = input("Path to rename: ").strip('"')
            new_name = input("New name (name only, not a path): ")
            print(rename_file(path, new_name).value)

        elif choice == "4":
            path = input("Path of the new folder: ").strip('"')
            print(create_folder(path).value)

        elif choice == "5":
            path = input("Path to delete: ").strip('"')
            answer = input("Move it to Trash? (y/n): ").strip().lower()
            if answer == "y":
                print(trash_item(path).value)
            else:
                print("Cancelled.")

        elif choice == "6":
            show_trash(list_trash())

        elif choice == "7":
            try:
                item_id = int(input("Enter the id of the item to restore: "))
            except ValueError:
                print("Please enter a number.")
                continue
            print(restore_item(item_id).value)

        elif choice == "8":
            try:
                item_id = int(input("Enter the id of the item to delete permanently: "))
            except ValueError:
                print("Please enter a number.")
                continue
            print("WARNING: this cannot be undone.")
            answer = input("Type yes to confirm: ").strip().lower()
            if answer == "yes":
                print(delete_permanently(item_id).value)
            else:
                print("Cancelled.")

        elif choice == "9":
            break

        else:
            print("Invalid choice. Please select a valid option from the menu.")