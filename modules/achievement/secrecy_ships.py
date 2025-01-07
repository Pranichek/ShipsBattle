from ..classes import DrawImage , master_of_disguist_achievement
from .four_decker_sniper import list_save_coords_achiv

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
        medal_secrecy_ships.y_cor = 64
        list_save_coords_achiv.append((6 , medal_secrecy_ships.x_cor , medal_secrecy_ships.y_cor))

medal_secrecy_ships = DrawImage(
    x_cor = 810 ,
    y_cor = -50,
    width = 50,
    height = 50,
    folder_name = "achievement",
    image_name = "master_of_disguist_medal.png"
)

