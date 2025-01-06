from ..classes import DrawImage , target_attack_achievement
from .four_decker_sniper import list_save_coords_achiv

target_medal_count = [0]
def show_target_attack_medal(flag):
    if flag == "Enemy did the target_attack achiv" and target_medal_count[0] == 0:
        target_medal_count[0] += 1
        target_attack_achievement.ACTIVE = True
        medal_target_attack.y_cor = 64
        list_save_coords_achiv.append((11 , medal_target_attack.x_cor , medal_target_attack.y_cor))

medal_target_attack = DrawImage(
    x_cor = 1100,
    y_cor = -50,
    width = 50,
    height = 50,
    folder_name = "achievement",
    image_name = "target_attack_medal.png"
)
