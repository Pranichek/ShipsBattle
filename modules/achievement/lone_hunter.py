from ..classes import DrawImage , lone_hunter_achievement
from .four_decker_sniper import list_save_coords_achiv


# kill four single ships in a row
single_ships_achiv = []
def lone_hunter(cell):
    single_ships_achiv.append(cell)
    one = single_ships_achiv.count(1)

    if single_ships_achiv.count(0) > 0 and one >= 0:
        single_ships_achiv.clear()
        one = 0
        return False
        
    if single_ships_achiv.count(2) >= 2 and one >= 0:
        single_ships_achiv.clear()
        one = 0
        return False
    
    if single_ships_achiv.count(3) >= 3 and one >= 0:
        single_ships_achiv.clear()
        one = 0
        return False
    
    if single_ships_achiv.count(4) >= 4 and one >= 0:
        single_ships_achiv.clear()
        one = 0
        return False


    if one == 4 and "Kill four single ships in a row" not in single_ships_achiv:
        single_ships_achiv.append("Kill four single ships in a row")
        lone_hunter_achievement.ACTIVE = True
        medal_lone_hunter.y_cor = 24
        list_save_coords_achiv.append((7 , medal_lone_hunter.x_cor , medal_lone_hunter.y_cor))

medal_lone_hunter = DrawImage(
    x_cor = 840 ,
    y_cor = -50,
    width = 50,
    height = 50,
    folder_name = "achievement",
    image_name = "lone_hunter_medal.png"
)
