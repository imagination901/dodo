from datamodel import Task


width = 68 
header_div_pct = {
                        'num': 8,
                        'description': 55,
                        'due_date': 20,
                        'priority': 17
                    }


def beautify_output(tasks: list[Task], message: str='') -> None:
    column_width = {
                            'num': round(width/100* header_div_pct['num']),
                            'description': round(width/100*header_div_pct['description']),
                            'due_date': round(width/100*header_div_pct['due_date']),
                            'priority': round(width/100*header_div_pct['priority'])
                        }
    adjusted_width = width+2 # Adjusted to account for borders
    horizontal_line =   '+' + '-' * adjusted_width + '+'
    line_prefix = '| '
    empty_line = '|' +  ' ' * adjusted_width + '|'


    def _print_headers():
        headers = {
            'num': f'| #{" "*column_width["num"]}'[:column_width['num']],
            'description': f'| Description{" "*column_width["description"]}'[:column_width['description']],
            'due_date': f'| Due{" "*column_width["due_date"]}'[:column_width['due_date']],
            'priority': f'| Priority{" "*column_width["priority"]}'[:column_width['priority']]
            }
        space_adjustment = width - (len(headers['num'])+len(headers['description'])+len(headers['due_date'])+len(headers['priority']))

        print(horizontal_line)
        print(headers['num'], headers['description'], headers['due_date'], headers['priority']+' '*space_adjustment+'|')
        print(horizontal_line)
        print(empty_line)
    
    def _print_task_placeholder():
        print(line_prefix, end='')
        print(('Such empty. There are no tasks to show. ' + ' '*width)[:width] + ' ', end='')
        print(line_prefix)
    
    def _print_task(task: Task, task_number: int):

        def _task_to_string(task: Task, task_number: int) -> str:
            task_num = str(task_number)
            task_data = {
                'num': f'| {task_num}{" "*column_width["num"]}'[:column_width['num']+1],
                'description': f'| {task.description}{" "*column_width["description"]}'[:column_width['description']+1],
                'due_date': f'| {task.due_time}{" "*column_width["due_date"]}'[:column_width['due_date']+1],
                'priority': f'| {task.priority}{" "*column_width["priority"]}'[:column_width['priority']]
                }
            space_adjustment = width - (len(task_data['num'])+len(task_data['description'])+len(task_data['due_date'])+len(task_data['priority']))

            return f"{task_data['num']}{task_data['description']}{task_data['due_date']}{task_data['priority']}{' '*space_adjustment}|"


        print(_task_to_string(task=task, task_number=task_number))
    
    def _print_message():
        print(empty_line)
        print(horizontal_line)
        print(f'{message}')
    

    _print_headers()

    if not tasks:
        _print_task_placeholder()
    else:
        for number, task in enumerate(tasks, start=1):
            _print_task(task=task, task_number=number)

    _print_message()
