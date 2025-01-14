from .did_three_tasks import check_completed_tasks


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