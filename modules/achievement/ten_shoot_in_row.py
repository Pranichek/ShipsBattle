from ..classes import  ten_shoot_in_row_achievement , perfect_shooter_medal
from .four_decker_sniper import list_save_coords_achiv

#2 задание

shoots = []
def ten_shoot_in_row(cell: int):
    count_shoots = 0
    shoots.append(cell)

    for check_cell in shoots:
        if check_cell != 0 and check_cell != 5:
            count_shoots += 1
        else:
            shoots.clear()
            return False
    
    if count_shoots >= 10 and "True" not in shoots:
        shoots.append("True")
        ten_shoot_in_row_achievement.ACTIVE = True
        perfect_shooter_medal.ACTIVE = True
        list_save_coords_achiv.append((2))
        print("10 выстрелов по кораблям подряд")



