from ..classes import strategist_achievement , strategist_medal
from .four_decker_sniper import list_save_coords_achiv 

#3 медалька

check_end_game = [0]
def strategist(player_killed_ships: list, role: str, winner: str):
    if check_end_game[0] != 13:
        if player_killed_ships != "yes":
            if len(player_killed_ships) == 0:
                if role == "server_player":
                    if winner == "win_server":
                        strategist_achievement.ACTIVE = True
                        strategist_medal.ACTIVE = True
                        list_save_coords_achiv.append((3))
                        check_end_game[0] = 13
                elif role == "player_client":
                    if winner == "win_client":
                        strategist_achievement.ACTIVE = True
                        strategist_medal.ACTIVE = True
                        list_save_coords_achiv.append(3)
                        check_end_game[0] = 13


