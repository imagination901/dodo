from datamodel import Task
from config import OUTPUT_WIDTH, HEADERS, HEADER_DIV_PCT


OUTPUT_WIDTH    = OUTPUT_WIDTH 
HEADERS         = HEADERS
HEADER_DIV_PCT  = HEADER_DIV_PCT


class StringFormatter():
    '''Provides interface to conform dividers and other scrings 
    to follow the same unified format to be used as output.'''

    def __init__(cls, str_width: int = 80, 
                 headers: list[str] = ['#', 'Task description', 'Due', 'Priority'], 
                 headers_div_pct: list[int]= [5, 60, 18, 17]) -> None:
        cls.outer_width     = str_width 
        cls.inner_width     = str_width-2
        cls.headers         = headers
        cls.headers_div_pct = headers_div_pct


    def generate_divider(cls, border_char: str = '+', filler_char: str = '-') -> str:
        return f'{border_char}{filler_char*cls.inner_width}{border_char}'
    
    
    def generate_header(cls, border_char: str = '|') -> str:
        header_str = ''
        space = ' '

        for header, div_pct in zip(cls.headers, cls.headers_div_pct):
            current_div = int(cls.inner_width / 100 * div_pct)
            current_str = f' {header}{space * current_div}'
            header_str = header_str + f'{current_str[:current_div]}|'

        return f'{border_char}{header_str[: cls.inner_width] + border_char}'
    

    def generate_task(cls, task: Task, task_nr: int, border_char: str = '|') -> str:
        task_str = ''
        task_items = [task_nr, task.description, task.due_time, task.priority]
        space = ' '

        for item, div_pct in zip(task_items, cls.headers_div_pct):
            current_div = int(cls.inner_width / 100 * div_pct)
            current_str = f' {item}{space * current_div}'
            task_str = task_str + f'{current_str[:current_div]}|'

        return f'{border_char}{task_str[: cls.inner_width] + border_char}'
        pass
    
    
    def generate_placeholder(cls, border_char: str = '|') -> str:
        message = " Such empty. 'dodo To water flowers' will add a new task."
        return f'{border_char}{(message + " "*cls.inner_width)[:cls.inner_width]}{border_char}'


def beautify_output(tasks: list[Task], message: str='') -> None:

    output_formatter = StringFormatter(str_width        =OUTPUT_WIDTH,
                                       headers          =HEADERS, 
                                       headers_div_pct  =HEADER_DIV_PCT)

    def _print_headers():
        print(output_formatter.generate_divider())
        print(output_formatter.generate_header())
        print(output_formatter.generate_divider())
        print(output_formatter.generate_divider(border_char='|', filler_char=' '))
    
    def _print_task_placeholder():
        print(output_formatter.generate_placeholder())
    
    def _print_task(task: Task, task_number: int):
        print(output_formatter.generate_task(task=task, task_nr=task_number))
    
    def _print_message():
        print(output_formatter.generate_divider(border_char='|', filler_char=' '))
        print(output_formatter.generate_divider())
        print(message)
    

    _print_headers()
    if not tasks:
        _print_task_placeholder()
    else:
        for number, task in enumerate(tasks, start=1):
            _print_task(task=task, task_number=number)
    _print_message()
