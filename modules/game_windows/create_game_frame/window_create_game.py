import pygame, socket
import modules.game_windows as game_windows
import modules.screens.screen as module_screen
from ...classes.class_image import DrawImage
from ...classes.class_button import Button
from ...classes.class_click import music_click
from ...classes.class_input_text import input_ip_adress, input_nick, input_port, input_password
from .launch_server import check_server_started, fail_start_server, start_server
from ..button_pressed import check_press_button, button_action
from ..change_window import change_scene, list_current_scene
from ...game_tools import apply_fade_effect
from ...json_functions import read_json

flag_ip = [None]
def get_local_ip():
    try:
        try:
            # Попробовать получить IPv4
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.connect(("8.8.8.8", 80))
            ip = sock.getsockname()[0]
            sock.close()
        except:
            # Если IPv4 недоступен пробуем IPv6
            sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
            sock.connect(("2001:4860:4860::8888", 80)) 
            ip = sock.getsockname()[0]
            sock.close()
        music_click.play2(0)
        input_ip_adress.user_text = ip
        input_ip_adress.VISIBLE = 0
        input_ip_adress.active = True 
        flag_ip[0] = True
    except Exception as error:
        print(f"Ошибка при получении IP: {error}")
        return None
    
def set_wan_ip():
    music_click.play2(0)
    input_ip_adress.user_text = "0.0.0.0"
    input_ip_adress.VISIBLE = 0
    input_ip_adress.active = True 
    flag_ip[0] = True


#images 
#фон для окон д=где вводим данные для запуска сервера и подключение к нему
input_data_bg = DrawImage(width = 1280,height = 832 , x_cor = 0 , y_cor = 0 ,folder_name= "backgrounds" , image_name= "input_data.png")
third_cold_image = DrawImage(width=  150, height= 68 , x_cor= 536 , y_cor= 705 , folder_name= "decorations" , image_name= "ice.png")
fourth_cold_image = DrawImage(width= 150, height= 68 , x_cor= 686 , y_cor= 705 , folder_name= "decorations" , image_name= "ice.png")

#buttons
lan_ip_button = Button(x = 790, y = 410, image_path = "lan_ip_button.png", image_hover_path = "lan_ip_button_hover.png", width = 58, height = 60, action = get_local_ip)
wan_ip_button = Button(x = 437, y = 410, image_path = "wan_ip.png", image_hover_path = "wan_ip_hover.png", width = 58, height = 60, action = set_wan_ip)
#кнопка которая возвращает назад к главному окну
back_to_menu = Button(x= 33 , y = 41 ,image_path= "back_button.png" , image_hover_path= "back_button_hover.png" , width= 158 , height = 41 , action = button_action)
#кнопка которая запускает сервер(игру)
start_game_button = Button(x= 352 , y = 642,image_path= "create_game_button.png" , image_hover_path= "create_game_button_hover.png" , width = 575 , height = 80 , action= start_server)



def create_game_window():
    #викликаємо функцію для запуску серверу
    #встановлюємо назву вікна гри для сервера
    pygame.display.set_caption("Create Game Window")
    #створюжмо змінну для того щоб відстежувати коли треба закривати вікно
    run_game = True

    #основний цикл роботи вікна користувача
    while run_game:
        x, y = pygame.mouse.get_pos()
        module_screen.FPS.tick(60)
        input_data_bg.draw_image(screen = module_screen.main_screen)
        data = read_json(name_file = "utility.json")
        status_server = data["status"]

        wan_ip_button.draw(surface = module_screen.main_screen)
        lan_ip_button.draw(surface = module_screen.main_screen)

        input_ip_adress.draw_text()
        input_port.draw_text()

        back_to_menu.draw(surface = module_screen.main_screen)

        third_cold_image.draw_image(screen = module_screen.main_screen)
        fourth_cold_image.draw_image(screen = module_screen.main_screen)
        start_game_button.draw(surface =module_screen.main_screen)

            
        if input_ip_adress.active == True or flag_ip[0] == True:
            if input_ip_adress.VISIBLE >= 255:
                flag_ip[0] = None
            if input_ip_adress.user_text == input_ip_adress.base_text or input_ip_adress.user_text == "":
                input_ip_adress.fade_out()
            else:
                input_ip_adress.fade_in()
        else:
            if input_ip_adress.user_text == "" or input_ip_adress.user_text == input_ip_adress.base_text:
                input_ip_adress.user_text = input_ip_adress.base_text
                input_ip_adress.fade_in()
     
        
        if input_port.active == True:
            if input_port.user_text == input_port.base_text or input_port.user_text == "":
                input_port.fade_out()
            else:
                input_port.fade_in()
        else:
            if input_port.user_text == "" or input_port.user_text == input_port.base_text:
                input_port.user_text = input_port.base_text
                input_port.fade_in()

            
        #если попытались создать сервер кторый нельзя(например неправильны айпи) , то выводим предуприждение об этом
        if check_server_started[0] == "error_server":
            fail_start_server.draw_image(screen = module_screen.main_screen)
            fail_start_server.check_touch()
            #когда игрок закрыл табличку записываем True в список , чтобы знали что уже пытались запустить сервер
            if fail_start_server.visible == False:
                check_server_started[0] = True
        #Обробляємо всі події у вікні
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False  
                list_current_scene[0] = None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                back_to_menu.check_click(event = event)
                start_game_button.check_click(event = event)
                lan_ip_button.check_click(event = event)
                wan_ip_button.check_click(event = event)

            elif check_press_button[0] == "button is pressed":
                check_press_button[0] = None
                run_game = False
                input_nick.user_text = input_nick.base_text
                input_ip_adress.user_text = input_ip_adress.base_text
                input_port.user_text = input_port.base_text
                input_password.user_text = input_password.base_text
                change_scene(game_windows.main_window())
        
            input_nick.check_event(event)
            input_ip_adress.check_event(event)
            input_port.check_event(event)  
            input_password.check_event(event)

        #оновлюєио екран щоб можна було бачити зміни на ньому
        pygame.display.flip()