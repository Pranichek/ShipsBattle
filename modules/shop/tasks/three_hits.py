from .did_three_tasks import check_completed_tasks
from ..shop_button import first_tasks_copy
from ..shop_image import shop_item, done_task_one

three_hits_in_a_row = []
def three_hits_in_row(cell: int):
    if "True" not in three_hits_in_a_row:
        count_ships = 0
        three_hits_in_a_row.append(cell)

        for cell in three_hits_in_a_row:
            if cell!= 5 and cell != 0:
                count_ships += 1
            else:
                three_hits_in_a_row.clear()
                return False
        if count_ships > 2 and "True" not in three_hits_in_a_row:
            check_completed_tasks[0] += 1
            print("Three hits in a row")
            three_hits_in_a_row.append("True")
            del first_tasks_copy[-1]
            if done_task_one.VISIBLE <= 254:
                done_task_one.VISIBLE = 255
        if "True" in three_hits_in_a_row:
            if done_task_one.VISIBLE <= 254:
                done_task_one.VISIBLE = 255