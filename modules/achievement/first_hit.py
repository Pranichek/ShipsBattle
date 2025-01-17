from ..classes import first_hit_achievement, first_hit_medal
from .four_decker_sniper import list_save_coords_achiv 
import modules.client as client_module

#4 медалька

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
                first_hit_medal.ACTIVE = True
                list_save_coords_achiv.append(4)
                client_module.data_player_shot.append("medal")
                client_module.data_player_shot.append(4)
                client_module.list_check_need_send[0] = True

