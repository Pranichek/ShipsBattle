from ...screens import list_grid
from ...json_functions import write_json
import modules.server as server_module

def connect_to_fight():
    count_zero = 0
    for row in list_grid:
        for cell in row:
            if cell == 0:
                count_zero += 1
    enemy_zero = 0
    print(count_zero, enemy_zero)
    if count_zero == 80:
        dict_game_status = {
                "status": "fight"
            }
        write_json(filename = "status_connect_game.json" , object_dict = dict_game_status)
    elif count_zero >= 81:
        dict_game_status = {
                "status": "position ships"
            }
        write_json(filename = "status_connect_game.json" , object_dict = dict_game_status)