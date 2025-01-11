from .did_three_tasks import check_completed_tasks
from ...achievement import enemy_dies_ships_for_ahiv, player_died_ships_for_achiv

our_ships_3decker = [0]
enemy_ships_3decker = [0]
def first_kill_three_decker():
     if enemy_dies_ships_for_ahiv[0] != 0:
        if enemy_ships_3decker[0] != "kill three-decker ship":
            our_ships_3decker[0] = 0
            enemy_ships_3decker[0] = 0

            our_ships_3decker[0] = 2 - player_died_ships_for_achiv[0].count(3)
            enemy_ships_3decker[0] = 2 - enemy_dies_ships_for_ahiv[0].count(3)
            if enemy_ships_3decker[0] != "kill three-decker ship":
                if our_ships_3decker[0] > enemy_ships_3decker[0] and enemy_ships_3decker[0] == 1 and enemy_ships_3decker[0] != "kill three-decker ship":
                    enemy_ships_3decker[0] = "kill three-decker ship"
                    check_completed_tasks[0] += 1
                    print("oda")