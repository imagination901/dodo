from typing import Optional
from datamodel import ParsedTaskData, Task
from lib.task_manager import add_task                           #type: ignore
from lib.view_controller import beautify_output                 #type: ignore


def _parse_input(input_args: Optional[list[str]]) -> Optional[ParsedTaskData]:
    '''Parses a list of arguments and returns an instance of 
    ParseTaskData class.'''

    def _parse_description() -> str:
        if input_args:
            return ' '.join(input_args[1:]).capitalize()
        else:
            return '' 

    def _parse_due_time() -> str:
        return input('Due: ').capitalize()
    
    if input_args:
        return ParsedTaskData(description=_parse_description(), 
                                due_time=_parse_due_time())
    else: 
        return None


def handle_user_input(input: list[str], task_list: list[Task]) -> None:

    def _called_with_no_args() -> bool:
        return True if len(input) == 1 else False
    
    def _user_needs_help() -> bool:
        help_keywords = ('help', '-h', '-H', 'hlep', 'h')
        if input[1] in help_keywords and len(input) == 2:
            return True
        return False

    def _show_help():
        msg = "To add a new task: 'dodo this new task'"
        beautify_output(tasks=task_list, message=msg)
    
    def _show_tasks():
        msg = "New task: 'dodo My new task'"
        beautify_output(tasks=task_list, message=msg)


    if _called_with_no_args():
        _show_tasks()
    elif  _user_needs_help():
        _show_help()
    else:
        add_task(task_data=_parse_input(input_args=input),
                 task_list=task_list)
        _show_tasks()
