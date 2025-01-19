from .did_three_tasks import check_completed_tasks
from ..shop_button import first_tasks_copy

two_hits_in_a_row = []
def two_hits_in_row(number_cell: int):
    if "True" not in two_hits_in_a_row:
        count_ships = 0
        two_hits_in_a_row.append(number_cell)

        for cell in two_hits_in_a_row:
            if cell != 5 and cell != 0:
                count_ships += 1
            else:
                two_hits_in_a_row.clear()
                return False
            
        if count_ships > 1 and "True" not in two_hits_in_a_row:
            check_completed_tasks[0] += 1
            print("Two hits in a row")
            two_hits_in_a_row.append("True")
            del first_tasks_copy[0]