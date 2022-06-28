from dataclasses import dataclass
from datetime import datetime


@dataclass
class ParsedTaskData:
    description:    str
    due_time:       str


@dataclass
class Task:
    description:    str
    due_time:       datetime
    priority:       int


@dataclass
class TaskCollection:
    list_of_tasks:  list