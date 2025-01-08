from ..classes import lone_hunter_achievement, lone_hunter_medal
from .four_decker_sniper import list_save_coords_achiv 
from .four_decker_sniper import enemy_dies_ships_for_ahiv


# kill four single ships in a row
single_ships_achiv = []
check_killed_for_single_ships_achiv = []
start_index_single_achiv = [0]
def lone_hunter():
    if enemy_dies_ships_for_ahiv[0] != 0 and enemy_dies_ships_for_ahiv[0] != "":
        one = single_ships_achiv.count(1)
        check_killed_for_single_ships_achiv.clear()
        check_killed_for_single_ships_achiv.extend(enemy_dies_ships_for_ahiv[0][start_index_single_achiv[0]:])
        if one > 0:
            if one <= 0:
                check_killed_for_single_ships_achiv.clear()

            if one <= 0:
                if 0 in single_ships_achiv:
                    for i in range(0 , len(single_ships_achiv)):
                        if single_ships_achiv[i] == 0:
                            del single_ships_achiv[i]

            if single_ships_achiv.count(0) > 0 and one > 0:
                single_ships_achiv.clear()
                one = 0
                return False
                
            if single_ships_achiv.count(2) >= 2 and one > 0 and 2 in check_killed_for_single_ships_achiv:
                single_ships_achiv.clear()
                one = 0
                return False
            
            if single_ships_achiv.count(3) >= 3 and one > 0 and 3 in check_killed_for_single_ships_achiv:
                single_ships_achiv.clear()
                one = 0
                return False
            
            if single_ships_achiv.count(4) >= 4 and one > 0 and 4 in check_killed_for_single_ships_achiv:
                single_ships_achiv.clear()
                one = 0
                return False

            if one == 4 and "Kill four single ships in a row" not in single_ships_achiv:
                single_ships_achiv.append("Kill four single ships in a row")
                lone_hunter_achievement.ACTIVE = True
                lone_hunter_medal.ACTIVE = True
                list_save_coords_achiv.append(7)
                print("You are kill four single ships in a row")
        else:
            single_ships_achiv.clear()
            if enemy_dies_ships_for_ahiv [0] != "" and len(enemy_dies_ships_for_ahiv [0]) >= start_index_single_achiv[0]: 
                start_index_single_achiv[0] += 1


