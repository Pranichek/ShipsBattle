from ..classes import DrawImage , ten_shoot_in_row_achievement
from .four_decker_sniper import list_save_coords_achiv


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
        medal_ten_shoot_in_row.y_cor = 24
        ten_shoot_in_row_achievement.ACTIVE = True
        list_save_coords_achiv.append((2 , medal_ten_shoot_in_row.x_cor , medal_ten_shoot_in_row.y_cor))
        print("10 выстрелов по кораблям подряд")



medal_ten_shoot_in_row = DrawImage(
    x_cor = 888 ,
    y_cor = -50,
    width = 50 ,
    height = 50 ,
    folder_name = "achievement",
    image_name = "perfect_shooter_medal.png"
)