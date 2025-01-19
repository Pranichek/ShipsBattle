from ..classes import strategist_achievement , strategist_medal
from .four_decker_sniper import list_save_coords_achiv 
import modules.client as client_module
from ..game_tools import count_money_hit

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
                        check_end_game[0] = 13
                        client_module.data_player_shot.append("medal")
                        client_module.data_player_shot.append(3)
                        client_module.list_check_need_send[0] = True
                        count_money_hit[0] += 20
                elif role == "player_client":
                    if winner == "win_client":
                        strategist_achievement.ACTIVE = True
                        strategist_medal.ACTIVE = True
                        check_end_game[0] = 13
                        list_save_coords_achiv[0] = True
                        count_money_hit[0] += 20


