import pygame, random
import modules.game_windows as game_windows
import modules.shop as shop
import modules.screens.screen as module_screen
from ...game_tools import add_money
from ...screens import grid_player, list_object_map, list_object_map_enemy, enemy_grid, list_grid
from ...classes.class_music import music_load_waiting, fight_music
from ...classes.class_click import miss_water_sound
from ...classes.class_medal import player_medal, enemy_medals
from ...classes.class_image import DrawImage
from ...classes.achive_window import list_achieves
from ...classes.class_button import Button
from ...classes.class_text import Font
from ...classes.animation import Animation, rocket_animation, miss_rocket_animation, animation_boom, animation_bomb_boom, animation_health, bomb_animation
from ...classes.class_ship import list_ships
import modules.achievement as achievement
import modules.classes.class_medal as class_medal
from ..button_pressed import check_press_button
from ...game_tools import player_balance_in_jar, enemy_balance_in_jar, ship_border, list_animation_miss, check_number_cell, Missile_200, apply_fade_effect
from ..change_window import change_scene
import modules.server as server_module
from .bomb import upgrade_attack
from ...client import list_check_need_send
# from ...server import enemy_died_ships, player_died_ships, save_medals_coordinates, list_player_role, turn, flag_bomb_animation, dict_save_information

list_check_shop = [None]
def show_shop():
    if shop.shop_item[0].TURN == "Down": 
        list_check_shop[0] = True

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

#fonts
player_nick = Font(size = 48 , name_font= "Jersey15.ttf" , text = server_module.dict_save_information["player_nick"] , screen = module_screen.main_screen , x_cor = 914 , y_cor = 126, text_color = "White")
enemy_nick = Font(size = 48 , name_font= "Jersey15.ttf" , text = server_module.dict_save_information["enemy_nick"] , screen = module_screen.main_screen , x_cor = 437 , y_cor = 126, text_color = "White")
player_points = Font(size = 48 , name_font= "Jersey15.ttf" , text = str(server_module.dict_save_information["player_points"]) , screen = module_screen.main_screen , x_cor = 743 , y_cor = 126, text_color = "White")
enemy_points = Font(size = 48 , name_font= "Jersey15.ttf" , text = str(server_module.dict_save_information["enemy_points"]) , screen = module_screen.main_screen , x_cor = 270 , y_cor = 126, text_color = "White")
frame_nick_player = DrawImage(width = 362 ,height = 69 , x_cor = 222 , y_cor = 116 , folder_name= "backgrounds" , image_name= "frame_nick.png")
second_frame_nick_player = DrawImage(width = 362 ,height = 69 , x_cor = 699 , y_cor = 116 , folder_name= "backgrounds" , image_name= "frame_nick.png")

#Buttons
shop_and_tasks = Button(x= 33 , y = 32,image_path= "show_shop.png" , image_hover_path= "show_shop_hover.png" , width = 36, height = 31 , action= show_shop)


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
    xxxx=grid.coordinates_to_number(center_x, center_y)
    print (f"aahahahavot eta cletca,{xxxx}")
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
# лист в котором хранятся все обьяекты зачеркивания клеточки после промаха ракетой
list_miss_cell = []
#------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------

# флаг который првоеряет надо ли запускать анимацию ракеты если игрок ударил
check_animation_rocket = [""]
# флаг когда надо проигрывать анимацию крестика если попали по кораблю
check_cross_animation  = [""]
# список где хранятся крестики которые отрисовываются в том случаи если игрок попал ко кораблю
list_cross = []
#------------------------------------------------------------------------------------------------


# спсики в которых хранятся координаты где должны отрисовываться анимации если игрок ударил по полю
x_hit_the_ship = [0]
y_hit_the_ship = [0]


# спсиок где хранятся крестки которые ресуюются если враг попал по кораблю игрока
list_cross_player = []

check_achiv = [False]
index_achiv = [100]


numberofbim = [""]

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

    while run_game:
        module_screen.FPS.tick(60)
        current_fps = module_screen.FPS.get_fps()
        rocket_animation.ANIMATION_SPEED = 3 * (60 / current_fps)
        animation_health.ANIMATION_SPEED = 4 * (60 / current_fps)
        animation_boom.ANIMATION_SPEED = 3 * (60 / current_fps)
        animation_bomb_boom.ANIMATION_SPEED = 4 * (60 / current_fps)
        miss_rocket_animation.ANIMATION_SPEED = 3 * (60 / current_fps)
        # print(rocket_animation.ANIMATION_SPEED)
        achievement.player_died_ships_for_achiv[0] = server_module.player_died_ships
        achievement.enemy_dies_ships_for_ahiv[0] = server_module.enemy_died_ships[0]
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


        # ставимо фпс на значення 60
      
        # функция которая красиво добавляет монетки
        add_money(check_buy_bomb = shop.check_buy_bomb_attack[0])


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
        
        # робимо умови щоб відмальовувати картинки чиї зараз хід
        # тобто якщо роль гравця(гравець може бути сервером або клієнтом) співпадає із чергою , то відмальовуємо зображення 
        # яке вказуємо що можемо зараз ходити , якщо ні , то малюємо зображення про заборону ходу
        if server_module.list_player_role[0] == "server_player" and server_module.turn[0] == "server_turn":
            player_face.image_name = "active_player.png"
            enemy_face.image_name = "not_active_enemy.png"
            player_face.load_image()
            enemy_face.load_image()
        elif server_module.list_player_role[0] == "player_client" and server_module.turn[0] == "client_turn":
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


        
        # оновлюємо дані про ник та очки , та відмольовуємо їх
        player_nick.text = server_module.dict_save_information["player_nick"]
        enemy_nick.text = server_module.dict_save_information["enemy_nick"]
        player_points.text = str(server_module.dict_save_information["player_points"])
        enemy_points.text = str(server_module.dict_save_information["enemy_points"])
        player_nick.update_text()
        enemy_nick.update_text()
        player_points.update_text()
        enemy_points.update_text()
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
        # анимация зачеркивания клеточек вокруг убитого корабля
        ship_border()
        # #----------------------------------------------------------------

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
       
        #----------------------------------------------------------------
        # отрисовка зачеркнутых клеточек когда игрок промазал по полю
        for anim_miss in server_module.our_miss_anim:
            anim_miss.animation(main_screen=module_screen.main_screen, count_image=29)
        #----------------------------------------------------------------

        #----------------------------------------------------------------
        #перебор матрицы врага чтобы если что отрисовали не достающие крестики и зачеркнутые клеточки(матрица врага слева)
        # например после удара бомбой
        if server_module.flag_bomb_animation[0] == False and check_animation_rocket[0] == "" and flag_miss_rocket_animation[0] == "":
            for row in range(len(server_module.enemy_matrix[0])):
                for cell in range(len(server_module.enemy_matrix[0][row])):
                    if server_module.enemy_matrix[0][row][cell] in [1, 2, 3, 4]:
                        cltka = (row * 10) + cell
                        x_anim_miss = list_object_map_enemy[cltka].x
                        y_anim_miss = list_object_map_enemy[cltka].y

                        for cross in list_cross:
                            if cross.X_COR == x_anim_miss and cross.Y_COR == y_anim_miss:
                               list_cross.remove(cross)
                    if server_module.enemy_matrix[0][row][cell] == 7:
                        cltka = (row * 10) + cell
                        x_anim_miss = list_object_map_enemy[cltka].x
                        y_anim_miss = list_object_map_enemy[cltka].y

                        cross_animation = Animation(
                        image_name = "0.png", 
                        width = 55, 
                        height = 55, 
                        x_cor = x_anim_miss, 
                        y_cor = y_anim_miss, 
                        need_clear = False , 
                        name_folder = "animation_cross",
                        animation_speed = 3
                        )
                        exists = False
                        for cross in list_cross:
                            if cross.X_COR == cross_animation.X_COR and cross.Y_COR == cross_animation.Y_COR:
                                exists = True
                                break
                        if not exists:
                            list_cross.append(cross_animation)
                    elif server_module.enemy_matrix[0][row][cell] == 5:
                        cltka = (row * 10) + cell
                        x_anim_miss = list_object_map_enemy[cltka].x
                        y_anim_miss = list_object_map_enemy[cltka].y

                        miss_cell_animation = Animation(
                        image_name = "0.png", 
                        width = 55, 
                        height = 55, 
                        x_cor = x_anim_miss + 1, 
                        y_cor = y_anim_miss, 
                        need_clear = False , 
                        name_folder = "animation_miss",
                        animation_speed = 3
                        )
                        exists = False
                        for miss_cell in server_module.our_miss_anim:
                            if miss_cell.X_COR == miss_cell_animation.X_COR and miss_cell.Y_COR == miss_cell_animation.Y_COR:
                                exists = True
                                break
                        if not exists:
                            server_module.our_miss_anim.append(miss_cell_animation)
         #----------------------------------------------------------------

                   
        # #****************************************************************
        # отрисовка крестиков если игрок попал по кораблю(на поле врага , слева)
        # if check_cross_animation[0] == "starts_cross_animation":
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
                    print("--------------------------------")
                    check_animation_rocket[0] = ""
                    # check_cross_animation[0] = "starts_cross_animation"
        #----------------------------------------------------------------

         #************************************************************************************************
        # отрисовка промаха ракетой, и зарисовка клеточек(когда игрок атакует врага)
        if flag_miss_rocket_animation[0] == "start_animation":
            miss_rocket_animation.X_COR = x_hit_the_ship[0] - 231
            miss_rocket_animation.Y_COR = y_hit_the_ship[0] - 23
            if miss_rocket_animation.animation(main_screen = module_screen.main_screen , count_image = 7):
                miss_rocket_animation.clear_animation()
                flag_miss_rocket_animation[0] = ""
        #************************************************************************************************


        shop.button_restores_cell.draw(screen = module_screen.main_screen)

        # эти циклы для проверки , попал ли соперник по нашем кораблям
        for index_row ,row in enumerate(list_grid):
            for index_cell , cell in enumerate(row):
                # то есть если в нашей матрице находится 7 , то это значит что соперник выстрелил успешно
                # 7 - значит что соперник выстрелил успешно по нашей сетке
                if cell == 7:
                    # сохраняем индекс рядка и клеточки в которой находится наш подсетрленный корабль
                    row = index_row
                    cell = str(index_cell)
                    # из двух чисел(индекс рядка и клеточки) мы находим номер клеточки куда выстрелил соперник
                    # То есть например 2й рядок и первая клеточка , то будет клеточка под номером 11
                    cltx = (row * 10) + int(cell[-1])
                    # получаем через список где хранятся клеточки , координати , в якій буде відображатися анимація попадання по нашему кораблю
                    x_enemy_cross[0] = list_object_map[cltx].x
                    y_enemy_cross[0] = list_object_map[cltx].y
                    # создаем екземпляр крестика , чтобы мы могли их отрисовывать столько раз , сколько попали по нашему кораблю
                    cross_animation = Animation(
                        image_name = "0.png" , 
                        width = 55 , 
                        height = 55 , 
                        x_cor =  list_object_map[cltx].x, 
                        y_cor = list_object_map[cltx].y, 
                        need_clear = False , 
                        name_folder = "animation_cross",
                        animation_speed = 3
                    )
                    # Проверка на то чтобы если в определенной клеточке уже стоит крестик, то мы не создавали еще один(для того чтобы не нагружать устройство)
                    exists = False
                    for cross in list_cross_player:
                        # проверяем по координатам каждый крестик с тем который хотим создать 
                        # если такой уже есть, то выходим из цикла и не добавляем с список
                        if cross.X_COR == cross_animation.X_COR and cross.Y_COR == cross_animation.Y_COR:
                            exists = True
                            break
                    if not exists:
                        list_cross_player.append(cross_animation)

        if health_anim[0] == True:
            for cross in list_cross_player:
                if cross.X_COR  == animation_health.X_COR and cross.Y_COR  == animation_health.Y_COR:
                    list_cross_player.remove(cross)
            if animation_health.animation(main_screen = module_screen.main_screen, count_image = 6):
                health_anim[0] = False
                animation_health.clear_animation()


        mouse_x , mouse_y = pygame.mouse.get_pos()
         
        if shop.shop_item[0].TURN != "Up":
            if shop.flagbimb200[0] == 'yes':
                center_xy=draw_cursor(screen = module_screen.main_screen, mouse_x=mouse_x, mouse_y=mouse_y,grid =enemy_grid, color =colorsetka)
                draw_cursor(screen = module_screen.main_screen, mouse_x=mouse_x, mouse_y=mouse_y,grid =enemy_grid, color =colorsetka)
                
                x_mouse=center_xy[0]
                y_mouse=center_xy[1]
                numberofbim[0] = enemy_grid.coordinates_to_number(x_mouse, y_mouse)
                print (x_mouse,y_mouse)
            
            
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

        achievement.piooner() 
        achievement.lone_hunter()
        achievement.first_kill_four_decker_achivment()
        achievement.strategist(player_killed_ships = server_module.player_died_ships , role = server_module.list_player_role[0] , winner = server_module.list_check_win[0])
    
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
                shop_and_tasks.check_click(event = event)
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
                if shop.but_flag[0] == True:
                    if shop.shop_item[0].TURN != "Up":          
                        if x_mouse >= 705 and x_mouse <= 705 + 550:# перевіряємо щоб гравець натискав на свою сітку 
                            if y_mouse >= 257 and y_mouse <= 257 + 550:
                                # шукаємо клітинку на яку натиснув гравець
                                for cell in list_object_map: 
                                    if cell.x <= x_mouse and x_mouse < cell.x + 55:
                                        if cell.y <= y_mouse and y_mouse < cell.y + 55:
                                            # Узнаем номер клетки где стоит кораблик
                                            number_cell_our = list_object_map.index(cell)
                                            # Переделываем значение клетки в строку чтобы можно было лекго узнать в калоночке он стоит
                                            str_col_our = str(number_cell_our) 
                                            # Вычисляем номер рядка где стоит корабль(например 23 , делим на 10 без остатка и получаем 2 , вот нашь столбец)
                                            row = number_cell_our // 10  
                                            #Колонку кораблика вычисляем по такому принципу
                                            # Например опять 23 число номер колонки где стоит корабль , тогда с помощью -1 мы берем последнее число тоесть тройку, и вот так получаем номер колонки
                                            col = int(str_col_our[-1])

                                            clt = (row * 10) + int(str_col_our[-1])

                                            x_anim = list_object_map[clt].x
                                            y_anim = list_object_map[clt].y
                                            # номер клеточки
                                            if list_grid[row][col] == 7:
                                                # сохраняем индекс рядка и клеточки в которой находится наш подсетрленный корабль
                                                row_our = index_row
                                                cell_our = str(index_cell)
                                                cltx = (row_our * 10) + int(cell_our[-1])


                                                animation_health.X_COR = x_anim
                                                animation_health.Y_COR = y_anim
                                                
                                                
                                                if cltx not in check_number_cell:
                                                    try:
                                                        if list_grid[row + 1][col] == 2:
                                                            list_grid[row][col] = 2
                                                    except:
                                                        print("index error")
                                                    try:
                                                        if list_grid[row - 1][col] == 2:
                                                            list_grid[row][col] = 2
                                                    except:
                                                        print("index error")
                                                    try:
                                                        if list_grid[row][col + 1] == 2:
                                                            list_grid[row][col] = 2
                                                    except:
                                                        print("index error")
                                                    try:
                                                        if list_grid[row][col - 1] == 2:
                                                            list_grid[row][col] = 2
                                                    except:
                                                        print("index error")
                                                    try:
                                                        if list_grid[row + 1][col] == 3:
                                                            list_grid[row][col] = 3
                                                    except:
                                                        print("index error")
                                                    try:
                                                        if list_grid[row - 1][col] == 3:
                                                            list_grid[row][col] = 3
                                                    except:
                                                        print("index error")
                                                    try:
                                                        if list_grid[row][col + 1] == 3:
                                                            list_grid[row][col] = 3
                                                    except:
                                                        print("index error")
                                                    try:
                                                        if list_grid[row][col - 1] == 3:
                                                            list_grid[row][col] = 3
                                                    except:
                                                        print("index error")

                                                    try:
                                                        if list_grid[row + 1][col] == 4:
                                                            list_grid[row][col] = 4
                                                    except:
                                                        print("index error")
                                                    try:
                                                        if list_grid[row - 1][col] == 4:
                                                            list_grid[row][col] = 4
                                                    except:
                                                        print("index error")
                                                    try:
                                                        if list_grid[row][col + 1] == 4:
                                                            list_grid[row][col] = 4
                                                    except:
                                                        print("index error")
                                                    try:
                                                        if list_grid[row][col - 1] == 4:
                                                            list_grid[row][col] = 4
                                                    except:
                                                        print("index error")
                                                    if list_grid[row][col] != 7:
                                                        health_anim[0] = True
                                                        shop.but_flag[0] = False
                                                    server_module.row_list[0] = row
                                                    server_module.col_list[0] = col
                                                    server_module.number_list[0] = list_grid[row][col]
                                                    print(list_grid[row][col])

                
                if shop.shop_item[0].TURN != "Up":
                    if check_animation_rocket[0] == "" and flag_miss_rocket_animation[0] == "":
                        # нижче умови для атаки 
                        # перевіряємо за яку роль грає гравець
                        if server_module.list_player_role[0] == "player_client":
                            if server_module.turn[0] == "client_turn":
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
                                                    if shop.check_buy_bomb_attack[0] == True:
                                                        print("BOMBASTIK")
                                                        shop.check_buy_bomb_attack[0] = False
                                                        server_module.flag_bomb_animation[0] = True
                                                        x_hit_the_ship[0] = list_object_map_enemy[list_object_map_enemy.index(cell)].x
                                                        y_hit_the_ship[0] = list_object_map_enemy[list_object_map_enemy.index(cell)].y
                                                        count_7 = [0]
                                                        count_ships = []
                                                        count_misses = []
                                                        server_module.old_killed_ships[0] = len(server_module.enemy_died_ships[0])
                                                        if row == 0 and col == 0:
                                                            upgrade_attack(index = "top_left_corner", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = server_module.count_5)
                                                        elif 0 < row < 9 and 0 < col < 9:
                                                            upgrade_attack(index = "entry_cell", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = server_module.count_5)
                                                        elif 1 <= row < 9 and col == 0:
                                                            upgrade_attack(index = "left_wall", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = server_module.count_5)
                                                        elif row == 9 and col == 0:
                                                            upgrade_attack(index = "bot_left_corner", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = server_module.count_5)
                                                        elif row == 0 and col == 9:
                                                            upgrade_attack(index = "top_right_corner", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = server_module.count_5)          
                                                        elif row == 9 and col == 9:
                                                            upgrade_attack(index = "bot_right_corner", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = server_module.count_5)        
                                                        elif row == 9 and 0 < col < 9:
                                                            upgrade_attack(index = "bot_wall", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = server_module.count_5)
                                                        elif row == 0 and 0 < col < 9:
                                                            upgrade_attack(index = "top_wall", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = server_module.count_5)
                                                        elif 0 < row < 9 and col == 9:
                                                            upgrade_attack(index = "right_wall", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = server_module.count_5)
                                                        
                                                        if count_7[0] > 0:
                                                            server_module.check_time[0] = 0
                                                            if shop.third_task.TEXT == shop.list_third_task[1]:
                                                                shop.single_ships.extend(count_ships)
                                                            if shop.fourth_task.TEXT == shop.list_fourth_task[0]:
                                                                if 1 in list_ships:
                                                                    shop.first_shot_is_kill(1)
                                                                else:
                                                                    shop.first_shot_is_kill(2)
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
                                                            achievement.single_ships_achiv.extend(list_ships)
                                                            achievement.list_hits_achiv.extend(list_ships)
                                                            server_module.check_bomb[0] = True
                                                            list_check_need_send[0] = "yes" 
                                                            server_module.turn[0] = "client_turn"
                                                        else:
    
                                                            if shop.third_task.TEXT == shop.list_third_task[1]:
                                                                shop.single_ships.extend(count_misses)
                                                            if shop.fourth_task.TEXT == shop.list_fourth_task[0]:
                                                                shop.first_shot_is_kill(0)
                                                            if shop.third_task.TEXT == shop.list_third_task[2]:
                                                                shop.check_three_2decker_ship_in_row.extend(count_misses)
                                                            if shop.first_task.TEXT == shop.list_first_task[-1]:
                                                                shop.three_hits_in_row(0)
                                                            if shop.third_task.TEXT == shop.list_third_task[-1]:
                                                                shop.count_three_ships.extend(count_misses)
                                                            if shop.second_task.TEXT == shop.list_second_task[2]:
                                                                shop.ship_hits.extend(count_misses)
                                                            if shop.fourth_task.TEXT == shop.list_fourth_task[1]:
                                                                shop.ship_hits_three.extend(count_misses)
                                                            if shop.first_task.TEXT == shop.list_first_task[0]:
                                                                shop.two_hits_in_row(number_cell = 5)
                                                            if shop.first_task.TEXT == shop.list_first_task[1]:
                                                                shop.four_hits_in_row(number_cell = 5)
                                                            if shop.fourth_task.TEXT == shop.list_fourth_task[-1]:
                                                                shop.eight_hits_in_row(number_cell = 5)
                                                            # ачивки
                                                            achievement.ten_shoot_in_row(5)
                                                            achievement.first_shot(0)
                                                            achievement.single_ships_achiv.extend(list_ships)
                                                            achievement.list_hits_achiv.extend(list_ships)
                                                            list_check_need_send[0] = "yes" 
                                                            server_module.turn[0] = "server_turn"
                                                            server_module.check_time[0] = 0
                                                        count_7[0] = 0
                                                        count_ships.clear()
                                                        count_misses.clear()
                                                    else:                                              
                                                        if shop.third_task.TEXT == shop.list_third_task[1]:
                                                            shop.single_ships.append(server_module.enemy_matrix[0][row ][col])
                                                        if shop.fourth_task.TEXT == shop.list_fourth_task[0]:
                                                            shop.first_shot_is_kill(cell = server_module.enemy_matrix[0][row][col])
                                
                                                        if shop.third_task.TEXT == shop.list_third_task[2]:
                                                            shop.check_three_2decker_ship_in_row.append(server_module.enemy_matrix[0][row ][col])
                                                            
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
                                                            flag_miss_rocket_animation[0] = "start_animation"
                                                            # передаем в список координаты клетки в которую ударили , чтобы в этой же клеточке мы и отрисовывали анимацию
                                                            x_hit_the_ship[0] = list_object_map_enemy[list_object_map_enemy.index(cell)].x
                                                            y_hit_the_ship[0] = list_object_map_enemy[list_object_map_enemy.index(cell)].y
                                                            server_module.enemy_matrix[0][row][col] = 5
                                                            # оскільки ці умови , якщо гравець це клієнт
                                                            # то коли гравець зробив постріл і схибив , записуємо флаг "yes", щоб відправити на сервер інформацію про те ,що треба змінити чергу 
                                                            list_check_need_send[0] = "yes"  # Готуємо дані для відправки
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
                                                        elif server_module.enemy_matrix[0][row][col] != 0 and server_module.enemy_matrix[0][row][col] != 5 and server_module.enemy_matrix[0][row][col]:
                                                            # передаем в список где хранится флаг нужно ли отрисовывать анимацию удара "start_animation" - то есть надо
                                                            check_animation_rocket[0] = "start_animation"
                                                            # передаем в список координаты клетки в которую ударили , чтобы в этой же клеточке мы и отрисовывали анимацию
                                                            x_hit_the_ship[0] = list_object_map_enemy[list_object_map_enemy.index(cell)].x
                                                            y_hit_the_ship[0] = list_object_map_enemy[list_object_map_enemy.index(cell)].y
                                                            # у матрицю ворога записуємо 7
                                                            server_module.enemy_matrix[0][row][col] = 7
                                                            # обнуляємо час ходу
                                                            server_module.check_time[0] = 0
                                                            # записуємо у лист який перевіряє чи потрібно відпарвляти дані на сервер флаг "yes", але чергу не змінюємо оскільки гравець попав по кораблю
                                                            list_check_need_send[0] = "yes"
                                                            server_module.turn[0] = "client_turn"     
                                                            if shop.first_task.TEXT == shop.list_first_task[0]:
                                                                shop.two_hits_in_row(number_cell = 7)
                                                            if shop.first_task.TEXT == shop.list_first_task[1]:
                                                                shop.four_hits_in_row(number_cell = 7)
                                                            if shop.fourth_task.TEXT == shop.list_fourth_task[-1]:
                                                                shop.eight_hits_in_row(number_cell = 7)  

                        # перевіряємо за яку роль грає гравець                    
                        elif server_module.list_player_role[0] == "server_player":
                            if server_module.turn[0] == "server_turn":
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

                                                    if shop.flagbimb200[0] =="yes" and numberofbim[0] not in shop.cheak: 
                                                        kord = Missile_200(row,col,server_module.enemy_matrix)
                                                        #если false flag  то бан клетка и если NOne значит нету корабликов 
                                                        if kord != "false" and kord != None :
                                                            if kord[0][0] != "True":
                                                                lenkord = len(kord)
                                                                for i in range(lenkord):
                                                                    # знаходим номер клетки 
                                                                    kletka= kord[i][0]*10 + kord[i][1]
                                                                    print (f"kletka",kletka)
                                                                    print (f"col row ",col,row,i )

                                                                    # cell_number_to_coordinates — новая функция, преобразующая номер клетки в координаты. Функция находится в screen.py, в create_grid.py.                         
                                                                    x_y = enemy_grid.cell_number_to_coordinates(kletka)
                                                                    print ("шиталово 0",x_y)
                                                                    check_animation_rocket[0] = "start_animation"  
                                                                    x_hit_the_ship[0] = x_y[0]
                                                                    y_hit_the_ship[0] = x_y[1]
                                                                    print (x_hit_the_ship[0],y_hit_the_ship[0])
                                                                    
                                                                    # у матрицю ворога записуємо 7
                                                                    server_module.enemy_matrix[0][kord[i][0]][kord[i][1]] = 7
                                                                    # обнуляємо час ходу
                                                                    server_module.check_time[0] = 0
                                                                    # записуємо у лист який перевіряє чи потрібно відпарвляти дані на сервер флаг "yes", але чергу не змінюємо оскільки гравець попав по кораблю
                                                                    server_module.turn[0] = "server_turn"      
                                                                    shop.flagbimb200[0] ="no"
                                                            else:
                                                                #знаходим номер клетки 
                                                                kletka= kord[0][1]*10 + kord[0][2]
                                                                print (f"kletka",kletka)
                                                                print (f"col row ",col,row,0 )
                                                                # cell_number_to_coordinates — новая функция, преобразующая номер клетки в координаты. Функция находится в screen.py, в create_grid.py.                         
                                                                x_y = enemy_grid.cell_number_to_coordinates(kletka)
                                                                print ("шиталово 0",x_y)
                                                                check_animation_rocket[0] = "start_animation"  
                                                                x_hit_the_ship[0] = x_y[0]
                                                                y_hit_the_ship[0] = x_y[1]
                                                            
                                                                # у матрицю ворога записуємо 7
                                                                server_module.enemy_matrix[0][kord[0][1]][kord[0][2]] = 5 
                                                                # обнуляємо час ходу
                                                                server_module.check_time[0] = 0
                                                                # записуємо у лист який перевіряє чи потрібно відпарвляти дані на сервер флаг "yes", але чергу не змінюємо оскільки гравець попав по кораблю
                                                                
                                                                list_check_need_send[0] = "yes"
                                                                server_module.turn[0] = "client_turn"      
                                                                #bimbcordlistx.append(x_y[0])
                                                                #bimbcordlisty.append(x_y[1])
                                                                shop.flagbimb200[0] ="no"
                                                    elif shop.check_buy_bomb_attack[0] == True:
                                                        print("BOMBASTIK")
                                                        shop.check_buy_bomb_attack[0] = False
                                                        server_module.flag_bomb_animation[0] = True
                                                        x_hit_the_ship[0] = list_object_map_enemy[list_object_map_enemy.index(cell)].x
                                                        y_hit_the_ship[0] = list_object_map_enemy[list_object_map_enemy.index(cell)].y
                                                        count_7 = [0]
                                                        
                                                        count_ships = []
                                                        count_misses = []
                                                        server_module.old_killed_ships[0] = len(server_module.enemy_died_ships[0])
                                                        if row == 0 and col == 0:
                                                            upgrade_attack(index = "top_left_corner", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = server_module.count_5)
                                                        elif 0 < row < 9 and 0 < col < 9:
                                                            upgrade_attack(index = "entry_cell", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = server_module.count_5)
                                                        elif 1 <= row < 9 and col == 0:
                                                            upgrade_attack(index = "left_wall", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = server_module.count_5)
                                                        elif row == 9 and col == 0:
                                                            upgrade_attack(index = "bot_left_corner", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = server_module.count_5)
                                                        elif row == 0 and col == 9:
                                                            upgrade_attack(index = "top_right_corner", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = server_module.count_5)          
                                                        elif row == 9 and col == 9:
                                                            upgrade_attack(index = "bot_right_corner", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = server_module.count_5)        
                                                        elif row == 9 and 0 < col < 9:
                                                            upgrade_attack(index = "bot_wall", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = server_module.count_5)
                                                        elif row == 0 and 0 < col < 9:
                                                            upgrade_attack(index = "top_wall", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = server_module.count_5)
                                                        elif 0 < row < 9 and col == 9:
                                                            upgrade_attack(index = "right_wall", col = col, row = row, count_7 = count_7, count_ships = count_ships, count_misses = count_misses, count_5 = server_module.count_5)
                                                        
                                                        if count_7[0] > 0:
                                                            server_module.check_bomb[0] = True
                                                            server_module.turn[0] = "server_turn"
                                                            server_module.check_time[0] = 0
                                                            if shop.third_task.TEXT == shop.list_third_task[1]:
                                                                shop.single_ships.extend(count_ships)
                                                            if shop.fourth_task.TEXT == shop.list_fourth_task[0]:
                                                                if 1 in list_ships:
                                                                    shop.first_shot_is_kill(1)
                                                                else:
                                                                    shop.first_shot_is_kill(2)
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
                                                            achievement.single_ships_achiv.extend(list_ships)
                                                            achievement.list_hits_achiv.extend(list_ships)
                                                        else:
                                                            server_module.turn[0] = "client_turn"
                                                            server_module.check_time[0] = 0
                                                            if shop.third_task.TEXT == shop.list_third_task[1]:
                                                                shop.single_ships.extend(count_misses)
                                                            if shop.fourth_task.TEXT == shop.list_fourth_task[0]:
                                                                shop.first_shot_is_kill(0)
                                                            if shop.third_task.TEXT == shop.list_third_task[2]:
                                                                shop.check_three_2decker_ship_in_row.extend(count_misses)
                                                            if shop.first_task.TEXT == shop.list_first_task[-1]:
                                                                shop.three_hits_in_row(0)
                                                            if shop.third_task.TEXT == shop.list_third_task[-1]:
                                                                shop.count_three_ships.extend(count_misses)
                                                            if shop.second_task.TEXT == shop.list_second_task[2]:
                                                                shop.ship_hits.extend(count_misses)
                                                            if shop.fourth_task.TEXT == shop.list_fourth_task[1]:
                                                                shop.ship_hits_three.extend(count_misses)
                                                            if shop.first_task.TEXT == shop.list_first_task[0]:
                                                                shop.two_hits_in_row(number_cell = 5)
                                                            if shop.first_task.TEXT == shop.list_first_task[1]:
                                                                shop.four_hits_in_row(number_cell = 5)
                                                            if shop.fourth_task.TEXT == shop.list_fourth_task[-1]:
                                                                shop.eight_hits_in_row(number_cell = 5)
                                                            # ачивки
                                                            achievement.ten_shoot_in_row(5)
                                                            achievement.first_shot(0)
                                                            achievement.single_ships_achiv.extend(list_ships)
                                                            achievement.list_hits_achiv.extend(list_ships)
                                                        count_7[0] = 0
                                                        count_ships.clear()
                                                        count_misses.clear()
                                                    else:
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
                                                            # оскільки гравець не потрапив по кораблю , то змінюємо чергу ходу
                                                            server_module.turn[0] = "client_turn"
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
                                                            if shop.first_task.TEXT == shop.list_first_task[0]:
                                                                shop.two_hits_in_row(number_cell = 7)
                                                            if shop.first_task.TEXT == shop.list_first_task[1]:
                                                                shop.four_hits_in_row(number_cell = 7)
                                                            if shop.fourth_task.TEXT == shop.list_fourth_task[-1]:
                                                                shop.eight_hits_in_row(number_cell = 7)


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
                # якщо вже їтось виграв , то робимо ефект затемнення
                apply_fade_effect(screen = module_screen.main_screen)
                # зупиняємо цикл гри
                run_game = False
                # змінюємо фрейм бою , на фрейм показу результатів
                change_scene(scene =game_windows.finish_window())
                check_press_button[0] = None

        if screen_shake[0] > 1:
            screen_shake[0] -= 1

        # if row_list[0] != 100:
        #         row_list[0] = 100
        #         col_list[0] = 100
        #         number_list[0] = 100
   

        # відмальовуємо екран із координатами що збергаються у списку render_offset , щоб якщо гравець потрапив по карблю , то був ефект трясіння
        module_screen.main_screen.blit(pygame.transform.scale(module_screen.main_screen, (1280 , 832)), render_offset)
        # оновлюємо екран
        pygame.display.flip()