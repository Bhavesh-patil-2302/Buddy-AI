import os
from buddy.core.status import FileStatus

def list_files(folder_path):
    try:
        files = os.listdir(folder_path)
        
        print("\n file found:\n")
        for file in files:
            print(file)

    except FileNotFoundError:
        print(f"Error: The folder '{folder_path}' does not exist.")

    except PermissionError:
        print(f"Error: Permission denied to access '{folder_path}'.")
        
def scan_folder(folder_path):
    if not os.path.exists(folder_path):
        return FileStatus.SOURCE_NOT_FOUND, []
    if not os.path.isdir(folder_path):
        return FileStatus.NOT_A_FOLDER, []

    entries = []
    try:
        with os.scandir(folder_path) as items:
            for item in items:
                try:
                    info = item.stat(follow_symlinks=False)
                except OSError:
                    continue  # skip anything we can't read

                is_dir = item.is_dir(follow_symlinks=False)
                entries.append({
                    "name": item.name,
                    "path": item.path,
                    "is_dir": is_dir,
                    "is_symlink": item.is_symlink(),
                    "extension": "" if is_dir else os.path.splitext(item.name)[1].lower(),
                    "size": 0 if is_dir else info.st_size,
                    "created": getattr(info, "st_birthtime", info.st_ctime),
                    "modified": info.st_mtime,
                })
    except PermissionError:
        return FileStatus.PERMISSION_DENIED, []
        
    except OSError:
        return FileStatus.OPERATION_FAILED, []

    return FileStatus.FOLDER_SCANNED, entries
