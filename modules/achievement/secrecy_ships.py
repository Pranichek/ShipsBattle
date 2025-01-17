from ..classes import master_of_disguist_achievement, master_of_disguist_medal
from .four_decker_sniper import list_save_coords_achiv
import modules.client as client_module

count_turns_achiv = [0]
save_sevens_achiv = []
def kept_all_ships_alive_for_ten_turns(grid: object):
    count_turns_achiv[0] += 1
    for row in range(len(grid)):
        for cell in range(len(grid[row])):
            if grid[row][cell] == 7 and (row * 10) + cell not in save_sevens_achiv:
                count_turns_achiv[0] = 0
                save_sevens_achiv.append((row * 10) + cell)

    if count_turns_achiv[0] >= 10 and "True" not in count_turns_achiv:
        count_turns_achiv.append("True")
        master_of_disguist_achievement.ACTIVE = True
        master_of_disguist_medal.ACTIVE = True
        list_save_coords_achiv.append(6)
        client_module.data_player_shot.append("medal")
        client_module.data_player_shot.append(6)
        client_module.list_check_need_send[0] = True
