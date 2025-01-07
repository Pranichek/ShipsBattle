from ..classes import DrawImage , perfictionists_achiement
from .four_decker_sniper import list_save_coords_achiv 
from .four_decker_sniper import enemy_dies_ships_for_ahiv


list_hits_achiv = []
def monster_of_perfictionists():
    if enemy_dies_ships_for_ahiv[0] != 0 and enemy_dies_ships_for_ahiv[0] != "":
        indx_one = 0
        indx_two = 0
        indx_three = 0
        indx_four = 0
        for idx, died_ship in enumerate(enemy_dies_ships_for_ahiv[0]):
            if died_ship == 1:
                indx_one = idx
        if indx_one + 3 < len(enemy_dies_ships_for_ahiv[0]):
            print(1)  # Проверка длины списка
            if enemy_dies_ships_for_ahiv[0][indx_one + 1] == 2:  
                print(2)# Уточняем индекс
                indx_two = enemy_dies_ships_for_ahiv[0][indx_one + 1]
                if enemy_dies_ships_for_ahiv[0][indx_one + 2] == 3:
                    print(3)
                    indx_three = enemy_dies_ships_for_ahiv[0][indx_one + 2]
                    if enemy_dies_ships_for_ahiv[0][indx_one + 3] == 4:
                        print(4)
                        indx_four = enemy_dies_ships_for_ahiv[0][indx_one + 3]
                        indx_one = 1
                        if 0 not in list_hits_achiv and 5 not in list_hits_achiv:
                            print(5)
                            print(indx_one , indx_two , indx_three , indx_four)
                            if indx_one < indx_two < indx_three < indx_four:
                                if indx_four - indx_one == 3:
                                    perfictionists_achiement.ACTIVE = True
                                    medal_perfictionists.y_cor = 74
                                    list_save_coords_achiv.append((12, medal_perfictionists.x_cor, medal_perfictionists.y_cor))
                        else:
                            list_hits_achiv.clear()

medal_perfictionists = DrawImage(
    x_cor = 970 ,
    y_cor = -50,
    width = 55,
    height = 54,
    folder_name = "achievement",
    image_name = "medal_perfectionists.png"
)