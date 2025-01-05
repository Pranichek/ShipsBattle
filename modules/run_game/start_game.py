#імпортуємо усі потрібні модулі
import pygame , random
import modules.shop as shop
import modules.achievement as achievement
import modules.screens.screen as module_screen_server
from ..classes.achive_window import strategist_achievement , list_achieves
from ..screens import main_screen , list_object_map , grid_player , list_grid , enemy_grid , list_object_map_enemy
from ..classes import DrawImage , Button , Font  , list_ships 
from ..classes.animation import rocket_animation , animation_boom , Animation
from ..classes.class_input_text import input_ip_adress ,input_nick ,input_port
from ..classes.class_music import music_load_main , music_load_waiting , fight_music
from ..classes.class_click import music_click
from ..json_functions import read_json , write_json , list_users
from .launch_server import start_server , fail_start_server , check_server_started
from .clinent_connect import connect_to_server , list_check_connection , fail_connect
from .random_placing import random_places_ships
from ..server import enemy_died_ships , list_check_ready_to_fight , dict_save_information , check_time , turn , list_player_role , enemy_matrix , list_check_win , list_check_win , our_miss_anim , enemy_balance , save_medals_coordinates
from ..client import list_check_need_send 
from ..game_tools import ship_border , enemy_balance_in_jar , player_balance_in_jar , add_money

#ініціалізуємо pygame щоб можна було із ним працювати
pygame.init()


#список для проверки нажата ли кнопка
check_press_button = [None]
#список для відслужування чи нажата кнопка підключення до серверу чи ні
check_client_connected = [False]
#ліст для зберігання яке зараз вікно активне
list_current_scene = [None]
#список для того щоб головна музика починала грати лише один раз і не приривалася
once_play_music = [0]
# список для трясіння екрану
screen_shake = [0]



#fonts(text)
createbutton_font = Font(size= 48 , name_font= "Jersey15.ttf" , text= "create" , screen= main_screen , x_cor = 218, y_cor= 663 , text_color = "White") 
join_game_fonts = Font(size= 48 , name_font= "Jersey15.ttf" , text= "join" , screen= main_screen , x_cor = 974 , y_cor= 663, text_color = "White")
#Текст с никами игроков
player_nick = Font(size = 48 , name_font= "Jersey15.ttf" , text = dict_save_information["player_nick"] , screen = main_screen , x_cor = 914 , y_cor = 126, text_color = "White")
enemy_nick = Font(size = 48 , name_font= "Jersey15.ttf" , text = dict_save_information["enemy_nick"] , screen = main_screen , x_cor = 437 , y_cor = 126, text_color = "White")
player_points = Font(size = 48 , name_font= "Jersey15.ttf" , text = str(dict_save_information["player_points"]) , screen = main_screen , x_cor = 743 , y_cor = 126, text_color = "White")
enemy_points = Font(size = 48 , name_font= "Jersey15.ttf" , text = str(dict_save_information["enemy_points"]) , screen = main_screen , x_cor = 270 , y_cor = 126, text_color = "White")
# Текста для фрейму де показують переміг ти чи програв№
win_lose_text = Font(size = 96 , name_font= "Goldman_Bold.ttf" , text = "" , screen = main_screen , x_cor = 383 , y_cor = 248, text_color = "White")

def test():
    print(1)
    
def button_action():
    check_press_button[0] = "button is pressed"
    music_click.play2(0)
    # apply_fade_effect(screen = main_screen)


#функція для перезаписування яке зараз вікно активне
def change_scene(scene):
    list_current_scene[0] = scene
    # apply_fade_effect(screen = main_screen)

def music_up():
    get = pygame.mixer.music.get_volume()
    print(get)
    pygame.mixer.music.set_volume(get + 0.1)

def music_lower():
    get2 = pygame.mixer.music.get_volume()
    print(get2)
    pygame.mixer.music.set_volume(get2 - 0.1)
    if get2 - 0.1 < 0.01:
        pygame.mixer.music.set_volume(0)

# функция для подключения к бою
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
    
def apply_fade_effect(screen, fade_speed=3, max_fade_alpha=76):
    #fade_speed=3 -скорочть затемнения 
    #max_fade_alpha=76 -максимальное затемнение  до 255
    # Создаём полупрозрачную поверхность для затемнения
    overlay = pygame.Surface(screen.get_size())
    overlay.fill((0, 0, 0))  # Черный цвет
    overlay.set_alpha(0)  # Начальная прозрачность (0 - полностью прозрачный)

    # Постепенное увеличение альфа-канала для эффекта затемнения
    while overlay.get_alpha() < max_fade_alpha:
        # Увеличиваем альфа-канал с каждой итерацией
        overlay.set_alpha(min(overlay.get_alpha() + fade_speed, max_fade_alpha))

        # Отображаем затемнение
        screen.blit(overlay, (0, 0))
        pygame.display.flip()
        pygame.time.Clock().tick(60)
    

list_check_shop = [None]
def show_shop():
    if shop.shop_item[0].TURN == "Down": 
        list_check_shop[0] = True


flag_upgrade = [False]
def upgrade_flag():
    flag_upgrade[0] = True




#buttons
#кнопка кторая перекидывает на фрейм по созданию игры(запуска сервера)
create_game_frame = Button(x= 113, y = 653,image_path= "button_create.png" , image_hover_path= "create_button_hover.png" , width= 346 , height = 80 , action = button_action)
#кнопка кторая перекидывает на фрейм по присоеденению к игре(серверу)
join_game_frame = Button(x= 832 , y = 653,image_path= "join_button.png" , image_hover_path= "join_button_hover.png" , width= 346 , height = 80 , action = button_action)
#кнопка которая возвращает назад к главному окну
back_to_menu = Button(x= 33 , y = 41 ,image_path= "back_button.png" , image_hover_path= "back_button_hover.png" , width= 158 , height = 41 , action = button_action)
#кнопка которая запускает сервер(игру)
start_game_button = Button(x= 352 , y = 642,image_path= "create_game_button.png" , image_hover_path= "create_game_button_hover.png" , width = 575 , height = 80 , action= start_server)
#кнопка которая подключается к игре
join_game_button = Button(x= 352 , y = 642,image_path= "join_to_game.png" , image_hover_path= "joint_to_game_hover.png" , width= 575 , height = 80 , action = connect_to_server)
#кнопка коли розставив кораблі та підлючаєшься до бою
ready_for_battle = Button(x= 798 , y = 626,image_path= "start_battle.png" , image_hover_path= "start_battle_hover.png" , width= 408 , height = 61 , action = connect_to_fight)
#кнопка яка будеть розставляти кораблі у ранломному положені
random_place_ships = Button(x= 205 , y = 709,image_path= "random_place.png" , image_hover_path= "random_place_hover.png" , width= 318 , height = 48 , action = random_places_ships)
# кнопка для добавления звука
button_upp = Button(x=53 ,y=44 , image_path="button_music_upp.png", image_hover_path="button_volue_up_hover.png", width = 74, height = 71, action = music_up)
button_lower = Button(x=53,y=136, image_path="button_music_lower.png", image_hover_path="button_music_lower_hover.png", width = 74, height= 71, action = music_lower)
#кнопка возвращения на сервер
back_to_server = Button(x= 39 , y = 56 ,image_path= "back_button.png" , image_hover_path= "back_button_hover.png" , width = 158 , height = 41 , action= button_action)
# Restart game
restart_game = Button(x = 437, y = 713,image_path= "restart_game.png" , image_hover_path= "restart_game_hover.png" , width = 408, height = 61 , action= test)
# кнопка котороя показывает магазинчик и задания
shop_and_tasks = Button(x= 33 , y = 32,image_path= "show_shop.png" , image_hover_path= "show_shop_hover.png" , width = 36, height = 31 , action= show_shop)
# 
upgrade_button = Button(x = 100, y = 100, image_path= "restart_game.png", image_hover_path= "restart_game_hover.png", width= 106, height= 50, action = upgrade_flag)



#images decoration
cold_image = DrawImage(width= 152 , height= 68 , x_cor= 207 , y_cor= 716 , folder_name= "decorations" , image_name= "ice.png")
second_cold_image = DrawImage(width= 152 , height= 68 , x_cor= 940, y_cor= 716 , folder_name= "decorations" , image_name= "ice.png")
third_cold_image = DrawImage(width=  150, height= 68 , x_cor= 536 , y_cor= 705 , folder_name= "decorations" , image_name= "ice.png")
fourth_cold_image = DrawImage(width= 150, height= 68 , x_cor= 686 , y_cor= 705 , folder_name= "decorations" , image_name= "ice.png")
#image for the grid
grid_image = DrawImage(width = 662  , height = 662 , x_cor = 40 , y_cor = 37 , folder_name = "grid", image_name = "background_grid.png")
grid_image_for_enemy = DrawImage(width = 596  , height = 597 , x_cor = 23 , y_cor = 211 , folder_name = "grid", image_name = "background_grid.png")
# image for window where players are fighting against each other
fight_bg = DrawImage(width = 1280,height = 832 , x_cor = 0 , y_cor = 0 , folder_name= "backgrounds" , image_name= "fight_background.png")
# Зображення для декаративної рамки для ніку та очок на фремі бою
frame_nick_player = DrawImage(width = 362 ,height = 69 , x_cor = 222 , y_cor = 116 , folder_name= "backgrounds" , image_name= "frame_nick.png")
second_frame_nick_player = DrawImage(width = 362 ,height = 69 , x_cor = 699 , y_cor = 116 , folder_name= "backgrounds" , image_name= "frame_nick.png")
# Зображення аватрів гравців
player_face = DrawImage(width = 154 , height = 123 ,x_cor = 1104 , y_cor = 79 , folder_name = "decorations" , image_name = "active_player.png")
enemy_face = DrawImage(width = 154 , height = 123  ,x_cor = 20 , y_cor = 79 , folder_name = "decorations" , image_name = "not_active_enemy.png")
# Зображення яке показує скуільки залишилось часу
clock_image = DrawImage(width = 206 , height = 57 , x_cor = 544 , y_cor = 20 , folder_name = "animation_clock" , image_name = "0.png")
# Зображення для фрейми де показують виграв чи програв користувач
win_background = DrawImage(width = 315 , height = 199 , x_cor = 97 , y_cor = 416 , folder_name = "backgrounds" , image_name = "result_game_bg.png")
defeat_background = DrawImage(width = 315 , height = 199 , x_cor = 860 , y_cor = 416 , folder_name = "backgrounds" , image_name = "result_game_bg.png")
end_game_image  = DrawImage(width = 606 , height = 131 , x_cor = 337 , y_cor = 80 , folder_name = "decorations" , image_name = "end_game.png")
# картинка для того что бы под текстом кто выиграл проиграл была тень
shadow_text = DrawImage(width = 816 , height = 150 , x_cor = 233 , y_cor = 255 , folder_name = "decorations" , image_name = "shadow_text.png")
new_year_cap = DrawImage(width = 133 , height = 133 , x_cor = 331 , y_cor = 80 , folder_name = "decorations" , image_name = "new_year_cap.png")
# картинка для выделения монеток , достижения , и оружия игрока(серый фон)
shadow_data_user = DrawImage(x_cor = -28 , y_cor = -95 , width = 1351 , height = 236 , folder_name = "decorations" , image_name = "shadow_user_data.png")
# картинки баночек с балансом игроков
player_jar = DrawImage(x_cor = 1190 , y_cor = 18 , width = 90 , height = 76 , folder_name = "decorations" , image_name = "jar_balance.png")
enemy_jar = DrawImage(x_cor = 102 , y_cor = 18 , width = 90 , height = 76 , folder_name = "decorations" , image_name = "jar_balance.png")
# место где будет отображаться какое спец оружие купил пользователь
user_weapon = DrawImage(x_cor = 1046 , y_cor = -26 , width = 260 , height = 135 , folder_name = "backgrounds" , image_name = "user_weapon.png")
# enemy_medals 
four_decker_enemy_medal = DrawImage(x_cor = 221 , y_cor = -50 , width = 50 , height = 50 , folder_name = "achievement" , image_name = "medal_four_decker.png")
auto_sight_medal = DrawImage(x_cor = 424 , y_cor = -50 , width = 50 , height = 50 , folder_name = "achievement" , image_name = "auto_sight_medal.png")
destroying_medal = DrawImage(x_cor = 415 , y_cor = -50 , width = 50 , height = 50 , folder_name = "achievement" , image_name = "destroying_medal.png")
first_hit_enemy_medal = DrawImage(x_cor = 272 , y_cor = -50 , width = 50 , height = 50 , folder_name = "achievement" , image_name = "first_hit_medal.png")
lone_hunter_enemy_medal = DrawImage(x_cor = 311 , y_cor = -50 , width = 50 , height = 50 , folder_name = "achievement" , image_name = "lone_hunter_medal.png")
master_of_disguise_enemy_medal = DrawImage(x_cor = 341 , y_cor = -50 , width = 50 , height = 50 , folder_name = "achievement", image_name = "master_of_disguist_medal.png")
enemy_prefect_shooter_medal = DrawImage(x_cor = 360 , y_cor = -50 , width = 50 , height = 50 , folder_name = "achievement" , image_name = "perfect_shooter_medal.png")
pioneer_enemy_medal = DrawImage(x_cor = 472 , y_cor = -50 , width = 100 , height = 50 , folder_name = "achievement" , image_name = "pioneer_medal.png")
strategist_enemy_medal = DrawImage(x_cor = 267 , y_cor = -50 , width = 50 , height = 50 , folder_name = "achievement" , image_name = "strategist_medal.png")
openin_the_batte_enemy_medal = DrawImage(x_cor = 368 , y_cor = -80 , width = 50 , height = 75 , folder_name = "achievement" , image_name = "medal_opening_the_battle.png")

#backgrounds
main_bg = DrawImage(width = 1280,height = 832 , x_cor = 0 , y_cor = 0 ,folder_name= "backgrounds" , image_name= "main_background.png")
#фон для окон д=где вводим данные для запуска сервера и подключение к нему
input_data_bg= DrawImage(width = 1280,height = 832 , x_cor = 0 , y_cor = 0 ,folder_name= "backgrounds" , image_name= "input_data.png")
#фон для очікування користувача
waiting_background = DrawImage(width = 1280,height = 832 , x_cor= 0 , y_cor = 0 ,folder_name= "backgrounds" , image_name= "waiting_background.png")
#фон для розташування кораблів перед ігрою
ships_position_bg = DrawImage(width = 1280,height = 832 , x_cor = 0 , y_cor=  0 ,folder_name= "backgrounds" , image_name= "position_ships_bg.png")
# фон на якомй стоять кораблі перед початком бою
place_for_ships = DrawImage(width = 477 , height = 559 , x_cor = 763 , y_cor = 37 ,folder_name= "backgrounds" , image_name= "bg_place_for_ships.png")
# Фон який показує що користувач може зараз ходити
can_attack = DrawImage(width = 191 , height = 53 , x_cor = 820 , y_cor = 118 , folder_name = "backgrounds" , image_name = "active_player.png")
# Фон який вказує що користувач зараз не може ходити
can_not_attack = DrawImage(width = 191 , height = 53 , x_cor = 311 , y_cor = 118 , folder_name = "backgrounds" , image_name = "not_active.png")
# Finish background
finish_bg = DrawImage(width = 1280 , height = 832 , x_cor = 0 , y_cor = 0 , folder_name = "backgrounds" , image_name = "win_game_bg.png")

#створюємо функцію, яка викликається при запуску гри для користувача який запускає сервер
def main_window():
    list_check_ready_to_fight[0] = None
    #викликаємо функцію для запуску серверу
    #встановлюємо назву вікна гри для сервера
    pygame.display.set_caption("BattleShips")
    #створюжмо змінну для того щоб відстежувати коли треба закривати вікно
    run_game = True
    if once_play_music[0] < 1:
        music_load_main.play()

    once_play_music[0] += 1

    while run_game:
        module_screen_server.FPS.tick(120)
        mouse_x , mouse_y = pygame.mouse.get_pos()
        main_bg.draw_image(screen= main_screen)

        cold_image.draw_image(screen= main_screen)  
        create_game_frame.draw(surface= main_screen)
        button_upp.draw(surface= main_screen)
        button_lower.draw(surface= main_screen)
        
        second_cold_image.draw_image(screen= main_screen)
        join_game_frame.draw(surface= main_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False  
                change_scene(None)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                create_game_frame.check_click(event = event)
                join_game_frame.check_click(event = event)
                button_upp.check_click(event = event)
                button_lower.check_click(event = event)

 
            elif check_press_button[0] == "button is pressed":
                x_pos , y_pos = pygame.mouse.get_pos()
                check_press_button[0] = None 
                run_game = False
                if x_pos >= join_game_frame.x:
                    if x_pos <= join_game_frame.x + join_game_frame.width:
                        if y_pos >= join_game_frame.y:
                            if y_pos <= join_game_frame.y + join_game_frame.height:
                                print("Join windo")
                                change_scene(join_game_window())
                elif x_pos >= create_game_frame.x:
                    if x_pos <= create_game_frame.x + create_game_frame.width:
                        if y_pos >= create_game_frame.y:
                            if y_pos <= create_game_frame.y + create_game_frame.height:
                                print("Create window")
                                change_scene(create_game_window())
        pygame.display.flip()



def create_game_window():
    #викликаємо функцію для запуску серверу
    #встановлюємо назву вікна гри для сервера
    pygame.display.set_caption("Create Game Window")
    #створюжмо змінну для того щоб відстежувати коли треба закривати вікно
    run_game = True
    #основний цикл роботи вікна користувача
    while run_game:
        module_screen_server.FPS.tick(120)
        input_data_bg.draw_image(screen= main_screen)
        data = read_json(name_file = "utility.json")
        status_server = data["status"]

        input_nick.draw_text()
        input_ip_adress.draw_text()
        input_port.draw_text()

        back_to_menu.draw(surface= main_screen)

        third_cold_image.draw_image(screen= main_screen)
        fourth_cold_image.draw_image(screen= main_screen)
        start_game_button.draw(surface= main_screen)

        #если попытались создать сервер кторый нельзя(например неправильны айпи) , то выводим предуприждение об этом
        if check_server_started[0] == "error_server":
            fail_start_server.draw_image(screen = main_screen)
            fail_start_server.check_touch()
            #когда игрок закрыл табличку записываем True в список , чтобы знали что уже пытались запустить сервер
            if fail_start_server.visible == False:
                check_server_started[0] = True

        #если запустили сервер но к нему еще никто не подлючился перекидываем на окно ожидания игрока
        if status_server == "wait":
            check_press_button[0] = None 
            run_game = False
            apply_fade_effect(screen = main_screen)
            change_scene(waiting_window())
        #Обробляємо всі події у вікні
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False  
                list_current_scene[0] = None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                back_to_menu.check_click(event = event)
                start_game_button.check_click(event = event)
            elif check_press_button[0] == "button is pressed":
                check_press_button[0] = None
                run_game = False
                input_nick.user_text = input_nick.base_text
                input_ip_adress.user_text = input_ip_adress.base_text
                input_port.user_text = input_port.base_text
                change_scene(main_window())
        
                
            input_nick.check_event(event)
            input_ip_adress.check_event(event)
            input_port.check_event(event)  

        #оновлюєио екран щоб можна було бачити зміни на ньому
        pygame.display.flip()



def join_game_window():
    #викликаємо функцію для запуску серверу
    #встановлюємо назву вікна гри для сервера
    pygame.display.set_caption("Join to Game Window")
    #створюжмо змінну для того щоб відстежувати коли треба закривати вікно
    run_game = True
    #основний цикл роботи вікна користувача
    while run_game:
        module_screen_server.FPS.tick(120)
        try:
            data = read_json(name_file = "utility.json")
            status_server = data["status"]
        except:
            status_server = "wait"
            continue
        input_data_bg.draw_image(screen= main_screen)

        input_nick.draw_text()
        input_ip_adress.draw_text()
        input_port.draw_text()

        back_to_menu.draw(surface= main_screen)

        third_cold_image.draw_image(screen= main_screen)
        fourth_cold_image.draw_image(screen= main_screen)
        join_game_button.draw(surface= main_screen)

        #если не нашли сервер по которому подключаемся или ввели что то неправильно, выводим табличку о том что таокго сервера нет
        #этот список находится в файле connect_to_server.check_after_randomy
        if list_check_connection[0] == "error_connection":
            # рисуем табличку ошибки
            fail_connect.draw_image(screen = main_screen)
            # вызываем метод этой таблички который позволяет отслеживать наведен ли курсор на нее или нет
            # если он находится на картинке то она пропадет
            fail_connect.check_touch()
            if fail_connect.visible == False:
                list_check_connection[0] = True

        if status_server == "connect":
            apply_fade_effect(screen = main_screen)
            change_scene(ships_position_window())
            check_press_button[0] = None
            run_game = False
        #Обробляємо всі події у вікні
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False  
                change_scene(None)
            elif check_press_button[0] == "button is pressed":
                check_press_button[0] = None
                input_nick.user_text =  input_nick.base_text
                input_ip_adress.user_text = input_ip_adress.base_text
                input_port.user_text = input_port.base_text
                run_game = False
                change_scene(main_window())
            elif event.type == pygame.MOUSEBUTTONDOWN:
                back_to_menu.check_click(event= event)
                join_game_button.check_click(event= event)


            input_nick.check_event(event)
            input_ip_adress.check_event(event)
            input_port.check_event(event)  


        #оновлюємо екран щоб можна було бачити зміни на ньому
        pygame.display.flip()


def waiting_window():
    print("Зашло")
    pygame.display.set_caption("Waiting window")
    run_game = True
    music_load_main.stop()
    music_load_waiting.play()
    while run_game:
        try:
            data = read_json(name_file = "utility.json")
            status_server = data["status"]
        except Exception as e:
            status_server = "wait"
            continue
        # module_screen_server.FPS.tick(60)

        if list_check_ready_to_fight[0] == "fight":
            apply_fade_effect(screen = main_screen)
            check_press_button[0] = None
            run_game = False
            change_scene(fight_window())
            

        waiting_background.draw_image(screen = main_screen)

        if list_check_ready_to_fight[0] == None:
            if status_server == "connect":
                check_press_button[0] = None
                run_game = False
                apply_fade_effect(screen = main_screen)
                change_scene(ships_position_window())
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False  
                change_scene(None)
                 
        pygame.display.flip()

  

def ships_position_window():
    music_load_waiting.stop()
    music_load_main.play()
    pygame.display.set_caption("Position Ships")
    run_game = True
    
    #generate grid with class
    grid_player.generate_grid()

    while run_game:
        # module_screen_server.FPS.tick(60)
        if list_check_ready_to_fight[0] == "fight":
            apply_fade_effect(screen = main_screen)
            run_game = False
            change_scene(None)
            change_scene(fight_window())
            check_press_button[0] = None
            
        elif list_check_ready_to_fight[0] == "wait":
            apply_fade_effect(screen = main_screen)
            run_game = False
            change_scene(None)
            change_scene(scene = waiting_window())
            check_press_button[0] = None
            
        
        ships_position_bg.draw_image(screen = main_screen)

        # прямокутник де стоять коряблі перед початком бою
        place_for_ships.draw_image(screen = main_screen)

        #отрисовка картинки цифер и букв для поля
        grid_image.draw_image(screen = main_screen)
        #отрисовка обьектов(пустых клеток) который хранятся в списке обьектов
        for object in list_object_map:
            object.draw(screen = main_screen) 

        for ship in list_ships:
            ship.draw_sheep(screen = main_screen)
        
        #draw buttons
        ready_for_battle.draw(surface= main_screen)
        random_place_ships.draw(surface= main_screen)

        for event in pygame.event.get():
            for ship in list_ships:
                ship.matrix_move(event = event, matrix_width = 620, matrix_height = 620, cell = 100)
                ship.rotate_ship(event = event)

            if event.type == pygame.QUIT:
                run_game = False  
                change_scene(None)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ready_for_battle.check_click(event = event)
                random_place_ships.check_click(event = event)
                
        pygame.display.flip()


# списки в которых хранятся координаты крестиков , если враг попал по кораблю игрока
x_enemy_cross = [0]
y_enemy_cross = [0]

# флаг который првоеряет надо ли запускать анимацию ракеты если игрок ударил
check_animation_rocket = [""]
# флаг когда надо проигрывать анимацию крестика если попали по кораблю
check_cross_animation  = [""]

# список где хранятся крестики которые отрисовываются в том случаи если игрок попал ко кораблю
list_cross = []

# спсики в которых хранятся координаты где должны отрисовываться анимации если игрок ударил по полю
x_hit_the_ship = [0]
y_hit_the_ship = [0]


# спсиок где хранятся крестки которые ресуюются если враг попал по кораблю игрока
list_cross_player = []

check_achiv = [False]
index_achiv = [100]

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
        for medal in range(0 , len(save_medals_coordinates)):
            if save_medals_coordinates[medal][0] == 1:
                four_decker_enemy_medal.y_cor = save_medals_coordinates[medal][2]
            elif save_medals_coordinates[medal][0] == 2:
                enemy_prefect_shooter_medal.y_cor = save_medals_coordinates[medal][2]
            elif save_medals_coordinates[medal][0] == 3:
                strategist_enemy_medal.y_cor = save_medals_coordinates[medal][2]
            elif save_medals_coordinates[medal][0] == 4:
                first_hit_enemy_medal.y_cor = save_medals_coordinates[medal][2]
            elif save_medals_coordinates[medal][0] == 6:
                master_of_disguise_enemy_medal.y_cor = save_medals_coordinates[medal][2]
            elif save_medals_coordinates[medal][0] == 7:
                lone_hunter_enemy_medal.y_cor = save_medals_coordinates[medal][2]
            elif save_medals_coordinates[medal][0] == 8:
                pioneer_enemy_medal.y_cor = save_medals_coordinates[medal][2]
            elif save_medals_coordinates[medal][0] == 10:
                openin_the_batte_enemy_medal.y_cor = save_medals_coordinates[medal][2]

        # ставимо фпс на значення 60
        module_screen_server.FPS.tick(120)
        # функция которая красиво добавляет монетки
        add_money()

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
        if list_player_role[0] == "server_player" and turn[0] == "server_turn":
            player_face.image_name = "active_player.png"
            enemy_face.image_name = "not_active_enemy.png"
            player_face.load_image()
            enemy_face.load_image()
        elif list_player_role[0] == "player_client" and turn[0] == "client_turn":
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
        fight_bg.draw_image(screen = main_screen)

        # отрисовка всех элементов для визуального отображения монеток , медалек , и оружия
        shadow_data_user.draw_image(screen = main_screen)

        user_weapon.draw_image(screen = main_screen)

        player_jar.draw_image(screen = main_screen)
        enemy_jar.draw_image(screen = main_screen)

        player_balance_in_jar.draw_font()
        enemy_balance_in_jar.text = str(enemy_balance[0])
        enemy_balance_in_jar.update_text()
        enemy_balance_in_jar.draw_font()


        # завантажуємо , та відмальовуємо зображення годинників(скільки часу пройшло)
        clock_image.image_name = f'{check_time[0]}.png'
        clock_image.load_image()
        clock_image.draw_image(screen = main_screen)

        # відмальовуємо рамки де будуть находитися ніки гравців
        frame_nick_player.draw_image(screen = main_screen)
        second_frame_nick_player.draw_image(screen = main_screen)

        # відмальовуємо зображення які вказують чиї зараз ход
        player_face.draw_image(screen = main_screen)
        enemy_face.draw_image(screen = main_screen)

        # выполнить первые три задания
        if shop.fourth_task.TEXT == shop.list_fourth_task[2]:
            shop.complete_three_tasks()


        
        # оновлюємо дані про ник та очки , та відмольовуємо їх
        player_nick.text = dict_save_information["player_nick"]
        enemy_nick.text = dict_save_information["enemy_nick"]
        player_points.text = str(dict_save_information["player_points"])
        enemy_points.text = str(dict_save_information["enemy_points"])
        player_nick.update_text()
        enemy_nick.update_text()
        player_points.update_text()
        enemy_points.update_text()
        player_nick.draw_font()
        enemy_nick.draw_font()
        player_points.draw_font()
        enemy_points.draw_font()

        # відмальовуємо зображення сітки , по якій можемо ореєнтуватися куди бити(тобто A1 , B9 � тд)
        grid_image.draw_image(screen = main_screen)
        grid_image_for_enemy.draw_image(screen = main_screen)

        # малюємо клітинки сітки(просто пусті клітини) гравців
        for cell in list_object_map:
            cell.draw(screen=main_screen)
        for empty_cell in list_object_map_enemy:
            empty_cell.draw(screen=main_screen)

        # відмалбовуємо кораблі які ми роставляли , але у змнешаному вигялді , та у іншому місці(сітці яка також зменшилась у розмірі)
        for num , ship  in enumerate(list_ships):
            list_ships[num].draw_sheep(screen = main_screen)

        for cross_animation in list_cross_player:
            cross_animation.animation(main_screen = main_screen , count_image = 13)

        # кнопка для открытия магазина
        shop_and_tasks.draw(surface = main_screen)
        #----------------------------------------------------------------
        # анимация зачеркивания клеточек вокруг убитого корабля
        ship_border()
        # #----------------------------------------------------------------

        # отрисовка зачеркнутых клеточек , если игрок убил полностью корабль врага
        for anim_miss in our_miss_anim:
            anim_miss.animation(main_screen=main_screen, count_image=29)

        # #****************************************************************
        # отрисовка крестиков если игрок попал по кораблю
        if check_cross_animation[0] == "starts_cross_animation":
            for cross in list_cross:
                # print(len(list_cross))
                cross.animation(main_screen = main_screen , count_image = 13)


        if check_animation_rocket[0] == "start_animation":
            rocket_animation.X_COR = x_hit_the_ship[0] - 231
            rocket_animation.Y_COR = y_hit_the_ship[0] - 23
            # проверка на окончание анимация полета ракеті 
            if rocket_animation.animation(main_screen = main_screen , count_image = 7):
                animation_boom.X_COR = x_hit_the_ship[0] - 23
                animation_boom.Y_COR = y_hit_the_ship[0] - 23
                screen_shake[0] = 31
                if animation_boom.animation(main_screen = main_screen , count_image = 7):
                    cross_animation = Animation(
                        image_name = "0.png" , 
                        width = 55 , 
                        height = 55 , 
                        x_cor = x_hit_the_ship[0], 
                        y_cor = y_hit_the_ship[0], 
                        need_clear = False , 
                        name_folder = "animation_cross"
                    )
                    list_cross.append(cross_animation)
                    rocket_animation.clear_animation()
                    animation_boom.clear_animation()
                    print("--------------------------------")
                    check_animation_rocket[0] = ""
                    check_cross_animation[0] = "starts_cross_animation"
        #----------------------------------------------------------------




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
                        name_folder = "animation_cross"
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

        #enemy_medals
        four_decker_enemy_medal.draw_image(screen = main_screen)
        enemy_prefect_shooter_medal.draw_image(screen = main_screen)
        first_hit_enemy_medal.draw_image(screen = main_screen)
        strategist_enemy_medal.draw_image(screen = main_screen)
        master_of_disguise_enemy_medal.draw_image(screen = main_screen)
        pioneer_enemy_medal.draw_image(screen = main_screen)
        lone_hunter_enemy_medal.draw_image(screen = main_screen)
        openin_the_batte_enemy_medal.draw_image(screen = main_screen)

        # отрисовка наших медалей игрока
        achievement.medal_four_decker.draw_image(screen = main_screen)
        achievement.medal_ten_shoot_in_row.draw_image(screen = main_screen)
        achievement.medal_hit_shoot.draw_image(screen = main_screen)
        achievement.strategist_medal.draw_image(screen = main_screen)
        achievement.medal_secrecy_ships.draw_image(screen = main_screen)
        achievement.medal_lone_hunter.draw_image(screen = main_screen)
        #piooner
        achievement.medal_fisr_kill_any_ship.draw_image(screen = main_screen)
        achievement.medal_opening_battle.draw_image(screen = main_screen)

        # відмаловуємо усі елементи які знаходяться у магазині 
        for item in shop.shop_item:
            item.draw(screen = main_screen)
            item.move()

        #----------------------------------------------------------------
        # конструкция которая показывает окошки с выполнеными ачивками по очереди , а не одновременно
        for achiv in list_achieves:
            if achiv.ACTIVE == True and check_achiv[0] == False:
                index_achiv[0] = list_achieves.index(achiv)
                check_achiv[0] = True
        if index_achiv[0] != 100:
            list_achieves[index_achiv[0]].draw(screen = main_screen)
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
            shop.kill_three_ships_in_a_row(cell = enemy_matrix[0][row][col])

        if shop.third_task.TEXT == shop.list_third_task[-2]:
            shop.count_three_ships.append(enemy_matrix[0][row][col])

        if shop.third_task.TEXT == shop.list_third_task[2]:
            shop.kill_three_double_decker_in_a_row(cell = enemy_matrix[0][row][col])

        if shop.third_task.TEXT == shop.list_third_task[1]:
            shop.kill_four_single_ships_in_a_row(cell = enemy_matrix[0][row ][col]) 
        
        
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

                if shop.shop_item[0].TURN != "Up":
                    # нижче умови для атаки 
                    # перевіряємо за яку роль грає гравець
                    if list_player_role[0] == "player_client":
                        if turn[0] == "client_turn":
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
                                                
                                                if shop.third_task.TEXT == shop.list_third_task[1]:
                                                    shop.single_ships.append(enemy_matrix[0][row ][col])
                                                if shop.fourth_task.TEXT == shop.list_fourth_task[0]:
                                                    shop.first_shot_is_kill(cell = enemy_matrix[0][row][col])
                                                if shop.third_task.TEXT == shop.list_third_task[-1]:
                                                    shop.kill_two_three_decker_in_a_row(cell = enemy_matrix[0][row][col])
                                                if shop.third_task.TEXT == shop.list_third_task[2]:
                                                    shop.count_two_3decker_ship.append(enemy_matrix[0][row ][col])
                                                    shop.kill_three_double_decker_in_a_row(cell = enemy_matrix[0][row][col])
                                                if shop.third_task.TEXT == shop.list_third_task[-2]:
                                                    shop.count_three_ships.append(enemy_matrix[0][row][col])

                                                if shop.first_task.TEXT == shop.list_first_task[-1]:
                                                    shop.three_hits_in_row(cell = enemy_matrix[0][row][col])

                                                if shop.second_task.TEXT == shop.list_second_task[2]:
                                                    shop.ship_hits.append(enemy_matrix[0][row][col])
                                                if shop.fourth_task.TEXT == shop.list_fourth_task[1]:
                                                    shop.ship_hits_three.append(enemy_matrix[0][row][col])

                                                # ачивки
                                                achievement.piooner(cell = enemy_matrix[0][row][col] , grid = list_grid) 
                                                achievement.ten_shoot_in_row(cell = enemy_matrix[0][row][col])
                                                achievement.first_shot(cell = enemy_matrix[0][row][col])
                                                achievement.lone_hunter(cell = enemy_matrix[0][row][col])

                                                # якщо гравець натиснув на пусту клітинку , то у матрицю ворога записуємо цифру 5
                                                # 5 - значить , що гравець зробив постріл , але схибив його
                                                if enemy_matrix[0][row][col] == 0:
                                                    enemy_matrix[0][row][col] = 5
                                                    # оскільки ці умови , якщо гравець це клієнт
                                                    # то коли гравець зробив постріл і схибив , записуємо флаг "yes", щоб відправити на сервер інформацію про те ,що треба змінити чергу 
                                                    list_check_need_send[0] = "yes"  # Готуємо дані для відправки
                                                    turn[0] = "server_turn"  # Передаємо хід серверу
                                                    if shop.first_task.TEXT == shop.list_first_task[0]:
                                                        shop.two_hits_in_row(number_cell = 5)
                                                    if shop.first_task.TEXT == shop.list_first_task[1]:
                                                        shop.four_hits_in_row(number_cell = 5)
                                                    if shop.fourth_task.TEXT == shop.list_fourth_task[-1]:
                                                        shop.eight_hits_in_row(number_cell = 5)

                                                # робимо умову для випадку коли по клітичнці вже били
                                                elif enemy_matrix[0][row][col] == 5 or enemy_matrix[0][row][col] == 7:
                                                    print("Уже стреляли в эту клетку")
                                                
                                                # якщо гравець зробив постріл , і попав по кораблю , то у матрицю ворога запсиуємо 7
                                                # 7 - значить , що гравець зробив постріл і попав по кораблю
                                                elif enemy_matrix[0][row][col] != 0 and enemy_matrix[0][row][col] != 5 and enemy_matrix[0][row][col]:
                                                    # передаем в список где хранится флаг нужно ли отрисовывать анимацию удара "start_animation" - то есть надо
                                                    check_animation_rocket[0] = "start_animation"
                                                    # передаем в список координаты клетки в которую ударили , чтобы в этой же клеточке мы и отрисовывали анимацию
                                                    x_hit_the_ship[0] = list_object_map_enemy[list_object_map_enemy.index(cell)].x
                                                    y_hit_the_ship[0] = list_object_map_enemy[list_object_map_enemy.index(cell)].y
                                                    # у матрицю ворога записуємо 7
                                                    enemy_matrix[0][row][col] = 7
                                                    # обнуляємо час ходу
                                                    check_time[0] = 0
                                                    # записуємо у лист який перевіряє чи потрібно відпарвляти дані на сервер флаг "yes", але чергу не змінюємо оскільки гравець попав по кораблю
                                                    list_check_need_send[0] = "yes"
                                                    turn[0] = "client_turn"     
                                                    if shop.first_task.TEXT == shop.list_first_task[0]:
                                                        shop.two_hits_in_row(number_cell = 7)
                                                    if shop.first_task.TEXT == shop.list_first_task[1]:
                                                        shop.four_hits_in_row(number_cell = 7)
                                                    if shop.fourth_task.TEXT == shop.list_fourth_task[-1]:
                                                        shop.eight_hits_in_row(number_cell = 7)  

                    # перевіряємо за яку роль грає гравець                    
                    elif list_player_role[0] == "server_player":
                        if turn[0] == "server_turn":
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

                                                if shop.third_task.TEXT == shop.list_third_task[1]:
                                                    shop.single_ships.append(enemy_matrix[0][row ][col])
                                                if shop.fourth_task.TEXT == shop.list_fourth_task[0]:
                                                    shop.first_shot_is_kill(cell = enemy_matrix[0][row][col])
                                                if shop.third_task.TEXT == shop.list_third_task[-1]:
                                                    shop.kill_two_three_decker_in_a_row(cell = enemy_matrix[0][row][col])
                                                if shop.third_task.TEXT == shop.list_third_task[2]:
                                                    shop.count_two_3decker_ship.append(enemy_matrix[0][row ][col])
                                                    shop.kill_three_double_decker_in_a_row(cell = enemy_matrix[0][row][col])
                                                if shop.third_task.TEXT == shop.list_third_task[-2]:
                                                    shop.count_three_ships.append(enemy_matrix[0][row][col])

                                                if shop.first_task.TEXT == shop.list_first_task[-1]:
                                                    shop.three_hits_in_row(cell = enemy_matrix[0][row][col])

                                                if shop.second_task.TEXT == shop.list_second_task[2]:
                                                    shop.ship_hits.append(enemy_matrix[0][row][col])
                                                if shop.fourth_task.TEXT == shop.list_fourth_task[1]:
                                                    shop.ship_hits_three.append(enemy_matrix[0][row][col])

                                                # ачивки
                                                achievement.piooner(cell = enemy_matrix[0][row][col] , grid = list_grid) 
                                                achievement.ten_shoot_in_row(cell = enemy_matrix[0][row][col])
                                                achievement.first_shot(cell = enemy_matrix[0][row][col])
                                                achievement.lone_hunter(cell = enemy_matrix[0][row][col])
                                                

                                                # якщо гравець натиснув на пусту клітинку , то у матрицю ворога записуємо цифру 5
                                                # 5 - значить , що гравець зробив постріл , але схибив його
                                                if enemy_matrix[0][row][col] == 0:
                                                    # записуємо у матрицю ворога 5
                                                    enemy_matrix[0][row][col] = 5
                                                    # обнуляємо час для ходу
                                                    check_time[0] = 0
                                                    # оскільки гравець не потрапив по кораблю , то змінюємо чергу ходу
                                                    turn[0] = "client_turn"
                                                    if shop.first_task.TEXT == shop.list_first_task[0]:
                                                        shop.two_hits_in_row(number_cell = 5)
                                                    if shop.first_task.TEXT == shop.list_first_task[1]:
                                                        shop.four_hits_in_row(number_cell = 5)
                                                    if shop.fourth_task.TEXT == shop.list_fourth_task[-1]:
                                                        shop.eight_hits_in_row(number_cell = 5)


                                                # робимо умову для випадку коли по клітичнці вже били
                                                elif enemy_matrix[0][row][col] == 5 or enemy_matrix[0][row][col] == 7:
                                                    print("Уже стреляли в эту клетку")
                                                # якщо гравець зробив постріл , і попав по кораблю , то у матрицю ворога запсиуємо 7
                                                # 7 - значить , що гравець зробив постріл і попав по кораблю
                                                elif enemy_matrix[0][row][col] != 0 and enemy_matrix[0][row][col] != 5 and enemy_matrix[0][row][col] != 7:
                                                    # передаем в список где хранится флаг нужно ли отрисовывать анимацию удара "start_animation" - то есть надо
                                                    check_animation_rocket[0] = "start_animation"
                                                    # передаем в список координаты клетки в которую ударили , чтобы в этой же клеточке мы и отрисовывали анимацию
                                                    x_hit_the_ship[0] = list_object_map_enemy[list_object_map_enemy.index(cell)].x
                                                    y_hit_the_ship[0] = list_object_map_enemy[list_object_map_enemy.index(cell)].y
                                                    # у матрицю ворога записуємо 7
                                                    enemy_matrix[0][row][col] = 7
                                                    # обнуляємо час для ходу
                                                    check_time[0] = 0
                                                    if shop.first_task.TEXT == shop.list_first_task[0]:
                                                        shop.two_hits_in_row(number_cell = 7)
                                                    if shop.first_task.TEXT == shop.list_first_task[1]:
                                                        shop.four_hits_in_row(number_cell = 7)
                                                    if shop.fourth_task.TEXT == shop.list_fourth_task[-1]:
                                                        shop.eight_hits_in_row(number_cell = 7)



                                                
                                            
        # Перевіряємо чи не пустий список який зберігає чи хтось виграв
        if strategist_achievement.ACTIVE == False:
            if list_check_win[0] != None:   
                # якщо вже їтось виграв , то робимо ефект затемнення
                apply_fade_effect(screen = main_screen)
                # зупиняємо цикл гри
                run_game = False
                # змінюємо фрейм бою , на фрейм показу результатів
                change_scene(scene = finish_window())
                check_press_button[0] = None

        if screen_shake[0] > 1:
            screen_shake[0] -= 1
   

        # відмальовуємо екран із координатами що збергаються у списку render_offset , щоб якщо гравець потрапив по карблю , то був ефект трясіння
        main_screen.blit(pygame.transform.scale(main_screen, (1280 , 832)), render_offset)
        # оновлюємо екран
        pygame.display.flip()


# лист для того чтобы для игрока добавлились/отнимались очки только один раз
check_points = [0]
def finish_window():
    #установка заголовка та початкові налаштування
    pygame.display.set_caption("Finish Window")
    run_game = True
    check_points[0] = 0
    # створюємо основний цикл малювання вікна
    while run_game:
        check_points[0] += 1
        #обмежує частоту кадрів до 60
        module_screen_server.FPS.tick(60)
        # перевірка ролі гравця та результату гри
        #якщо гравець є клієнтом
        if list_player_role[0] == "player_client":
            # перевіряється, чи виграв він (win_client), і залежно від цього завантажується фон
            if list_check_win[0] == "win_client":
                finish_bg.image_name = "win_game_bg.png"
                finish_bg.load_image()
                finish_bg.draw_image(screen = main_screen)
            else:
                finish_bg.image_name = "lose_game_bg.png"
                finish_bg.load_image()
                finish_bg.draw_image(screen = main_screen)
        # якщо гравець є сервером (server_player), аналогічно перевіряється перемога (win_server) чи поразка, і вибирається відповідний фон
        elif list_player_role[0] == "server_player":
            if list_check_win[0] == "win_server":
                finish_bg.image_name = "win_game_bg.png"
                finish_bg.load_image()
                finish_bg.draw_image(screen = main_screen)
            else:
                finish_bg.image_name = "lose_game_bg.png"
                finish_bg.load_image()
                finish_bg.draw_image(screen = main_screen)

        # виводимо текст про завершення гри
        end_game_image.draw_image(screen = main_screen)
        # малюємо декорації
        new_year_cap.draw_image(screen = main_screen)
        shadow_text.draw_image(screen = main_screen)
        # відобраємо фони
        win_background.draw_image(screen = main_screen)
        defeat_background.draw_image(screen = main_screen)

        win_lose_text.draw_font()

        # відображення тексту та оновлення балів
        if list_player_role[0] == "player_client":
            #якщо клієнт виграв, відображається повідомлення про перемогу, бали гравця збільшуються на 100
            if list_check_win[0] == "win_client":
                win_lose_text.text = dict_save_information["player_nick"] + " won"
                win_lose_text.draw_font()

                # відмальовка ників та балів
                player_nick.text = dict_save_information["player_nick"]
                player_nick.size = 52
                player_nick.x_cor = 970
                player_nick.y_cor = 450
                player_nick.draw_font()
                player_points.text = str(dict_save_information["player_points"] + 100)
                player_points.size = 52
                player_points.x_cor = 980
                player_points.y_cor = 531
                player_points.draw_font()
                enemy_nick.text = dict_save_information["enemy_nick"]
                enemy_nick.size = 52
                enemy_nick.x_cor = 200
                enemy_nick.y_cor = 450
                enemy_nick.draw_font()
                if dict_save_information["enemy_points"] == 0:
                    enemy_points.text = str(dict_save_information["enemy_points"])
                else:
                    enemy_points.text = str(dict_save_information["enemy_points"] - 50)
                enemy_points.size = 52
                enemy_points.x_cor = 240
                enemy_points.y_cor = 531
                enemy_points.draw_font()

                nickname = input_nick.user_text
                if check_points[0] == 1:
                    list_users[nickname]["points"] += 100
                    write_json(filename = "data_base.json" , object_dict = list_users)
            # якщо клієнт програв, його бали зменшуються на 50 (якщо вони більше 0)
            else:
                win_lose_text.text = dict_save_information["player_nick"] + " Lost"
                win_lose_text.draw_font()

                # відмальовка ників та балів
                player_nick.text = dict_save_information["player_nick"]
                player_nick.size = 52
                player_nick.x_cor = 200
                player_nick.y_cor = 450
                player_nick.draw_font()
                if dict_save_information["player_points"] == 0:
                    player_points.text = str(dict_save_information["player_points"])
                else:
                    player_points.text = str(dict_save_information["player_points"] - 50)
                player_points.size = 52
                player_points.x_cor = 220
                player_points.y_cor = 531
                player_points.draw_font()

                enemy_nick.text = dict_save_information["enemy_nick"]
                enemy_nick.size = 52
                enemy_nick.x_cor = 970
                enemy_nick.y_cor = 450
                enemy_nick.draw_font()

                enemy_points.text = str(dict_save_information["enemy_points"] + 100)
                enemy_points.size = 52
                enemy_points.x_cor = 980
                enemy_points.y_cor = 531
                enemy_points.draw_font()

                data_base = read_json(name_file = "data_base.json")
                #беремо кол-во баллів користувача який запсукає сервер, щоб відправати оновлену кількість 
                data_points = data_base[input_nick.user_text]["points"]

                nickname = input_nick.user_text
                if check_points[0] == 1:
                    if data_points > 0:
                        list_users[nickname]["points"] -= 50
                        write_json(filename = "data_base.json" , object_dict = list_users)
         
        # аналогічно клієнту, але логіка перевірки пов'язана з win_server та lose_server
        elif list_player_role[0] == "server_player":
            if list_check_win[0] == "win_server":
                win_lose_text.text = dict_save_information["player_nick"] + " won"
                win_lose_text.draw_font()
                # відмальовка ників та балів
                player_nick.text = dict_save_information["player_nick"]
                player_nick.size = 52
                player_nick.x_cor = 970
                player_nick.y_cor = 450
                player_nick.draw_font()
                player_points.text = str(dict_save_information["player_points"] + 100)
                player_points.size = 52
                player_points.x_cor = 980
                player_points.y_cor = 531
                player_points.draw_font()
                enemy_nick.text = dict_save_information["enemy_nick"]
                enemy_nick.size = 52
                enemy_nick.x_cor = 200
                enemy_nick.y_cor = 450
                enemy_nick.draw_font()
                if dict_save_information["enemy_points"] == 0:
                    enemy_points.text = str(dict_save_information["enemy_points"])
                else:
                    enemy_points.text = str(dict_save_information["enemy_points"] - 50)
                enemy_points.size = 52
                enemy_points.x_cor = 240
                enemy_points.y_cor = 531
                enemy_points.draw_font()

                nickname = input_nick.user_text
                if check_points[0] == 1:
                    list_users[nickname]["points"] += 100
                    write_json(filename = "data_base.json" , object_dict = list_users)
            else:
                win_lose_text.text = dict_save_information["player_nick"] + " Lost"
                win_lose_text.draw_font()
                # відмальовка ників та балів
                player_nick.text = dict_save_information["player_nick"]
                player_nick.size = 52
                player_nick.x_cor = 200
                player_nick.y_cor = 450
                player_nick.draw_font()
                if dict_save_information["player_points"] == 0:
                    player_points.text = str(dict_save_information["player_points"])
                else:
                    player_points.text = str(dict_save_information["player_points"] - 50)
                player_points.size = 52
                player_points.x_cor = 220
                player_points.y_cor = 531
                player_points.draw_font()

                enemy_nick.text = dict_save_information["enemy_nick"]
                enemy_nick.size = 52
                enemy_nick.x_cor = 970
                enemy_nick.y_cor = 450
                enemy_nick.draw_font()

                enemy_points.text = str(dict_save_information["enemy_points"] + 100)
                enemy_points.size = 52
                enemy_points.x_cor = 980
                enemy_points.y_cor = 531
                enemy_points.draw_font()

                data_base = read_json(name_file = "data_base.json")
                #беремо кол-во баллів користувача який запсукає сервер, щоб відправати оновлену кількість 
                data_points = data_base[input_nick.user_text]["points"]

                nickname = input_nick.user_text
                if check_points[0] == 1:
                    if data_points > 0:
                        list_users[nickname]["points"] -= 50
                        write_json(filename = "data_base.json" , object_dict = list_users)
        # відмальвока кнопки рестарту гри
        restart_game.draw(surface = main_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False  
                change_scene(None)

        pygame.display.flip()