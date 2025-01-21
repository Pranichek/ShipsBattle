check_completed_tasks = [0]
from ..shop_button import fourth_tasks_copy
from ..shop_image import done_task_four, shop_item

def complete_three_tasks():
    if check_completed_tasks[0] != 999:
        if check_completed_tasks[0] == 3:
            check_completed_tasks[0] = 999
            print("Ты выполнил все три завдання")
            del fourth_tasks_copy[2]
            if done_task_four.VISIBLE <= 254:
                done_task_four.VISIBLE = 255
    else:
        if done_task_four.VISIBLE <= 254:
            done_task_four.VISIBLE = 255