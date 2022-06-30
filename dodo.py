#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
import sys
from lib.input_handler import handle_input                      #type: ignore
from lib.task_manager import load_tasks                         #type: ignore
import os


def main():
    tasks = load_tasks()
    handle_input(input=sys.argv, task_list=tasks)

if __name__ == '__main__':
    main()
