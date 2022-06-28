from dataclasses import dataclass
from typing import Optional


@dataclass
class ParsedTaskData:
    description:    str
    due_time:       str


def parse_input(list_args: list[str]) -> Optional[ParsedTaskData]:
    def _show_help():
        print("Add a new task: dodo To water the flowers")

    def _called_with_no_args() -> bool:
        return True if len(list_args) == 1 else False
    
    def _user_needs_help() -> bool:
        help_keywords = ('help', '-h', '-H', 'hlep')
        if list_args[1] in help_keywords:
            return True
        return False 

    def _parse_description() -> str:
        return ' '.join(list_args[1:]).capitalize()

    def _parse_due_time() -> str:
        return input('Due: ').capitalize()
    

    if _called_with_no_args() or _user_needs_help():
        _show_help()
    else:
        return ParsedTaskData(description=_parse_description(), 
                              due_time=_parse_due_time())
    return None
