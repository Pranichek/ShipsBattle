from .did_three_tasks import check_completed_tasks
from ..shop_button import first_tasks_copy

four_hits_in_a_row = []
def four_hits_in_row(number_cell: int):
    if "True" not in four_hits_in_a_row:
        count_ships = 0
        four_hits_in_a_row.append(number_cell)

        for cell in four_hits_in_a_row:
            if cell!= 5 and cell != 0:
                count_ships += 1
            else:
                four_hits_in_a_row.clear()
                return False
        if count_ships > 3 and "True" not in four_hits_in_a_row:
            check_completed_tasks[0] += 1
            print("Four hits in a row")
            four_hits_in_a_row.append("True")
            del first_tasks_copy[1]
