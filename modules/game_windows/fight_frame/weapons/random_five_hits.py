import random
from ....screens import enemy_matrix
from ....client import list_check_need_send, data_player_shot
from ....server import check_time, list_player_role, turn


def random_hits_matrix():
    count_hit = 0
    shots = 0  # Лічильник ударів
    available_cells = []  # Список координат доступних клітинок (рядок, стовпець)
    data_player_shot.append("random_hits")  
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
            enemy_matrix[row][col] = 7
        else:  # Мимо
            enemy_matrix[row][col] = 5
        
        shots += 1  # Збільшуємо кількість ударів
    list_check_need_send[0] = True
    check_time[0] = 0  
    if count_hit >= 1:
        if list_player_role[0] == "server_player":
            turn[0] = "server_turn"
        elif list_player_role[0] == "client_player":
            turn[0] = "client_turn"
    else:
        if list_player_role[0] == "server_player":
            turn[0] = "client_turn"
        elif list_player_role[0] == "client_player":
            turn[0] = "server_turn"

    

    