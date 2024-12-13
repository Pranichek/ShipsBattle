#імпортуємо усі потрібні модулі
import pygame
from ..screens import main_screen , list_object_map , grid_player , list_grid 
import modules.screens.screen as module_screen_server
from ..classes import DrawImage , Button , Font  , list_ships 
from ..classes.class_input_text import input_ip_adress ,input_nick ,input_port
from ..json_functions import read_json , write_json
from ..classes.class_music import music_load_main , music_load_waiting
from ..classes.class_click import music_click
from .launch_server import start_server , fail_start_server , check_server_started
from .connect_to_server import connect_to_server , list_check_connection , fail_connect
from .random_placing import random_places_ships
from ..server import list_check_ready_to_fight , dict_save_information

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



#fonts(text)
createbutton_font = Font(size= 48 , name_font= "Jersey15.ttf" , text= "create" , screen= main_screen , x_cor= 218, y_cor= 663)
join_game_fonts = Font(size= 48 , name_font= "Jersey15.ttf" , text= "join" , screen= main_screen , x_cor= 974 , y_cor= 663)
#Текст с никами игроков
player_nick = Font(size = 48 , name_font= "Jersey15.ttf" , text = dict_save_information["player_nick"] , screen = main_screen , x_cor = 914 , y_cor = 126)
enemy_nick = Font(size = 48 , name_font= "Jersey15.ttf" , text = dict_save_information["enemy_nick"] , screen = main_screen , x_cor = 437 , y_cor = 126)
player_points = Font(size = 48 , name_font= "Jersey15.ttf" , text = str(dict_save_information["player_points"]) , screen = main_screen , x_cor = 743 , y_cor = 126)
enemy_points = Font(size = 48 , name_font= "Jersey15.ttf" , text = str(dict_save_information["enemy_points"]) , screen = main_screen , x_cor = 270 , y_cor = 126)




def test():
    print(1)
    
def button_action():
    check_press_button[0] = "button is pressed"
    music_click.play2(0)


#функція для перезаписування яке зараз вікно активне
def change_scene(scene):
    list_current_scene[0] = scene

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


#buttons
#кнопка кторая перекидывает на фрейм по созданию игры(запуска сервера)
create_game_frame = Button(x= 113, y = 653,image_path= "button_create.png" , image_hover_path= "create_button_hover.png" , width= 346 , height= 80 , action= button_action)
#кнопка кторая перекидывает на фрейм по присоеденению к игре(серверу)
join_game_frame = Button(x= 832 , y = 653,image_path= "join_button.png" , image_hover_path= "join_button_hover.png" , width= 346 , height= 80 , action= button_action)
#кнопка которая возвращает назад к главному окну
back_to_menu = Button(x= 33 , y = 41 ,image_path= "back_button.png" , image_hover_path= "back_button_hover.png" , width= 158 , height= 41 , action= button_action)
#кнопка которая запускает сервер(игру)
start_game_button = Button(x= 352 , y = 642,image_path= "create_game_button.png" , image_hover_path= "create_game_button_hover.png" , width= 575 , height= 80 , action= start_server)
#кнопка которая подключается к игре
join_game_button = Button(x= 352 , y = 642,image_path= "join_to_game.png" , image_hover_path= "joint_to_game_hover.png" , width= 575 , height= 80 , action= connect_to_server)
#кнопка коли розставив кораблі та підлючаєшься до бою
ready_for_battle = Button(x= 798 , y = 626,image_path= "start_battle.png" , image_hover_path= "start_battle_hover.png" , width= 408 , height= 61 , action= connect_to_fight)
#кнопка яка будеть розставляти кораблі у ранломному положені
random_place_ships = Button(x= 205 , y = 709,image_path= "random_place.png" , image_hover_path= "random_place_hover.png" , width= 318 , height= 48 , action= random_places_ships)
# кнопка для добавления звука
button_upp = Button(x=53 ,y=44 , image_path="button_music_upp.png", image_hover_path="button_volue_up_hover.png", width= 74, height= 71, action= music_up)
button_lower = Button(x=53,y=136, image_path="button_music_lower.png", image_hover_path="button_music_lower_hover.png", width= 74, height= 71, action= music_lower)
#кнопка возвращения на сервер
back_to_server = Button(x= 39 , y = 56 ,image_path= "back_button.png" , image_hover_path= "back_button_hover.png" , width= 158 , height= 41 , action= button_action)


#images decoration
cold_image = DrawImage(width= 152 , height= 68 , x_cor= 207 , y_cor= 716 , folder_name= "decorations" , image_name= "ice.png")
second_cold_image = DrawImage(width= 152 , height= 68 , x_cor= 940, y_cor= 716 , folder_name= "decorations" , image_name= "ice.png")
third_cold_image = DrawImage(width=  150, height= 68 , x_cor= 536 , y_cor= 705 , folder_name= "decorations" , image_name= "ice.png")
fourth_cold_image = DrawImage(width= 150, height= 68 , x_cor= 686 , y_cor= 705 , folder_name= "decorations" , image_name= "ice.png")
#image for the grid
grid_image = DrawImage(width = 662  , height = 662 , x_cor = 40 , y_cor = 37 , folder_name = "grid", image_name = "background_grid.png")
# image for window where players are fighting against each other
fight_bg = DrawImage(width = 1280,height = 832 , x_cor = 0 , y_cor = 0 , folder_name= "backgrounds" , image_name= "fight_background.png")
# Зображення для декаративної рамки для ніку та очок на фремі бою
frame_nick_player = DrawImage(width = 362 ,height = 69 , x_cor = 222 , y_cor = 116 , folder_name= "backgrounds" , image_name= "frame_nick.png")
second_frame_nick_player = DrawImage(width = 362 ,height = 69 , x_cor = 699 , y_cor = 116 , folder_name= "backgrounds" , image_name= "frame_nick.png")

player_face = DrawImage(width = 195 , height = 122  ,x_cor = 1065 , y_cor = 64 , folder_name = "decorations" , image_name = "player_image.png")
enemy_face = DrawImage(width = 195 , height = 122  ,x_cor = 20 , y_cor = 64 , folder_name = "decorations" , image_name = "enemy_image.png")


#backgrounds
main_bg = DrawImage(width = 1280,height = 832 , x_cor = 0 , y_cor = 0 ,folder_name= "backgrounds" , image_name= "main_background.jpg")
#фон для окон д=где вводим данные для запуска сервера и подключение к нему
input_data_bg= DrawImage(width = 1280,height = 832 , x_cor = 0 , y_cor = 0 ,folder_name= "backgrounds" , image_name= "input_data.png")
#фон для очікування користувача
waiting_background = DrawImage(width = 1280,height = 832 , x_cor= 0 , y_cor = 0 ,folder_name= "backgrounds" , image_name= "waiting_background.png")
#фон для розташування кораблів перед ігрою
ships_position_bg = DrawImage(width = 1280,height = 832 , x_cor = 0 , y_cor=  0 ,folder_name= "backgrounds" , image_name= "position_ships_bg.png")
# фон на якомй стоять кораблі перед початком бою
place_for_ships = DrawImage(width = 477 , height = 559 , x_cor = 763 , y_cor = 37 ,folder_name= "backgrounds" , image_name= "bg_place_for_ships.png")


#Ships 
# ship_one = DrawImage(width = , height = , x_cor = , y_cor = , folder_name = "ships" , image_name = "ship_one.png")



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
        module_screen_server.FPS.tick(60)
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
            elif check_press_button[0] == "button is pressed":
                # music_click.check_after_randomlay2(0)
                check_press_button[0] = None
                run_game = False
                x_pos , y_pos = pygame.mouse.get_pos()
                if x_pos > 600:
                    change_scene(fight_window())
                elif x_pos < 600:
                    change_scene(create_game_window())
            elif event.type == pygame.MOUSEBUTTONDOWN:
                create_game_frame.check_click()
                join_game_frame.check_click()
                button_upp.check_click()
                button_lower.check_click()

        pygame.display.flip()


    

def create_game_window():
    #викликаємо функцію для запуску серверу
    #встановлюємо назву вікна гри для сервера
    pygame.display.set_caption("Create Game Window")
    #створюжмо змінну для того щоб відстежувати коли треба закривати вікно
    run_game = True
    #основний цикл роботи вікна користувача
    while run_game:
        module_screen_server.FPS.tick(60)
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
                    run_game = False
                    change_scene(waiting_window())
                    check_press_button[0] = None

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
                print(100)
                change_scene(main_window())
            elif event.type == pygame.MOUSEBUTTONDOWN:
                back_to_menu.check_click()
                start_game_button.check_click()
                
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
        data = read_json(name_file = "utility.json")
        status_server = data["status"]
        module_screen_server.FPS.tick(60)
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
                back_to_menu.check_click()
                join_game_button.check_click()
               

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
        data = read_json(name_file = "utility.json")
        status_server = data["status"]
        module_screen_server.FPS.tick(60)

        if list_check_ready_to_fight[0] == "fight":
            change_scene(fight_window())
            run_game = False

        waiting_background.draw_image(screen = main_screen)
        back_to_server.draw(surface= main_screen)

        if list_check_ready_to_fight[0] == None:
            if status_server == "connect":
                change_scene(ships_position_window())
                check_press_button[0] = None
                run_game = False
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
        module_screen_server.FPS.tick(60)
        if list_check_ready_to_fight[0] == "fight":
            change_scene(fight_window())
            run_game = False
        elif list_check_ready_to_fight[0] == "wait":
            change_scene(scene = waiting_window())
            run_game = False
        
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
                ready_for_battle.check_click()
                random_place_ships.check_click()
                
        pygame.display.flip()

x = 0

def fight_window():
    global x

    #568 - по иску
    #127 - по игреку 

    music_load_waiting.stop()
    music_load_main.play()
    pygame.display.set_caption("Battle Screen")
    run_game = True

    grid_player.generate_grid()


    while run_game:
        module_screen_server.FPS.tick(60)

        fight_bg.draw_image(screen = main_screen)

        frame_nick_player.draw_image(screen = main_screen)
        second_frame_nick_player.draw_image(screen = main_screen)

        player_face.draw_image(screen = main_screen)
        enemy_face.draw_image(screen = main_screen)

        player_nick.text = dict_save_information["player_nick"]
        player_nick.draw_font()
        enemy_nick.text = dict_save_information["enemy_nick"]
        enemy_nick.draw_font()
        player_points.text = str(dict_save_information["player_points"])
        player_points.draw_font()
        enemy_points.text = str(dict_save_information["enemy_points"])
        enemy_points.draw_font()

        #отрисовка обьектов(пустых клеток) который хранятся в списке обьектов
        for object in list_object_map:
            object.x += 568
            object.y += 127 
            object.draw(screen = main_screen)
            x += 1
            print(x)
        
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False  
                change_scene(None)
                 
        pygame.display.flip()