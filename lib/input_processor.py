from typing import Optional
from datamodel import ParsedTaskData


def handle_input(input: list[str]) -> Optional[list[str]]:

    def _called_with_no_args() -> bool:
        return True if len(input) == 1 else False
    
    def _user_needs_help() -> bool:
        help_keywords = ('help', '-h', '-H', 'hlep', 'h')
        if input[1] in help_keywords and len(input) == 2:
            return True
        return False

    def _show_help():
        print("To add a new task: 'dodo this new task'")
    
    def _show_tasks():
        print("Such empty. Type 'dodo this new task' to create one.")

    if _called_with_no_args():
        _show_tasks()
    elif  _user_needs_help():
        _show_help()
    else:
        return input

    return None


def parse_input(input_args: list[str]) -> Optional[ParsedTaskData]:
    '''Parses a list of arguments and returns an instance of 
    ParseTaskData class.'''

    def _parse_description() -> str:
        return ' '.join(input_args[1:]).capitalize()

    def _parse_due_time() -> str:
        return input('Due: ').capitalize()
    
    return ParsedTaskData(description=_parse_description(), 
                              due_time=_parse_due_time())
