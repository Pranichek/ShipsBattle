from ...screens import list_grid
from ...json_functions import write_json
import modules.client as client_module

def connect_to_fight():
    count_zero = 0
    for row in list_grid:
        for cell in row:
            if cell == 0:
                count_zero += 1
    enemy_zero = 0
    if count_zero == 80:
        dict_game_status = {
                "status": "fight"
            }
        write_json(filename = "status_connect_game.json" , object_dict = dict_game_status)
        client_module.save_data_posistion_ships[0] = "fight"
    elif count_zero >= 81:
        dict_game_status = {
                "status": "position"
            }
        write_json(filename = "status_connect_game.json" , object_dict = dict_game_status)
        client_module.save_data_posistion_ships[0] = "position"