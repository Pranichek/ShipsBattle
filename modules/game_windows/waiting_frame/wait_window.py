import pygame
from ..fight_frame import fight_window
from ..ships_position_frame import ships_position_window
import modules.screens.screen as module_screen
import modules.game_windows as game_windows
from ...screens import main_screen
from ...classes.class_music import music_load_main, music_load_waiting
from ...classes.class_image import DrawImage
from ..change_window import change_scene
from ..button_pressed import button_action, check_press_button
from ...json_functions import read_json
from ...game_tools import apply_fade_effect
from ...client import check_connection_users, check_can_connect_to_fight, save_data_posistion_ships, connection
from ...volume_settings import volume_down_button, volume_up_button, off_sound_button
from ...classes.class_click import all_sounds
from ...volume_settings import save_data_volume

#фон для очікування користувача
waiting_background = DrawImage(width = 1280,height = 832 , x_cor= 0 , y_cor = 0 ,folder_name= "backgrounds" , image_name= "waiting_background.png")

def waiting_window():
    print("Зашло")
    pygame.display.set_caption("Waiting window")
    run_game = True
    music_load_main.stop()
    music_load_waiting.play()

    for song in all_sounds:
        song.set_volume(save_data_volume[0])
        pygame.mixer.music.set_volume(save_data_volume[0])

    volume_down_button.x = 1096
    volume_down_button.y = 26
    volume_up_button.x = 1004
    volume_up_button.y = 26
    off_sound_button.x = 1188
    off_sound_button.y = 26
    while run_game:
        module_screen.FPS.tick(60)
        waiting_background.draw_image(screen = main_screen)

        volume_up_button.draw(surface = main_screen)
        volume_down_button.draw(surface = main_screen)
        off_sound_button.draw(surface = main_screen)
        if check_can_connect_to_fight[2] == 'True':
            check_connection_users[0] = "fight"
            apply_fade_effect(screen = main_screen)
            change_scene(fight_window())
            run_game = False
            check_press_button[0] = None

        if check_connection_users[0] != False and save_data_posistion_ships[0]=="":
            apply_fade_effect(screen = module_screen.main_screen)
            change_scene(ships_position_window())
            check_press_button[0] = None
            run_game = False

        if connection[0] == False:
            game_windows.fight_frame.reonnect_image.draw_image(screen = main_screen)
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False  
                change_scene("END GAME")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                volume_up_button.check_click(event = event)
                volume_down_button.check_click(event = event)
                off_sound_button.check_click(event = event)
                 
        pygame.display.flip()