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
                    index_killed_ships[0] += len(killed_ships[0]) - 1
                elif killed_ships[0].count(2) >= 2:
                    index_killed_ships[0] += len(killed_ships[0]) - 1
                elif killed_ships[0].count(3) >= 2:
                    index_killed_ships[0] += len(killed_ships[0]) - 1
                elif killed_ships[0].count(4) >= 2:
                    index_killed_ships[0] += len(killed_ships[0]) - 1
            
            if len(killed_ships[0]) >= 4:
               
                if 0 not in list_hits_achiv and 5 not in list_hits_achiv:
                    if 1 in killed_ships[0] and 2 in killed_ships[0] and 3 in killed_ships[0] and 4 in killed_ships[0]:
                    
                        if killed_ships[0].count(1) == 1 and killed_ships[0].count(2) == 1 and killed_ships[0].count(3) == 1 and killed_ships[0].count(4) == 1:
                      
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
                
     