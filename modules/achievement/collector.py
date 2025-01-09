from ..classes import perfictionists_achiement, collector_medal
from .four_decker_sniper import list_save_coords_achiv 
from .four_decker_sniper import enemy_dies_ships_for_ahiv


list_hits_achiv = []
index_killed_ships = [0]
killed_ships = [""]
def monster_of_perfictionists():
    if True not in killed_ships:
        if enemy_dies_ships_for_ahiv[0] != 0 and enemy_dies_ships_for_ahiv[0] != "":
                # for killed_ship in enemy_dies_ships_for_ahiv[0]:
            killed_ships[0] =  enemy_dies_ships_for_ahiv[0][index_killed_ships[0]:]


            if 0 in list_hits_achiv or 5 in list_hits_achiv:
                index_killed_ships[0] += 1
                

            if len(killed_ships[0]) == 2:
                for indx , ship in enumerate(killed_ships[0]):
                    if indx > 0:
                        if killed_ships[0][indx - 1] == ship:
                            index_killed_ships[0] += 1
            if len(killed_ships[0]) >= 3:
                if killed_ships[0].count(1) >= 2:
                    print(8989)
                    index_killed_ships[0] += len(killed_ships[0]) - 1
                elif killed_ships[0].count(2) >= 2:
                    index_killed_ships[0] += len(killed_ships[0]) - 1
                elif killed_ships[0].count(3) >= 2:
                    index_killed_ships[0] += len(killed_ships[0]) - 1
                elif killed_ships[0].count(4) >= 2:
                    index_killed_ships[0] += len(killed_ships[0]) - 1
            
        
            if len(killed_ships[0]) >= 4:
                print(777)
                if 0 not in list_hits_achiv and 5 not in list_hits_achiv:
                    if 1 in killed_ships[0] and 2 in killed_ships[0] and 3 in killed_ships[0] and 4 in killed_ships[0]:
                        print(888)
                        if killed_ships[0].count(1) == 1 and killed_ships[0].count(2) == 1 and killed_ships[0].count(3) == 1 and killed_ships[0].count(4) == 1:
                            print(999)
                            killed_ships.append(True)
                            perfictionists_achiement.ACTIVE = True
                            collector_medal.ACTIVE = True
                            list_save_coords_achiv.append(12)
                        else:
                            index_killed_ships[0] += 3
                            list_hits_achiv.clear()
                else:
                    index_killed_ships[0] += 3
                    list_hits_achiv.clear()
                
        # indx_one = 0
        # indx_two = 0
        # indx_three = 0
        # indx_four = 0
        # for idx, died_ship in enumerate(enemy_dies_ships_for_ahiv[0]):
        #     if died_ship == 1:
        #         indx_one = idx
        # if indx_one + 3 < len(enemy_dies_ships_for_ahiv[0]):
        #     print(1)  # Проверка длины списка
        #     if enemy_dies_ships_for_ahiv[0][indx_one + 1] == 2:  
        #         print(2)# Уточняем индекс
        #         indx_two = enemy_dies_ships_for_ahiv[0][indx_one + 1]
        #         if enemy_dies_ships_for_ahiv[0][indx_one + 2] == 3:
        #             print(3)
        #             indx_three = enemy_dies_ships_for_ahiv[0][indx_one + 2]
        #             if enemy_dies_ships_for_ahiv[0][indx_one + 3] == 4:
        #                 print(4)
        #                 indx_four = enemy_dies_ships_for_ahiv[0][indx_one + 3]
        #                 indx_one = 1
        #                 if 0 not in list_hits_achiv and 5 not in list_hits_achiv:
        #                     print(5)
        #                     print(indx_one , indx_two , indx_three , indx_four)
        #                     if indx_one < indx_two < indx_three < indx_four:
        #                         if indx_four - indx_one == 3:
        #                             perfictionists_achiement.ACTIVE = True
        #                             collector_medal.ACTIVE = True
        #                             list_save_coords_achiv.append(12)
        #                 else:
        #                     list_hits_achiv.clear()

