from ..classes import DrawImage , strategist_achievement 
from .four_decker_sniper import list_save_coords_achiv 

check_end_game = [0]
def strategist(player_killed_ships: list, role: str, winner: str):
    if check_end_game[0] != 13:
        if player_killed_ships != "yes":
            if len(player_killed_ships) == 0:
                if role == "server_player":
                    if winner == "win_server":
                        strategist_achievement.ACTIVE = True
                        strategist_medal.y_cor = 64
                        list_save_coords_achiv.append((3 , strategist_medal.x_cor , strategist_medal.y_cor))
                        check_end_game[0] = 13
                elif role == "player_client":
                    if winner == "win_client":
                        strategist_achievement.ACTIVE = True
                        strategist_medal.y_cor = 64
                        list_save_coords_achiv.append((3 , strategist_medal.x_cor , strategist_medal.y_cor))
                        check_end_game[0] = 13



strategist_medal = DrawImage(
    x_cor = 760 ,
    y_cor = -50,
    width = 50,
    height = 50,
    folder_name = "achievement",
    image_name = "strategist_medal.png"
)