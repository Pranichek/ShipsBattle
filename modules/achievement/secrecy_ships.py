from ..classes import master_of_disguist_achievement, master_of_disguist_medal
from .four_decker_sniper import list_save_coords_achiv
from ..game_tools import count_money_hit
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
        list_save_coords_achiv[0] = True
        count_money_hit[0] += 20
