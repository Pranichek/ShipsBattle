r'''
Модуль, который содержит в себе функцию для :mod:`Защиты корабля`
'''
# Необходимые импорты
from ....screens.grid_list import list_grid, enemy_matrix
import modules.server as server_module 
from ....server import  turn
from ....client import list_check_need_send, data_player_shot, list_check_need_send, check_two_times

# Флаг для отправление данных 
flag_hit_shield = [False]


def shield_func(row: int, col: int):
    r'''
    `Функция` для обработки установки щита для заданной роли игрока.

    `Параметры:`
    - :mod:`role`: Роль игрока (client_player или server_player).
    - :mod:`row`: Номер строки в матрице.
    - :mod:`col`: Номер столбца в матрице.
    - :mod:`shipik`: Значение корабля, на который устанавливается щит.
    
    '''
    if list_grid[row][col] != 0 and list_grid[row][col] != 5 and list_grid[row][col] != 7 and list_grid[row][col] != 6:
        shipik = list_grid[row][col]
    
        # Если очередь "клиента" ( что бы не рушить логику игры, Вова решил сохранить такую методику )
        if server_module.list_player_role[0] == "client_player":
            # Мы опять еж записываем У НЕГО в матрице 6
            list_grid[row][col] = 6
            # Формируем флаг 
            flag_hit_shield[0] = "place_shield"

            # Отправляем данные через метод extend, так же записывая всё в виде строки

            data_player_shot.append('shield')
            data_player_shot.append(flag_hit_shield[0])
            data_player_shot.append(str(row))
            data_player_shot.append(str(shipik))
            data_player_shot.append(str(col))
            print(data_player_shot[3])
            # Ставим флаг что надо отослать
            list_check_need_send[0] = True 
            # Оставляем ход у клиента   
            turn[0] = "client_turn" 

            # Обнуляем время
            check_two_times[0] =  1
        
        # Если очередь "сервера" то ничего особенного не меняем, всё тоже самое 
        if server_module.list_player_role[0] == "server_player":

            list_grid[row][col] = 6
            flag_hit_shield[0] = "place_shield"
            data_player_shot.append('shield')
            data_player_shot.append(flag_hit_shield[0])
            data_player_shot.append(str(row))
            data_player_shot.append(str(shipik))
            data_player_shot.append(str(col))
            print(f'Это флаг который мне нужен{data_player_shot[3]}')

            list_check_need_send[0] = True    
            turn[0] = "server_turn"
            check_two_times[0] = 1