import modules.shop as shop
import modules.server as server_module
import modules.client as client_module
import modules.achievement as achievement
from ....screens import list_object_map_enemy
from ....classes.class_click import miss_water_sound


def simple_shot(row: int, col: int, cell: int, x_hit_the_ship: list, y_hit_the_ship: list, flag_miss_rocket_animation: list, check_animation_rocket: list):
    """
    Ця функція для простого пострілу гравця
    """
    if shop.third_task.TEXT == shop.list_third_task[1]:
        shop.single_ships.append(server_module.enemy_matrix[0][row][col])
    if shop.fourth_task.TEXT == shop.list_fourth_task[0]:
        shop.first_shot_is_kill(cell = server_module.enemy_matrix[0][row][col])
    if shop.third_task.TEXT == shop.list_third_task[2]:
        shop.check_three_2decker_ship_in_row.append(server_module.enemy_matrix[0][row][col])
    if shop.first_task.TEXT == shop.list_first_task[-1]:
        shop.three_hits_in_row(cell = server_module.enemy_matrix[0][row][col])
    if shop.third_task.TEXT == shop.list_third_task[-1]:
        shop.count_three_ships.append(server_module.enemy_matrix[0][row][col])
    if shop.second_task.TEXT == shop.list_second_task[2]:
        shop.ship_hits.append(server_module.enemy_matrix[0][row][col])
    if shop.fourth_task.TEXT == shop.list_fourth_task[1]:
        shop.ship_hits_three.append(server_module.enemy_matrix[0][row][col])
    # ачивки
    achievement.ten_shoot_in_row(cell = server_module.enemy_matrix[0][row][col])
    achievement.first_shot(cell = server_module.enemy_matrix[0][row][col])
    achievement.single_ships_achiv.append(server_module.enemy_matrix[0][row][col])
    achievement.list_hits_achiv.append(server_module.enemy_matrix[0][row][col])
    
    # якщо гравець натиснув на пусту клітинку , то у матрицю ворога записуємо цифру 5
    # 5 - значить , що гравець зробив постріл , але схибив його
    if server_module.enemy_matrix[0][row][col] == 0:
        # передаем в список котором храним флаг о том нужно ли запускать анимацию промаха ракетой флаг который запустит эту анимацию
        flag_miss_rocket_animation[0] = "start_animation"
        # передаем в список координаты клетки в которую ударили , чтобы в этой же клеточке мы и отрисовывали анимацию
        x_hit_the_ship[0] = list_object_map_enemy[list_object_map_enemy.index(cell)].x
        y_hit_the_ship[0] = list_object_map_enemy[list_object_map_enemy.index(cell)].y
        # записуємо у матрицю ворога 5
        server_module.enemy_matrix[0][row][col] = 5
        # обнуляємо час для ходу
        server_module.check_time[0] = 0
        if server_module.list_player_role[0] == "server_player":
            # оскільки гравець не потрапив по кораблю , то змінюємо чергу ходу
            server_module.turn[0] = "client_turn"
        elif server_module.list_player_role[0] ==  "player_client":
            client_module.list_check_need_send[0] = "yes"  # Готуємо дані для відправки
            server_module.turn[0] = "server_turn"  # Передаємо хід серверу
        if shop.first_task.TEXT == shop.list_first_task[0]:
            shop.two_hits_in_row(number_cell = 5)
        if shop.first_task.TEXT == shop.list_first_task[1]:
            shop.four_hits_in_row(number_cell = 5)
        if shop.fourth_task.TEXT == shop.list_fourth_task[-1]:
            shop.eight_hits_in_row(number_cell = 5)
        miss_water_sound.play2(loops = 1)

    # робимо умову для випадку коли по клітичнці вже били
    elif server_module.enemy_matrix[0][row][col] == 5 or server_module.enemy_matrix[0][row][col] == 7:
        print("Уже стреляли в эту клетку")
    # якщо гравець зробив постріл , і попав по кораблю , то у матрицю ворога запсиуємо 7
    # 7 - значить , що гравець зробив постріл і попав по кораблю
    elif server_module.enemy_matrix[0][row][col] != 0 and server_module.enemy_matrix[0][row][col] != 5 and server_module.enemy_matrix[0][row][col] != 7:
        # передаем в список где хранится флаг нужно ли отрисовывать анимацию удара "start_animation" - то есть надо
        check_animation_rocket[0] = "start_animation"
        # передаем в список координаты клетки в которую ударили , чтобы в этой же клеточке мы и отрисовывали анимацию
        x_hit_the_ship[0] = list_object_map_enemy[list_object_map_enemy.index(cell)].x
        y_hit_the_ship[0] = list_object_map_enemy[list_object_map_enemy.index(cell)].y
        # у матрицю ворога записуємо 7
        server_module.enemy_matrix[0][row][col] = 7
        # обнуляємо час для ходу
        server_module.check_time[0] = 0
        if server_module.list_player_role[0] == "player_client":
            client_module.list_check_need_send[0] = "yes"
            server_module.turn[0] = "client_turn"   
        if shop.first_task.TEXT == shop.list_first_task[0]:
            shop.two_hits_in_row(number_cell = 7)
        if shop.first_task.TEXT == shop.list_first_task[1]:
            shop.four_hits_in_row(number_cell = 7)
        if shop.fourth_task.TEXT == shop.list_fourth_task[-1]:
            shop.eight_hits_in_row(number_cell = 7)