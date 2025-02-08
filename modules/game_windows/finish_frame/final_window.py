# import pygame, sys
# import modules.game_windows as game_windows
# import modules.screens.screen as module_screen
# from ...classes.class_image import DrawImage
# from ...classes.class_text import Font
# from ...classes import input_nick, input_ip_adress, input_port, input_password
# from ...client import dict_save_information
# from ...server import list_player_role, list_check_win
# from ..change_window import change_scene
# from ...json_functions import read_json, write_json, list_users
# from ...game_tools import apply_fade_effect
# from ...classes import Button
# from ...json_functions import write_json
# from ...server import list_check_win, SERVER, list_check_ready_to_fight
# from ...client import check_can_connect_to_fight, check_start_connect, save_data_posistion_ships, check_connection_users
# from ..main_frame import once_play_music

# leave_game = [False]
# def back_to_main():
#     apply_fade_effect(screen = module_screen.main_screen)
#     change_scene(game_windows.main_window)
#     leave_game[0] = True

# #Button
# restart_button = Button(x = 436, y = 700, image_path = "restart_button_hover.png", image_hover_path = "restart_button_hover.png", width = 436, height = 68, action = back_to_main)

# # Images
# finish_bg = DrawImage(width=1280, height=832, x_cor=0, y_cor=0, folder_name="backgrounds", image_name="win_game_bg.png")
# end_game_image = DrawImage(width=606, height=131, x_cor=337, y_cor=80, folder_name="decorations", image_name="end_game.png")
# new_year_cap = DrawImage(width=133, height=133, x_cor=331, y_cor=80, folder_name="decorations", image_name="new_year_cap.png")
# shadow_text = DrawImage(width=816, height=150, x_cor=233, y_cor=255, folder_name="decorations", image_name="shadow_text.png")
# win_background = DrawImage(width=315, height=199, x_cor=97, y_cor=416, folder_name="backgrounds", image_name="result_game_bg.png")
# defeat_background = DrawImage(width=315, height=199, x_cor=860, y_cor=416, folder_name="backgrounds", image_name="result_game_bg.png")

# # Fonts
# win_lose_text = Font(size=96, name_font="Goldman_Bold.ttf", text="", screen=module_screen.main_screen, x_cor = 383, y_cor = 248, text_color="White")
# player_nick = Font(size=48, name_font="Jersey15.ttf", text=dict_save_information["player_nick"], screen=module_screen.main_screen, x_cor=914, y_cor=126, text_color="White")
# enemy_nick = Font(size=48, name_font="Jersey15.ttf", text=dict_save_information["enemy_nick"], screen=module_screen.main_screen, x_cor=437, y_cor=126, text_color="White")
# player_points = Font(size=48, name_font="Jersey15.ttf", text=str(dict_save_information["player_points"]), screen=module_screen.main_screen, x_cor=743, y_cor=126, text_color="White")
# enemy_points = Font(size=48, name_font="Jersey15.ttf", text=str(dict_save_information["enemy_points"]), screen=module_screen.main_screen, x_cor=270, y_cor=126, text_color="White")

# # Лист для уникнення багаторазового оновлення балів
# check_points = [0]

# def finish_window():
#     pygame.display.set_caption("Finish Window")
#     run_game = True
#     check_points[0] = 0
#     leave_game[0] = False

#     while run_game:
#         module_screen.FPS.tick(60)
#         module_screen.main_screen.fill((0, 0, 0))  # Очищення екрану чорним фоном

#         if list_player_role[0] == "client_player":
#             #якщо клієнт виграв, відображається повідомлення про перемогу, бали гравця збільшуються на 100
#             if list_check_win[0] == "win_client":
#                 win_lose_text.text = dict_save_information["player_nick"] + " won"
#                 # відмальовка ників та балів
#                 player_nick.text = dict_save_information["player_nick"]
#                 player_nick.size = 52
#                 player_nick.x_cor = 970
#                 player_nick.y_cor = 450
#                 player_nick.draw_font()
#                 player_points.text = str(dict_save_information["player_points"] + 100)
#                 player_points.size = 52
#                 player_points.x_cor = 980
#                 player_points.y_cor = 531
#                 enemy_nick.text = dict_save_information["enemy_nick"]
#                 enemy_nick.size = 52
#                 enemy_nick.x_cor = 200
#                 enemy_nick.y_cor = 450
#                 if dict_save_information["enemy_points"] == 0:
#                     enemy_points.text = str(dict_save_information["enemy_points"])
#                 else:
#                     enemy_points.text = str(dict_save_information["enemy_points"] - 50)
#                 enemy_points.size = 52
#                 enemy_points.x_cor = 240
#                 enemy_points.y_cor = 531

#                 nickname = input_nick.user_text
#                 if check_points[0] == 1:
#                     list_users[nickname]["points"] += 100
#                     write_json(filename = "data_base.json" , object_dict = list_users)
#             # якщо клієнт програв, його бали зменшуються на 50 (якщо вони більше 0)
#             else:
#                 win_lose_text.text = dict_save_information["player_nick"] + " Lost"

#                 # відмальовка ників та балів
#                 player_nick.text = dict_save_information["player_nick"]
#                 player_nick.size = 52
#                 player_nick.x_cor = 200
#                 player_nick.y_cor = 450
#                 if dict_save_information["player_points"] == 0:
#                     player_points.text = str(dict_save_information["player_points"])
#                 else:
#                     player_points.text = str(dict_save_information["player_points"] - 50)
#                 player_points.size = 52
#                 player_points.x_cor = 220
#                 player_points.y_cor = 531

#                 enemy_nick.text = dict_save_information["enemy_nick"]
#                 enemy_nick.size = 52
#                 enemy_nick.x_cor = 970
#                 enemy_nick.y_cor = 450

#                 enemy_points.text = str(dict_save_information["enemy_points"] + 100)
#                 enemy_points.size = 52
#                 enemy_points.x_cor = 980
#                 enemy_points.y_cor = 531

#                 data_base = read_json(name_file = "data_base.json")
#                 #беремо кол-во баллів користувача який запсукає сервер, щоб відправати оновлену кількість 
#                 data_points = data_base[input_nick.user_text]["points"]

#                 nickname = input_nick.user_text
#                 if check_points[0] == 1:
#                     if data_points > 0:
#                         list_users[nickname]["points"] -= 50
#                         write_json(filename = "data_base.json" , object_dict = list_users)
         
#         # аналогічно клієнту, але логіка перевірки пов'язана з win_server та lose_server
#         elif list_player_role[0] == "server_player":
#             if list_check_win[0] == "win_server":
#                 win_lose_text.text = dict_save_information["player_nick"] + " won"
#                 win_lose_text.draw_font()
#                 # відмальовка ників та балів
#                 player_nick.text = dict_save_information["player_nick"]
#                 player_nick.size = 52
#                 player_nick.x_cor = 970
#                 player_nick.y_cor = 450
#                 player_points.text = str(dict_save_information["player_points"] + 100)
#                 player_points.size = 52
#                 player_points.x_cor = 980
#                 player_points.y_cor = 531
#                 enemy_nick.text = dict_save_information["enemy_nick"]
#                 enemy_nick.size = 52
#                 enemy_nick.x_cor = 200
#                 enemy_nick.y_cor = 450
                
#                 if dict_save_information["enemy_points"] == 0:
#                     enemy_points.text = str(dict_save_information["enemy_points"])
#                 else:
#                     enemy_points.text = str(dict_save_information["enemy_points"] - 50)
#                 enemy_points.size = 52
#                 enemy_points.x_cor = 240
#                 enemy_points.y_cor = 531
                

#                 nickname = input_nick.user_text
#                 if check_points[0] == 1:
#                     list_users[nickname]["points"] += 100
#                     write_json(filename = "data_base.json" , object_dict = list_users)
#             else:
#                 win_lose_text.text = dict_save_information["player_nick"] + " Lost"
#                 win_lose_text.draw_font()
#                 # відмальовка ників та балів
#                 player_nick.text = dict_save_information["player_nick"]
#                 player_nick.size = 52
#                 player_nick.x_cor = 200
#                 player_nick.y_cor = 450
                
#                 if dict_save_information["player_points"] == 0:
#                     player_points.text = str(dict_save_information["player_points"])
#                 else:
#                     player_points.text = str(dict_save_information["player_points"] - 50)
#                 player_points.size = 52
#                 player_points.x_cor = 220
#                 player_points.y_cor = 531
                

#                 enemy_nick.text = dict_save_information["enemy_nick"]
#                 enemy_nick.size = 52
#                 enemy_nick.x_cor = 970
#                 enemy_nick.y_cor = 450
            

#                 enemy_points.text = str(dict_save_information["enemy_points"] + 100)
#                 enemy_points.size = 52
#                 enemy_points.x_cor = 980
#                 enemy_points.y_cor = 531
               

#                 data_base = read_json(name_file = "data_base.json")
#                 #беремо кол-во баллів користувача який запсукає сервер, щоб відправати оновлену кількість 
#                 data_points = data_base[input_nick.user_text]["points"]

#                 nickname = input_nick.user_text
#                 if check_points[0] == 1:
#                     if data_points > 0:
#                         list_users[nickname]["points"] -= 50
#                         write_json(filename = "data_base.json" , object_dict = list_users)

    

#         # Малювання елементів
#         finish_bg.draw_image(screen=module_screen.main_screen)
#         end_game_image.draw_image(screen=module_screen.main_screen)
#         new_year_cap.draw_image(screen=module_screen.main_screen)
#         shadow_text.draw_image(screen=module_screen.main_screen)
#         win_background.draw_image(screen=module_screen.main_screen)
#         defeat_background.draw_image(screen=module_screen.main_screen)

#         win_lose_text.update_text()
#         win_lose_text.draw_font()

#         player_nick.update_text()
#         player_nick.draw_font()

#         enemy_nick.update_text()
#         enemy_nick.draw_font()

#         player_points.update_text()
#         player_points.draw_font()

#         enemy_points.update_text()
#         enemy_points.draw_font()

#         restart_button.draw(surface = module_screen.main_screen)
#         list_check_win[0] = None
#         list_player_role[0] = ""
#         SERVER.START_CONNECT = False
#         input_nick.user_text = input_nick.base_text
#         input_ip_adress.user_text = input_ip_adress.base_text
#         input_password.user_text = input_password.base_text
#         input_port.user_text = input_port.base_text
#         save_data_posistion_ships[0] = "start"
#         check_can_connect_to_fight[0] = 0
#         check_can_connect_to_fight[1] = False
#         check_can_connect_to_fight[2] = False

#         check_start_connect[0] = False
#         check_start_connect[1] = False
#         check_start_connect[2] = False

#         check_connection_users[0] = False
#         check_connection_users[1] = False

#         list_check_ready_to_fight[0] = None
#         once_play_music[0] = 0
#         clear_json_data = {
#             "status": "places"
#         }
#         write_json(
#             filename = "status_connect_game.json",
#             object_dict = clear_json_data
#         )
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run_game = False
#                 change_scene("END GAME")
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 restart_button.check_click(event = event)
#         if leave_game[0] == True:
#             run_game = False
#         pygame.display.flip()


import pygame, sys
import modules.game_windows as game_windows
import modules.screens.screen as module_screen
from ...classes.class_image import DrawImage
from ...classes.class_text import Font
from ...classes import input_nick, input_ip_adress, input_port, input_password
from ...client import dict_save_information
from ...server import list_player_role, list_check_win
from ..change_window import change_scene
from ...json_functions import read_json, write_json, list_users
from ...game_tools import apply_fade_effect
from ...classes import Button
import modules.server as server_module
import modules.shop.shop_button as shop_button_module
from ...json_functions import write_json
from ...server import list_check_win, SERVER, list_check_ready_to_fight
from ...client import check_can_connect_to_fight, check_start_connect, save_data_posistion_ships, check_connection_users, list_check_need_send, list_check_connection, data_player_shot, connection, your_turn
from ..main_frame import once_play_music
from ...shop import money_list, player_balance
import modules.game_tools as game_tools_module
import modules.shop.tasks as tasks_module
import modules.achievement as achievement_module
from ...shop.text_shop import change_tasks
from ...shop.shop_image import done_task_one, done_task_two, done_task_three, done_task_four
import modules.game_windows.fight_frame.window_fight as window_fight_frame
from ...classes.animation import animation_random_player
from ..fight_frame.window_fight import enemy_before_choice, player_before_choice, count_sound_time
from ...classes.class_medal import player_medal, enemy_medals

leave_game = [False]
def back_to_main():
    apply_fade_effect(screen = module_screen.main_screen)
    change_scene(game_windows.main_window)
    leave_game[0] = True

#Button
restart_button = Button(x = 436, y = 700, image_path = "restart_game_button.png", image_hover_path = "restart_game_button_hover.png", width = 436, height = 68, action = back_to_main)

# Images
finish_bg = DrawImage(width=1280, height=832, x_cor=0, y_cor=0, folder_name="backgrounds", image_name="win_game_bg.png")
end_game_image = DrawImage(width=606, height=131, x_cor=337, y_cor=80, folder_name="decorations", image_name="end_game.png")
new_year_cap = DrawImage(width=133, height=133, x_cor=331, y_cor=80, folder_name="decorations", image_name="new_year_cap.png")
shadow_text = DrawImage(width=816, height=150, x_cor=233, y_cor=255, folder_name="decorations", image_name="shadow_text.png")
win_background = DrawImage(width=315, height=199, x_cor=97, y_cor=416, folder_name="backgrounds", image_name="result_game_bg.png")
defeat_background = DrawImage(width=315, height=199, x_cor=860, y_cor=416, folder_name="backgrounds", image_name="result_game_bg.png")

# Fonts
win_lose_text = Font(size=96, name_font="Goldman_Bold.ttf", text="", screen=module_screen.main_screen, x_cor = 383, y_cor = 248, text_color="White")
player_nick = Font(size=48, name_font="Jersey15.ttf", text=dict_save_information["player_nick"], screen=module_screen.main_screen, x_cor=914, y_cor=126, text_color="White")
enemy_nick = Font(size=48, name_font="Jersey15.ttf", text=dict_save_information["enemy_nick"], screen=module_screen.main_screen, x_cor=437, y_cor=126, text_color="White")
player_points = Font(size=48, name_font="Jersey15.ttf", text=str(dict_save_information["player_points"]), screen=module_screen.main_screen, x_cor=743, y_cor=126, text_color="White")
enemy_points = Font(size=48, name_font="Jersey15.ttf", text=str(dict_save_information["enemy_points"]), screen=module_screen.main_screen, x_cor=270, y_cor=126, text_color="White")

# Лист для уникнення багаторазового оновлення балів
check_points = [0]

def finish_window():
    pygame.display.set_caption("Finish Window")
    run_game = True
    if SERVER.START_CONNECT == True:
        SERVER.server_socket.close()
    SERVER.run = False
    SERVER.clients = 0
    SERVER.START_CONNECT = False
    SERVER.RESTART = False
    SERVER.PORT = 0
    while run_game:
        module_screen.FPS.tick(60)
        module_screen.main_screen.fill((0, 0, 0))  # Очищення екрану чорним фоном

        if list_player_role[0] == "client_player":
            #якщо клієнт виграв, відображається повідомлення про перемогу, бали гравця збільшуються на 100
            if list_check_win[0] == "win_client":
                win_lose_text.text = dict_save_information["player_nick"] + " won"
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
                enemy_nick.text = dict_save_information["enemy_nick"]
                enemy_nick.size = 52
                enemy_nick.x_cor = 200
                enemy_nick.y_cor = 450
                if dict_save_information["enemy_points"] == 0:
                    enemy_points.text = str(dict_save_information["enemy_points"])
                else:
                    enemy_points.text = str(dict_save_information["enemy_points"] - 50)
                enemy_points.size = 52
                enemy_points.x_cor = 240
                enemy_points.y_cor = 531

                nickname = input_nick.user_text
                if check_points[0] == 1:
                    list_users[nickname]["points"] += 100
                    write_json(filename = "data_base.json" , object_dict = list_users)
            # якщо клієнт програв, його бали зменшуються на 50 (якщо вони більше 0)
            else:
                win_lose_text.text = dict_save_information["player_nick"] + " Lost"

                # відмальовка ників та балів
                player_nick.text = dict_save_information["player_nick"]
                player_nick.size = 52
                player_nick.x_cor = 200
                player_nick.y_cor = 450
                if dict_save_information["player_points"] == 0:
                    player_points.text = str(dict_save_information["player_points"])
                else:
                    player_points.text = str(dict_save_information["player_points"] - 50)
                player_points.size = 52
                player_points.x_cor = 220
                player_points.y_cor = 531

                enemy_nick.text = dict_save_information["enemy_nick"]
                enemy_nick.size = 52
                enemy_nick.x_cor = 970
                enemy_nick.y_cor = 450

                enemy_points.text = str(dict_save_information["enemy_points"] + 100)
                enemy_points.size = 52
                enemy_points.x_cor = 980
                enemy_points.y_cor = 531

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
                player_points.text = str(dict_save_information["player_points"] + 100)
                player_points.size = 52
                player_points.x_cor = 980
                player_points.y_cor = 531
                enemy_nick.text = dict_save_information["enemy_nick"]
                enemy_nick.size = 52
                enemy_nick.x_cor = 200
                enemy_nick.y_cor = 450
                
                if dict_save_information["enemy_points"] == 0:
                    enemy_points.text = str(dict_save_information["enemy_points"])
                else:
                    enemy_points.text = str(dict_save_information["enemy_points"] - 50)
                enemy_points.size = 52
                enemy_points.x_cor = 240
                enemy_points.y_cor = 531
                

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
                
                if dict_save_information["player_points"] == 0:
                    player_points.text = str(dict_save_information["player_points"])
                else:
                    player_points.text = str(dict_save_information["player_points"] - 50)
                player_points.size = 52
                player_points.x_cor = 220
                player_points.y_cor = 531
                

                enemy_nick.text = dict_save_information["enemy_nick"]
                enemy_nick.size = 52
                enemy_nick.x_cor = 970
                enemy_nick.y_cor = 450
            

                enemy_points.text = str(dict_save_information["enemy_points"] + 100)
                enemy_points.size = 52
                enemy_points.x_cor = 980
                enemy_points.y_cor = 531
               

                data_base = read_json(name_file = "data_base.json")
                #беремо кол-во баллів користувача який запсукає сервер, щоб відправати оновлену кількість 
                data_points = data_base[input_nick.user_text]["points"]

                nickname = input_nick.user_text
                if check_points[0] == 1:
                    if data_points > 0:
                        list_users[nickname]["points"] -= 50
                        write_json(filename = "data_base.json" , object_dict = list_users)

    

        # Малювання елементів
        finish_bg.draw_image(screen=module_screen.main_screen)
        end_game_image.draw_image(screen=module_screen.main_screen)
        new_year_cap.draw_image(screen=module_screen.main_screen)
        shadow_text.draw_image(screen=module_screen.main_screen)
        win_background.draw_image(screen=module_screen.main_screen)
        defeat_background.draw_image(screen=module_screen.main_screen)

        win_lose_text.update_text()
        win_lose_text.draw_font()

        player_nick.update_text()
        player_nick.draw_font()

        enemy_nick.update_text()
        enemy_nick.draw_font()

        player_points.update_text()
        player_points.draw_font()

        enemy_points.update_text()
        enemy_points.draw_font()

        restart_button.draw(surface = module_screen.main_screen)
        list_check_win[0] = None
        list_player_role[0] = ""
        input_nick.user_text = input_nick.base_text
        input_ip_adress.user_text = input_ip_adress.base_text
        input_password.user_text = input_password.base_text
        input_port.user_text = input_port.base_text
        save_data_posistion_ships[0] = "start"
        check_can_connect_to_fight[0] = 0
        check_can_connect_to_fight[1] = False
        check_can_connect_to_fight[2] = False

        check_start_connect[0] = False
        check_start_connect[1] = False
        check_start_connect[2] = False

        check_connection_users[0] = False
        check_connection_users[1] = False

        list_check_ready_to_fight[0] = None
        once_play_music[0] = 0
        clear_json_data = {
            "status": "places"
        }
        write_json(
            filename = "status_connect_game.json",
            object_dict = clear_json_data
        )
        count_sound_time[0] = 0
        check_points[0] = 0
        leave_game[0] = False
        server_module.enemy_data[0] = ""
        #где стоят корабли соперника
        # server_module.enemy_ships.clear()
        # для восстановления клеточки
        server_module.number_list[0] = 100
        server_module.row_list[0] = 100
        server_module.col_list[0] = 100
        # список для проверки перехода на фрейм боя
        server_module.list_check_ready_to_fight[0] = None
        # лист очереди
        server_module.turn[0] = "server_turn"
        server_module.turn[1] = False
        # лист таймер времени
        server_module.check_time[0] = 0 
        # Лист для проверки за кого мы играем(сервер или клиент)
        # список куда сохраняем кто выиграл
        server_module.list_check_win[0] = None
        # список где сохраняем баланс врага
        server_module.enemy_balance[0] = 0
        # сохраняем координаты вражеских медалей
        server_module.save_medals_coordinates.clear()
        # список в котором храним какие корабли убили у игрока
        server_module.player_died_ships.clear()
        # список в коотором храним какие корабли убил игрок у врага
        server_module.enemy_died_ships.clear()
        #------------------------------------------------------------------------------------------------
        server_module.flag_bomb_animation[0] = False
        #------------------------------------------------------------------------------------------------
        # флаг в котором храним все ли впорядке с связью между игроками
        server_module.check_connection[0] = True
        list_check_connection[0] = False
        list_check_need_send[0] = False
        connection[0] = True
        data_player_shot.clear()
        your_turn[0] = 0
        shop_button_module.waste_money[0] = 0
        shop_button_module.flag_arson[0] = "no"
        shop_button_module.flag_put_out_the_fire[0] = "no"
        shop_button_module.check_buy_bomb_attack[0] = False
        shop_button_module.flagbimb200[0] = "no"
        shop_button_module.but_flag[0] = False
        shop_button_module.flag_radar[0] = False
        shop_button_module.random_hits[0] = False
        money_list[0] = 0
        change_tasks()
        tasks_module.check_completed_tasks[0] = 0
        tasks_module.our_ships_2decker[0] = 0
        tasks_module.enemy_ships_2decker[0] = 0
        tasks_module.count_shot[0] = 0
        tasks_module.count_turns[0] = 0
        tasks_module.save_sevens.clear()
        tasks_module.four_hits_in_a_row.clear()
        tasks_module.single_ships.clear()
        tasks_module.check_killed_for_single_ships.clear()
        tasks_module.start_index_single.clear()
        tasks_module.check_three_2decker_ship_in_row.clear()
        tasks_module.check_killed_for_double_ships.clear()
        tasks_module.start_index_two[0] = 0
        tasks_module.our_ships_3decker[0] = 0
        tasks_module.enemy_ships_3decker[0] = 0
        tasks_module.our_ships_4decker[0] = 0
        tasks_module.enemy_ships_4decker[0] = 0
        tasks_module.kill_three_deckcer_ship[0] = 0
        tasks_module.ship_hits.clear()
        tasks_module.kill_count[0] = 0
        tasks_module.count_zero[0] = 0
        tasks_module.egight_hits_in_a_row.clear()
        tasks_module.two_hits_in_a_row.clear()
        tasks_module.three_hits_in_a_row.clear()
        tasks_module.ship_hits_three.clear()
        tasks_module.count_zero_thrible[0] = 0
        tasks_module.count_kill_three[0] = 0
        tasks_module.count_three_ships.clear()
        tasks_module.check_killed_for_three_ships.clear()
        tasks_module.start_index[0] = 0

        achievement_module.list_hits_achiv.clear()
        achievement_module.index_killed_ships[0] = 0
        achievement_module.killed_ships[0] = ""
        achievement_module.count_shot[0] = 0
        achievement_module.shoots.clear()
        achievement_module.list_save_coords_achiv[0] = False
        achievement_module.player_died_ships_for_achiv[0] = ""
        achievement_module.enemy_dies_ships_for_ahiv[0] = ""
        achievement_module.our_ships_4decker_achiv[0] = ""
        achievement_module.enemy_ships_4decker_achiv[0] = ""
        achievement_module.single_ships_achiv.clear
        achievement_module.check_killed_for_single_ships_achiv.clear()
        achievement_module.start_index_single_achiv[0] = 0
        achievement_module.player_ships[0] = 0
        achievement_module.enemy_ships[0] = 0  
        achievement_module.count_player_ships_achiv[0] = 0
        achievement_module.count_enemy_kill_achiv[0] = 0
        achievement_module.count_turns_achiv[0] = 0
        achievement_module.save_sevens_achiv.clear()
        achievement_module.check_end_game[0] = 0
        achievement_module.shoots.clear()
        done_task_one.VISIBLE = 0
        done_task_two.VISIBLE = 0
        done_task_three.VISIBLE = 0
        done_task_four.VISIBLE = 0

        window_fight_frame.Cordi_Burning_Ship.clear()
        window_fight_frame.fire_extinguisher[0] = "no"
        window_fight_frame.number_of_ship_sonfire[0] = 0
        window_fight_frame.pozhar_row.clear()
        window_fight_frame.pozhar_col.clear()
        window_fight_frame.list_check_shop[0] = None
        window_fight_frame.screen_shake[0] = 0
        window_fight_frame.list_fire.clear()
        window_fight_frame.row_fire_col_anim.clear()
        window_fight_frame.col_fire_row_anim.clear()
        window_fight_frame.list_already_fire_cells.clear()
        window_fight_frame.first_shot_fire.clear()
        window_fight_frame.enemy_col_fire.clear()
        window_fight_frame.enemy_row_fire.clear()
        window_fight_frame.enemy_list_fire.clear()
        window_fight_frame.enemy_check_fire[0] = 0
        window_fight_frame.count_hit_auto_rocket[0] = 0
        window_fight_frame.fire_fighter_anim[0] = False
        window_fight_frame.health_anim[0] = False
        window_fight_frame.x_enemy_cross[0] = 0
        window_fight_frame.y_enemy_cross[0] = 0
        window_fight_frame.flag_miss_rocket_animation[0] = ""
        window_fight_frame.check_animation_miss_cell[0] = ""
        window_fight_frame.check_animation_miss_cell[0] = "" 
        window_fight_frame.radar_flag[0] = ""
        window_fight_frame.radar_flag[1] = 0
        window_fight_frame.check_animation[0] = ""
        window_fight_frame.check_cross_animation[0] = ""
        window_fight_frame.x_hit_the_ship[0] = 0
        window_fight_frame.y_hit_the_ship[0] = 0
        window_fight_frame.list_cross_player.clear()
        window_fight_frame.check_achiv[0] = False
        window_fight_frame.index_achiv[0] = 100
        window_fight_frame.numberofbim[0] = ""
        window_fight_frame.activate_auto_rocket[0] = False
        window_fight_frame.activate_restore_cell[0] = False
        window_fight_frame.activate_bomb[0] = False
        window_fight_frame.activate_radar[0] = False
        window_fight_frame.activate_fire_rocket[0] = False
        window_fight_frame.activate_fire_fighter[0] = False
        window_fight_frame.activate_random_hits[0] = False
        window_fight_frame.count_5[0] = 0
        window_fight_frame.old_killed_ships[0] = False
        window_fight_frame.new_killed_ships[0] = False
        window_fight_frame.check_bomb[0] = False
        window_fight_frame.count_sound_time[0] = False
        window_fight_frame.check_player_balance[0] = 0
        window_fight_frame.check_player_balance[0] = False
        window_fight_frame.check_alive_ten[0] = False
        window_fight_frame.check_alive_five[0] = False
        window_fight_frame.check_target_attack[0] = "None"
        window_fight_frame.our_miss_anim.clear()
        window_fight_frame.list_cross.clear()
        game_tools_module.miss_row_enemy[0] = 0
        game_tools_module.miss_col_enemy[0] = 0
        game_tools_module.list_direction_enemy[0] = ""
        game_tools_module.check_number_cell_enemy.clear()
        game_tools_module.check_kill_enemy[0] = False
        game_tools_module.count_len_enemy[0] = 1
        game_tools_module.count_five_around[0] = 0
        game_tools_module.check_money_two_hits_in_row[0] = 0
        game_tools_module.check_money_four_hits_in_row[0] = 0
        game_tools_module.check_kill_one_3deck[0] = 0
        game_tools_module.check_money_two_kill_in_a_row[0] = 0
        game_tools_module.check_2_kills_3deck_in_row[0] = 0
        game_tools_module.check_kill_first_four_deck[0] = 0
        game_tools_module.check_kill_four_1decker_in_row[0] = 0
        game_tools_module.check_kill_in_first_shot[0] = 0
        game_tools_module.check_kept_alive_for_5_turns[0] = 0
        game_tools_module.check_kill_three_ships_in_row[0] = 0
        game_tools_module.check_completed_three_tasks[0] = 0
        game_tools_module.check_money_three_hits_in_row[0] = 0
        game_tools_module.check_first_kill_three_3dec[0] = 0
        game_tools_module.check_money_eight_hits_in_row[0] = 0
        game_tools_module.check_three_2decker_ship_in_row[0] = 0
        game_tools_module.check_first_kill_twodecker[0] = 0
        game_tools_module.count_money_hit[0] = 0
        game_tools_module.check_money_bomb[0] = 0
        game_tools_module.check_money_restoration[0] = 0
        game_tools_module.check_money_auto_rocket[0] = 0
        game_tools_module.check_but_radar[0] = 0
        game_tools_module.buy_random_hit[0] = 0
        game_tools_module.buy_fire_rocket[0] = 0
        game_tools_module.buy_fire_fighter[0] = 0
        game_tools_module.miss_row[0] = 0
        game_tools_module.miss_col[0] = 0
        game_tools_module.list_direction[0] = ""
        game_tools_module.check_number_cell.clear()
        game_tools_module.check_kill[0] = False
        game_tools_module.count_len[0] = 1
        game_tools_module.list_animation_miss.clear()
        game_tools_module.count_fives[0] = 0
        animation_random_player.clear_animation()
        animation_random_player.ANIMATION_SPEED = 6
        enemy_before_choice.visible = 255
        player_before_choice.visible = 255
        player_balance.update_text()
        game_tools_module.player_balance_in_jar.update_text()
        game_tools_module.enemy_balance_in_jar.update_text()

        for medal in player_medal:
            medal.VISIBLE = 100
            medal.ACTIVE = False
        for enm_medal in enemy_medals:
            enm_medal.VISIBLE = 100
            enm_medal.ACTIVE = False
        print("UBANAYA OTCHISTKA IDI NAHUI")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                change_scene("END GAME")
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                restart_button.check_click(event = event)
        if leave_game[0] == True:
            run_game = False
            break
        pygame.display.flip()
