check_completed_tasks = [0]
from ..shop_button import fourth_tasks_copy
def complete_three_tasks():
    if check_completed_tasks[0] != 999:
        if check_completed_tasks[0] == 3:
            check_completed_tasks[0] = 999
            print("Ты выполнил все три завдання")
            del fourth_tasks_copy[2]