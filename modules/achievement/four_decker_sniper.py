from ..classes import  first_four_decker_achivment , four_decker_sniper_medal
from ..game_tools import count_money_hit

#1 медалька
list_save_coords_achiv = [False]

# хранятся наши умершие корабли
player_died_ships_for_achiv = [""]
# умершие корабли врага
enemy_dies_ships_for_ahiv = [""]

our_ships_4decker_achiv = [0]
enemy_ships_4decker_achiv = [0]
def first_kill_four_decker_achivment():
    if enemy_dies_ships_for_ahiv[0] != "":
        if enemy_ships_4decker_achiv[0] != "kill four-decker ship":
            our_ships_4decker_achiv[0] = 0
            enemy_ships_4decker_achiv[0] = 0
            if enemy_dies_ships_for_ahiv[0] != "":
                our_ships_4decker_achiv[0] = 1 - player_died_ships_for_achiv[0].count(4)
                enemy_ships_4decker_achiv[0] = 1 - enemy_dies_ships_for_ahiv[0].count(4)

                if enemy_ships_4decker_achiv[0] != "kill four-decker ship":
                    if our_ships_4decker_achiv[0] == 1 and enemy_ships_4decker_achiv[0] == 0 and enemy_ships_4decker_achiv[0]!= "kill four-decker ship":
                        enemy_ships_4decker_achiv[0] = "kill four-decker ship"
                        first_four_decker_achivment.ACTIVE = True
                        four_decker_sniper_medal.ACTIVE = True
                        list_save_coords_achiv.append(1)
                        list_save_coords_achiv[0] = True
                        count_money_hit[0] += 20
                                    

