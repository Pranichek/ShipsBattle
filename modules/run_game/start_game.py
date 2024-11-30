#імпортуємо усі потрібні модулі
import pygame
from ..screens import main_screen , Grid , list_object_map , grid_player
import modules.screens.screen as module_screen_server
from ..classes import DrawImage , Button , Font , ship_three , ship_two , ship_one , ship_four , list_ships
from ..server import server_thread 
from ..client import thread_connect , event_connect_to_server , list_check_connection
from ..classes.class_input_text import input_ip_adress ,input_nick ,input_port
from ..json_functions.read_json import read_json
from ..classes.class_music import music_load_main , music_load_waiting
from ..classes.class_click import music_click
from .start_server import start_server , fail_start_server , check_server_started
from .connect_to_server import connect_to_server , list_check_connection , fail_connect


#список для проверки нажата ли кнопка
check_press_button = [None]
#список для відслужування чи нажата кнопка підключення до серверу чи ні
check_client_connected = [False]
#ліст для зберігання яке зараз вікно активне
list_current_scene = [None]
#список для того щоб головна музика починала грати лише один раз і не приривалася
once_play_music = [0]
#список для відслуджування чи нажати кнопка заупску серверу чи ні
# check_server_started = [False]
# #список для відслуджування чи підключився користувач до серверу чи ні
# list_check_connection = [False]


#ініціалізуємо pygame щоб можна було із ним працювати
pygame.init()


#fonts(text)
createbutton_font = Font(size= 48 , name_font= "Jersey15.ttf" , text= "create" , screen= main_screen , x_cor= 218, y_cor= 663)
join_game_fonts = Font(size= 48 , name_font= "Jersey15.ttf" , text= "join" , screen= main_screen , x_cor= 974 , y_cor= 663)

def test():
    print(1)

#функція для запуску серверу
# def start_server():
#     #запускаємо звук кліку кнопки
#     music_click.play2(0)
#     # розділяем нашь айпі на числа , тобо якщо воно було таке 192.168.0.1 то стане таким 192 168 0 1
#     # це для того щоб можна було перевірити кожне число окремо
#     ip_address = input_ip_adress.user_text.split(".")
#     # якщо цих чисел не 4 , то користувач не правильно увів дані 
#     if len(ip_address) != 4:
#         # передаємо у список повідомлення про помилку шоб можна було вивести на екрані вікно помилки
#         check_server_started[0] = "error_server"
#         # якщо вже було це вікно , то робимо його видимим 
#         if fail_start_server.visible == False:
#             fail_start_server.visible = True
#             print("error_server")
#         # return False - означає що сталася помилка ,та код не буде далі рухатися
#         return False
#     # перевіряємо чи кожне число в межах допустимого діапазону
#     for number in ip_address:
#         # перевіряємо чи це взагалі числа а не наприклад літери
#         if not number.isdigit():
#             # якшо це не цифри, то передаємо у список повідомлення про помилку шоб можна було вивести на екрані вікно помилки
#             check_server_started[0] = "error_server"
#             print("зашло")
#             # якщо вже було це вікно , то робимо його видимим 
#             if fail_start_server.visible == False:
#                 fail_start_server.visible = True
#                 print("error_server")
#             # return False - означає що сталася помилка ,та код не буде далі рухатися
#             return False
#         # якщо користувач увів числа але вони не підходять під рамки для нормального айпі, то виводимо окно про помилку
#         if not 0 <= int(number) <= 255:
#             check_server_started[0] = "error_server"
#             print("зашло")
#             if fail_start_server.visible == False:
#                 fail_start_server.visible = True
#                 print("error_server")
#             # return False - означає що сталася помилка ,та код не буде далі рухатися
#             return False
#     try:
#         # тепер перівіряємо на правильність порт 
#         port = int(input_port.user_text)
#         #  якщо користувач увів нічого або лише тільки одну цифру то виводимо окно с помилкою
#         if len(ip_address) <= 1:
#                 check_server_started[0] = "error_server"
#                 print("зашло")
#                 if fail_start_server.visible == False:
#                     fail_start_server.visible = True
#                     print("error_server")
#                 # return False - означає що сталася помилка ,та код не буде далі рухатися
#                 return False
#         # якщо порт не підходить під рамки, то виводимо окно с помилкою
#         elif not 1240 < port < 65553:
#             check_server_started[0] = "error_server"
#             print("зашло")
#             if fail_start_server.visible == False:
#                 fail_start_server.visible = True
#                 print("error_server")
#             # return False - означає що сталася помилка ,та код не буде далі рухатися
#             return False
#     except ValueError:
#         #  якщо порт взагалі не цифри то також виводимо окно із помилкою
#         check_server_started[0] = "error_server"
#         print("зашло")
#         if fail_start_server.visible == False:
#             fail_start_server.visible = True
#             print("error_server")
#         # return False - означає що сталася помилка ,та код не буде далі рухатися
#         return False
#     # якщо все вірно , то запускаємо сервер
#     server_thread.start()





# def connect_to_server():
#     #запускаємо звук кліку кнопки
#     music_click.play2(0)
#     # розділяем нашь айпі на числа , тобо якщо воно було таке 192.168.0.1 то стане таким 192 168 0 1
#     # це для того щоб можна було перевірити кожне число окремо
#     ip_address = input_ip_adress.user_text.split(".")
#     # якщо воно має більше чисел ніж 4 або менш ніж 4 чисел, то такий айпі не є вірним , і виводимо помилку
#     if len(ip_address) != 4:
#         list_check_connection[0] = "error_connection"
#         print("зашло")
#         if fail_connect.visible == False:
#             fail_connect.visible = True
#             print("error_connection")
#         # return False - означає що сталася помилка ,та код не буде далі рухатися
#         return False
    
#     # перевіряємо чи кожне число в межах допустимого діапазону
#     for number in ip_address:
#         # перевіряємо чи це взагалі числа а не наприклад літери
#         if not number.isdigit():
#             # якшо це не цифри, то передаємо у список повідомлення про помилку шоб можна було вивести на екрані вікно помилки
#             list_check_connection[0] = "error_server"
#             print("зашло")
#             # якщо вже було це вікно , то робимо його видимим 
#             if fail_connect.visible == False:
#                 fail_connect.visible = True
#                 print("error_server")
#             # return False - означає що сталася помилка ,та код не буде далі рухатися
#             return False
#         # якщо айпі не підходить у рамки нормальних значеннь виводимо помулку
#         if not 0 <= int(number) <= 255:
#             list_check_connection[0] = "error_connection"
#             print("зашло")
#             if fail_connect.visible == False:
#                 fail_connect.visible = True
#                 print("error_connection")
#             # return False - означає що сталася помилка ,та код не буде далі рухатися
#             return False
#     try:
#         #  тепер первіряємо порт на правильність написання
#         port = int(input_port.user_text)
#         # якщо користувач взагалі не увів цифр або тільки одну то виводимо помилку за допомогою передавання про помилку у список
#         if len(ip_address) <= 1:
#                 list_check_connection[0] = "error_connection"
#                 print("зашло")
#                 if fail_connect.visible == False:
#                     fail_connect.visible = True
#                     print("error_connection")
#                 # return False - означає що сталася помилка ,та код не буде далі рухатися
#                 return False
#         # якщо користувач увів порт який не підходить у рамки портів то виводимо помилку за допомогою передавання про помилку у список
#         elif not 1240 < port < 65553:
#             list_check_connection[0] = "error_connection"
#             print("зашло")
#             if fail_connect.visible == False:
#                 fail_connect.visible = True
#                 print("error_connection")
#             # return False - означає що сталася помилка ,та код не буде далі рухатися
#             return False
#     except ValueError:
#         # якщо порт взагалі не цифра , то  виводимо помилку за допомогою передавання про помилку у список
#         list_check_connection[0] = "error_connection"
#         print("зашло")
#         if fail_connect.visible == False:
#             fail_connect.visible = True
#             print("error_server")
#         # return False - означає що сталася помилка ,та код не буде далі рухатися
#         return False
#     # якщо усі перевірки пройдені і користувач вперше натиснув на цю кнопку то запускаємо підключення до серверу
#     if event_connect_to_server.is_set():
#         thread_connect.start()
#     # якщо усі перевікри пройдені але це не перший запуск, наприклад перший раз увів айди сервера якого ще немає, а тепер такий сервер є 
#     # то передаємо у  event_connect_to_server значення True за допомогою .set()
#     else:
#         event_connect_to_server.set()
        
    
def button_action():
    check_press_button[0] = "button is pressed"
    music_click.play2(0)


#функція для перезаписування яке зараз вікно активне
def change_scene(scene):
    list_current_scene[0] = scene



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
ready_for_battle = Button(x= 799 , y = 678,image_path= "start_battle.png" , image_hover_path= "start_battle_hover.png" , width= 408 , height= 61 , action= test)
#кнопка яка будеть розставляти кораблі у ранломному положені
random_place_ships = Button(x= 205 , y = 709,image_path= "random_place.png" , image_hover_path= "random_place_hover.png" , width= 318 , height= 48 , action= test)

#images decoration
cold_image = DrawImage(width= 152 , height= 68 , x_cor= 207 , y_cor= 716 , folder_name= "decorations" , image_name= "ice.png")
second_cold_image = DrawImage(width= 152 , height= 68 , x_cor= 940, y_cor= 716 , folder_name= "decorations" , image_name= "ice.png")
third_cold_image = DrawImage(width=  150, height= 68 , x_cor= 536 , y_cor= 705 , folder_name= "decorations" , image_name= "ice.png")
fourth_cold_image = DrawImage(width= 150, height= 68 , x_cor= 686 , y_cor= 705 , folder_name= "decorations" , image_name= "ice.png")
#image for the grid
grid_image = DrawImage(width = 600 , height = 597 , x_cor = 40 , y_cor = 89 , folder_name = "grid", image_name = "background_grid.png")


#backgrounds
main_bg = DrawImage(width = 1280,height= 832 , x_cor= 0 , y_cor= 0 ,folder_name= "images_background" , image_name= "main_background.jpg")
#фон для окон д=где вводим данные для запуска сервера и подключение к нему
input_data_bg= DrawImage(width = 1280,height= 832 , x_cor= 0 , y_cor= 0 ,folder_name= "images_background" , image_name= "input_data.png")
#фон для очікування користувача
waiting_background = DrawImage(width = 1280,height= 832 , x_cor= 0 , y_cor= 0 ,folder_name= "images_background" , image_name= "waiting_background.png")
#фон для розташування кораблів перед ігрою
ships_position_bg = DrawImage(width = 1280,height= 832 , x_cor= 0 , y_cor= 0 ,folder_name= "images_background" , image_name= "position_ships_bg.png")
# #фон коли користувач пробує підключитися до серверу якого немає
# fail_connect = DrawImage(width = 901 , height = 283 , x_cor = 180 , y_cor = 273 , folder_name = "images_background" , image_name = "fail_background.png")
# #фон коли користувач пробує запустити сервер який вже запущений
# fail_start_server = DrawImage(width = 901 , height = 283 , x_cor = 180 , y_cor = 273 , folder_name = "images_background" , image_name = "fail_server.png")




#створюємо функцію, яка викликається при запуску гри для користувача який запускає сервер
def main_window():
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
 
        second_cold_image.draw_image(screen= main_screen)
        join_game_frame.draw(surface= main_screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False  
                change_scene(None)
            elif check_press_button[0] == "button is pressed":
                # music_click.play2(0)
                check_press_button[0] = None
                run_game = False
                x_pos , y_pos = pygame.mouse.get_pos()
                if x_pos > 600:
                    change_scene(join_game_window())
                elif x_pos < 600:
                    change_scene(create_game_window())
            elif event.type == pygame.MOUSEBUTTONDOWN:
                create_game_frame.check_click()
                join_game_frame.check_click()

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
                music_click.play2(0)
                check_press_button[0] = None
                input_nick.user_text =  input_nick.base_text
                input_ip_adress.user_text = input_ip_adress.base_text
                input_port.user_text = input_port.base_text
                run_game = False
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

        #если не нашли сервер по которому подключаемся , выводим табличку о том что таокго сервера нет
        if list_check_connection[0] == "error_connection":
            fail_connect.draw_image(screen = main_screen)
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
                music_click.play2(0)
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
    pygame.display.set_caption("Waiting window")
    run_game = True
    music_load_main.stop()
    music_load_waiting.play()
    while run_game:
        data = read_json(name_file = "utility.json")
        status_server = data["status"]
        module_screen_server.FPS.tick(60)
        waiting_background.draw_image(screen = main_screen)

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
    pygame.display.set_caption("Position Ships")
    run_game = True
    
    #generate grid with class
    grid_player.generate_grid()

    while run_game:
        module_screen_server.FPS.tick(60)
        ships_position_bg.draw_image(screen = main_screen)

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
                ship.rotate_ship(event = event)
                ship.matrix_move(event = event, matrix_width = 558, matrix_height = 558, cell = 81)

            if event.type == pygame.QUIT:
                run_game = False  
                change_scene(None)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ready_for_battle.check_click()
                random_place_ships.check_click()
        
        pygame.display.flip()
        