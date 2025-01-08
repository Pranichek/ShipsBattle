from ..classes import piooner_achievement, pioneer_medal 
from .four_decker_sniper import list_save_coords_achiv , enemy_dies_ships_for_ahiv , player_died_ships_for_achiv



count_player_ships_achiv = [0]
count_enemy_kill_achiv = [0]
def piooner():
    if enemy_dies_ships_for_ahiv[0] != 0 and enemy_dies_ships_for_ahiv[0] != "":
        if count_enemy_kill_achiv[0] != "task piooner is done":
            if enemy_dies_ships_for_ahiv[0] != "":
                count_player_ships_achiv[0] = len(enemy_dies_ships_for_ahiv[0])
                count_enemy_kill_achiv[0] = len(player_died_ships_for_achiv[0])

                if count_player_ships_achiv[0] == 1 and count_enemy_kill_achiv[0] == 0 and count_enemy_kill_achiv[0] != "task piooner is done":
                    count_enemy_kill_achiv[0] = "task piooner is done"
                    piooner_achievement.ACTIVE = True
                    pioneer_medal.ACTIVE = True
                    list_save_coords_achiv.append((8))
                    print("Ure")


