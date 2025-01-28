import random
import modules.shop as shop
import modules.achievement as achievement
from ....screens import enemy_matrix
from ....client import list_check_need_send, data_player_shot
from ....server import check_time, list_player_role, turn


def random_hits_matrix():
    count_hit = 0
    shots = 0  # Лічильник ударів
    available_cells = []  # Список координат доступних клітинок (рядок, стовпець)
    data_player_shot.append("random_hits")  
    count_ships = []
    count_7 = [0]
    # Збираємо всі доступні клітинки
    for row in range(10):
        for col in range(10):
            if enemy_matrix[row][col] in [1, 2, 3, 4, 0]:  # Доступні для удару
                available_cells.append((row, col))
    
    # Виконуємо до 5 ударів, якщо є доступні клітинки
    while shots < 3 and available_cells:
        # Випадково вибираємо клітинку з доступних
        row, col = random.choice(available_cells)
        data_player_shot.append(row)
        data_player_shot.append(col)
        available_cells.remove((row, col))  # Видаляємо вибрану клітинку зі списку

        # Змінюємо значення залежно від попадання
        if enemy_matrix[row][col] in [1, 2, 3, 4]:  # Влучання
            count_hit += 1
            count_7[0] += 1
            count_ships.append(enemy_matrix[row][col])
            enemy_matrix[row][col] = 7
        else:  # Мимо
            enemy_matrix[row][col] = 5
        
        shots += 1  # Збільшуємо кількість ударів
    check_time[0] = 0  
    if count_hit >= 1:
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
            for hit in range(0, count_7[0]):
                shop.three_hits_in_row(7)
        if shop.third_task.TEXT == shop.list_third_task[-1]:
            shop.count_three_ships.extend(count_ships)
        if shop.second_task.TEXT == shop.list_second_task[2]:
            shop.ship_hits.extend(count_ships)
        if shop.fourth_task.TEXT == shop.list_fourth_task[1]:
            shop.ship_hits_three.extend(count_ships)
        if shop.first_task.TEXT == shop.list_first_task[0]:
            for hit in range(0, count_7[0]):
                shop.two_hits_in_row(number_cell = 7)
        if shop.first_task.TEXT == shop.list_first_task[1]:
            for hit in range(0, count_7[0]):
                shop.four_hits_in_row(number_cell = 7)
        if shop.fourth_task.TEXT == shop.list_fourth_task[-1]:
            for hit in range(0, count_7[0]):
                shop.eight_hits_in_row(number_cell = 7)
        # ачивки
        for hit in range(0, count_7[0]):
            achievement.ten_shoot_in_row(7)
        achievement.first_shot(7)
        achievement.single_ships_achiv.append(count_ships)
        achievement.list_hits_achiv.append(count_ships)
        if list_player_role[0] == "server_player":
            turn[0] = "server_turn"
        elif list_player_role[0] == "client_player":
            turn[0] = "client_turn"
    else:
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
        if list_player_role[0] == "server_player":
            turn[0] = "client_turn"
        elif list_player_role[0] == "client_player":
            turn[0] = "server_turn"

    

    