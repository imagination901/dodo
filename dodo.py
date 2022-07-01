#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
import sys
from lib.input_handler import handle_user_input                     #type: ignore
from lib.task_manager import _load_tasks                            #type: ignore
import os


def main():
    tasks = _load_tasks()
    handle_user_input(input=sys.argv, task_list=tasks)

if __name__ == '__main__':
    main()
