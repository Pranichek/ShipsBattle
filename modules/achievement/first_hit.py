from ..classes import DrawImage , first_hit_achievement 
from .four_decker_sniper import list_save_coords_achiv 

count_shot = [0]
shoots = []
def first_shot(cell: int):
    count_shot[0] += 1
    shoots.append(cell)
    for shoot in shoots:
        if shoot == 0 or shoot == 5:
            return False
        else:
            if count_shot[0] == 1 and "True" not in shoots:
                shoots.append("True")
                first_hit_achievement.ACTIVE = True
                medal_hit_shoot.y_cor = 24
                list_save_coords_achiv.append((4 , medal_hit_shoot.x_cor , medal_hit_shoot.y_cor))

medal_hit_shoot = DrawImage(
    x_cor = 800,
    y_cor = -50,
    width = 50,
    height = 50,
    folder_name = "achievement",
    image_name = "first_hit_medal.png"
)