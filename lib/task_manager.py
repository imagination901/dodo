from datamodel import ParsedTaskData, Task
import pickle
import os


def load_tasks() -> list[Task]:
    tasks = []
    try:
        filepath = f'{os.path.dirname(__file__)}/tasks.pickle'
        with open(filepath, 'rb') as file:
            tasks = pickle.load(file)
    except FileNotFoundError:
        pass
    return tasks


def _save_tasks(tasks: list[Task]) -> None:
    filepath = f'{os.path.dirname(__file__)}/tasks.pickle'
    with open(filepath, 'wb') as file:
        pickle.dump(obj=tasks, file=file, protocol=pickle.HIGHEST_PROTOCOL)


def list_tasks():
    pass


def add_task(task_data: ParsedTaskData, task_list: list[Task]) -> None:
    task_list.append(Task(description=task_data.description,
                          due_time=task_data.due_time,
                          priority=1))
    _save_tasks(tasks=task_list)


def delete_task():
    pass