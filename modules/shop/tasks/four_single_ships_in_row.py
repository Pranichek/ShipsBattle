from .did_three_tasks import check_completed_tasks
from ...achievement import enemy_dies_ships_for_ahiv

single_ships = []
check_killed_for_single_ships = []
start_index_single = [0]
def kill_four_single_ships_in_a_row():
    if enemy_dies_ships_for_ahiv[0] != "":
        one = single_ships.count(1)
        check_killed_for_single_ships.clear()
        check_killed_for_single_ships.extend(enemy_dies_ships_for_ahiv[0][start_index_single[0]:])
        if one > 0:
            if one <= 0:
                check_killed_for_single_ships.clear()

            if one <= 0:
                if 0 in single_ships:
                    for i in range(0 , len(single_ships)):
                        if single_ships[i] == 0:
                            del single_ships[i]

            if single_ships.count(0) > 0 and one > 0:
                single_ships.clear()
                one = 0
                return False
                
            if single_ships.count(2) >= 2 and one > 0 and 2 in check_killed_for_single_ships:
                single_ships.clear()
                one = 0
                return False
            
            if single_ships.count(3) >= 3 and one > 0 and 3 in check_killed_for_single_ships:
                single_ships.clear()
                one = 0
                return False
            
            if single_ships.count(4) >= 4 and one > 0 and 4 in check_killed_for_single_ships:
                single_ships.clear()
                one = 0
                return False

            if one == 4 and "Kill four single ships in a row" not in single_ships:
                single_ships.append("Kill four single ships in a row")
                check_completed_tasks[0] += 1
                print("You are kill four single ships in a row")
        else:
            single_ships.clear()
            if enemy_dies_ships_for_ahiv[0] != "" and len(enemy_dies_ships_for_ahiv[0]) >= start_index_single[0]: 
                start_index_single[0] += 1