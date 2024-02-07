from enum import Enum
class TaskStatus(Enum):
    UNASSIGNED = "Unassigned"
    IN_PROGRESS = "In Progress"
    DONE = "Completed"    
    ARCHIVED = "Archived"
