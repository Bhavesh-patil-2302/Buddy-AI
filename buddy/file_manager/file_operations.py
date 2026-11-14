import shutil
from pathlib import Path
from buddy.core.status import FileStatus



def _final_destination(src, destination):
    # if destination is an existing folder, put the file inside it
    dst = Path(destination)
    if dst.is_dir():
        dst = dst / src.name
    return dst

# copy function to copy a file from source to destination
def copy_file(source, destination):
    src = Path(source)
    if not src.exists():
        return FileStatus.SOURCE_NOT_FOUND
     
    dst = _final_destination(src, destination)
    if dst.exists():
        return FileStatus.DESTINATION_EXISTS

    try:
        if src.is_dir():
            shutil.copytree(src, dst, symlinks=True)
        else:
            shutil.copy2(src, dst)
        return FileStatus.FILE_COPIED
    except OSError:
        return FileStatus.OPERATION_FAILED
    
    
    
    # move function to move files or folders from source to destination
def move_file(source, destination):
    src = Path(source)
    if not src.exists():
        return FileStatus.SOURCE_NOT_FOUND

    dst = _final_destination(src, destination)
    if dst.exists():
        return FileStatus.DESTINATION_EXISTS

    try:
        shutil.move(str(src), str(dst))
        return FileStatus.FILE_MOVED
    except OSError:
        return FileStatus.OPERATION_FAILED
    
    # rename function to rename  a file or folder
def rename_file(path, new_name):
    src = Path(path)
    if not src.exists():
        return FileStatus.SOURCE_NOT_FOUND

    # new_name must be only a name, not a path like "folder/x.txt"
    if not new_name or Path(new_name).name != new_name:
        return FileStatus.INVALID_NAME

    target = src.with_name(new_name)
    if target.exists():
        return FileStatus.DESTINATION_EXISTS

    try:
        src.rename(target)
        return FileStatus.FILE_RENAMED
    except OSError:
        return FileStatus.OPERATION_FAILED
    
    
    # create a new folder
def create_folder(path):
    folder = Path(path)
    if folder.exists():
        return FileStatus.DESTINATION_EXISTS

    try:
        folder.mkdir(parents=True)
        return FileStatus.FOLDER_CREATED
    except OSError:
        return FileStatus.OPERATION_FAILED