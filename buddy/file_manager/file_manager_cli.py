from datetime import datetime
from buddy.core.status import FileStatus
from buddy.scanner.file_scanner import scan_folder
from buddy.file_manager.file_filters import (
    FILE_CATEGORIES, SORT_OPTIONS,
    filter_by_category, filter_by_extensions, sort_entries,
)
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

# raw bytes - human readable format
def format_size(num_bytes):
    if num_bytes < 1024:
        return f"{num_bytes} B"
    for unit in ["KB", "MB", "GB"]:
        num_bytes /= 1024
        if num_bytes < 1024:
            return f"{num_bytes:.1f} {unit}"
    return f"{num_bytes / 1024:.1f} TB"


def show_entries(entries):
    if not entries:
        print("Nothing found.")
        return
    print()
    for e in entries:
        kind = "[LINK]" if e["is_symlink"] else ("[DIR] " if e["is_dir"] else "[FILE]")
        size = "-" if e["is_dir"] else format_size(e["size"])
        modified = datetime.fromtimestamp(e["modified"]).strftime("%Y-%m-%d %H:%M")
        print(f"{kind} {e['name']}  |  {size}  |  modified {modified}")
    print(f"\n{len(entries)} item(s)")


def list_files_menu():
    folder = input("Folder path: ").strip().strip('"')
    status, entries = scan_folder(folder)
    if status != FileStatus.FOLDER_SCANNED:
        print(status.value)
        return

    print("Filter: images, documents, code, videos, audio, archives, custom")
    choice = input("Filter (press Enter for no filter): ").strip().lower()
    if choice in FILE_CATEGORIES:
        entries = filter_by_category(entries, choice)
    elif choice == "custom":
        raw = input("Extensions separated by commas (e.g. py, txt): ")
        extensions = [x.strip() for x in raw.split(",") if x.strip()]
        entries = filter_by_extensions(entries, extensions)
    elif choice != "":
        print("Unknown filter, showing everything.")

    sort_by = input("Sort by (name / size / created / modified) [name]: ").strip().lower() or "name"
    if sort_by not in SORT_OPTIONS:
        print("Unknown sort option, using name.")
        sort_by = "name"
    order = input("Order (asc / desc) [asc]: ").strip().lower()
    
    if order not in ("", "asc", "desc"):
        print("Unknown order, using asc.")
        order = "asc"

    entries = sort_entries(entries, sort_by, descending=(order == "desc"))
    show_entries(entries)

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
        print("9. List files (sort / filter)")
        print("10. Return to main menu")

        choice = input("Please enter the number of your choice: ")

        if choice == "1":
            source = input("Path to copy: ").strip().strip('"')
            destination = input("Copy to (folder or new path): ").strip().strip('"')
            print(copy_file(source, destination).value)

        elif choice == "2":
            source = input("Path to move: ").strip().strip('"')
            destination = input("Move to (folder or new path): ").strip().strip('"')
            print(move_file(source, destination).value)

        elif choice == "3":
            path = input("Path to rename: ").strip().strip('"')
            new_name = input("New name (name only, not a path): ")
            print(rename_file(path, new_name).value)

        elif choice == "4":
            path = input("Path of the new folder: ").strip().strip('"')
            print(create_folder(path).value)

        elif choice == "5":
            path = input("Path to delete: ").strip().strip('"')
            answer = input("Move it to Trash? (y/n): ").strip().lower()
            if answer == "y":
                print(trash_item(path).value)
            else:
                print("Cancelled.")

        elif choice == "6":
            items = list_trash()
            if items is None:
                print(FileStatus.STORAGE_ERROR.value)
            else:
                show_trash(items)

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
            list_files_menu()

        elif choice == "10":
            break

        else:
            print("Invalid choice. Please select a valid option from the menu.")