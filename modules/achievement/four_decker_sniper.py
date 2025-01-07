from ..classes import DrawImage , first_four_decker_achivment 

list_save_coords_achiv = []

# хранятся наши умершие корабли
player_died_ships_for_achiv = [""]
# умершие корабли врага
enemy_dies_ships_for_ahiv = [""]

our_ships_4decker_achiv = [0]
enemy_ships_4decker_achiv = [0]
def first_kill_four_decker_achivment():
    if enemy_dies_ships_for_ahiv[0] != 0 and enemy_dies_ships_for_ahiv[0] != "":
        if enemy_ships_4decker_achiv[0] != "kill four-decker ship":
            our_ships_4decker_achiv[0] = 0
            enemy_ships_4decker_achiv[0] = 0
            if enemy_dies_ships_for_ahiv[0] != "":
                our_ships_4decker_achiv[0] = 1 - player_died_ships_for_achiv[0].count(4)
                enemy_ships_4decker_achiv[0] = 1 - enemy_dies_ships_for_ahiv[0].count(4)

                if enemy_ships_4decker_achiv[0] != "kill four-decker ship":
                    if our_ships_4decker_achiv[0] > enemy_ships_4decker_achiv[0] and enemy_ships_4decker_achiv[0] == 0 and enemy_ships_4decker_achiv[0]!= "kill four-decker ship":
                        enemy_ships_4decker_achiv[0] = "kill four-decker ship"
                        medal_four_decker.y_cor = 24
                        first_four_decker_achivment.ACTIVE = True
                        # 1 - номе задания
                        # 2 - икс
                        # 3 - игрек
                        list_save_coords_achiv.append((1 , medal_four_decker.x_cor , medal_four_decker.y_cor))
                        print("Ты убил четыреx палубный кораблик 777")
                            

medal_four_decker = DrawImage(
    x_cor = 750 ,
    y_cor = -50,
    width = 50 ,
    height = 50 ,
    folder_name = "achievement",
    image_name = "medal_four_decker.png"
)