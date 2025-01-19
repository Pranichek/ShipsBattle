import pygame
import modules.screens.screen as module_screen
import modules.server as server_module
from ..create_game_frame import room_data, ip_room_text, port_room_text
from ...server import SERVER
from ...client import check_can_connect_to_fight
import modules.game_windows as game_windows
from ...classes.class_image import DrawImage
from ...classes.class_button import Button
from ...classes.class_input_text import input_ip_adress, input_nick, input_port, input_password
from .clinent_connect import connect_to_server, list_check_connection,fail_connect
from ..button_pressed import check_press_button, button_action
from ..change_window import change_scene
from ...game_tools import apply_fade_effect
from ...json_functions import read_json
from ...volume_settings import volume_down_button, off_sound_button, volume_up_button


#images
input_data_bg = DrawImage(width = 1280,height = 832 , x_cor = 0 , y_cor = 0 ,folder_name= "backgrounds" , image_name= "input_data.png")
third_cold_image = DrawImage(width=  150, height= 68 , x_cor= 536 , y_cor= 705 , folder_name= "decorations" , image_name= "ice.png")
fourth_cold_image = DrawImage(width= 150, height= 68 , x_cor= 686 , y_cor= 705 , folder_name= "decorations" , image_name= "ice.png")

#buttons 
back_to_menu = Button(x = 33 , y = 41 ,image_path = "back_button.png" , image_hover_path = "back_button_hover.png" , width = 158 , height = 41 , action = button_action)
join_game_button = Button(x= 352 , y = 642,image_path= "join_to_game.png" , image_hover_path= "joint_to_game_hover.png" , width= 575 , height = 80 , action = connect_to_server)


def join_game_window():
    #викликаємо функцію для запуску серверу
    #встановлюємо назву вікна гри для сервера
    pygame.display.set_caption("Join to Game Window")
    #створюжмо змінну для того щоб відстежувати коли треба закривати вікно
    run_game = True

    volume_down_button.x = 1096
    volume_down_button.y = 26
    volume_up_button.x = 1004
    volume_up_button.y = 26
    off_sound_button.x = 1188
    off_sound_button.y = 26
    
    check_connect_to_game = 0
    if SERVER.START_CONNECT == False:
        ip_room_text.text = ""
        ip_room_text.update_text()
        port_room_text.text = ""
        port_room_text.update_text()
    #основний цикл роботи вікна користувача
    while run_game:
        module_screen.FPS.tick(60)
        try:
            data = read_json(name_file = "utility.json")
            status_server = data["status"]
        except:
            status_server = "wait"
            continue

        input_data_bg.draw_image(screen = module_screen.main_screen)

        input_nick.draw_text()
        input_ip_adress.draw_text()
        input_port.draw_text()
        input_password.draw_text()

        back_to_menu.draw(surface= module_screen.main_screen)

        third_cold_image.draw_image(screen= module_screen.main_screen)
        fourth_cold_image.draw_image(screen= module_screen.main_screen)
        join_game_button.draw(surface= module_screen.main_screen)

        room_data.draw_image(screen= module_screen.main_screen)
        ip_room_text.draw_font()
        port_room_text.draw_font()

        if input_nick.active == True:
            if input_nick.user_text == input_nick.base_text or input_nick.user_text == "":
                input_nick.fade_out()
            else:
                input_nick.fade_in()
        else:  # Если поле неактивно
            if input_nick.user_text == "" or input_nick.user_text == input_nick.base_text:  # Если пользователь ничего не ввел
                input_nick.user_text = input_nick.base_text  # Восстановление базового текста
                input_nick.fade_in()  # Плавное появление базового текста

        if input_ip_adress.active == True:
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

        if input_password.active == True:
            if input_password.user_text == input_password.base_text or input_password.user_text == "":
                input_password.fade_out()
            else:
                input_password.fade_in()
        else:
            if input_password.user_text == "" or input_password.user_text == input_password.base_text:
                input_password.user_text = input_password.base_text
                input_password.fade_in()

        #если не нашли сервер по которому подключаемся или ввели что то неправильно, выводим табличку о том что таокго сервера нет
        #этот список находится в файле connect_to_server.check_after_randomy
        if list_check_connection[0] == "error_connection":
            # рисуем табличку ошибки
            fail_connect.draw_image(screen = module_screen.main_screen)
            # вызываем метод этой таблички который позволяет отслеживать наведен ли курсор на нее или нет
            # если он находится на картинке то она пропадет
            fail_connect.check_touch()
            if fail_connect.visible == False:
                list_check_connection[0] = True
    
        if server_module.list_player_role[0] != "" and check_can_connect_to_fight[2] == False:
            check_connect_to_game += 1
            if check_connect_to_game >= 13:
                apply_fade_effect(screen = module_screen.main_screen)
                change_scene(game_windows.waiting_window())
                check_press_button[0] = None
                run_game = False
        elif server_module.list_player_role[0] != "" and check_can_connect_to_fight[2] != False:
            apply_fade_effect(screen = module_screen.main_screen)
            change_scene(game_windows.ships_position_window())
            check_press_button[0] = None
            run_game = False

        volume_up_button.draw(surface = module_screen.main_screen)
        volume_down_button.draw(surface = module_screen.main_screen)
        off_sound_button.draw(surface = module_screen.main_screen)

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
                input_password.user_text = input_password.base_text
                run_game = False
                change_scene(game_windows.main_window())
            elif event.type == pygame.MOUSEBUTTONDOWN:
                back_to_menu.check_click(event= event)
                join_game_button.check_click(event= event)
                volume_up_button.check_click(event= event)
                volume_down_button.check_click(event= event)
                off_sound_button.check_click(event= event)


            input_nick.check_event(event)
            input_ip_adress.check_event(event)
            input_port.check_event(event)  
            input_password.check_event(event)

        #оновлюємо екран щоб можна було бачити зміни на ньому
        pygame.display.flip()