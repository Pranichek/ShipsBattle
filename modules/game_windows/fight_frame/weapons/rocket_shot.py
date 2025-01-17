import modules.shop as shop
import modules.server as server_module
import modules.client as client_module
import modules.achievement as achievement
from ....screens import list_object_map_enemy
from ....classes.class_click import miss_water_sound, shot_sound
from ....screens import enemy_matrix
from ....client import list_check_need_send, data_player_shot
from ....game_tools import count_money_hit


def simple_shot(row: int, col: int, cell: int, x_hit_the_ship: list, y_hit_the_ship: list, flag_miss_rocket_animation: list, check_animation_rocket: list):
    """
    Ця функція для простого пострілу гравця
    """
    if enemy_matrix != "yes":
        if shop.third_task.TEXT == shop.list_third_task[1]:
            shop.single_ships.append(enemy_matrix[row][col])
        if shop.fourth_task.TEXT == shop.list_fourth_task[0]:
            shop.first_shot_is_kill(cell = enemy_matrix[row][col])
        if shop.third_task.TEXT == shop.list_third_task[2]:
            shop.check_three_2decker_ship_in_row.append(enemy_matrix[row][col])
        if shop.first_task.TEXT == shop.list_first_task[-1]:
            shop.three_hits_in_row(cell = enemy_matrix[row][col])
        if shop.third_task.TEXT == shop.list_third_task[-1]:
            shop.count_three_ships.append(enemy_matrix[row][col])
        if shop.second_task.TEXT == shop.list_second_task[2]:
            shop.ship_hits.append(enemy_matrix[row][col])
        if shop.fourth_task.TEXT == shop.list_fourth_task[1]:
            shop.ship_hits_three.append(enemy_matrix[row][col])
        # ачивки
        achievement.ten_shoot_in_row(cell = enemy_matrix[row][col])
        achievement.first_shot(cell = enemy_matrix[row][col])
        achievement.single_ships_achiv.append(enemy_matrix[row][col])
        achievement.list_hits_achiv.append(enemy_matrix[row][col])
        
        # якщо гравець натиснув на пусту клітинку , то у матрицю ворога записуємо цифру 5
        # 5 - значить , що гравець зробив постріл , але схибив його
        if enemy_matrix[row][col] == 0:
            data_player_shot.append("rocket_shot")
            data_player_shot.append(str(row))
            data_player_shot.append(str(col))
            list_check_need_send[0] = True
            # передаем в список котором храним флаг о том нужно ли запускать анимацию промаха ракетой флаг который запустит эту анимацию
            flag_miss_rocket_animation[0] = "start_animation"
            # передаем в список координаты клетки в которую ударили , чтобы в этой же клеточке мы и отрисовывали анимацию
            x_hit_the_ship[0] = list_object_map_enemy[list_object_map_enemy.index(cell)].x
            y_hit_the_ship[0] = list_object_map_enemy[list_object_map_enemy.index(cell)].y
            # записуємо у матрицю ворога 5
            print(enemy_matrix, "enemy_matrix")
            enemy_matrix[row][col] = 5
            # обнуляємо час для ходу
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
            if server_module.list_player_role[0] == "server_player":
                server_module.turn[0] = "client_turn"
            else:
                server_module.turn[0] = "server_turn"
            server_module.check_time[0] = 0

        # робимо умову для випадку коли по клітичнці вже били
        elif enemy_matrix[row][col] == 5 or enemy_matrix[row][col] == 7:
            print("Уже стреляли в эту клетку")
        # якщо гравець зробив постріл , і попав по кораблю , то у матрицю ворога запсиуємо 7
        # 7 - значить , що гравець зробив постріл і попав по кораблю
        elif enemy_matrix[row][col] != 0 and enemy_matrix[row][col] != 5 and enemy_matrix[row][col] != 7:
            data_player_shot.append("rocket_shot")
            data_player_shot.append(str(row))
            data_player_shot.append(str(col))
            list_check_need_send[0] = True
            count_money_hit[0] += 10
            # передаем в список где хранится флаг нужно ли отрисовывать анимацию удара "start_animation" - то есть надо
            check_animation_rocket[0] = "start_animation"
            # передаем в список координаты клетки в которую ударили , чтобы в этой же клеточке мы и отрисовывали анимацию
            x_hit_the_ship[0] = list_object_map_enemy[list_object_map_enemy.index(cell)].x
            y_hit_the_ship[0] = list_object_map_enemy[list_object_map_enemy.index(cell)].y
            shot_sound.play2(loops = 1)
            # у матрицю ворога записуємо 7
            enemy_matrix[row][col] = 7
            # обнуляємо час для ходу
            if server_module.list_player_role[0] == "player_client":
                client_module.list_check_need_send[0] = "yes"
                server_module.turn[0] = "client_turn"   
            if shop.first_task.TEXT == shop.list_first_task[0]:
                shop.two_hits_in_row(number_cell = 7)
            if shop.first_task.TEXT == shop.list_first_task[1]:
                shop.four_hits_in_row(number_cell = 7)
            if shop.fourth_task.TEXT == shop.list_fourth_task[-1]:
                shop.eight_hits_in_row(number_cell = 7)
            if server_module.list_player_role[0] == "server_player":
                server_module.turn[0] = "server_turn"
            else:
                server_module.turn[0] = "client_turn"
            server_module.check_time[0] = 0