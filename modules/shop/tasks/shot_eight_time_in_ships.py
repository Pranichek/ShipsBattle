from .did_three_tasks import check_completed_tasks
from ..shop_button import fourth_tasks_copy

#4 8 hits in a row
egight_hits_in_a_row = []
def eight_hits_in_row(number_cell: int):
    count_ships = 0
    egight_hits_in_a_row.append(number_cell)

    for cell in egight_hits_in_a_row:
        if cell!= 5 and cell != 0:
            count_ships += 1
        else:
            egight_hits_in_a_row.clear()
            return False
    if count_ships > 7 and "True" not in egight_hits_in_a_row:
        check_completed_tasks[0] += 1
        print("Eight hits in a row")
        egight_hits_in_a_row.append("True")
        del fourth_tasks_copy[-1]