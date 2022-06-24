#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
import sys
from lib.arg_parser import parse_input                          #type: ignore


input_args = sys.argv
parsed_task_data = parse_input(list_args=input_args)
if parsed_task_data:
    print(parsed_task_data)