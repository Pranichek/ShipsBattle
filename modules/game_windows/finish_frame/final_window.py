import pygame
import modules.game_windows as game_windows
import modules.screens.screen as module_screen
from ...classes.class_image import DrawImage
from ...classes.class_text import Font
from ...classes import input_nick
from ...server import list_player_role, list_check_win, dict_save_information
from ..change_window import change_scene
from ...json_functions import read_json, write_json, list_users

# Images
finish_bg = DrawImage(width=1280, height=832, x_cor=0, y_cor=0, folder_name="backgrounds", image_name="win_game_bg.png")
end_game_image = DrawImage(width=606, height=131, x_cor=337, y_cor=80, folder_name="decorations", image_name="end_game.png")
new_year_cap = DrawImage(width=133, height=133, x_cor=331, y_cor=80, folder_name="decorations", image_name="new_year_cap.png")
shadow_text = DrawImage(width=816, height=150, x_cor=233, y_cor=255, folder_name="decorations", image_name="shadow_text.png")
win_background = DrawImage(width=315, height=199, x_cor=97, y_cor=416, folder_name="backgrounds", image_name="result_game_bg.png")
defeat_background = DrawImage(width=315, height=199, x_cor=860, y_cor=416, folder_name="backgrounds", image_name="result_game_bg.png")

# Fonts
win_lose_text = Font(size=96, name_font="Goldman_Bold.ttf", text="", screen=module_screen.main_screen, x_cor=383, y_cor=248, text_color="White")
player_nick = Font(size=48, name_font="Jersey15.ttf", text=dict_save_information["player_nick"], screen=module_screen.main_screen, x_cor=914, y_cor=126, text_color="White")
enemy_nick = Font(size=48, name_font="Jersey15.ttf", text=dict_save_information["enemy_nick"], screen=module_screen.main_screen, x_cor=437, y_cor=126, text_color="White")
player_points = Font(size=48, name_font="Jersey15.ttf", text=str(dict_save_information["player_points"]), screen=module_screen.main_screen, x_cor=743, y_cor=126, text_color="White")
enemy_points = Font(size=48, name_font="Jersey15.ttf", text=str(dict_save_information["enemy_points"]), screen=module_screen.main_screen, x_cor=270, y_cor=126, text_color="White")

# Лист для уникнення багаторазового оновлення балів
check_points = [0]

def finish_window():
    pygame.display.set_caption("Finish Window")
    run_game = True
    check_points[0] = 0

    while run_game:
        module_screen.FPS.tick(60)
        module_screen.main_screen.fill((0, 0, 0))  # Очищення екрану чорним фоном

        if list_player_role[0] == "player_client":
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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                change_scene(None)

        pygame.display.flip()
