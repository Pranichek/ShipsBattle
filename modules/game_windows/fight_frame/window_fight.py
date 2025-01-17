import pygame, random
import modules.game_windows as game_windows
import modules.shop as shop
from ...screens import main_screen
from os.path import abspath, join
import modules.screens.screen as module_screen
import modules.server as server_module
import modules.achievement as achievement
import modules.classes.class_medal as class_medal
from ...game_tools import count_money
from ...screens import grid_player, list_object_map, list_object_map_enemy, enemy_grid, list_grid, enemy_matrix
from ...classes.class_music import music_load_waiting, fight_music
from ...classes.class_medal import player_medal, enemy_medals, target_attack_medal, destroyer_medal
from ...classes.class_image import DrawImage
from ...classes.achive_window import list_achieves, target_attack_achievement, destroyer_achievement
from ...classes.class_button import Button
from ...classes.class_text import Font
from ...classes.animation import Animation, rocket_animation, miss_rocket_animation, animation_boom, animation_bomb_boom, animation_health, bomb_animation, animation_connection_problem
from ...classes.class_ship import list_ships
from ...game_tools import player_balance_in_jar, enemy_balance_in_jar, ship_border, list_animation_miss, check_number_cell, Missile_200, kill_enemy_ships, list_cross, our_miss_anim, check_target_attack, count_money_hit
from ..change_window import change_scene
from ...client import list_check_need_send, check_two_times, send_matrix, dict_save_information, data_player_shot 
from .weapons import simple_shot, bomb_shot, restore_part_of_ship
from .animations_on_grid import update_enemy_matrix_animations, check_and_add_hit_markers

list_check_shop = [None]
def show_shop():
    if shop.shop_item[0].TURN == "Down": 
        list_check_shop[0] = True

# функция для отчистки активации оружия(того что кпуил пользователь)
def clear_weapon_function():
    activate_auto_rocket[0] = False
    activate_restore_cell[0] = False
    activate_bomb[0] = False
    active_product_shine.x_cor = -100
    active_product_shine.y_cor = -100

# картинка курсора
cursor_image = pygame.transform.scale(pygame.image.load(abspath(join(__file__, "..", "..", "..", "..", "media", "decorations", "cursor.png"))), (32, 32))
cursor_img_rect = cursor_image.get_rect()

#images
grid_image = DrawImage(width = 662  , height = 662 , x_cor = 40 , y_cor = 37 , folder_name = "grid", image_name = "background_grid.png")
player_face = DrawImage(width = 154 , height = 123 ,x_cor = 1104 , y_cor = 79 , folder_name = "decorations" , image_name = "active_player.png")
enemy_face = DrawImage(width = 154 , height = 123  ,x_cor = 20 , y_cor = 79 , folder_name = "decorations" , image_name = "not_active_enemy.png")
fight_bg = DrawImage(width = 1280,height = 832 , x_cor = 0 , y_cor = 0 , folder_name= "backgrounds" , image_name= "fight_background.png")
shadow_data_user = DrawImage(x_cor = -28 , y_cor = -95 , width = 1351 , height = 236 , folder_name = "decorations" , image_name = "shadow_user_data.png")
user_weapon = DrawImage(x_cor = 1046 , y_cor = -26 , width = 260 , height = 135 , folder_name = "backgrounds" , image_name = "user_weapon.png")
player_jar = DrawImage(x_cor = 1190 , y_cor = 18 , width = 90 , height = 76 , folder_name = "decorations" , image_name = "jar_balance.png")
enemy_jar = DrawImage(x_cor = 102 , y_cor = 18 , width = 90 , height = 76 , folder_name = "decorations" , image_name = "jar_balance.png")
clock_image = DrawImage(width = 206 , height = 57 , x_cor = 544 , y_cor = 20 , folder_name = "animation_clock" , image_name = "0.png")
grid_image_for_enemy = DrawImage(width = 596  , height = 597 , x_cor = 23 , y_cor = 211 , folder_name = "grid", image_name = "background_grid.png")
#products icons
bomb_icon = DrawImage(x_cor = 1104, y_cor = 64, width = 27, height = 26, folder_name = "products_icons" , image_name = "bomb_icon.png")
auto_rocket_icon = DrawImage(x_cor = 1137, y_cor = 58, width = 45.54, height = 40.09, folder_name = "products_icons", image_name = "auto_rocket_icon.png")
restore_cell_icon = DrawImage(x_cor = 1147, y_cor = 23, width = 31, height = 28.4, folder_name = "products_icons", image_name = "restore_cell_icon.png")
# сияние которое подсвечивает активаное оружие
active_product_shine = DrawImage(x_cor = -100, y_cor = -100, width = 60, height = 60, folder_name = "decorations", image_name = "shine_for_weapon.png")
frame_nick_player = DrawImage(width = 362 ,height = 69 , x_cor = 222 , y_cor = 116 , folder_name= "backgrounds" , image_name= "frame_nick.png")
second_frame_nick_player = DrawImage(width = 362 ,height = 69 , x_cor = 699 , y_cor = 116 , folder_name= "backgrounds" , image_name= "frame_nick.png")

#fonts
player_nick = Font(size = 48 , name_font= "Jersey15.ttf" , text = dict_save_information["player_nick"] , screen = module_screen.main_screen , x_cor = 914 , y_cor = 126, text_color = "White")
enemy_nick = Font(size = 48 , name_font= "Jersey15.ttf" , text = dict_save_information["enemy_nick"] , screen = module_screen.main_screen , x_cor = 437 , y_cor = 126, text_color = "White")
player_points = Font(size = 48 , name_font= "Jersey15.ttf" , text = str(dict_save_information["player_points"]) , screen = module_screen.main_screen , x_cor = 743 , y_cor = 126, text_color = "White")
enemy_points = Font(size = 48 , name_font= "Jersey15.ttf" , text = str(dict_save_information["enemy_points"]) , screen = module_screen.main_screen , x_cor = 270 , y_cor = 126, text_color = "White")
#Buttons
shop_and_tasks = Button(x= 33 , y = 32,image_path= "show_shop.png" , image_hover_path= "show_shop_hover.png" , width = 36, height = 31 , action = show_shop)
clear_weapon = Button(x = 1064, y = 8, image_path = "clear_weapon.png" , image_hover_path = "clear_weapon_hover.png" , width = 109, height = 13, action = clear_weapon_function)


screen_shake = [0]

list_check_shop = [None]
def show_shop():
    if shop.shop_item[0].TURN == "Down": 
        list_check_shop[0] = True


flag_upgrade = [True]
def upgrade_flag():
    flag_upgrade[0] = True

# функция которая отрисовывает сетку при авто-ударе
def draw_cursor(screen, mouse_x, mouse_y, grid, color=(0, 255, 0), grid_width=5, grid_height=5, cell_size=55):
    # Привязываем центральную точку курсора к сетке
    snapped_x, snapped_y = grid.snap_to_grid_enemy(mouse_x, mouse_y)
    # Вычисляем координаты левого верхнего угла сетки 5x5
    rect_x = snapped_x - (grid_width // 2) * cell_size
    rect_y = snapped_y - (grid_height // 2) * cell_size
    center_x = rect_x +137
    center_y = rect_y +137
    xxxx = grid.coordinates_to_number(center_x, center_y)

    # Рисуем сетку
    for row in range(grid_height):
        for col in range(grid_width):
            cell_rect = pygame.Rect(
                rect_x + col * cell_size,
                rect_y + row * cell_size,
                cell_size,
                cell_size
            )
            pygame.draw.rect(screen, color, cell_rect, 1)

    return center_x, center_y


# флаг для анимации аптечки
health_anim = [False]
# списки в которых хранятся координаты крестиков , если враг попал по кораблю игрока
x_enemy_cross = [0]
y_enemy_cross = [0]
#------------------------------------------------------------------------------------------------
#флаг который говорит надо ли запускать анимация промаха ракеты, если игрок уларил но промахнулся
flag_miss_rocket_animation = [""]
# флаг который говорит надо ли запускать анимацию зачеркивания клеточки , если игрок промахнулся по кораблю
check_animation_miss_cell = [""]

#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------
# флаг который првоеряет надо ли запускать анимацию ракеты если игрок ударил
check_animation_rocket = [""]
# флаг когда надо проигрывать анимацию крестика если попали по кораблю
check_cross_animation  = [""]
#------------------------------------------------------------------------------------------------
# спсики в которых хранятся координаты где должны отрисовываться анимации если игрок ударил по полю
x_hit_the_ship = [0]
y_hit_the_ship = [0]

# спсиок где хранятся крестки которые ресуюются если враг попал по кораблю игрока
list_cross_player = []

check_achiv = [False]
index_achiv = [100]

numberofbim = [""]
# списки которые проверяют нажал ли пользователь на использования своего оружия
activate_auto_rocket = [False]
activate_restore_cell = [False]
activate_bomb = [False]
#----------------------------------------------------------------
#для бомбы чтобы считать сколько клеточек в радиусе 3х3 было 5
count_5 = [0]
#для ачивки убить два или больше корабля одной бомбой
old_killed_ships = [0]
new_killed_ships = [0]
check_bomb = [False]

# для сравнения изменился ли нашь баланс
check_player_balance = [0]

# для ачивок на выживвание раундов
check_alive_ten = [False]
check_alive_five = [False]
# функція для бою між гравцями
def fight_window():
    # зупиняємо музику яка грала перед боєм
    music_load_waiting.stop()
    # вмикаємо музику для бою
    fight_music.play()
    # задаємо назву вікну
    pygame.display.set_caption("Battle Screen")
    # створюємо змінну для нескінченого циклу гри
    run_game = True

    # створюємо дві сітки для гри(нашу та ворога) , ці сітки просто як звичайний малюнок
    enemy_grid.X_SCREEN = 67
    enemy_grid.Y_SCREEN = 257
    enemy_grid.generate_grid(width_cell=55, height_cell=55)

    grid_player.X_SCREEN = 705
    grid_player.Y_SCREEN = 257
    grid_player.generate_grid(width_cell=55, height_cell=55)


    # оновлюємо координати кораблів , та їхній розмір , щоб можна було відмалювати на сітці
    for num , ship  in enumerate(list_ships):
        grid_x = list_ships[num].col
        grid_y = list_ships[num].row
        list_ships[num].X_COR = grid_player.X_SCREEN + grid_x * 55
        list_ships[num].Y_COR = grid_player.Y_SCREEN + grid_y * 55
        list_ships[num].WIDTH = 55
        list_ships[num].HEIGHT = 55
        list_ships[num].load_image()

    # Завантажуємо картинку для сітки , по якій можемо ореєнутватися куди бити(тобто A1 , B9 і тд)
    grid_image.width = 597
    grid_image.height = 597
    grid_image.x_cor = 659
    grid_image.y_cor = 211
    grid_image.load_image()

    # оновлюємо дані про ник та бали гравців
    player_nick.text = dict_save_information["player_nick"]
    enemy_nick.text = dict_save_information["enemy_nick"]
    player_points.text = str(dict_save_information["player_points"])
    enemy_points.text = str(dict_save_information["enemy_points"])
    player_nick.update_text()
    enemy_nick.update_text()
    player_points.update_text()
    enemy_points.update_text()
    send_matrix()
    while run_game:
        module_screen.FPS.tick(60)
        #----------------------------------------------------------------
        ship_border()
        #----------------------------------------------------------------
        kill_enemy_ships()
        if len(server_module.enemy_died_ships) > 0:
            achievement.player_died_ships_for_achiv[0] = server_module.player_died_ships
            achievement.enemy_dies_ships_for_ahiv[0] = server_module.enemy_died_ships
        for medal in range(0 , len(server_module.save_medals_coordinates)):
            if server_module.save_medals_coordinates[medal] == 1:
                class_medal.enemy_four_decker_sniper_medal.ACTIVE = True
            elif server_module.save_medals_coordinates[medal] == 2:
                class_medal.enemy_perfect_shooter_medal.ACTIVE = True
            elif server_module.save_medals_coordinates[medal] == 3:
                class_medal.enemy_strategist_medal.ACTIVE = True
            elif server_module.save_medals_coordinates[medal] == 4:
                class_medal.enemy_first_hit_medal.ACTIVE= True
            elif server_module.save_medals_coordinates[medal] == 6:
                class_medal.enemy_master_of_disguist_medal.ACTIVE = True
            elif server_module.save_medals_coordinates[medal] == 7:
                class_medal.enemy_lone_hunter_medal.ACTIVE = True
            elif server_module.save_medals_coordinates[medal] == 8:
                class_medal.enemy_pioneer_medal.ACTIVE = True
            elif server_module.save_medals_coordinates[medal] == 9:
                class_medal.enemy_destroyer_medal.ACTIVE = True
            elif server_module.save_medals_coordinates[medal] == 10:
                class_medal.enemy_opening_battle_medal.ACTIVE = True
            elif server_module.save_medals_coordinates[medal] == 11:
                class_medal.enemy_target_attack_medal.ACTIVE = True
            elif server_module.save_medals_coordinates[medal] == 12:
                class_medal.enemy_collector_medal = True

        if check_two_times.count(3) >= 2:
            server_module.check_time[0] += 1
            check_two_times.clear()

        if len(server_module.enemy_data) > 0:
            check_data = server_module.enemy_data[0].split(' ')
            #"rocket_shot 3 1"
            #["rocket_shot", "3", "1" , " "]
            if check_data[0] == "enemy_matrix":
                check_list = server_module.enemy_data[0].split(' ')
                row = 0
                column = 0
                for str_number in check_list[1:101]:
                    enemy_matrix[row][column] = int(str_number)
                    column += 1
                    if column == 10:
                        row += 1
                        column = 0
                for data_ship in range(101, len(check_list) - 1, 4):
                    server_module.enemy_ships.append((int(check_list[data_ship]), int(check_list[data_ship + 1]), int(check_list[data_ship + 2]), (check_list[data_ship + 3])))

            elif check_data[0] == "rocket_shot":
                if list_grid[int(check_data[1])][int(check_data[2])] in [1, 2, 3, 4, 7]:
                    if list_grid[int(check_data[1])][int(check_data[2])] == 7:
                        pass
                    else:
                        list_grid[int(check_data[1])][int(check_data[2])] = 7
                        server_module.check_time[0] = 0
                    if server_module.list_player_role[0] == "server_player":
                        server_module.turn[0] = "client_turn"
                    elif server_module.list_player_role[0] == "client_player":
                        server_module.turn[0] = "server_turn"
                else:
                    list_grid[int(check_data[1])][int(check_data[2])] = 5
                    server_module.check_time[0] = 0
                    if server_module.list_player_role[0] == "server_player":
                        server_module.turn[0] = "server_turn"
                    elif server_module.list_player_role[0] == "client_player":
                        server_module.turn[0] = "client_turn"
            elif check_data[0] == "restore_cell":
                enemy_matrix[int(check_data[2])][int(check_data[3])] = int(check_data[1])
            elif check_data[0] == "bomb_shot":
                for cell in range(1 , 19):
                    try:
                        if cell % 2 == 0:
                            if list_grid[int(check_data[cell - 1])][int(check_data[cell])] in [1, 2, 3, 4, 7]:
                                if list_grid[int(check_data[cell - 1])][int(check_data[cell])] == 7:
                                    pass
                                else:
                                    list_grid[int(check_data[cell - 1])][int(check_data[cell])] = 7
                            elif list_grid[int(check_data[cell - 1])][int(check_data[cell])] in [0, 5]:
                                list_grid[int(check_data[cell - 1])][int(check_data[cell])] = 5
                    except:
                        continue
                if int(check_data[-3]) == 0:
                    if server_module.list_player_role[0] == "server_player":
                        server_module.turn[0] = "server_turn"
                    elif server_module.list_player_role[0] == "client_player":
                        server_module.turn[0] = "client_turn"
                else:
                    if server_module.list_player_role[0] == "server_player":
                        server_module.turn[0] = "client_turn"
                    elif server_module.list_player_role[0] == "client_player":
                        server_module.turn[0] = "server_turn"
                server_module.check_time[0] = 0
            elif check_data[0] == "auto_rocket":
                index_cell = 1
                count_hit = 0
                for cell in check_data[1:-1]:
                    if index_cell % 2 == 0:
                        if list_grid[int(check_data[index_cell - 1])][int(check_data[index_cell])] in [1, 2, 3, 4, 7]:
                            count_hit += 1
                            if list_grid[int(check_data[index_cell - 1])][int(check_data[index_cell])] == 7:
                                pass
                            else:
                                list_grid[int(check_data[index_cell - 1])][int(check_data[index_cell])] = 7
                        elif list_grid[int(check_data[index_cell - 1])][int(check_data[index_cell])] in [0, 5]:
                            list_grid[int(check_data[index_cell - 1])][int(check_data[index_cell])] = 5
                    index_cell += 1
                if count_hit == 0:
                    if server_module.list_player_role[0] == "server_player":
                        server_module.turn[0] = "server_turn"
                    elif server_module.list_player_role[0] == "client_player":
                        server_module.turn[0] = "client_turn"
                elif count_hit >= 1:
                    if server_module.list_player_role[0] == "server_player":
                        server_module.turn[0] = "client_turn"
                    elif server_module.list_player_role[0] == "client_player":
                        server_module.turn[0] = "server_turn"
                server_module.check_time[0] = 0
            elif check_data[0] == "medal":
                for medal in check_data[1:-1]:
                    print(check_data[1:-1])
                    if int(medal) not in server_module.save_medals_coordinates:
                        server_module.save_medals_coordinates.append(int(medal))
            elif check_data[0] == "money":
                server_module.enemy_balance[0] = int(check_data[1])
                enemy_balance_in_jar.update_text()

        
        # обнуление времени и хода, если игрок не походил
        if server_module.check_time[0] >= 30:
            server_module.check_time[0] = 0
            if server_module.list_player_role[0] == "server_player":
                if server_module.turn[0] == "server_turn":
                    server_module.turn[0] = "client_turn"
                else:
                    server_module.turn[0] = "server_turn"
            if server_module.list_player_role[0] == "client_player":
                if server_module.turn[0] == "client_turn":
                    server_module.turn[0] = "server_turn"
                else:
                    server_module.turn[0] = "client_turn"

        achievement.opening_the_battle(grid = list_grid , enemy_grid = enemy_matrix)

        if server_module.check_time[0] == 0 and check_alive_ten[0] == True:
            check_alive_ten[0] = False
            check_alive_five[0] = False

        if (server_module.list_player_role[0] == "server_player" and server_module.turn[0] == "client_turn") or (server_module.list_player_role[0] == "client_player" and server_module.turn[0] == "server_turn"):
            if server_module.check_time[0] == 1 and not check_alive_ten[0]:
                if shop.second_task.TEXT == shop.list_second_task[1]:
                    achievement.kept_all_ships_alive_for_ten_turns(grid = list_grid)
                    check_alive_ten[0] = True
        if (server_module.list_player_role[0] == "server_player" and server_module.turn[0] == "client_turn") or (server_module.list_player_role[0] == "client_player" and server_module.turn[0] == "server_turn"):
            if server_module.check_time[0] == 1 and not check_alive_five[0]:
                if shop.second_task.TEXT == shop.list_second_task[1]:
                    shop.kept_all_ships_alive_for_five_turns(grid = list_grid)
                    check_alive_five[0] = True

        # отправка полученных медалек врагу
        if achievement.list_save_coords_achiv[0] == True and len(data_player_shot) == 0:
            data_player_shot.append("medal")
            for medals in achievement.list_save_coords_achiv[1:]:
                data_player_shot.append(medals)
            list_check_need_send[0] = True
            achievement.list_save_coords_achiv[0] = False
            

        #----------------------------------------------------------------
        # код который раньше был на серваке и клиенте , теперь тут
        # try:
        #     if screen_module.enemy_matrix == "yes":
        #         if server_module.list_player_role[0] == "server_player":
        #             screen_module.enemy_matrix = server_module.enemy_data[0]["client_matrix"]
        #         elif server_module.list_player_role[0] == "client_player":
        #             screen_module.enemy_matrix = server_module.enemy_data[0]["server_matrix"]

        #     if server_module.check_repeat[0] >= 2:
        #         for ship in list_ships:
        #             server_module.player_ships_coord_len.append((ship.X_COR, ship.Y_COR, ship.LENGHT, ship.ORIENTATION_SHIP))

        #     if screen_module.enemy_matrix != "yes":
        #         # счетчик кораблей сервера
        #         count_player_ships = 0
        #         # счетчик кораблей клиента
        #         count_enemy_ships = 0
        #         # делаем перебор матриц сервера и клиента, чтобы проверять ввыиграл уже кто то или нет
        #         for row_server in range(len(list_grid)):
        #             for cell_server in range(len(list_grid[row_server])):
        #                 # 5 - по клетке уже стреляли
        #                 # 0 - кораблей просто нет
        #                 # 7 - уже потопленный корабль
        #                 if list_grid[row_server][cell_server] in [1, 2, 3, 4]:
        #                     count_player_ships += 1

        #         for row_client in range(len(screen_module.enemy_matrix)):
        #             for cell_client in range(len(screen_module.enemy_matrix[row_client])):
        #                 # 5 - по клетке уже стреляли
        #                 # 0 - кораблей просто нет
        #                 # 7 - уже потопленный корабль
        #                 if screen_module.enemy_matrix[row_client][cell_client] in [1, 2, 3,4]:
        #                     count_enemy_ships += 1

        #         # achievement.target_attack()
        #         if count_player_ships == 0 and count_enemy_ships > 0:
        #             if server_module.list_player_role[0] == "server_player":
        #                 # список для хранения кто выиграл
        #                 server_module.list_check_win[0] = "win_client"
        #             elif server_module.list_player_role[0] == "client_player":
        #                 server_module.list_check_win[0] = "win_server"
        #         elif count_enemy_ships == 0 and count_player_ships > 0:
        #             if server_module.list_player_role[0] == "server_player":
        #                 # список для хранения кто выиграл
        #                 server_module.list_check_win[0] = "win_server"
        #             elif server_module.list_player_role[0] == "client_player":
        #                 server_module.list_check_win[0] = "win_client"

        #     server_module.enemy_ships[0] = server_module.enemy_data[0]["player_ships"]

        #     # для восстановления клеточки
        #     if server_module.enemy_data[0]["row"] != 100:
        #         screen_module.enemy_matrix[server_module.enemy_data[0]["row"]][server_module.enemy_data[0]["col"]] = server_module.enemy_data[0]["number"]

        #     if screen_module.enemy_matrix != "yes":
        #         server_module.enemy_balance[0] = server_module.enemy_data[0]["money_balance"]
        #         # координаты медалей врага
        #         for medal in server_module.enemy_data[0]["medals_coordinates"]:
        #             if medal not in server_module.save_medals_coordinates:
        #                 server_module.save_medals_coordinates.append(medal)

        #         # обновляем матрицу сервера(ready_client_data["new_for_server"] - матрица в которой хранится пострелы клиента)
        #         if server_module.check_repeat[0] >= 1:
        #             if server_module.list_player_role[0] == "server_player":
        #                 for row in range(len(server_module.enemy_data[0]["new_for_server"])):
        #                     for cell in range(len(server_module.enemy_data[0]["new_for_server"][row])):
        #                         list_grid[row][cell] = server_module.enemy_data[0]["new_for_server"][row][cell]
        #             else:
        #                 for row in range(len(server_module.enemy_data[0]["new_for_client"])):
        #                     for cell in range(len(server_module.enemy_data[0]["new_for_client"][row])):
        #                         list_grid[row][cell] = server_module.enemy_data[0]["new_for_client"][row][cell]


        #         if server_module.list_player_role[0] == "server_player":
        #             # проверяем стрелял ли клиент или нет
        #             if server_module.enemy_data[0]["need"] == "no":
        #                 # если нет , то ничего не делаем
        #                 pass
        #             # если клиент стерлял , записываем чья сейчас очерель(это зависит от того попал ли клиент или нет)
        #             elif server_module.enemy_data[0]["need"] == "yes":
        #                 print("зашло сюда")
        #                 server_module.turn[0] = server_module.enemy_data[0]["turn"]
        #                 server_module.check_time[0] = 0

        #         if server_module.list_player_role[0] == "server_player" and server_module.turn[0] == "client_turn":
        #             if server_module.check_time[0] == 1 and server_module.check_ten_times.count(1) == 1:
        #                 if shop.second_task.TEXT == shop.list_second_task[1]:
        #                     shop.kept_all_ships_alive_for_five_turns(grid = list_grid)
        #         elif server_module.list_player_role[0] == "client_player" and server_module.turn[0] == "server_turn":
        #             if server_module.check_time[0] == 1 and server_module.enemy_data[0]["check_ten_times"] == 1:
        #                 if shop.second_task.TEXT == shop.list_second_task[1]:
        #                     shop.kept_all_ships_alive_for_five_turns(grid = list_grid)

        #         if server_module.list_player_role[0] == "server_player" and server_module.turn[0] == "client_turn":
        #             if server_module.check_time[0] == 1 and server_module.check_ten_times.count(1) == 1:
        #                 achievement.kept_all_ships_alive_for_ten_turns(grid = list_grid)
        #         elif server_module.list_player_role[0] == "client_player" and server_module.turn[0] == "server_turn":
        #             if server_module.check_time[0] == 1 and server_module.enemy_data[0]["check_ten_times"] == 1:
        #                 shop.kept_all_ships_alive_for_five_turns(grid = list_grid)

        #         achievement.opening_the_battle(grid = list_grid , enemy_grid = server_module.enemy_matrix)

        #         if server_module.row_list[0] != 100 and server_module.check_send_data_health[0] > 9:
        #             server_module.row_list[0] = 100
        #             server_module.col_list[0] = 100
        #             server_module.number_list[0] = 100
        #             server_module.check_send_data_health[0] = 0
        # except:
        #     pass       
        #----------------------------------------------------------------
        check_player_balance[0] = shop.money_list[0]
        # функция которая красиво добавляет/отнимает монетки
        count_money(
            check_buy_bomb = shop.check_buy_bomb_attack[0], 
            check_buy_restorce = shop.but_flag[0],
            check_buy_auto_rocket = shop.flagbimb200[0]
            )
        
        if shop.money_list[0] - check_player_balance[0] > 0 and len(data_player_shot) == 0:
            data_player_shot.append("money")
            data_player_shot.append(shop.money_list[0])
            list_check_need_send[0] = True


        # отримцємо координати курсору
        x_mouse , y_mouse = pygame.mouse.get_pos()
        # створюємо спсиок , завдяки якому будемо трясти екран при ударі
        render_offset = [0, 0]

        if screen_shake[0] > 0:
            # записуємо рандомні числа у список render_offset , щоб за ними трясти екран
            render_offset[0] = random.randint(-4, 4)
            render_offset[1] = random.randint(-4, 4)
            screen_shake[0] -= 1  # Уменьшаем значение screen_shake до 0
        else:
            # якщо не треба трясти екран , то обнуляємо значення
            render_offset = [0, 0] 
        
        # робимо умови щоб відмальовувати картинки якого гравця зараз хід
        # тобто якщо роль гравця(гравець може бути сервером або клієнтом) співпадає із чергою , то відмальовуємо зображення 
        # яке вказуємо що можемо зараз ходити , якщо ні , то малюємо зображення про заборону ходу
        if server_module.list_player_role[0] == "server_player" and server_module.turn[0] == "server_turn":
            player_face.image_name = "active_player.png"
            enemy_face.image_name = "not_active_enemy.png"
            player_face.load_image()
            enemy_face.load_image()
        elif server_module.list_player_role[0] == "client_player" and server_module.turn[0] == "client_turn":
            player_face.image_name = "active_player.png"
            enemy_face.image_name = "not_active_enemy.png"
            player_face.load_image()
            enemy_face.load_image()
        else:
            player_face.image_name = "not_active_player.png"
            enemy_face.image_name = "active_enemy.png"
            player_face.load_image()
            enemy_face.load_image()

        # відмальовуємо фон для фрейма бою
        fight_bg.draw_image(screen = module_screen.main_screen)
        # отрисовка всех элементов для визуального отображения монеток , медалек , и оружия
        shadow_data_user.draw_image(screen = module_screen.main_screen)
        user_weapon.draw_image(screen = module_screen.main_screen)
        player_jar.draw_image(screen = module_screen.main_screen)
        enemy_jar.draw_image(screen = module_screen.main_screen)
        player_balance_in_jar.draw_font()
        enemy_balance_in_jar.text = str(server_module.enemy_balance[0])
        enemy_balance_in_jar.update_text()
        enemy_balance_in_jar.draw_font()


        # завантажуємо , та відмальовуємо зображення годинників(скільки часу пройшло)
        clock_image.image_name = f'{server_module.check_time[0]}.png'
        clock_image.load_image()
        clock_image.draw_image(screen = module_screen.main_screen)

        # відмальовуємо рамки де будуть находитися ніки гравців
        frame_nick_player.draw_image(screen = module_screen.main_screen)
        second_frame_nick_player.draw_image(screen = module_screen.main_screen)

        # відмальовуємо зображення які вказують чиї зараз ход
        player_face.draw_image(screen = module_screen.main_screen)
        enemy_face.draw_image(screen = module_screen.main_screen)

        # выполнить первые три задания
        if shop.fourth_task.TEXT == shop.list_fourth_task[2]:
            shop.complete_three_tasks()

        
        # малюємо ніки та бали гравців
        player_nick.draw_font()
        enemy_nick.draw_font()
        player_points.draw_font()
        enemy_points.draw_font()

        # відмальовуємо зображення сітки , по якій можемо ореєнтуватися куди бити(тобто A1 , B9 � тд)
        grid_image.draw_image(screen = module_screen.main_screen)
        grid_image_for_enemy.draw_image(screen = module_screen.main_screen)

        # малюємо клітинки сітки(просто пусті клітини) гравців
        for cell in list_object_map:
            cell.draw(screen=module_screen.main_screen)
        for empty_cell in list_object_map_enemy:
            empty_cell.draw(screen=module_screen.main_screen)

        # відмалбовуємо кораблі які ми роставляли , але у змнешаному вигялді , та у іншому місці(сітці яка також зменшилась у розмірі)
        for num , ship  in enumerate(list_ships):
            list_ships[num].draw_sheep(screen = module_screen.main_screen)

        for cross_animation in list_cross_player:
            cross_animation.animation(main_screen = module_screen.main_screen , count_image = 13)

        # кнопка для открытия магазина
        shop_and_tasks.draw(surface = module_screen.main_screen)

        
        #----------------------------------------------------------------
        #зарисовка зачеркнутых клеточек если враг ударил обычным выстрелом в игрока(на поле игрока)
        for row in range(len(list_grid)):
            for cell in range(len(list_grid[row])):
                if list_grid[row][cell] == 5:
                    cltka = (row * 10) + cell
                    x_anim_miss = list_object_map[cltka].x
                    y_anim_miss = list_object_map[cltka].y

                    miss_cell_animation = Animation(
                    image_name = "0.png", 
                    width = 55, 
                    height = 55, 
                    x_cor = x_anim_miss, 
                    y_cor = y_anim_miss, 
                    need_clear = False , 
                    name_folder = "animation_miss",
                    animation_speed = 3
                    )
                    
                    exists = False
                    for misses_cells in list_animation_miss:
                        if misses_cells.X_COR == miss_cell_animation.X_COR and misses_cells.Y_COR == miss_cell_animation.Y_COR:
                            exists = True
                            break
                    if not exists:
                        list_animation_miss.append(miss_cell_animation)

        #----------------------------------------------------------------
        # отрисовываем анимации зачерканных клеточек на своем поле, если враг промазал
        for animation_miss in list_animation_miss:
            animation_miss.animation(main_screen=module_screen.main_screen, count_image = 29)
       
        #----------------------------------------------------------------
        # отрисовка зачеркнутых клеточек когда игрок промазал по кораблю
        for anim_miss in our_miss_anim:
            anim_miss.animation(main_screen=module_screen.main_screen, count_image = 29)
        #----------------------------------------------------------------
        #----------------------------------------------------------------
        #перебор матрицы врага чтобы если что отрисовали не достающие крестики и зачеркнутые клеточки(матрица врага слева)
        # например после удара бомбой
        update_enemy_matrix_animations(
            check_animation_rocket = check_animation_rocket, 
            flag_miss_rocket_animation = flag_miss_rocket_animation, 
            list_cross = list_cross,
            our_miss_anim = our_miss_anim
        )
                           
        # отрисовка крестиков если игрок попал по кораблю(на поле врага , слева)
        for cross in list_cross:
            cross.animation(main_screen = module_screen.main_screen , count_image = 13)

        if check_animation_rocket[0] == "start_animation":
            rocket_animation.X_COR = x_hit_the_ship[0] - 231
            rocket_animation.Y_COR = y_hit_the_ship[0] - 23
            # проверка на окончание анимация полета ракеті 
            if rocket_animation.animation(main_screen = module_screen.main_screen , count_image = 7):
                animation_boom.X_COR = x_hit_the_ship[0] - 23
                animation_boom.Y_COR = y_hit_the_ship[0] - 23
                screen_shake[0] = 31
                if animation_boom.animation(main_screen = module_screen.main_screen , count_image = 7):
                    rocket_animation.clear_animation()
                    animation_boom.clear_animation()
                    check_animation_rocket[0] = ""


        #************************************************************************************************
        # отрисовка промаха ракетой, и зарисовка клеточек(когда игрок атакует врага)
        if flag_miss_rocket_animation[0] == "start_animation":
            miss_rocket_animation.X_COR = x_hit_the_ship[0] - 231
            miss_rocket_animation.Y_COR = y_hit_the_ship[0] - 23
            if miss_rocket_animation.animation(main_screen = module_screen.main_screen , count_image = 7):
                miss_rocket_animation.clear_animation()
                flag_miss_rocket_animation[0] = ""
        #************************************************************************************************
        #----------------------------------------------------------------
        # анимация потери соеденения
        if server_module.check_connection[0] == False:
            animation_connection_problem.animation(main_screen = main_screen, count_image = 5)
            if animation_connection_problem.COUNT_IMAGES >= 4:
                animation_connection_problem.clear_animation()
        #----------------------------------------------------------------

        shop.button_restores_cell.draw(screen = module_screen.main_screen)

        # эти функция для проверки , попал ли соперник по нашем кораблям
        check_and_add_hit_markers(
            x_enemy_cross = x_enemy_cross, 
            y_enemy_cross = y_enemy_cross, 
            list_cross_player = list_cross_player,
            
        )

        # анимация использования аптечки
        if health_anim[0] == True:
            for cross in list_cross_player:
                if cross.X_COR  == animation_health.X_COR and cross.Y_COR  == animation_health.Y_COR:
                    list_cross_player.remove(cross)
            if animation_health.animation(main_screen = module_screen.main_screen, count_image = 6):
                health_anim[0] = False
                animation_health.clear_animation()


        mouse_x , mouse_y = pygame.mouse.get_pos()
        # отрисовка сетки для прицеливания при авто-ударе
        if shop.shop_item[0].TURN != "Up":
            if shop.flagbimb200[0] == 'yes' and activate_auto_rocket[0] == True:
                center_xy = draw_cursor(screen = module_screen.main_screen, mouse_x=mouse_x, mouse_y=mouse_y,grid =enemy_grid, color =colorsetka)
                draw_cursor(screen = module_screen.main_screen, mouse_x=mouse_x, mouse_y=mouse_y,grid =enemy_grid, color = colorsetka)
                
                x_mouse=center_xy[0]
                y_mouse=center_xy[1]
                numberofbim[0] = enemy_grid.coordinates_to_number(x_mouse, y_mouse)
    
            if x_mouse >= 182 and x_mouse <= 67 + 450:
                if y_mouse >= 322 and y_mouse <= 257 + 450  and numberofbim[0] not in shop.check_2:
                    colorsetka=(0, 255, 0)    
                else:
                    colorsetka=(255, 0, 0)
            else:
                colorsetka=(255, 0, 0)

        #----------------------------------------------------------------
        #отрисовка медалей 
        for enemy_medal in enemy_medals:
            enemy_medal.draw_medals(screen = module_screen.main_screen)
            enemy_medal.completed_task()

        for medal in player_medal:
            medal.draw_medals(screen = module_screen.main_screen)
            medal.completed_task()

        for enem in enemy_medals:
            enem.show_descriptions(screen = module_screen.main_screen)

        for player in player_medal:
            player.show_descriptions(screen = module_screen.main_screen)
        #----------------------------------------------------------------
        # кнопка которая отчищает оружие
        clear_weapon.draw(surface = main_screen)

        # подсвечивание товара(суперспособности) какой сейчас активен
        active_product_shine.draw_image(screen = main_screen)
        # products icon in the right top corner of the screen
        if shop.check_buy_bomb_attack[0] == True:
            bomb_icon.draw_image(screen = module_screen.main_screen)
        if shop.flagbimb200[0] == "yes":
            auto_rocket_icon.draw_image(screen = module_screen.main_screen)
        if shop.but_flag[0] == True:
            restore_cell_icon.draw_image(screen = module_screen.main_screen)

        # відмаловуємо усі елементи які знаходяться у магазині 
        for item in shop.shop_item:
            item.draw(screen = module_screen.main_screen)
            item.move()

        #----------------------------------------------------------------
        # конструкция которая показывает окошки с выполнеными ачивками по очереди , а не одновременно
        for achiv in list_achieves:
            if achiv.ACTIVE == True and check_achiv[0] == False:
                index_achiv[0] = list_achieves.index(achiv)
                check_achiv[0] = True
        if index_achiv[0] != 100:
            list_achieves[index_achiv[0]].draw(screen = module_screen.main_screen)
            list_achieves[index_achiv[0]].move()
        if index_achiv[0] != 100:
            if list_achieves[index_achiv[0]].VISIBLE == 0:
                check_achiv[0] = False
                index_achiv[0] = 100

        #----------------------------------------------------------------
        if shop.first_task.TEXT == shop.list_first_task[2]:
            shop.kill_one_three_decker_ship()

        if shop.second_task.TEXT == shop.list_second_task[2]:
            shop.kill_two_ships_in_a_row()

        if shop.fourth_task.TEXT == shop.list_fourth_task[1]:
            shop.kill_three_ships_in_a_row()

        # первым убить четрыех палбный кораблик
        if shop.third_task.TEXT == shop.list_third_task[0]:
            shop.first_kill_four_decker()
        # первым убить трех палубный корабль
        if shop.second_task.TEXT == shop.list_second_task[-1]:
            shop.first_kill_three_decker()



        # destoyer achievement
        # для бомбы задание
        if check_bomb[0] == True and 9 not in achievement.list_save_coords_achiv:
            new_killed_ships[0] = len(server_module.enemy_died_ships)
            if new_killed_ships[0] - old_killed_ships[0] >= 2:
                destroyer_medal.ACTIVE = True
                destroyer_achievement.ACTIVE = True
                achievement.list_save_coords_achiv.append(9)
                achievement.list_save_coords_achiv[0] = True

        if check_bomb[0] == True and 11 not in achievement.list_save_coords_achiv:
            new_killed_ships[0] = len(server_module.enemy_died_ships)
            if new_killed_ships[0] - old_killed_ships[0] >= 1:
                if count_5[0] <= 0:
                    if 11 not in achievement.list_save_coords_achiv:
                        target_attack_achievement.ACTIVE = True
                        target_attack_medal.ACTIVE = True
                        achievement.list_save_coords_achiv.append(11)
                        achievement.list_save_coords_achiv[0] = True
                    else:
                        count_5[0] = 0
                else:
                    count_5[0] = 0
            else:
                count_5[0] = 0

        if check_bomb[0] == True:
            check_bomb[0] = False
        
        #target attack
        if check_target_attack[0] == True and 11 not in achievement.list_save_coords_achiv:
            target_attack_achievement.ACTIVE = True
            target_attack_medal.ACTIVE = True
            achievement.list_save_coords_achiv.append(11)
            achievement.list_save_coords_achiv[0] = True
        

        achievement.piooner() 
        achievement.lone_hunter()
        achievement.first_kill_four_decker_achivment()
        achievement.strategist(player_killed_ships = server_module.player_died_ships , role = server_module.list_player_role[0] , winner = server_module.list_check_win[0])

        for button in shop.shop_item:
            try:
                if button.ACTION:
                    mouse = pygame.mouse.get_pos()
                    if button.RECT.collidepoint(mouse):
                        pygame.mouse.set_visible(False)
                        cursor_img_rect.center = pygame.mouse.get_pos()
                        main_screen.blit(cursor_image, cursor_img_rect)
                        break
                    else:
                        pygame.mouse.set_visible(True)
            except:
                continue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False  
                change_scene(None)
            # перевіряємо чи натиснули на кнопку показу магазину 
            if list_check_shop[0] == True:
                # якщо так , то говоримо щоб усі елементи рухались униз(щоб гравець зміг їх побачити)
                # якщо items.ACTIVE дорівнює True , то це значить що магазин знаходиться у стані руху
                for items in shop.shop_item:
                    items.ACTIVE = True
                # обнуляємо флаг кнопки на False , щоб гра не думала що ми постійно тиснемо на кнопку відкриття магазину
                list_check_shop[0] = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                clear_weapon.check_click(event = event)
                shop_and_tasks.check_click(event = event)
                # активация суперспособностей
                mouse = pygame.mouse.get_pos()
                if shop.check_buy_bomb_attack[0] == True:
                    if bomb_icon.rect.collidepoint(mouse):
                        activate_bomb[0] = True
                        activate_auto_rocket[0] = False
                        activate_restore_cell[0] = False
                        active_product_shine.x_cor = bomb_icon.x_cor - 17
                        active_product_shine.y_cor = bomb_icon.y_cor - 17
                elif shop.flagbimb200[0] == "yes":
                    if auto_rocket_icon.rect.collidepoint(mouse):
                        activate_auto_rocket[0] = True
                        activate_bomb[0] = False
                        activate_restore_cell[0] = False
                        active_product_shine.x_cor = auto_rocket_icon.x_cor - 13
                        active_product_shine.y_cor = auto_rocket_icon.y_cor - 10
                elif shop.but_flag[0] == True:
                    if restore_cell_icon.rect.collidepoint(mouse):
                        activate_restore_cell[0] = True
                        activate_bomb[0] = False
                        activate_auto_rocket[0] = False
                        active_product_shine.x_cor = restore_cell_icon.x_cor - 17
                        active_product_shine.y_cor = restore_cell_icon.y_cor - 20
                    
                # робимо перебор списку де знаходяться елементи магазину , та для кнопок застосовуємо функцію check_click()
                for button in shop.shop_item:
                    try:
                        button.check_click(event = event)
                    except:
                        continue

                # перевіряємо чи натиснули за зоною магазина , і якщо так то закриваємо його
                if y_mouse >= 24 and y_mouse <= 60 and x_mouse >= 11 and x_mouse <= 67 and shop.shop_item[0].TURN == "Up":
                    for items in shop.shop_item:
                        items.ACTIVE = True  
    
                if shop.shop_item[0].TURN != "Up":          
                    if x_mouse >= 705 and x_mouse <= 705 + 550:# перевіряємо щоб гравець натискав на свою сітку 
                        if y_mouse >= 257 and y_mouse <= 257 + 550:
                            # шукаємо клітинку на яку натиснув гравець
                            for cell in list_object_map: 
                                if cell.x <= x_mouse and x_mouse < cell.x + 55:
                                    if cell.y <= y_mouse and y_mouse < cell.y + 55:
                                        # для восстановления клеточки корабля
                                        if shop.but_flag[0] == True and activate_restore_cell[0] == True:
                                            # Узнаем номер клетки где стоит кораблик
                                            number_cell_our = list_object_map.index(cell)
                                            # Переделываем значение клетки в строку чтобы можно было лекго узнать в калоночке он стоит
                                            str_col_our = str(number_cell_our) 
                                            # Вычисляем номер рядка где стоит корабль(например 23 , делим на 10 без остатка и получаем 2 , вот нашь столбец)
                                            row = number_cell_our // 10  
                                            #Колонку кораблика вычисляем по такому принципу
                                            # Например опять 23 число номер колонки где стоит корабль , тогда с помощью -1 мы берем последнее число тоесть тройку, и вот так получаем номер колонки
                                            col = int(str_col_our[-1])

                                            cltx = (row * 10) + int(str_col_our[-1])

                                            # номер клеточки
                                            if list_grid[row][col] == 7:
                                                activate_restore_cell[0] = False
                                                shop.but_flag[0] = False
                                                if cltx not in check_number_cell:
                                                    restore_part_of_ship(
                                                    col = col,
                                                    row = row,
                                                    str_col = str_col_our,
                                                    health_anim = health_anim
                                                )
                                                active_product_shine.x_cor = -100
                                                active_product_shine.y_cor = -100
                                        
                x_mouse, y_mouse = pygame.mouse.get_pos()                                           
                if shop.shop_item[0].TURN != "Up":
                    if check_animation_rocket[0] == "" and flag_miss_rocket_animation[0] == "":
                        # перевіряємо за яку роль грає гравець                    
                        if (server_module.list_player_role[0] == "server_player" and server_module.turn[0] == "server_turn") or (server_module.list_player_role[0] == "client_player" and server_module.turn[0] == "client_turn"):
                            # перевіряємо щоб гравець натискав на сітку ворога
                            if x_mouse >= 67 and x_mouse <= 67 + 550:
                                if y_mouse >= 257 and y_mouse <= 257 + 550:
                                    # шукаємо клітинку на яку натиснув гравець
                                    for cell in list_object_map_enemy: 
                                        if cell.x <= x_mouse and x_mouse < cell.x + 55:
                                            if cell.y <= y_mouse and y_mouse < cell.y + 55:
                                                # Узнаем номер клетки где стоит кораблик
                                                number_cell = list_object_map_enemy.index(cell)
                                                # Переделываем значение клетки в строку чтобы можно было лекго узнать в калоночке он стоит
                                                str_col = str(number_cell) 
                                                # Вычисляем номер рядка где стоит корабль(например 23 , делим на 10 без остатка и получаем 2 , вот нашь столбец)
                                                row = number_cell // 10  
                                                #Колонку кораблика вычисляем по такому принципу
                                                # Например опять 23 число номер колонки где стоит корабль , тогда с помощью -1 мы берем последнее число тоесть тройку, и вот так получаем номер колонки
                                                col = int(str_col[-1])
                                                # автоудар
                                                if shop.flagbimb200[0] == "yes" and numberofbim[0] not in shop.cheak and activate_auto_rocket[0] == True: 
                                                    kord = Missile_200(row,col,enemy_matrix)
                                                    #если false flag  то бан клетка и если NOne значит нету корабликов 
                                                    if kord != "false" and kord != None :
                                                        if kord[0][0] != "True":
                                                            data_player_shot.append("auto_rocket")
                                                            lenkord = len(kord)
                                                            count_money_hit[0] += 10
                                                            for i in range(lenkord):
                                                                # знаходим номер клетки 
                                                                kletka = kord[i][0]*10 + kord[i][1]
                                                                # cell_number_to_coordinates — новая функция, преобразующая номер клетки в координаты. Функция находится в screen.py, в create_grid.py.                         
                                                                x_y = enemy_grid.cell_number_to_coordinates(kletka)
                                                                check_animation_rocket[0] = "start_animation"  
                                                                x_hit_the_ship[0] = x_y[0]
                                                                y_hit_the_ship[0] = x_y[1]
                                                                # у матрицю ворога записуємо 7
                                                                enemy_matrix[kord[i][0]][kord[i][1]] = 7
                                                                data_player_shot.append(kord[i][0])
                                                                data_player_shot.append(kord[i][1])
                                                                # обнуляємо час ходу
                                                                server_module.check_time[0] = 0
                                                                # записуємо у лист який перевіряє чи потрібно відпарвляти дані на сервер флаг "yes", але чергу не змінюємо оскільки гравець попав по кораблю
                                                                if server_module.list_player_role[0] == "server_player":
                                                                        server_module.turn[0] = "server_turn"
                                                                elif server_module.list_player_role[0] == "client_player":
                                                                    server_module.turn[0] = "client_turn"  
                                                                shop.flagbimb200[0] = "no"
                                                                activate_auto_rocket[0] = False
                                                                active_product_shine.x_cor = -100
                                                                active_product_shine.y_cor = -100
                                                        else:
                                                            #знаходим номер клетки 
                                                            kletka= kord[0][1] * 10 + kord[0][2]
                                                            # cell_number_to_coordinates — новая функция, преобразующая номер клетки в координаты. Функция находится в screen.py, в create_grid.py.                         
                                                            x_y = enemy_grid.cell_number_to_coordinates(kletka)
                                                            check_animation_rocket[0] = "start_animation"  
                                                            x_hit_the_ship[0] = x_y[0]
                                                            y_hit_the_ship[0] = x_y[1]
                                                            # у матрицю ворога записуємо 7
                                                            enemy_matrix[kord[0][1]][kord[0][2]] = 5 
                                                            data_player_shot.append(kord[0][1])
                                                            data_player_shot.append(kord[0][2])
                                                            # обнуляємо час ходу
                                                            server_module.check_time[0] = 0
                                                            # записуємо у лист який перевіряє чи потрібно відпарвляти дані на сервер флаг "yes", але чергу не змінюємо оскільки гравець попав по кораблю
                                                            if server_module.list_player_role[0] == "client_player":
                                                                server_module.turn[0] = "server_turn"
                                                            elif server_module.list_player_role[0] == "server_player":
                                                                server_module.turn[0] = "client_turn"

                                                            shop.flagbimb200[0] = "no"
                                                            activate_auto_rocket[0] = False
                                                            active_product_shine.x_cor = -100
                                                            active_product_shine.y_cor = -100
                                                        list_check_need_send[0] = True
                                                #бомба 3 на 3
                                                elif shop.check_buy_bomb_attack[0] == True and activate_bomb[0] == True:
                                                    shop.check_buy_bomb_attack[0] = False
                                                    server_module.flag_bomb_animation[0] = True
                                                    activate_bomb[0] = False
                                                    x_hit_the_ship[0] = list_object_map_enemy[list_object_map_enemy.index(cell)].x
                                                    y_hit_the_ship[0] = list_object_map_enemy[list_object_map_enemy.index(cell)].y
                                                    count_7 = [0]
                                                    
                                                    count_ships = []
                                                    count_misses = []
                                                    old_killed_ships[0] = len(server_module.enemy_died_ships)
                                                    bomb_shot(
                                                        row = row,
                                                        col = col,
                                                        count_7 = count_7,
                                                        count_ships = count_ships,
                                                        count_misses = count_misses,
                                                        count_5 = count_5,
                                                        check_bomb = check_bomb
                                                    )
                                                    active_product_shine.x_cor = -100
                                                    active_product_shine.y_cor = -100
                                                # простой удар
                                                elif activate_bomb[0] == False and activate_auto_rocket[0] == False:
                                                    simple_shot(
                                                        col = col, 
                                                        row = row, 
                                                        x_hit_the_ship = x_hit_the_ship, 
                                                        y_hit_the_ship = y_hit_the_ship, 
                                                        flag_miss_rocket_animation = flag_miss_rocket_animation, 
                                                        check_animation_rocket = check_animation_rocket,
                                                        cell = cell
                                                    )
                                                    active_product_shine.x_cor = -100
                                                    active_product_shine.y_cor = -100
                                                    


        if shop.third_task.TEXT == shop.list_third_task[-1]:
            shop.kill_two_three_decker_in_a_row()

        if shop.third_task.TEXT == shop.list_third_task[1]:
            shop.kill_four_single_ships_in_a_row() 

        if shop.third_task.TEXT == shop.list_third_task[2]:
            shop.kill_three_double_decker_in_a_row()

        achievement.monster_of_perfictionists()

       
        #************************************************************************************************
        #анимация бомбы и взрыва после бомбы
        if server_module.flag_bomb_animation[0] == True:
            bomb_animation.X_COR = x_hit_the_ship[0] - 280
            bomb_animation.Y_COR = y_hit_the_ship[0] - 90
            if bomb_animation.animation(main_screen = module_screen.main_screen, count_image = 16):
                animation_bomb_boom.X_COR = x_hit_the_ship[0] - 88
                animation_bomb_boom.Y_COR = y_hit_the_ship[0] - 88
                screen_shake[0] = 31 
                if animation_bomb_boom.animation(main_screen = module_screen.main_screen , count_image = 7):
                    bomb_animation.clear_animation()
                    animation_bomb_boom.clear_animation()
                    server_module.flag_bomb_animation[0] = False
        #************************************************************************************************

          
        # Перевіряємо чи не пустий список який зберігає чи хтось виграв
        # if achievement.strategist_achievement.ACTIVE == False:
        #     if server_module.list_check_win[0] != None:   
        #         # якщо вже їтось виграв , то робимо ефект затемнення
        #         apply_fade_effect(screen = module_screen.main_screen)
        #         # зупиняємо цикл гри
        #         run_game = False
        #         # змінюємо фрейм бою , на фрейм показу результатів
        #         change_scene(scene =game_windows.finish_window())
        #         check_press_button[0] = None

        if screen_shake[0] > 1:
            screen_shake[0] -= 1

        # відмальовуємо екран із координатами що збергаються у списку render_offset , щоб якщо гравець потрапив по карблю , то був ефект трясіння
        module_screen.main_screen.blit(pygame.transform.scale(module_screen.main_screen, (1280 , 832)), render_offset)
        # оновлюємо екран
        pygame.display.flip()