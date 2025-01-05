from ..classes import DrawImage 
from .four_decker_sniper import list_save_coords_achiv 
from .four_decker_sniper import enemy_dies_ships_for_ahiv


list_hits_achiv = []
def monster_of_perfictionists():
    if enemy_dies_ships_for_ahiv[0] != "":
        indx_one = 0
        indx_two = 0
        indx_three = 0
        indx_four = 0

        for idx, died_ship in enumerate(enemy_dies_ships_for_ahiv[0]):
            if died_ship == 1:
                indx_one = idx

        print(indx_one , len(enemy_dies_ships_for_ahiv[0]) , enemy_dies_ships_for_ahiv[0]) 

        if indx_one + 3 < len(enemy_dies_ships_for_ahiv[0]):
            indx_two = enemy_dies_ships_for_ahiv[indx_one + 1]
            indx_three = enemy_dies_ships_for_ahiv[indx_one + 2]
            indx_four = enemy_dies_ships_for_ahiv[indx_one + 3]
            
            if 0 not in list_hits_achiv and 5 not in list_hits_achiv:
                if indx_one < indx_two < indx_three < indx_four:
                    if indx_four - indx_one == 3:
                        print("Ты чертов перфикционист")
                       
            else:
                list_hits_achiv.clear()
