#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
import sys
from lib.input_processor import handle_input, parse_input                          #type: ignore


def main():
    task_input = handle_input(input=sys.argv)
    if task_input:
        parsed_task_data = parse_input(input_args=task_input)
        print(parsed_task_data)



if __name__ == '__main__':
    main()
