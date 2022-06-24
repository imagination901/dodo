from dataclasses import dataclass


@dataclass
class ParsedTaskData:
    description:    str
    due_time:       str
    project_name:   str


def parse_input(list_args: list[str]) -> ParsedTaskData:
    def _show_help() -> str:
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
        return input('Due time for this task: ').capitalize()
    
    def _parse_project_name() -> str:
        return input('Project name: ').capitalize()
    
    def _parsed_task_data() -> ParsedTaskData:
        return ParsedTaskData(description=' '.join(list_args[1:]))
    
    def _user_confirmation() -> bool:
        no_decision = input('Enter to Save (type anything else to Discard): ')
        if no_decision:
            print('Task discarded.')
            return False
        else:
            print('Task saved.')
            return True


    if _called_with_no_args() or _user_needs_help():
        _show_help()
    else:
        parsed_description  = _parse_description()
        parsed_due_time     = _parse_due_time()
        parsed_project      = _parse_project_name()
        if _user_confirmation():
            return ParsedTaskData(description=parsed_description,
                                  due_time=parsed_due_time,
                                  project_name=parsed_project)
