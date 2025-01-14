from ...screens import list_grid
from ...json_functions import write_json
import modules.server as server_module

def connect_to_fight():
    if list_grid.count(0) == 80 and server_module.enemy_data[0]["grid"].count(0) == 80:
        dict_game_status = {
                "status": "fight"
            }
    elif list_grid.count(0) == 80:
        dict_game_status = {
                "status": "wait window"
            }
    write_json(filename = "status_connect_game.json" , object_dict = dict_game_status)