import copy
import os
import shutil
from datetime import datetime
from pathlib import Path

from buddy.core.paths import TRASH_FILES_DIR, TRASH_INDEX_FILE
from buddy.core.defaults import DEFAULT_TRASH
from buddy.core.status import FileStatus
from buddy.memory.storage_manager import load_json, save_json


def _load_index():
    data = load_json(TRASH_INDEX_FILE)
    return data if data else copy.deepcopy(DEFAULT_TRASH)


def trash_item(path):
    src = Path(path)
    if not src.exists():
        return FileStatus.SOURCE_NOT_FOUND

    files_dir = Path(TRASH_FILES_DIR)

    # never trash the trash itself, or a folder that contains it
    src_real = src.resolve()
    trash_real = files_dir.resolve()
    if (src_real == trash_real
            or src_real.is_relative_to(trash_real)
            or trash_real.is_relative_to(src_real)):
        return FileStatus.PROTECTED_PATH
    
    files_dir.mkdir(parents=True, exist_ok=True)

    index = _load_index()
    item_id = index["next_id"]
    stored_name = f"{item_id}_{src.name}"

    try:
        shutil.move(str(src), str(files_dir / stored_name))
    except OSError:
        return FileStatus.OPERATION_FAILED

    index["items"].append({
        "id": item_id,
        "original_path": os.path.abspath(src),
        "stored_name": stored_name,
        "deleted_at": datetime.now().isoformat(timespec="seconds"),
    })
    index["next_id"] += 1
    save_json(TRASH_INDEX_FILE, index)
    return FileStatus.ITEM_TRASHED


def list_trash():
    return _load_index()["items"]


def restore_item(item_id):
    index = _load_index()

    for item in index["items"]:
        if item["id"] == item_id:
            stored = Path(TRASH_FILES_DIR) / item["stored_name"]
            original = Path(item["original_path"])

            if not stored.exists():
                return FileStatus.TRASH_ITEM_NOT_FOUND
            if original.exists():
                return FileStatus.DESTINATION_EXISTS

            try:
                original.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(stored), str(original))
            except OSError:
                return FileStatus.OPERATION_FAILED

            index["items"].remove(item)
            save_json(TRASH_INDEX_FILE, index)
            return FileStatus.ITEM_RESTORED

    return FileStatus.TRASH_ITEM_NOT_FOUND


def delete_permanently(item_id):
    index = _load_index()

    for item in index["items"]:
        if item["id"] == item_id:
            stored = Path(TRASH_FILES_DIR) / item["stored_name"]

            try:
                if stored.is_symlink() or stored.is_file():
                    stored.unlink()
                elif stored.is_dir():
                    shutil.rmtree(stored)
            except OSError:
                return FileStatus.OPERATION_FAILED

            index["items"].remove(item)
            save_json(TRASH_INDEX_FILE, index)
            return FileStatus.ITEM_PERMANENTLY_DELETED 

    return FileStatus.TRASH_ITEM_NOT_FOUND