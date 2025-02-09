import pygame, random, sys, threading
import modules.game_windows as game_windows
import modules.shop as shop
from ...screens import main_screen
from os.path import abspath, join
import modules.screens.screen as module_screen
import modules.server as server_module
import modules.achievement as achievement
import modules.classes.class_medal as class_medal
from ...game_tools import count_money, apply_fade_effect
from ...screens import grid_player, list_object_map, list_object_map_enemy, enemy_grid, list_grid, enemy_matrix
from ...classes.class_music import music_load_waiting, fight_music
from ...classes.class_medal import player_medal, enemy_medals, target_attack_medal, destroyer_medal, magnat_medal
from ...classes.class_image import DrawImage
from ...classes.achive_window import list_achieves, target_attack_achievement, destroyer_achievement, magnate_achievement
from ...classes.class_button import Button
from ...classes.class_text import Font
from ...classes.radar_class import radar
from ...classes.class_input_text import input_nick
from ...classes.class_click import random_first_choice_sound, player_turn_sound, enemy_turn_sound, miss_water_sound, shot_sound, radar_sound, all_sounds
from ...classes.animation import Animation, rocket_animation, miss_rocket_animation, animation_boom, animation_bomb_boom, animation_health, bomb_animation, animation_connection_problem, animation_random_player, animation_auto_rocket, miss_rocket, miss_auto_rocket, radar_animation, fire_rocket_animation, fire_fighter_animation, fire_animation
from ...classes.class_ship import list_ships
from ...game_tools import player_balance_in_jar, enemy_balance_in_jar, ship_border, list_animation_miss, check_number_cell, kill_enemy_ships, list_cross, our_miss_anim, check_target_attack, count_money_hit, find_all_neighbors, killed_ships_draw
from ..change_window import change_scene
from ...client import list_check_need_send, check_two_times, send_matrix, dict_save_information, data_player_shot, connection, count_time, check_start_time_thread
from .weapons import simple_shot, bomb_shot, restore_part_of_ship, random_hits_matrix, auto_aim
from .animations_on_grid import update_enemy_matrix_animations, check_and_add_hit_markers
from ..button_pressed import check_press_button
from ...volume_settings import save_data_volume
from ...json_functions import list_users, write_json



list_check_shop = [None]
def show_shop():
    if shop.shop_item[0].TURN == "Down": 
        list_check_shop[0] = True

# функция для отчистки активации оружия(того что кпуил пользователь)
def clear_weapon_function():
    activate_auto_rocket[0] = False
    activate_restore_cell[0] = False
    activate_bomb[0] = False
    activate_fire_fighter[0] = False
    activate_radar[0] = False
    activate_fire_rocket[0] = False
    activate_random_hits[0] = False
    active_product_shine.x_cor = -100
    active_product_shine.y_cor = -100


#((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
Cordi_Burning_Ship= []
fire_extinguisher=["no"]
number_of_ship_sonfire=[0]
pozhar_row= []
pozhar_col =[]
#((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((()))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))

# картинка курсора
cursor_image = pygame.transform.scale(pygame.image.load(abspath(join(__file__, "..", "..", "..", "..", "media", "decorations", "cursor.png"))), (32, 32))
cursor_img_rect = cursor_image.get_rect()

#images
grid_image = DrawImage(width = 662  , height = 662 , x_cor = 40 , y_cor = 37 , folder_name = "grid", image_name = "background_grid.png")
player_face = DrawImage(width = 154 , height = 123 ,x_cor = 1104 , y_cor = 79 , folder_name = "decorations" , image_name = "active_player.png")
enemy_face = DrawImage(width = 154 , height = 123  ,x_cor = 20 , y_cor = 79 , folder_name = "decorations" , image_name = "not_active_enemy.png")
player_before_choice = DrawImage(width = 154 , height = 123, x_cor = 1104, y_cor = 79, folder_name = "decorations" , image_name = "before_choice_player.png")
enemy_before_choice = DrawImage(width = 154 , height = 123 , x_cor = 20 , y_cor = 79 , folder_name = "decorations" , image_name = "before_choice_enemy.png")
fight_bg = DrawImage(width = 1280,height = 832 , x_cor = 0 , y_cor = 0 , folder_name= "backgrounds" , image_name= "fight_background.png")
shadow_data_user = DrawImage(x_cor = -28 , y_cor = -95 , width = 1351 , height = 236 , folder_name = "decorations" , image_name = "shadow_user_data.png")
user_weapon = DrawImage(x_cor = 1046 , y_cor = -26 , width = 260 , height = 135 , folder_name = "backgrounds" , image_name = "user_weapon.png")
player_jar = DrawImage(x_cor = 1190 , y_cor = 18 , width = 90 , height = 76 , folder_name = "decorations" , image_name = "jar_balance.png")
enemy_jar = DrawImage(x_cor = 102 , y_cor = 18 , width = 90 , height = 76 , folder_name = "decorations" , image_name = "jar_balance.png")
clock_image = DrawImage(width = 206 , height = 57 , x_cor = 544 , y_cor = 20 , folder_name = "animation_clock" , image_name = "0.png")
grid_image_for_enemy = DrawImage(width = 596  , height = 597 , x_cor = 23 , y_cor = 211 , folder_name = "grid", image_name = "background_grid.png")
reonnect_image = DrawImage(width = 200, height = 40, x_cor = 600, y_cor = -3, folder_name = "backgrounds", image_name = "reconnect.png")
#products icons
bomb_icon = DrawImage(x_cor = 1104, y_cor = 64, width = 27, height = 26, folder_name = "products_icons" , image_name = "bomb_icon.png")
auto_rocket_icon = DrawImage(x_cor = 1137, y_cor = 58, width = 45.54, height = 40.09, folder_name = "products_icons", image_name = "auto_rocket_icon.png")
restore_cell_icon = DrawImage(x_cor = 1165, y_cor = 24, width = 31, height = 28.4, folder_name = "products_icons", image_name = "restore_cell_icon.png")
radar_icon = DrawImage(x_cor = 1100, y_cor = 23, width = 27.68, height = 26.74, folder_name = "products_icons", image_name = "radar_icon.png")
fire_rocket_icon = DrawImage(x_cor = 1065, y_cor = 64, width = 34, height = 25, folder_name = "products_icons", image_name = "fire_rocket_icon.png")
fire_fighter_icon = DrawImage(x_cor = 1134, y_cor = 24, width = 25.89 , height = 28.4, folder_name = "products_icons", image_name = "fire_fighter_icon.png")
random_hits_icon = DrawImage(x_cor = 1050, y_cor = 24, width = 45, height = 27, folder_name = "products_icons", image_name = "random_hits_icon.png")
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

killed_1ship_rotate = DrawImage(x_cor = 0, y_cor = 0, width = 55, height = 55, folder_name = "ships", image_name = "rotate_ship_one.png")
killed_1ship = DrawImage(x_cor = 0, y_cor = 0, width = 55, height = 55, folder_name = "ships", image_name = "ship_one.png")

killed_2ship_rotate = DrawImage(x_cor = 0, y_cor = 0, width = 55, height = 110, folder_name = "ships", image_name = "rotate_ship_two.png")
killed_2ship = DrawImage(x_cor = 0, y_cor = 0, width = 110, height = 55, folder_name = "ships", image_name = "ship_two.png")

killed_3ship_rotate = DrawImage(x_cor = 0, y_cor = 0, width = 55, height = 165, folder_name = "ships", image_name = "rotate_ship_three.png")
killed_3ship = DrawImage(x_cor = 0, y_cor = 0, width = 165, height = 55, folder_name = "ships", image_name = "ship_three.png")

killed_4ship_rotate = DrawImage(x_cor = 0, y_cor = 0, width = 55, height = 220, folder_name = "ships", image_name = "rotate_ship_four.png")
killed_4ship = DrawImage(x_cor = 0, y_cor = 0, width = 220, height = 55, folder_name = "ships", image_name = "ship_four.png")

screen_shake = [0]
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


# список в котором храним анимацию огня если игрок поджог корабль
list_fire = []
row_fire_col_anim = []
col_fire_row_anim = []
list_already_fire_cells = []
first_shot_fire = []

enemy_col_fire = []
enemy_row_fire = []
enemy_list_fire =[]
enemy_check_fire = [0]
# счетчик для удрара авто ракетой
count_hit_auto_rocket = [0]
# флаг для анимации огнетушителя
fire_fighter_anim = [False]
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
# флаг для радара
radar_flag = ["", 0]
#------------------------------------------------------------------------------------------------
# флаг который првоеряет надо ли запускать анимацию ракеты если игрок ударил
check_animation = [""]
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
activate_radar = [False]
activate_fire_rocket = [False]
activate_fire_fighter = [False]
activate_random_hits = [False]
#----------------------------------------------------------------
#для бомбы чтобы считать сколько клеточек в радиусе 3х3 было 5
count_5 = [0]
#для ачивки убить два или больше корабля одной бомбой
old_killed_ships = [0]
new_killed_ships = [0]
check_bomb = [False]

# для того чтобы звук играл только один раз
count_sound_time = [0]

# для сравнения изменился ли нашь баланс
check_player_balance = [0, False]

# для ачивок на выживвание раундов
check_alive_ten = [False]
check_alive_five = [False]
# функція для бою між гравцями
def fight_window():
    # зупиняємо музику яка грала перед боєм
    music_load_waiting.stop()
    # вмикаємо музику для бою
    fight_music.play()
    for song in all_sounds:
        song.set_volume(save_data_volume[0])
        pygame.mixer.music.set_volume(save_data_volume[0])
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
    print("Заходит за пределы цикла vsegda?")
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
    check_two_times.clear()
    count_time_thread = threading.Thread(target = count_time, daemon = True)
    count_time_thread.start()
    random_first_choice_sound.play2(loops = 1)

    test_time = [0]
    Cordi_Burning_Shi = []
    stew_row = []
    stew_col =[]
    flagstop= False 
    shop.flag_arson[0] = ["no"]

    Schechik_before_removeall = [0]
    tsest = [False]

    one_data_fire = [0]
    target_time = [1]
    one_enemy_fire = [0, False]
    for medal in player_medal:
            medal.VISIBLE = 100
            medal.ACTIVE = False
    for enm_medal in enemy_medals:
        enm_medal.VISIBLE = 100
        enm_medal.ACTIVE = False
    shop.player_balance.TEXT = '0'
    player_balance_in_jar.text = '0'
    enemy_balance_in_jar.text = '0'
    shop.player_balance.update_text()
    player_balance_in_jar.update_text()
    enemy_balance_in_jar.update_text()
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
            else:
                class_medal.enemy_four_decker_sniper_medal.ACTIVE = False
            if server_module.save_medals_coordinates[medal] == 2:
                class_medal.enemy_perfect_shooter_medal.ACTIVE = True
            else:
                class_medal.enemy_perfect_shooter_medal.ACTIVE = False
            if server_module.save_medals_coordinates[medal] == 3:
                class_medal.enemy_strategist_medal.ACTIVE = True
            else:
                class_medal.enemy_strategist_medal.ACTIVE = False
            if server_module.save_medals_coordinates[medal] == 4:
                class_medal.enemy_first_hit_medal.ACTIVE= True
            else:
                class_medal.enemy_first_hit_medal.ACTIVE = False
            if server_module.save_medals_coordinates[medal] == 5:
                class_medal.enemy_magnat_medal.ACTIVE = True
            else:
                class_medal.enemy_magnat_medal.ACTIVE = False
            if server_module.save_medals_coordinates[medal] == 6:
                class_medal.enemy_master_of_disguist_medal.ACTIVE = True
            else:
                class_medal.enemy_master_of_disguist_medal.ACTIVE = False
            if server_module.save_medals_coordinates[medal] == 7:
                class_medal.enemy_lone_hunter_medal.ACTIVE = True
            else:
                class_medal.enemy_lone_hunter_medal.ACTIVE = False
            if server_module.save_medals_coordinates[medal] == 8:
                class_medal.enemy_pioneer_medal.ACTIVE = True
            else:
                class_medal.enemy_pioneer_medal.ACTIVE = False
            if server_module.save_medals_coordinates[medal] == 9:
                class_medal.enemy_destroyer_medal.ACTIVE = True
            else:
                class_medal.enemy_destroyer_medal.ACTIVE = False
            if server_module.save_medals_coordinates[medal] == 10:
                class_medal.enemy_opening_battle_medal.ACTIVE = True
            else:
                class_medal.enemy_opening_battle_medal.ACTIVE = False
            if server_module.save_medals_coordinates[medal] == 11:
                class_medal.enemy_target_attack_medal.ACTIVE = True
            else:  
                class_medal.enemy_target_attack_medal.ACTIVE = False
            if server_module.save_medals_coordinates[medal] == 12:
                class_medal.enemy_collector_medal = True
            else:
                class_medal.enemy_collector_medal = False

        if animation_random_player.COUNT_IMAGES >= 5 and animation_random_player.COUNT_IMAGES <= 10:
            animation_random_player.ANIMATION_SPEED = 3.2
        elif animation_random_player.COUNT_IMAGES >= 11 and animation_random_player.COUNT_IMAGES <= 16:
            animation_random_player.ANIMATION_SPEED = 4.2
        elif animation_random_player.COUNT_IMAGES >= 17 and animation_random_player.COUNT_IMAGES <= 22:
            animation_random_player.ANIMATION_SPEED = 5.2
        elif animation_random_player.COUNT_IMAGES >= 23 and animation_random_player.COUNT_IMAGES <= 27:
            animation_random_player.ANIMATION_SPEED = 8.2
        if server_module.list_player_role[0] == "server_player":
            if animation_random_player.COUNT_IMAGES >= 28 and animation_random_player.COUNT_IMAGES <= 31:
                animation_random_player.ANIMATION_SPEED = 120
        elif server_module.list_player_role[0] == "client_player":
            if animation_random_player.COUNT_IMAGES >= 29 and animation_random_player.COUNT_IMAGES <= 31:
                animation_random_player.ANIMATION_SPEED = 120

        if server_module.list_player_role[0] != "server_player" and animation_random_player.COUNT_IMAGES >= 29 and count_sound_time[0] == 0:
            enemy_turn_sound.play2(loops = 1)
            count_sound_time[0] = 1
            if dict_save_information["enemy_nick"] not in list_users:
                list_users[dict_save_information["enemy_nick"]] = {"points": int(dict_save_information["player_points"]), "password": dict_save_information["enemy_password"]}
                write_json(filename = "data_base.json" , object_dict = list_users)
            #якщо його нікнейм вже є , тоді просто оновлюємо його кількість баллів 
            elif dict_save_information["player_nick"] in list_users:
                list_users[dict_save_information["player_nick"]]["points"] = int(dict_save_information["player_points"])
                write_json(filename = "data_base.json" , object_dict = list_users)
        elif animation_random_player.COUNT_IMAGES >= 28 and count_sound_time[0] == 0 and server_module.list_player_role[0] != "client_player":
            player_turn_sound.play2(loops = 1)
            count_sound_time[0] = 1
            if dict_save_information["enemy_nick"] not in list_users:
                list_users[dict_save_information["enemy_nick"]] = {"points": int(dict_save_information["player_points"]), "password": dict_save_information["enemy_password"]}
                write_json(filename = "data_base.json" , object_dict = list_users)
            #якщо його нікнейм вже є , тоді просто оновлюємо його кількість баллів 
            elif dict_save_information["player_nick"] in list_users:
                list_users[dict_save_information["player_nick"]]["points"] = int(dict_save_information["player_points"])
                write_json(filename = "data_base.json" , object_dict = list_users)
    
        if animation_random_player.IS_ANIMATION_DONE == True:
            if check_two_times.count(3) >= 2:
                server_module.check_time[0] += 1
                check_two_times.clear()
        try:
            if len(server_module.enemy_data) > 0:
                check_data = server_module.enemy_data[0].split(' ')
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

                    dict_save_information["player_nick"] = str(input_nick.user_text)
                    dict_save_information["enemy_nick"] = str(check_list[141])
                    dict_save_information["player_points"] = int(list_users[input_nick.user_text]["points"])
                    dict_save_information["enemy_points"] = int(check_list[143])
                    dict_save_information["enemy_password"] = str(check_list[142])
                    player_nick.text = dict_save_information["player_nick"]
                    enemy_nick.text = dict_save_information["enemy_nick"]
                    player_points.text = str(dict_save_information["player_points"])
                    enemy_points.text = str(dict_save_information["enemy_points"])
                    player_nick.update_text()
                    enemy_nick.update_text()
                    player_points.update_text()
                    enemy_points.update_text()


                    server_module.enemy_ships.clear()  
                    count_data = 1
                    enemy_ship = []
                    for data_ship in check_list[101:141]:
                        if count_data <= 3:
                            enemy_ship.append(int(data_ship))
                        else:
                            enemy_ship.append(data_ship)

                        count_data += 1

                        if len(enemy_ship) >= 4:
                            server_module.enemy_ships.append(enemy_ship.copy())  
                            enemy_ship.clear()
                            count_data = 1  

                    
                else:
                    try:
                        if check_data[0] == "enemy_turn":
                            server_module.check_time[0] = 0
                            if server_module.list_player_role[0] == "server_player":
                                server_module.turn[0] = "server_turn"
                            elif server_module.list_player_role[0] == "client_player":
                                server_module.turn[0] = "client_turn"
                        if check_data[0] == "player_turn":
                            if server_module.list_player_role[0] == "server_player":
                                server_module.turn[0] = "client_turn"
                            elif server_module.list_player_role[0] == "client_player":
                                server_module.turn[0] = "server_turn"
                        for data_enemy in check_data:
                            if "fire" in check_data:
                                one_enemy_fire[1] = True
                                indices_fire = []
                                for i, value in enumerate(check_data):
                                    if value == "fire":
                                        indices_fire.append(i)
                                # Обрабатываем каждое вхождение "fire"
                                for index_fire in indices_fire:
                                    pozhar_row.append(int(check_data[(index_fire +1)]))
                                    pozhar_col.append(int(check_data[(index_fire +2)]))
                                    list_grid[int(check_data[(index_fire +1)])][int(check_data[(index_fire +2)])] = 7

                                    enemy_row_fire.append([int(check_data[(index_fire + 1)]), 0])
                                    enemy_col_fire.append([int(check_data[(index_fire + 2)]), 0])
                            elif data_enemy == "shot":
                                server_module.check_time[0] = 0
                                count_hit = 0
                                for data_enemy in range(1, len(check_data) - 1, 2): 
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
                            elif data_enemy == "auto_rocket":
                                for cell in check_data[1:-1]:
                                    row = int(cell) // 10
                                    col = int(cell) % 10
                                    if list_grid[row][col] in [1, 2, 3, 4]:
                                        count_hit_auto_rocket[0] += 1
                                        list_grid[row][col] = 7
                                        if server_module.list_player_role[0] == "server_player":
                                            server_module.turn[0] = "client_turn"
                                        elif server_module.list_player_role[0] == "client_player":
                                            server_module.turn[0] = "server_turn"
                                        continue
                                    elif list_grid[row][col] in [0, 5]:
                                        list_grid[row][col] = 5
                                        if server_module.list_player_role[0] == "server_player":
                                            server_module.turn[0] = "server_turn"
                                        elif server_module.list_player_role[0] == "client_player":
                                            server_module.turn[0] = "client_turn"
                                        continue
                                    elif list_grid[row][col] == 7:
                                        if count_hit_auto_rocket[0] == 0:
                                            if server_module.list_player_role[0] == "server_player":
                                                server_module.turn[0] = "server_turn"
                                            elif server_module.list_player_role[0] == "client_player":
                                                server_module.turn[0] = "client_turn"
                                        elif count_hit_auto_rocket[0] >= 1:
                                            if server_module.list_player_role[0] == "server_player":
                                                server_module.turn[0] = "client_turn"
                                            elif server_module.list_player_role[0] == "client_player":
                                                server_module.turn[0] = "server_turn"

                                server_module.check_time[0] = 0
                            elif data_enemy == "bomb":
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
                    except:
                        continue
                    if "fire_fighter" == check_data[0]:
                        for arson in list_fire:
                            if arson[0] == int(check_data[(1)]) and arson[1] == int(check_data[(2)]):
                                arson[-1] += 1
                        stew_row.append(int(check_data[(1)]))
                        stew_col.append(int(check_data[(2)]))

                    elif check_data[0] == 'random_hits':
                        index_cell = 0
                        count_hit = 0
                        for cell in range(1 , 7):
                            try:
                                if cell % 2 == 0:
                                    if list_grid[int(check_data[cell - 1])][int(check_data[cell])] in [1, 2, 3, 4, 7]:
                                        count_hit += 1
                                        if list_grid[int(check_data[cell - 1])][int(check_data[cell])] == 7:
                                            pass
                                        else:
                                            list_grid[int(check_data[cell - 1])][int(check_data[cell])] = 7
                                    elif list_grid[int(check_data[cell - 1])][int(check_data[cell])] in [0, 5]:
                                        list_grid[int(check_data[cell - 1])][int(check_data[cell])] = 5
                            except:
                                continue
                        server_module.check_time[0] = 0
                        if count_hit == 0:
                            if server_module.list_player_role[0] == "server_player":
                                server_module.turn[0] = "server_turn"
                            elif server_module.list_player_role[0] == "client_player":
                                server_module.turn[0] = "client_turn"
                        else:
                            if server_module.list_player_role[0] == "server_player":
                                server_module.turn[0] = "client_turn"
                            elif server_module.list_player_role[0] == "client_player":
                                server_module.turn[0] = "server_turn"
                    elif check_data[0] == "restore_cell":
                        enemy_matrix[int(check_data[2])][int(check_data[3])] = int(check_data[1])
                    elif check_data[0] == "medal":
                        for medal in check_data[1:-1]:
                            if int(medal) not in server_module.save_medals_coordinates:
                                server_module.save_medals_coordinates.append(int(medal))
                    elif check_data[0] == "money":
                        server_module.enemy_balance[0] = int(check_data[1])
                        enemy_balance_in_jar.update_text()
                    if check_data[0] == "keep-alive":
                        enemy_check_fire[0] = 0
                        count_hit_auto_rocket[0] = 0

                        for number_cell in check_data[1:-1]:
                            int_number_cell = int(number_cell)
                            row = int_number_cell // 10
                            col = int_number_cell % 10
                            if list_grid[row][col] != 7:
                                list_grid[row][col] = 7
        except:
            continue        
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
        #----------------------------------------------------------------
        if tsest[0] == True:
            if Schechik_before_removeall[0] < 1:
                stew_row.clear()
                stew_col.clear()
                tsest[0]=False
            Schechik_before_removeall[0] -= 1



        if len(server_module.player_died_ships) >= 10 and len(server_module.enemy_died_ships) <= 9:
            if server_module.list_player_role[0] == "server_player":
                # список для хранения кто выиграл
                server_module.list_check_win[0] = "win_client"
            elif server_module.list_player_role[0] == "client_player":
                server_module.list_check_win[0] = "win_server"
        elif len(server_module.player_died_ships) <= 9 and len(server_module.enemy_died_ships) >= 10:
            if server_module.list_player_role[0] == "server_player":
                # список для хранения кто выиграл
                server_module.list_check_win[0] = "win_server"
            elif server_module.list_player_role[0] == "client_player":
                server_module.list_check_win[0] = "win_client"

        if server_module.list_check_win[0] == None:
            count_ships_player = 0
            count_ships_enemy = 0
            count_zero = 0
            for row in list_grid:
                for cell in row:
                    if cell in [1, 2, 3, 4]:
                        count_ships_player += 1
            for row in enemy_matrix:
                for cell in row:
                    if cell in [1, 2, 3, 4]:
                        count_ships_enemy += 1
                    if cell == 0:
                        count_zero += 1
            if count_ships_player >= 1 and count_ships_enemy == 0 and count_zero != 100:
                if server_module.list_player_role[0] == "server_player":
                    # список для хранения кто выиграл
                    server_module.list_check_win[0] = "win_server"
                elif server_module.list_player_role[0] == "client_player":
                    server_module.list_check_win[0] = "win_client"
            elif count_ships_player == 0 and count_ships_enemy >= 1 and count_zero != 100:
                if server_module.list_player_role[0] == "server_player":
                    server_module.list_check_win[0] = "win_client"
                elif server_module.list_player_role[0] == "client_player":
                    server_module.list_check_win[0] = "win_server"
        #----------------------------------------------------------------
        check_player_balance[0] = shop.money_list[0]
        # функция которая красиво добавляет/отнимает монетки
        count_money(
            check_buy_bomb = shop.check_buy_bomb_attack[0], 
            check_buy_restorce = shop.but_flag[0],
            check_buy_auto_rocket = shop.flagbimb200[0],
            check_buy_radar = shop.flag_radar[0],
            check_buy_fire_fighter = shop.flag_put_out_the_fire[0],
            check_buy_random_hits = shop.random_hits[0],
            cehck_buy_fire_rocket = shop.flag_arson[0]
            )
        
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
        if count_sound_time[0] >= 1:
            player_face.draw_image(screen = module_screen.main_screen)
            enemy_face.draw_image(screen = module_screen.main_screen)
        enemy_before_choice.draw_image(screen = module_screen.main_screen)
        player_before_choice.draw_image(screen = module_screen.main_screen)

        if count_sound_time[0] >= 1:
            enemy_before_choice.fade_out()
            player_before_choice.fade_out()

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
            cell.draw(screen = module_screen.main_screen)
        for empty_cell in list_object_map_enemy:
            empty_cell.draw(screen = module_screen.main_screen)

        # відмалбовуємо кораблі які ми роставляли , але у змнешаному вигялді , та у іншому місці(сітці яка також зменшилась у розмірі)
        for num , ship  in enumerate(list_ships):
            list_ships[num].draw_sheep(screen = module_screen.main_screen)

            
        for killed_ship_draw in killed_ships_draw:
   
            if killed_ship_draw[2] == 1:
                if killed_ship_draw[3] == "horizontal":
                    killed_1ship.x_cor = killed_ship_draw[0]
                    killed_1ship.y_cor = killed_ship_draw[1]
                    killed_1ship.draw_image(screen= main_screen)
                elif killed_ship_draw[3] == "vertical":
                    killed_1ship_rotate.x_cor = killed_ship_draw[0]
                    killed_1ship_rotate.y_cor = killed_ship_draw[1]
                    killed_1ship_rotate.draw_image(screen= main_screen)
            if killed_ship_draw[2] == 2:
                if killed_ship_draw[3] == "horizontal":
                    killed_2ship.x_cor = killed_ship_draw[0]
                    killed_2ship.y_cor = killed_ship_draw[1]
                    killed_2ship.draw_image(screen= main_screen)
                elif killed_ship_draw[3] == "vertical":
                    killed_2ship_rotate.x_cor = killed_ship_draw[0]
                    killed_2ship_rotate.y_cor = killed_ship_draw[1]
                    killed_2ship_rotate.draw_image(screen= main_screen)
            if killed_ship_draw[2] == 3:
                if killed_ship_draw[3] == "horizontal":
                    killed_3ship.x_cor = killed_ship_draw[0]
                    killed_3ship.y_cor = killed_ship_draw[1]
                    killed_3ship.draw_image(screen= main_screen)
                elif killed_ship_draw[3] == "vertical":
                    killed_3ship_rotate.x_cor = killed_ship_draw[0]
                    killed_3ship_rotate.y_cor = killed_ship_draw[1]
                    killed_3ship_rotate.draw_image(screen= main_screen)
            if killed_ship_draw[2] == 4:
                if killed_ship_draw[3] == "horizontal":
                    killed_4ship.x_cor = killed_ship_draw[0]
                    killed_4ship.y_cor = killed_ship_draw[1]
                    killed_4ship.draw_image(screen= main_screen)
                elif killed_ship_draw[3] == "vertical":
                    killed_4ship_rotate.x_cor = killed_ship_draw[0]
                    killed_4ship_rotate.y_cor = killed_ship_draw[1]
                    killed_4ship_rotate.draw_image(screen= main_screen)           

        for cross_animation in list_cross_player:
            if len(enemy_list_fire) > 0:
                for row_col in enemy_list_fire:
                    exist = False
                    for cltk in list_object_map:
                        if cltk.x == cross_animation.X_COR and cltk.y == cross_animation.Y_COR:
                            number_cell_cross = list_object_map.index(cltk)
                    row_anim = number_cell_cross // 10
                    col_anim = number_cell_cross % 10
                    check_time = None
                    for row_col_enemy in enemy_list_fire:
                        if row_col_enemy[0] == row_anim and row_col_enemy[1] == col_anim:
                            check_time = row_col_enemy[-1]
                    if check_time == 0:
                        exist = True
                    if exist == False:
                        cross_animation.animation(main_screen = module_screen.main_screen , count_image = 13)
            else:
                cross_animation.animation(main_screen = module_screen.main_screen , count_image = 13)

        # кнопка для открытия магазина
        if one_data_fire[0] >= 1 and server_module.check_time[0] == 1:
            one_data_fire[0] = 0
        shop_and_tasks.draw(surface = module_screen.main_screen)
        if server_module.check_time[0] == 0 and one_data_fire[0] == 0:
            if len(row_fire_col_anim) > 0:
                for fire in list_fire:
                    fire[-1] += 1
            try:
                for fire in enemy_list_fire:
                    fire[-1] += 1
            except:
                pass
            one_data_fire[0] += 1
        if server_module.check_time[0] < 1:
                test_time[0] = 0
        if number_of_ship_sonfire != 0:  # Проверяет, есть ли хотя бы один непустой
            if test_time[0] == 0 and len(data_player_shot) == 0 and server_module.check_time[0] >= 1 and check_animation[0] == "" and flag_miss_rocket_animation[0] == "":
                test_time[0] += 1
                for index, element in enumerate(Cordi_Burning_Ship):
                    try:
                        if len(element) != 0:
                            if Cordi_Burning_Ship[index][0] != 0 and Cordi_Burning_Ship[index]:
                                # check_need_skip = False
                                if Cordi_Burning_Ship[index][0] == 4:
                                    ship_element = 1
                                elif Cordi_Burning_Ship[index][0] == 3:
                                    ship_element = 2
                                elif Cordi_Burning_Ship[index][0] == 2:
                                    ship_element = 3
                                elif Cordi_Burning_Ship[index][0] == 1:
                                    ship_element = 4

                                try:
                                    row_fire , col_fire = Cordi_Burning_Ship[index][ship_element]
                                except IndexError:
                                    ship_element -= 1
                                    row_fire , col_fire = Cordi_Burning_Ship[index][ship_element]
                                    Cordi_Burning_Ship[index][0] = 0
  
                                try:
                                    str_col = str(col_fire)
                                    cell_number = row_fire * 10 + int(str_col[-1])
                                    if enemy_matrix[row_fire][col_fire] == 7 and cell_number not in first_shot_fire:
                                        row_fire , col_fire = Cordi_Burning_Ship[index][ship_element + 1]
                                except:
                                    pass

                                if row_fire in stew_row:
                                    Cordi_Burning_Ship[index][0] = 0
                                    flagstop = True
                                    tsest[0]= True
                                    Schechik_before_removeall[0] = 40

                                if col_fire in stew_col:
                                    Cordi_Burning_Ship[index][0] = 0
                                    flagstop = True
                                    tsest[0] = True
                                    Schechik_before_removeall[0] = 40
                        
                                if  row_fire in stew_row  and  col_fire in stew_col:
                                    Cordi_Burning_Ship[index][0] = 0
                                    flagstop = True
                                    tsest[0]= True
                                    Schechik_before_removeall[0] = 40
            
                                if  (row_fire +1) in stew_row  and  col_fire in stew_col:
                                    Cordi_Burning_Ship[index][0] = 0
                                    flagstop = True
                                    tsest[0] = True
                                    Schechik_before_removeall[0] = 40
                                                                    
                                if  row_fire in stew_row  and  (col_fire + 1) in stew_col:
                                    Cordi_Burning_Ship[index][0] = 0
                                    flagstop = True
                                    tsest[0] = True
                                    Schechik_before_removeall[0] = 40
                                    
                                if  (row_fire -1) in stew_row  and  col_fire in stew_col:
                                    Cordi_Burning_Ship[index][0] = 0
                                    flagstop = True
                                    tsest[0]=True
                                    Schechik_before_removeall[0] = 40
                                    
                                if  row_fire in stew_row  and  (col_fire - 1) in stew_col:
                                    Cordi_Burning_Ship[index][0] = 0
                                    flagstop = True
                                    tsest[0] = True
                                    Schechik_before_removeall[0] = 40
                                
                                if flagstop != True: 
                                    enemy_matrix[row_fire][col_fire] = 7
                                    data_player_shot.append("fire")
                                    data_player_shot.append(row_fire)
                                    data_player_shot.append(col_fire)
                                    row_fire_col_anim.append([row_fire, 0])
                                    col_fire_row_anim.append([col_fire, 0])
                                    if Cordi_Burning_Ship[index][0] <= 5 - len(element) - 1: 
                                        Cordi_Burning_Ship[index][0] = 0
                                    else:
                                        Cordi_Burning_Ship[index][0] -= 1
                            else:
                                # очищаем данные если потушили пожар
                                flagstop = False 
                    except:
                        del Cordi_Burning_Ship[index]
                        continue
                    
                list_check_need_send[0] = True

        #----------------------------------------------------------------
        # когда игрок стреляет огнем анимация
        if len(row_fire_col_anim) > 0 and check_animation[0] == "":
            for i in range(0 , len(row_fire_col_anim)):
                row_anim = row_fire_col_anim[i][0]
                col_anim = col_fire_row_anim[i][0]
                str_col_anima = str(col_anim)
                cltx = (row_anim * 10) + int(str_col_anima[-1])
                x = list_object_map_enemy[cltx].x
                y = list_object_map_enemy[cltx].y

                fire_animation = Animation(
                    image_name = "0.png", 
                    width = 55, 
                    height = 50, 
                    x_cor = x,
                    y_cor = y + 5, 
                    need_clear = False, 
                    name_folder = "fire_animation",
                    animation_speed = 6
                    )
                bolinka = True
                for fireok in list_fire:
                    if fireok[0] == row_anim and fireok[1] == col_anim:
                        bolinka = False
                if bolinka:
                    list_fire.append([row_anim, col_anim, fire_animation, 0])

        for fire_animation in list_fire:
            if fire_animation[-1] == 0:
                fire_animation[2].animation(main_screen = module_screen.main_screen , count_image = 9)
                if fire_animation[2].COUNT_IMAGES >= 7:
                    fire_animation[2].COUNT_IMAGES = 0
                    fire_animation[2].IS_ANIMATION_DONE = False
                
        #----------------------------------------------------------------

        #----------------------------------------------------------------
        #огонь когда тсреляет соперник
        if len(enemy_row_fire) > 0:
            for i in range(0 , len(enemy_row_fire)):
                row_anim = enemy_row_fire[i][0]
                col_anim = enemy_col_fire[i][0]
                str_col_anima = str(col_anim)
                cltx = (row_anim * 10) + int(str_col_anima[-1])
                x = list_object_map[cltx].x
                y = list_object_map[cltx].y

                fire_animation = Animation(
                    image_name = "0.png", 
                    width = 55, 
                    height = 50, 
                    x_cor = x,
                    y_cor = y + 5, 
                    need_clear = False, 
                    name_folder = "fire_animation",
                    animation_speed = 6
                    )
                bolinka = True
                for fireok in enemy_list_fire:
                    if fireok[0] == row_anim and fireok[1] == col_anim:
                        bolinka = False
                if bolinka:
                    enemy_list_fire.append([row_anim, col_anim, fire_animation, 0])
        #----------------------------------------------------------------
        for enemy_fire in enemy_list_fire:
            if enemy_fire[-1] == 0:
                enemy_fire[2].animation(main_screen = module_screen.main_screen , count_image = 9)
                if enemy_fire[2].COUNT_IMAGES >= 7:
                    enemy_fire[2].COUNT_IMAGES = 0
                    enemy_fire[2].IS_ANIMATION_DONE = False

        
        #----------------------------------------------------------------
        # отрисовываем анимации зачерканных клеточек на своем поле, если враг промазал
        for animation_miss in list_animation_miss:
            animation_miss.animation(main_screen = module_screen.main_screen, count_image = 29)
    
        #----------------------------------------------------------------
        # отрисовка зачеркнутых клеточек когда игрок промазал по кораблю
        for anim_miss in our_miss_anim:
            anim_miss.animation(main_screen = module_screen.main_screen, count_image = 29)
        #----------------------------------------------------------------
        #----------------------------------------------------------------
        #перебор матрицы врага чтобы если что отрисовали не достающие крестики и зачеркнутые клеточки(матрица врага слева)
        # например после удара бомбой
        update_enemy_matrix_animations(
            check_animation_rocket = check_animation, 
            flag_miss_rocket_animation = flag_miss_rocket_animation, 
            list_cross = list_cross,
            our_miss_anim = our_miss_anim,
            list_fire = list_fire
        )
                        
        # отрисовка крестиков если игрок попал по кораблю(на поле врага , слева)
        for cross in list_cross:
            cross.animation(main_screen = module_screen.main_screen , count_image = 13)


        if check_animation[0] == "start_animation":
            rocket_animation.X_COR = x_hit_the_ship[0] - 231
            rocket_animation.Y_COR = y_hit_the_ship[0] - 23
            # проверка на окончание анимация полета ракеті 
            if rocket_animation.animation(main_screen = module_screen.main_screen , count_image = 7):
                # shot_sound.play2(loops = 1)
                animation_boom.X_COR = x_hit_the_ship[0] - 23
                animation_boom.Y_COR = y_hit_the_ship[0] - 23
                screen_shake[0] = 31
                if animation_boom.animation(main_screen = module_screen.main_screen , count_image = 7):
                    rocket_animation.clear_animation()
                    animation_boom.clear_animation()
                    check_animation[0] = ""
        elif check_animation[0] == "auto_rocket":
            animation_auto_rocket.X_COR = x_hit_the_ship[0] - 150
            animation_auto_rocket.Y_COR = y_hit_the_ship[0] - 23
            screen_shake[0] = 31
            if animation_auto_rocket.animation(main_screen = module_screen.main_screen , count_image = 13):

                animation_auto_rocket.clear_animation()
                check_animation[0] = ""
        elif check_animation[0] == "fire_rocket":
            fire_rocket_animation.X_COR = x_hit_the_ship[0] - 170
            fire_rocket_animation.Y_COR = y_hit_the_ship[0] - 70
            screen_shake[0] = 31
            if fire_rocket_animation.animation(main_screen = module_screen.main_screen , count_image = 20):
                fire_rocket_animation.clear_animation()
                check_animation[0] = ""
        elif check_animation[0] == "radar_animation":
            radar_animation.X_COR = x_hit_the_ship[0] - 55
            radar_animation.Y_COR = y_hit_the_ship[0] - 55
            if radar_animation.animation(main_screen = module_screen.main_screen , count_image = 41):
                radar_animation.clear_animation()
                check_animation[0] = ""
                radar_flag[0] = True

        if radar_flag[0] == True:
            if radar_flag[1] < 100:
                for cell_anim in radar.list_cells:
                    cell_anim.fade_in() 
                    cell_anim.visible += 100 / (radar.list_cells.index(cell_anim) + 1)
                    cell_anim.draw_image(screen = main_screen)
                    if cell_anim.visible >= 255:
                        radar_flag[1] += 1
            if radar_flag[1] >= 100:
                for cell_anim in radar.list_cells:
                    cell_anim.draw_image(screen = main_screen)
                radar_flag[1] += 1
                if radar_flag[1] >= 200:
                    for cell_anim in radar.list_cells:
                        cell_anim.fade_out()
                        if cell_anim.visible <= 1:
                            radar.list_cells.clear()
                            radar_flag[0] = False
                            radar_flag[1] = 0

        #************************************************************************************************
        # отрисовка промаха ракетой, и зарисовка клеточек(когда игрок атакует врага)
        if flag_miss_rocket_animation[0] == "start_animation":
            miss_rocket.X_COR = x_hit_the_ship[0] - 100
            miss_rocket.Y_COR = y_hit_the_ship[0] - 20
            if miss_rocket.animation(main_screen = module_screen.main_screen , count_image = 7):
                miss_water_sound.play2(loops = 1)
                miss_rocket.clear_animation()
                flag_miss_rocket_animation[0] = ""
        elif flag_miss_rocket_animation[0] == "miss_auto_rocket":
            miss_auto_rocket.X_COR = x_hit_the_ship[0] - 170
            miss_auto_rocket.Y_COR = y_hit_the_ship[0] - 20
            if miss_auto_rocket.animation(main_screen = module_screen.main_screen , count_image = 12):
                miss_water_sound.play2(loops = 1)
                miss_auto_rocket.clear_animation()
                flag_miss_rocket_animation[0] = ""
        #************************************************************************************************
        #----------------------------------------------------------------
        # анимация потери соеденения
        if server_module.check_connection[0] == False:
            animation_connection_problem.animation(main_screen = main_screen, count_image = 10)
            if animation_connection_problem.COUNT_IMAGES >= 4:
                animation_connection_problem.clear_animation()
        #----------------------------------------------------------------

        shop.button_restores_cell.draw(screen = module_screen.main_screen)

        # эти функция для проверки , попал ли соперник по нашем кораблям
        check_fire = server_module.enemy_data[0].split(' ')
        # if check_fire[0] == "keep-alive":
        check_and_add_hit_markers(
            x_enemy_cross = x_enemy_cross, 
            y_enemy_cross = y_enemy_cross, 
            list_cross_player = list_cross_player,
            enemy_list_fire = enemy_list_fire,
            list_animation_miss = list_animation_miss
        )

        # анимация использования аптечки
        if health_anim[0] == True:
            for cross in list_cross_player:
                if cross.X_COR  == animation_health.X_COR and cross.Y_COR  == animation_health.Y_COR:
                    list_cross_player.remove(cross)
            if animation_health.animation(main_screen = module_screen.main_screen, count_image = 6):
                health_anim[0] = False
                animation_health.clear_animation()

        if fire_fighter_anim[0] == True:
            fire_fighter_animation.X_COR = x_hit_the_ship[0] - 31
            fire_fighter_animation.Y_COR = y_hit_the_ship[0] - 26
            if fire_fighter_animation.animation(main_screen = module_screen.main_screen, count_image = 8):
                fire_fighter_anim[0] = False
                fire_fighter_animation.clear_animation()


        mouse_x , mouse_y = pygame.mouse.get_pos()
        # отрисовка сетки для прицеливания при авто-ударе
        if shop.shop_item[0].TURN != "Up":
            if shop.flagbimb200[0] == 'yes' and activate_auto_rocket[0] == True:
                center_xy = draw_cursor(screen = module_screen.main_screen, mouse_x=mouse_x, mouse_y=mouse_y,grid = enemy_grid, color =colorsetka)
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
        if shop.flag_radar[0] == True:
            radar_icon.draw_image(screen = module_screen.main_screen)
        if shop.flag_arson[0] == "yes":
            fire_rocket_icon.draw_image(screen = module_screen.main_screen)
        if shop.flag_put_out_the_fire[0] == "yes":
            fire_fighter_icon.draw_image(screen = module_screen.main_screen)
        if shop.random_hits[0] == True:
            random_hits_icon.draw_image(screen = module_screen.main_screen)

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
        if shop.second_task.TEXT == shop.list_second_task[0]:
            shop.first_kill_two_decker()

        # magnat echievement
        if shop.waste_money[0] >= 350 and 5 not in achievement.list_save_coords_achiv:
            magnate_achievement.ACTIVE = True
            magnat_medal.ACTIVE = True
            achievement.list_save_coords_achiv.append(5)
            achievement.list_save_coords_achiv[0] = True
            count_money_hit[0] += 20
        # destoyer achievement
        # для бомбы задание
        if check_bomb[0] == True and 9 not in achievement.list_save_coords_achiv:
            new_killed_ships[0] = len(server_module.enemy_died_ships)
            if new_killed_ships[0] - old_killed_ships[0] >= 2:
                destroyer_medal.ACTIVE = True
                destroyer_achievement.ACTIVE = True
                achievement.list_save_coords_achiv.append(9)
                achievement.list_save_coords_achiv[0] = True
                count_money_hit[0] += 20

        if check_bomb[0] == True and 11 not in achievement.list_save_coords_achiv:
            new_killed_ships[0] = len(server_module.enemy_died_ships)
            if new_killed_ships[0] - old_killed_ships[0] >= 1:
                if count_5[0] <= 0:
                    if 11 not in achievement.list_save_coords_achiv:
                        target_attack_achievement.ACTIVE = True
                        target_attack_medal.ACTIVE = True
                        achievement.list_save_coords_achiv.append(11)
                        achievement.list_save_coords_achiv[0] = True
                        count_money_hit[0] += 20
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
            count_money_hit[0] += 20

        # аниамция рандомного выбиора
        if server_module.list_player_role[0] == "server_player":
            animation_random_player.animation(main_screen = main_screen, count_image = 29)
        elif server_module.list_player_role[0] == "client_player":
            animation_random_player.animation(main_screen = main_screen, count_image = 30)

        

        achievement.piooner() 
        achievement.lone_hunter()
        achievement.first_kill_four_decker_achivment()
        achievement.strategist(player_killed_ships = server_module.player_died_ships , role = server_module.list_player_role[0] , winner = server_module.list_check_win[0])

        if connection[0] == False:
            reonnect_image.draw_image(screen = main_screen)

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
                change_scene("END GAME")
                pygame.quit()
                sys.exit()
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
                        activate_radar[0] = False
                        activate_fire_fighter[0] = False
                        activate_fire_rocket[0] = False
                        activate_random_hits[0] = False
                        active_product_shine.x_cor = bomb_icon.x_cor - 17
                        active_product_shine.y_cor = bomb_icon.y_cor - 17
                if shop.flagbimb200[0] == "yes":
                    if auto_rocket_icon.rect.collidepoint(mouse):
                        activate_auto_rocket[0] = True
                        activate_bomb[0] = False
                        activate_restore_cell[0] = False
                        activate_radar[0] = False
                        activate_fire_fighter[0] = False
                        activate_fire_rocket[0] = False
                        activate_random_hits[0] = False
                        active_product_shine.x_cor = auto_rocket_icon.x_cor - 13
                        active_product_shine.y_cor = auto_rocket_icon.y_cor - 10
                if shop.but_flag[0] == True:
                    if restore_cell_icon.rect.collidepoint(mouse):
                        activate_restore_cell[0] = True
                        activate_bomb[0] = False
                        activate_auto_rocket[0] = False
                        activate_radar[0] = False
                        activate_fire_fighter[0] = False
                        activate_fire_rocket[0] = False
                        activate_random_hits[0] = False
                        active_product_shine.x_cor = restore_cell_icon.x_cor - 17
                        active_product_shine.y_cor = restore_cell_icon.y_cor - 20
                if shop.flag_radar[0] == True:
                    if radar_icon.rect.collidepoint(mouse):
                        activate_radar[0] = True
                        activate_bomb[0] = False
                        activate_auto_rocket[0] = False
                        activate_restore_cell[0] = False
                        activate_fire_fighter[0] = False
                        activate_fire_rocket[0] = False
                        activate_random_hits[0] = False
                        active_product_shine.x_cor = radar_icon.x_cor - 15
                        active_product_shine.y_cor = radar_icon.y_cor - 15
                if shop.flag_arson[0] == "yes":
                    if fire_rocket_icon.rect.collidepoint(mouse):
                        activate_fire_rocket[0] = True
                        activate_bomb[0] = False
                        activate_auto_rocket[0] = False
                        activate_radar[0] = False
                        activate_fire_fighter[0] = False
                        activate_restore_cell[0] = False
                        activate_random_hits[0] = False
                        active_product_shine.x_cor = fire_rocket_icon.x_cor - 15
                        active_product_shine.y_cor = fire_rocket_icon.y_cor - 15
                if shop.flag_put_out_the_fire[0] == "yes":
                    if fire_fighter_icon.rect.collidepoint(mouse):
                        activate_fire_fighter[0] = True
                        activate_bomb[0] = False
                        activate_auto_rocket[0] = False
                        activate_radar[0] = False
                        activate_fire_rocket[0] = False
                        activate_restore_cell[0] = False
                        activate_random_hits[0] = False
                        active_product_shine.x_cor = fire_fighter_icon.x_cor - 15
                        active_product_shine.y_cor = fire_fighter_icon.y_cor - 15
                if shop.random_hits[0] == True:
                    if random_hits_icon.rect.collidepoint(mouse):
                        activate_random_hits[0] = True
                        activate_bomb[0] = False
                        activate_auto_rocket[0] = False
                        activate_radar[0] = False
                        activate_fire_fighter[0] = False
                        activate_fire_rocket[0] = False
                        activate_restore_cell[0] = False
                        active_product_shine.x_cor = random_hits_icon.x_cor - 15
                        active_product_shine.y_cor = random_hits_icon.y_cor - 15

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
    
                if shop.shop_item[0].TURN != "Up" and connection[0] == True:          
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
                                            x_animation = list_object_map[cltx].x
                                            y_animation = list_object_map[cltx].y
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

                                        if pozhar_col !=  []:
                                            if shop.flag_put_out_the_fire[0] == "yes" and activate_fire_fighter[0] == True:
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
                                                x_animation = list_object_map[cltx].x
                                                y_animation = list_object_map[cltx].y
                                                x_hit_the_ship[0] = x_animation
                                                y_hit_the_ship[0] = y_animation
                                                # Узнаем номер клетки где стоит кораблик
                                                number_cell_our = list_object_map.index(cell)
                                                # Переделываем значение клетки в строку чтобы можно было лекго узнать в калоночке он стоит
                                                str_col_our = str(number_cell_our) 
                                                # Вычисляем номер рядка где стоит корабль(например 23 , делим на 10 без остатка и получаем 2 , вот нашь столбец)
                                                row = number_cell_our // 10  
                                                #Колонку кораблика вычисляем по такому принципу
                                                # Например опять 23 число номер колонки где стоит корабль , тогда с помощью -1 мы берем последнее число тоесть тройку, и вот так получаем номер колонки
                                                col = int(str_col_our[-1])
                                                if row in pozhar_row:
                                                    if col in pozhar_col:
                                                        for arson in enemy_list_fire:
                                                            if arson[0] == row and arson[1] == col:
                                                                arson[-1] += 1
                                                        activate_fire_fighter[0] = False
                                                        fire_fighter_anim[0] = True
                                                        fire_fighter_animation.X_COR = x_animation
                                                        fire_fighter_animation.Y_COR = y_animation
                                                        data_player_shot.append("fire_fighter")
                                                        data_player_shot.append(row)
                                                        data_player_shot.append(col)
                                                        list_check_need_send[0] = True
                                                        shop.flag_put_out_the_fire[0] = "no"
                                                        active_product_shine.x_cor = -100
                                                        active_product_shine.y_cor = -100

                x_mouse, y_mouse = pygame.mouse.get_pos()                                           
                if shop.shop_item[0].TURN != "Up" and connection[0] == True:
                    if check_animation[0] == "" and flag_miss_rocket_animation[0] == "" and len(radar.list_cells) == 0:
                        # перевіряємо за яку роль грає гравець                    
                        if (server_module.list_player_role[0] == "server_player" and server_module.turn[0] == "server_turn" and len(data_player_shot) == 0) or (server_module.list_player_role[0] == "client_player" and server_module.turn[0] == "client_turn" and len(data_player_shot) == 0) :
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
                                                if enemy_matrix[row][col] not in (5, 7, 0):
                                                    if shop.flag_arson[0] == "yes" and activate_fire_rocket[0] is True:
                                                        check_animation[0] = "fire_rocket"
                                                        number_of_decks = enemy_matrix[row][col]
                                                        shop.flag_arson[0] = "no"
                                                        activate_fire_rocket[0] = False
                                                        promah = [0, 5, 7]
                                                        if number_of_decks not in promah:
                                                            if magnat_medal.ACTIVE == True:
                                                                count_money_hit[0] += 15
                                                            count_money_hit[0] += 5
                                                            str_col_gav = str(col)
                                                            cell_meow = (row * 10) + int(str_col_gav[-1])
                                                            first_shot_fire.append(cell_meow)
                                                            try:
                                                                xxxxx = find_all_neighbors(matrix=enemy_matrix, row=row, col=col, target_value=number_of_decks)
                                                                # xxxxx = find_all_auto_rocket(matrix=[row [:] for row in enemy_matrix], row=row, col=col, target_value=number_of_decks)  
                                                                # if len (xxxxx) == 10 :  
                                                                #     unique_data = []  
                                                                #     for item in xxxxx:  
                                                                #         if item not in unique_data:  
                                                                #             unique_data.append(item)  
                                                                #     xxxxx =  unique_data
                                                                colich = len(xxxxx)
                                                                Cordi_Burning_Ship.append([])
                                                                Cordi_Burning_Ship[number_of_ship_sonfire[0]] = xxxxx
                                                                Cordi_Burning_Ship[number_of_ship_sonfire[0]].insert(0, 0)
                                                                Cordi_Burning_Ship[number_of_ship_sonfire[0]][0] = 4
                                                                number_of_ship_sonfire[0] += 1
                                                            except:
                                                                pass
                                                        active_product_shine.x_cor = -100
                                                        active_product_shine.y_cor = -100
                                                # else:
                                                    # shop.flag_arson[0] = "no"
                                                if activate_radar[0] == True and shop.flag_radar[0] == True:
                                                    if row > 0 and row < 9:
                                                        if col > 0 and col < 9:
                                                            check_animation[0] = "radar_animation"
                                                            radar_sound.play2(loops = 1)
                                                            x_hit_the_ship[0] = list_object_map_enemy[list_object_map_enemy.index(cell)].x
                                                            y_hit_the_ship[0] = list_object_map_enemy[list_object_map_enemy.index(cell)].y
                                                            radar.check_target_grid(enemy_matrix = enemy_matrix, row = row, column = col)
                                                            activate_radar[0] = False
                                                            shop.flag_radar[0] = False
                                                            active_product_shine.x_cor = -100
                                                            active_product_shine.y_cor = -100
                                                            server_module.check_time[0] = 0
                                                            # записуємо у лист який перевіряє чи потрібно відпарвляти дані на сервер флаг "yes", але чергу не змінюємо оскільки гравець попав по кораблю
                                                            if server_module.list_player_role[0] == "client_player":
                                                                server_module.turn[0] = "server_turn"
                                                            elif server_module.list_player_role[0] == "server_player":
                                                                server_module.turn[0] = "client_turn"
                                                            data_player_shot.append("enemy_turn")
                                                            list_check_need_send[0] = True
                                                elif activate_random_hits[0] == True:
                                                    random_hits_matrix()
                                                    list_check_need_send[0] = True
                                                    shop.random_hits[0] = False
                                                    activate_random_hits[0] = False
                                                    active_product_shine.x_cor = -100
                                                    active_product_shine.y_cor = -100
                                                # автоудар
                                                elif shop.flagbimb200[0] == "yes" and numberofbim[0] not in shop.cheak and activate_auto_rocket[0] == True: 
                                                    cells = auto_aim(row = row, column = col)
                                                    if len(cells) > 0:
                                                        data_player_shot.append("auto_rocket")
                                                        cellek = cells[0]
                                                        row = cellek // 10
                                                        col = cellek % 10
                                                        if enemy_matrix[row][col] in [1, 2, 3, 4]:
                                                            screen_shake[0] = 31
                                                            check_animation[0] = "auto_rocket" 
                                                            server_module.check_time[0] = 0
                                                            # записуємо у лист який перевіряє чи потрібно відпарвляти дані на сервер флаг "yes", але чергу не змінюємо оскільки гравець попав по кораблю
                                                            if server_module.list_player_role[0] == "server_player":
                                                                    server_module.turn[0] = "server_turn"
                                                            elif server_module.list_player_role[0] == "client_player":
                                                                server_module.turn[0] = "client_turn"   
                                                            x_hit_the_ship[0] = list_object_map_enemy[cellek].x
                                                            y_hit_the_ship[0] = list_object_map_enemy[cellek].y
                                                            if shop.third_task.TEXT == shop.list_third_task[1]:
                                                                shop.single_ships.append(enemy_matrix[row][col])
                                                            if shop.fourth_task.TEXT == shop.list_fourth_task[0]:
                                                                shop.first_shot_is_kill(enemy_matrix[row][col])
                                                            if shop.third_task.TEXT == shop.list_third_task[2]:
                                                                shop.check_three_2decker_ship_in_row.append(enemy_matrix[row][col])
                                                            if shop.first_task.TEXT == shop.list_first_task[-1]:
                                                                shop.three_hits_in_row(7)
                                                            if shop.third_task.TEXT == shop.list_third_task[-1]:
                                                                shop.count_three_ships.append(enemy_matrix[row][col])
                                                            if shop.second_task.TEXT == shop.list_second_task[2]:
                                                                shop.ship_hits.append(enemy_matrix[row][col])
                                                            if shop.fourth_task.TEXT == shop.list_fourth_task[1]:
                                                                shop.ship_hits_three.append(enemy_matrix[row][col])
                                                            if shop.first_task.TEXT == shop.list_first_task[0]:
                                                                shop.two_hits_in_row(number_cell = 7)
                                                            if shop.first_task.TEXT == shop.list_first_task[1]:
                                                                shop.four_hits_in_row(number_cell = 7)
                                                            if shop.fourth_task.TEXT == shop.list_fourth_task[-1]:
                                                                shop.eight_hits_in_row(number_cell = 7)
                                                            # ачивки
                                                            achievement.ten_shoot_in_row(7)
                                                            achievement.first_shot(7)
                                                            achievement.single_ships_achiv.append(enemy_matrix[row][col])
                                                            achievement.list_hits_achiv.append(enemy_matrix[row][col])
                                                        elif enemy_matrix[row][col] in [0, 5, 7]:
                                                            server_module.check_time[0] = 0
                                                            # записуємо у лист який перевіряє чи потрібно відпарвляти дані на сервер флаг "yes", але чергу не змінюємо оскільки гравець попав по кораблю
                                                            if server_module.list_player_role[0] == "server_player":
                                                                    server_module.turn[0] = "client_turn"   
                                                            elif server_module.list_player_role[0] == "client_player":
                                                                server_module.turn[0] = "server_turn"   
                                                            flag_miss_rocket_animation[0] = "miss_auto_rocket"
                                                            x_hit_the_ship[0] = list_object_map_enemy[cellek].x
                                                            y_hit_the_ship[0] = list_object_map_enemy[cellek].y
                                                            if shop.third_task.TEXT == shop.list_third_task[1]:
                                                                shop.single_ships.append(0)
                                                            if shop.fourth_task.TEXT == shop.list_fourth_task[0]:
                                                                shop.first_shot_is_kill(0)
                                                            if shop.third_task.TEXT == shop.list_third_task[2]:
                                                                shop.check_three_2decker_ship_in_row.append(0)
                                                            if shop.first_task.TEXT == shop.list_first_task[-1]:
                                                                shop.three_hits_in_row(7)
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
                                                            achievement.first_shot(5)
                                                            achievement.single_ships_achiv.append(5)
                                                            achievement.list_hits_achiv.append(5)
                                                        for cell in cells:
                                                            data_player_shot.append(cell)
                                                            row = cell // 10
                                                            col = cell % 10
                                                            if enemy_matrix[row][col] in [1, 2, 3, 4]:
                                                                enemy_matrix[row][col] = 7
                                                            elif enemy_matrix[row][col] in [0, 5]:
                                                                enemy_matrix[row][col] = 5
                                                        list_check_need_send[0] = True
                                                        shop.flagbimb200[0] = "no"
                                                        activate_auto_rocket[0] = False
                                                        active_product_shine.x_cor = -100
                                                        active_product_shine.y_cor = -100
                                                        
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
                                                elif activate_bomb[0] == False and activate_auto_rocket[0] == False and activate_radar[0] == False and activate_random_hits[0] == False:
                                                    simple_shot(
                                                        col = col, 
                                                        row = row, 
                                                        x_hit_the_ship = x_hit_the_ship, 
                                                        y_hit_the_ship = y_hit_the_ship, 
                                                        flag_miss_rocket_animation = flag_miss_rocket_animation, 
                                                        check_animation_rocket = check_animation,
                                                        cell = cell
                                                    )
                                                    if activate_fire_rocket[0] == True:
                                                        activate_fire_rocket[0] = False
                                                        shop.flag_arson[0] = False
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
        if achievement.strategist_achievement.ACTIVE == False:
            if server_module.list_check_win[0] != None:
                if check_animation[0] == "" and flag_miss_rocket_animation[0] == "":   
                    # якщо вже їтось виграв , то робимо ефект затемнення
                    apply_fade_effect(screen = module_screen.main_screen)
                    # зупиняємо цикл гри
                    run_game = False
                    # змінюємо фрейм бою , на фрейм показу результатів
                    change_scene(game_windows.finish_window)

        if screen_shake[0] > 1:
            screen_shake[0] -= 1

        # отправка полученных медалек врагу
        if achievement.list_save_coords_achiv[0] == True and len(data_player_shot) == 0:
            data_player_shot.append("medal")
            for medals in achievement.list_save_coords_achiv[1:]:
                data_player_shot.append(medals)
            list_check_need_send[0] = True
            achievement.list_save_coords_achiv[0] = False

        if shop.money_list[0] - check_player_balance[0] > 0 or check_player_balance[1] == True:
            if len(data_player_shot) == 0:
                data_player_shot.append("money")
                data_player_shot.append(shop.money_list[0])
                list_check_need_send[0] = True
                check_player_balance[1] = False
            else:
                check_player_balance[1] = True

        # відмальовуємо екран із координатами що збергаються у списку render_offset , щоб якщо гравець потрапив по карблю , то був ефект трясіння
        module_screen.main_screen.blit(pygame.transform.scale(module_screen.main_screen, (1280 , 832)), render_offset)
        # оновлюємо екран
        pygame.display.flip()
