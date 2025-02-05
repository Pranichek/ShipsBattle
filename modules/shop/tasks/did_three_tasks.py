check_completed_tasks = [0]
from ..shop_button import fourth_tasks_copy
from ..shop_image import done_task_four, shop_item

def complete_three_tasks():
    try:
        if check_completed_tasks[0] != 999:
            if check_completed_tasks[0] == 3:
                check_completed_tasks[0] = 999
                if done_task_four.VISIBLE != 255:
                    done_task_four.VISIBLE = 255
        else:
            if done_task_four.VISIBLE != 255:
                done_task_four.VISIBLE = 255
    except:
        pass