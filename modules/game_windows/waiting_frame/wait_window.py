import pygame
from ..fight_frame import fight_window
from ..ships_position_frame import ships_position_window
import modules.screens.screen as module_screen
import modules.server as server_module
from ...screens import main_screen
from ...classes.class_music import music_load_main, music_load_waiting
from ...classes.class_image import DrawImage
from ..change_window import change_scene, list_current_scene
from ..button_pressed import button_action, check_press_button
from ...json_functions import read_json
from ...game_tools import apply_fade_effect
from ...client import check_connection_users, check_can_connect_to_fight

#фон для очікування користувача
waiting_background = DrawImage(width = 1280,height = 832 , x_cor= 0 , y_cor = 0 ,folder_name= "backgrounds" , image_name= "waiting_background.png")

def waiting_window():
    print("Зашло")
    pygame.display.set_caption("Waiting window")
    run_game = True
    music_load_main.stop()
    music_load_waiting.play()
    while run_game:
        module_screen.FPS.tick(60)
        waiting_background.draw_image(screen = main_screen)
        data_ready = read_json(name_file = "status_connect_game.json")
        status_ready_to_game = data_ready["status"] 

   
        if check_can_connect_to_fight[0] >= 3:
            check_connection_users[0] = "fight"
            apply_fade_effect(screen = main_screen)
            print(311131113111311131131)
            change_scene(fight_window())
            run_game = False
            check_press_button[0] = None
            break

            
        if check_connection_users[0] != False and status_ready_to_game == "places ships":
            apply_fade_effect(screen = module_screen.main_screen)
            print(1111111111111111111111)
            change_scene(ships_position_window())
            check_press_button[0] = None
            run_game = False
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False  
                change_scene(None)
                 
        pygame.display.flip()