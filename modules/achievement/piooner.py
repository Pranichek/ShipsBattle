from ..classes import DrawImage , piooner_achievement 
from .four_decker_sniper import list_save_coords_achiv , enemy_dies_ships_for_ahiv , player_died_ships_for_achiv



count_player_ships_achiv = [0]
count_enemy_kill_achiv = [0]
def piooner():
    if count_enemy_kill_achiv[0] != "You killes three ships in row":
        if enemy_dies_ships_for_ahiv[0] != "":
            count_player_ships_achiv[0] = len(enemy_dies_ships_for_ahiv[0])
            count_enemy_kill_achiv[0] = len(player_died_ships_for_achiv[0])

            if count_player_ships_achiv[0] == 1 and count_enemy_kill_achiv[0] == 0 and count_enemy_kill_achiv[0] != "You killes three ships in row":
                count_enemy_kill_achiv[0] = "You killes three ships in row"
                piooner_achievement.ACTIVE = True
                medal_fisr_kill_any_ship.y_cor = 24
                list_save_coords_achiv.append((8 , medal_fisr_kill_any_ship.x_cor , medal_fisr_kill_any_ship.y_cor))
                print("Ure")


medal_fisr_kill_any_ship = DrawImage(
    x_cor = 950 ,
    y_cor = -50,
    width = 100,
    height = 50,
    folder_name = "achievement",
    image_name = "pioneer_medal.png"
)

