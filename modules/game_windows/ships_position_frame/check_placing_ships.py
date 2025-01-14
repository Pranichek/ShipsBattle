from ...screens import list_grid
from ...json_functions import write_json

def connect_to_fight():
    count_zero = 0
    for row in list_grid:
        for cell in row:
            if cell == 0:
                count_zero += 1

    if count_zero == 80:
        print("You can connect to the game")
        dict_game_status = {
                "status": "You can connect to the game"
            }
    else:
        print("You can't connect to the game")
        dict_game_status = {
                "status": "You can't connect to the game"
            }
    write_json(filename = "status_connect_game.json" , object_dict = dict_game_status)