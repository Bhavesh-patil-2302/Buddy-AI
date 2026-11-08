# defining the status of the application
from enum import Enum

# defining the status of the application
class Status(Enum):
    SUCCESS = "SUCCESS"
    INVALID_KEY = "INVALID_KEY"
    INVALID_TYPE = "INVALID_TYPE"
    NO_CHANGE = "NO_CHANGE"

# print(Status.SUCCESS.value)


# notes 
class NoteStatus(Enum):
    NOTE_CREATED = "NOTE_CREATED"
    NOTE_UPDATED = "NOTE_UPDATED"
    NOTE_DELETED = "NOTE_DELETED"
    NOTE_NOT_FOUND = "NOTE_NOT_FOUND"

