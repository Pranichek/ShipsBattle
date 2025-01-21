from .did_three_tasks import check_completed_tasks
from ...achievement import enemy_dies_ships_for_ahiv
from ..shop_button import third_tasks_copy
from ..shop_image import shop_item, done_task_three

check_three_2decker_ship_in_row = []
check_killed_for_double_ships = []
start_index_two = [0]
def kill_three_double_decker_in_a_row():
    if enemy_dies_ships_for_ahiv[0] != "":
        two = check_three_2decker_ship_in_row.count(2)
        check_killed_for_double_ships.clear()
        check_killed_for_double_ships.extend(enemy_dies_ships_for_ahiv[0][start_index_two[0]:])
        if two > 0:
            if two <= 1:
                check_killed_for_double_ships.clear()

            if two <= 1:
                if 0 in check_three_2decker_ship_in_row:
                    for i in range(0 , len(check_three_2decker_ship_in_row)):
                        if check_three_2decker_ship_in_row[i] == 0:
                            del check_three_2decker_ship_in_row[i]

            if "You kill three double decker in row" not in check_three_2decker_ship_in_row:
                if check_three_2decker_ship_in_row.count(0) > 0 and two > 1:
                        check_three_2decker_ship_in_row.clear()
                        two = 0
                        return False
                
                if check_three_2decker_ship_in_row.count(1) >= 1 and two > 1 and 1 in check_killed_for_double_ships:
                    check_three_2decker_ship_in_row.clear()
                    two = 0
                    return False
                
                if check_three_2decker_ship_in_row.count(3) >= 3 and two > 1 and 3 in check_killed_for_double_ships:
                    check_three_2decker_ship_in_row.clear()
                    two = 0
                    return False
                
                if check_three_2decker_ship_in_row.count(4) >= 4 and two > 1 and 4 in check_killed_for_double_ships:
                    check_three_2decker_ship_in_row.clear()
                    two = 0
                    return False
                
                if two == 6 and "You kill two three decker in row" not in check_three_2decker_ship_in_row:
                    check_three_2decker_ship_in_row.append("You kill three double decker in row")
                    check_completed_tasks[0] += 1
                    print("Ты убил три двухпалубных кораблей подряд")
                    del third_tasks_copy[2]
                    if done_task_three.VISIBLE <= 254:
                        done_task_three.VISIBLE = 255
                elif "You kill two three decker in row" in check_three_2decker_ship_in_row:
                    if done_task_three.VISIBLE <= 254:
                        done_task_three.VISIBLE = 255
        else:
            check_three_2decker_ship_in_row.clear()
            if enemy_dies_ships_for_ahiv[0] != "" and len(enemy_dies_ships_for_ahiv[0]) >= start_index_two[0]:
                start_index_two[0] += 1