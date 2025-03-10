import modules.shop as shop
import modules.server as server_module
import modules.client as client_module
import random
from ....game_tools import count_money_hit
import modules.achievement as achievement
from ....classes.class_ship import list_ships
from ....screens import enemy_matrix
from ....classes.class_medal import magnat_medal

check_need_change_turn = [True]
def upgrade_attack(index : str, col: int, row: int, count_7: int, count_ships: list, count_misses: list, count_5: int):
    """
    `Функция` Для улучшение атаки, в диапозоне `3 на 3`

    (можно было без них, но уже слишком поздно)

    `Индексы` : Определяет тип области, где будет атака. Возможные значения:
    - :mod:`entry_cell` — центральная клетка
    - :mod:`'top_left_corner` — верхний левый угол
    - :mod:`bot_left_corner` — нижний левый угол
    - :mod:`left_wall` — левая стена
    - :mod:`top_right_corner` — верхний правый угол
    - :mod:`bot_right_corner` — нижний правый угол
    - :mod:`bot_wall` — нижняя стена
    - :mod:`top_wall` — верхняя стена
    - :mod:`right_wall` — правая стена

    `Параметры`
    - :mod:`col`: Колона на игровом поле, где происходит атака
    - :mod:`row`: Ряд на игровом поле, где происходит атака
    - :mod:`count_7`: Счётчик количества клеток, которые были обновлены в результате атаки (например, повреждённые корабли)
    - :mod:`count_ships`: Список для хранения информации о попаданиях в корабли (значения клеток поля)
    - :mod:`count_misses`: Список для хранения количества промахов
    - :mod:`count_5`: Счётчик количества обнаруженных защитных элементов (например, защитных полей)
    """
    check_need_change_turn[0] = True
    client_module.data_player_shot.append("bomb")
    if index == "entry_cell":
        for row_offset in range(-1, 2):
            for index_col in range(0, 3):
                current_row = row + row_offset
                current_col = col - 1 + index_col
                if enemy_matrix[current_row][current_col] in [1, 2, 3, 4]:
                    count_ships.append(enemy_matrix[current_row][current_col])
                    enemy_matrix[current_row][current_col] = 7
                    check_need_change_turn[0] = False
                    count_7[0] += 1
                    client_module.data_player_shot.extend((current_row,current_col))
                elif enemy_matrix[current_row][current_col] == 5:
                    count_5[0] += 1
                elif enemy_matrix[current_row][current_col] == 0 or enemy_matrix[current_row][current_col] == 5:
                    count_misses.append(0)
                    enemy_matrix[current_row][current_col] = 5
                    client_module.data_player_shot.extend((current_row,current_col))
    if index == "top_left_corner":
        for row_offset in range(0, 3):
            for index_col in range(0, 3):
                current_row = row + row_offset
                if enemy_matrix[current_row][col + index_col] in [1, 2, 3, 4]:
                    count_ships.append(enemy_matrix[current_row][col + index_col])
                    enemy_matrix[current_row][col  + index_col] = 7
                    count_7[0] += 1
                    check_need_change_turn[0] = False
                    client_module.data_player_shot.extend((current_row,col + index_col))
                elif enemy_matrix[current_row][col + index_col] == 5:
                    count_5[0] += 1
                elif enemy_matrix[current_row][col + index_col] == 0 or enemy_matrix[current_row][col + index_col] == 5:
                    count_misses.append(0)
                    enemy_matrix[current_row][col + index_col] = 5
                    client_module.data_player_shot.extend((current_row,col + index_col))

    if index == "bot_left_corner":
        for row_offset in range(0, 3):
            for index_col in range(0, 3):
                current_row = row - row_offset
                current_col = col + index_col
                if enemy_matrix[current_row][current_col] in [1, 2, 3, 4]:
                    count_ships.append(enemy_matrix[current_row][current_col])
                    enemy_matrix[current_row][current_col] = 7
                    count_7[0] += 1
                    check_need_change_turn[0] = False
                    client_module.data_player_shot.extend((current_row,current_col))
                elif enemy_matrix[current_row][current_col] == 5:
                    count_5[0] += 1
                elif enemy_matrix[current_row][current_col] == 0 or enemy_matrix[current_row][current_col] == 5:
                    count_misses.append(0)
                    enemy_matrix[current_row][current_col] = 5
                    client_module.data_player_shot.extend((current_row,current_col))
    
    if index == "left_wall":
        for row_offset in range(-1, 2):
            for index_col in range(0, 3):
                current_row = row + row_offset
                current_col = col + index_col
                if enemy_matrix[current_row][current_col] in [1, 2, 3, 4]:
                    count_ships.append(enemy_matrix[current_row][current_col])
                    enemy_matrix[current_row][current_col] = 7
                    count_7[0] += 1
                    check_need_change_turn[0] = False
                    client_module.data_player_shot.extend((current_row,current_col))
                elif enemy_matrix[current_row][current_col] == 5:
                    count_5[0] += 1
                elif enemy_matrix[current_row][current_col] == 0 or enemy_matrix[current_row][current_col] == 5:
                    count_misses.append(0)
                    enemy_matrix[current_row][current_col] = 5
                    client_module.data_player_shot.extend((current_row,current_col))
    
    if index == "top_right_corner":
        for row_offset in range(0, 3):
            for index_col in range(0, 3):
                current_row = row + row_offset
                if enemy_matrix[current_row][col - index_col] in [1, 2, 3, 4]:
                    count_ships.append(enemy_matrix[current_row][col - index_col])
                    enemy_matrix[current_row][col  - index_col] = 7
                    count_7[0] += 1
                    check_need_change_turn[0] = False
                    client_module.data_player_shot.extend((current_row,col - index_col))
                elif enemy_matrix[current_row][col - index_col] == 5:
                    count_5[0] += 1
                    client_module.data_player_shot.extend((row,col))
                elif enemy_matrix[current_row][col - index_col] == 0 or enemy_matrix[current_row][col - index_col] == 5:
                    count_misses.append(0)
                    enemy_matrix[current_row][col - index_col] = 5
                    client_module.data_player_shot.extend((current_row,col - index_col))
    if index == "bot_right_corner":
        for row_offset in range(0, 3):
            for index_col in range(0, 3):
                current_row = row - row_offset
                if enemy_matrix[current_row][col - index_col] in [1, 2, 3, 4]:
                    count_ships.append(enemy_matrix[current_row][col - index_col])
                    enemy_matrix[current_row][col  - index_col] = 7
                    count_7[0] += 1
                    check_need_change_turn[0] = False
                    client_module.data_player_shot.extend((current_row,col - index_col))
                elif enemy_matrix[current_row][col - index_col] == 5:
                    count_5[0] += 1
                elif enemy_matrix[current_row][col - index_col] == 0 or enemy_matrix[current_row][col - index_col] == 5:
                    count_misses.append(0)
                    enemy_matrix[current_row][col - index_col] = 5  
                    client_module.data_player_shot.extend((current_row,col - index_col))          

    if index == "bot_wall":
        for row_offset in range(0, 3):
            for index_col in range(0, 3):
                current_row = row - row_offset
                if enemy_matrix[current_row][col + index_col - 1] in [1, 2, 3, 4]:
                    count_ships.append(enemy_matrix[current_row][col + index_col - 1])
                    enemy_matrix[current_row][col + index_col - 1] = 7
                    count_7[0] += 1
                    check_need_change_turn[0] = False
                    client_module.data_player_shot.extend((current_row,col + index_col - 1))
                elif enemy_matrix[current_row][col + index_col - 1] == 5:
                    count_5[0] += 1
                elif enemy_matrix[current_row][col + index_col - 1] == 0 or enemy_matrix[current_row][col + index_col - 1] == 5:
                    count_misses.append(0)
                    enemy_matrix[current_row][col + index_col - 1] = 5
                    client_module.data_player_shot.extend((current_row,col + index_col - 1))
    if index == "top_wall":
        for row_offset in range(0, 3):
            for index_col in range(0, 3):
                current_row = row + row_offset
                if enemy_matrix[current_row][col + index_col - 1] in [1, 2, 3, 4]:
                    count_ships.append(enemy_matrix[current_row][col + index_col - 1])
                    enemy_matrix[current_row][col + index_col - 1] = 7
                    count_7[0] += 1
                    check_need_change_turn[0] = False
                    client_module.data_player_shot.extend((current_row,col + index_col - 1))
                elif enemy_matrix[current_row][col + index_col - 1] == 5:
                    count_5[0] += 1
                elif enemy_matrix[current_row][col + index_col - 1] == 0 or enemy_matrix[current_row][col + index_col - 1] == 5:
                    count_misses.append(0)
                    enemy_matrix[current_row][col + index_col - 1] = 5
                    client_module.data_player_shot.extend((current_row,col + index_col - 1))
    
    if index == "right_wall":
        for row_offset in range(-1, 2):
            for index_col in range(0, 3):
                current_row = row + row_offset
                if enemy_matrix[current_row][col - index_col] in [1, 2, 3, 4]:
                    count_ships.append(enemy_matrix[current_row][col - index_col])
                    enemy_matrix[current_row][col - index_col] = 7
                    count_7[0] += 1
                    check_need_change_turn[0] = False
                    client_module.data_player_shot.extend((current_row,col - index_col))
                elif enemy_matrix[current_row][col - index_col] == 5:
                    count_5[0] += 1
                elif enemy_matrix[current_row][col - index_col] == 0 or enemy_matrix[current_row][col - index_col] == 5:
                    count_misses.append(0)
                    enemy_matrix[current_row][col - index_col] = 5
                    client_module.data_player_shot.extend((current_row,col - index_col))
    client_module.data_player_shot.append(count_7[0])
    client_module.data_player_shot.append(count_5[0])
    if count_7[0] >= 1:
        server_module.check_time[0] = 0
        if server_module.list_player_role[0] == "server_player":
            server_module.turn[0] = "server_turn"
            # оскільки гравець не потрапив по кораблю , то змінюємо чергу ходу
        elif server_module.list_player_role[0] ==  "client_player":
            server_module.turn[0] = "client_turn"  # Передаємо хід серверу
    elif count_7[0] <= 0:
        server_module.check_time[0] = 0
        if server_module.list_player_role[0] == "server_player":
            server_module.turn[0] = "client_turn"
        elif server_module.list_player_role[0] ==  "client_player":
            server_module.turn[0] = "server_turn"
    client_module.list_check_need_send[0] = True

  

def bomb_shot(row: int, col:int, count_7: list, count_5,count_ships: list, count_misses: list, check_bomb:list):
    """
    Ця функція для удару бомбою
    """
    if row == 0 and col == 0:
        upgrade_attack(index = "top_left_corner", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = count_5)
    elif 0 < row < 9 and 0 < col < 9:
        upgrade_attack(index = "entry_cell", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = count_5)
    elif 1 <= row < 9 and col == 0:
        upgrade_attack(index = "left_wall", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = count_5)
    elif row == 9 and col == 0:
        upgrade_attack(index = "bot_left_corner", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = count_5)
    elif row == 0 and col == 9:
        upgrade_attack(index = "top_right_corner", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = count_5)          
    elif row == 9 and col == 9:
        upgrade_attack(index = "bot_right_corner", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = count_5)        
    elif row == 9 and 0 < col < 9:
        upgrade_attack(index = "bot_wall", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = count_5)
    elif row == 0 and 0 < col < 9:
        upgrade_attack(index = "top_wall", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = count_5)
    elif 0 < row < 9 and col == 9:
        upgrade_attack(index = "right_wall", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = count_5)
    
    if count_7[0] >= 1:
        count_money_hit[0] += 5
        check_bomb[0] = True
        if magnat_medal.ACTIVE == True:
            count_money_hit[0] += 15
        try:
            if shop.third_task.TEXT == shop.list_third_task[1]:
                shop.single_ships.extend(count_ships)
            if shop.fourth_task.TEXT == shop.list_fourth_task[0]:
                if 1 in count_ships:
                    shop.first_shot_is_kill(1)
                else:
                    shop.first_shot_is_kill(random.choice(count_ships))
            if shop.third_task.TEXT == shop.list_third_task[2]:
                shop.check_three_2decker_ship_in_row.extend(count_ships)
            if shop.first_task.TEXT == shop.list_first_task[-1]:
                shop.three_hits_in_row(7)
            if shop.third_task.TEXT == shop.list_third_task[-1]:
                shop.count_three_ships.extend(count_ships)
            if shop.second_task.TEXT == shop.list_second_task[2]:
                shop.ship_hits.extend(count_ships)
            if shop.fourth_task.TEXT == shop.list_fourth_task[1]:
                shop.ship_hits_three.extend(count_ships)
            if shop.first_task.TEXT == shop.list_first_task[0]:
                shop.two_hits_in_row(number_cell = 7)
            if shop.first_task.TEXT == shop.list_first_task[1]:
                shop.four_hits_in_row(number_cell = 7)
            if shop.fourth_task.TEXT == shop.list_fourth_task[-1]:
                shop.eight_hits_in_row(number_cell = 7)
            # ачивки
            achievement.ten_shoot_in_row(7)
            achievement.first_shot(7)
            achievement.single_ships_achiv.append(count_ships)
            achievement.list_hits_achiv.append(count_ships)
        except:
            pass
    elif count_7[0] <= 1:  # Передаємо хід серверу
        try:
            if shop.third_task.TEXT == shop.list_third_task[1]:
                shop.single_ships.append(0)
            if shop.fourth_task.TEXT == shop.list_fourth_task[0]:
                shop.first_shot_is_kill(0)
            if shop.third_task.TEXT == shop.list_third_task[2]:
                shop.check_three_2decker_ship_in_row.append(0)
            if shop.first_task.TEXT == shop.list_first_task[-1]:
                shop.three_hits_in_row(0)
            if shop.third_task.TEXT == shop.list_third_task[-1]:
                shop.count_three_ships.append(0)
            if shop.second_task.TEXT == shop.list_second_task[2]:
                shop.ship_hits.append(0)
            if shop.fourth_task.TEXT == shop.list_fourth_task[1]:
                shop.ship_hits_three.append(0)
            if shop.first_task.TEXT == shop.list_first_task[0]:
                shop.two_hits_in_row(number_cell = 5)
            if shop.first_task.TEXT == shop.list_first_task[1]:
                shop.four_hits_in_row(number_cell = 5)
            if shop.fourth_task.TEXT == shop.list_fourth_task[-1]:
                shop.eight_hits_in_row(number_cell = 5)
            # ачивки
            achievement.ten_shoot_in_row(5)
            achievement.first_shot(0)
            achievement.single_ships_achiv.append(0)
            achievement.list_hits_achiv.append(0)
        except:
            pass
    count_7[0] = 0
    count_ships.clear()
    count_misses.clear()