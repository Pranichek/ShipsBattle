from .did_three_tasks import check_completed_tasks
from ...achievement import enemy_dies_ships_for_ahiv
from ..shop_button import third_tasks_copy
from ..shop_image import shop_item, done_task_three
#3 kill two three-decker ships in a row
count_three_ships = []
check_killed_for_three_ships = []
start_index = [0]
def kill_two_three_decker_in_a_row():
    if enemy_dies_ships_for_ahiv[0] != "":
        count_three = count_three_ships.count(3)
        check_killed_for_three_ships.clear()
        check_killed_for_three_ships.extend(enemy_dies_ships_for_ahiv[0][start_index[0]:])
        if count_three > 0:
            if count_three <= 2:
                check_killed_for_three_ships.clear()

            if count_three <= 2:
                if 0 in count_three_ships:
                    for i in range(0 , len(count_three_ships)):
                        if count_three_ships[i] == 0:
                            del count_three_ships[i]

            if count_three_ships.count(0) > 0 and count_three >= 3:
                    print(count_three , count_three_ships.count(0))
                    count_three_ships.clear()
                    count_three = 0
                    print("с ноликом")
                    return False
            if count_three_ships.count(1) >= 1 and count_three >= 3 and 1 in check_killed_for_three_ships:
                count_three_ships.clear()
                count_three = 0
                print("с еденичкой")
                return False
            if count_three_ships.count(2) >= 2 and count_three >= 3 and 2 in check_killed_for_three_ships:
                count_three_ships.clear()
                count_three = 0
                print("с двоейчкой")
                return False
            if count_three_ships.count(4) >= 4 and count_three >= 3 and 4 in check_killed_for_three_ships: 
                count_three_ships.clear()
                count_three = 0
                print("с четверочкой")
                return False

    
            if count_three == 6 and "Kill two three decker in a row" not in count_three_ships:
                check_completed_tasks[0] += 1
                count_three_ships.append("Kill two three decker in a row")
                print("Ты убил два трехпалубных кораблей подряд")
                del third_tasks_copy[-1]
                if done_task_three.VISIBLE <= 254:
                    done_task_three.VISIBLE = 255
            if "Kill two three decker in a row" in count_three_ships:
                if done_task_three.VISIBLE <= 254:
                    done_task_three.VISIBLE = 255

        else:
            count_three_ships.clear()
            if enemy_dies_ships_for_ahiv[0]!= "" and len(enemy_dies_ships_for_ahiv[0]) >= start_index[0]:
                start_index[0] += 1