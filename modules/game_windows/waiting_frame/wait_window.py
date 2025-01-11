import pygame
import modules.game_windows as game_windows
import modules.screens.screen as module_screen
import modules.server as server_module
from ...screens import main_screen
from ...classes.class_music import music_load_main, music_load_waiting
from ...classes.class_image import DrawImage
from ..change_window import change_scene
from ..button_pressed import button_action, check_press_button
from ...json_functions import read_json
from ...game_tools import apply_fade_effect

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
        try:
            data = read_json(name_file = "utility.json")
            status_server = data["status"]
        except Exception as e:
            status_server = "wait"
            continue

        if server_module.list_check_ready_to_fight[0] == "fight":
            apply_fade_effect(screen = main_screen)
            check_press_button[0] = None
            run_game = False
            change_scene(game_windows.fight_window())
            

        waiting_background.draw_image(screen = main_screen)

        if server_module.list_check_ready_to_fight[0] == None:
            if status_server == "connect":
                check_press_button[0] = None
                run_game = False
                apply_fade_effect(screen = main_screen)
                change_scene(game_windows.ships_position_window())
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False  
                change_scene(None)
                 
        pygame.display.flip()