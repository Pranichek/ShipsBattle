import pygame, sys
import modules.screens as module_screen
from ...client import connection, check_can_connect_to_fight, check_connection_users, save_data_posistion_ships
from ..fight_frame import fight_window
import modules.game_windows as game_windows
import modules.server as server_module
from ...classes.animation import animation_connection_problem
from ...screens import grid_player, main_screen, list_object_map
from ...classes.class_music import music_load_main, music_load_waiting
from ...classes.class_ship import list_ships
from ...classes.class_image import DrawImage
from ...classes.class_button import Button
from ...game_tools import apply_fade_effect
from ..change_window import change_scene
from ...screens import list_grid, enemy_matrix
from ..button_pressed import check_press_button
from .check_placing_ships import connect_to_fight
from .random_placing import random_places_ships
from ...json_functions import read_json
from ...classes.class_click import all_sounds
from ...volume_settings import save_data_volume

#images 
ships_position_bg = DrawImage(width = 1280,height = 832 , x_cor = 0 , y_cor=  0 ,folder_name= "backgrounds" , image_name= "position_ships_bg.png")
# фон на якомй стоять кораблі перед початком бою
place_for_ships = DrawImage(width = 477 , height = 559 , x_cor = 763 , y_cor = 37 ,folder_name= "backgrounds" , image_name= "bg_place_for_ships.png")
grid_image = DrawImage(width = 662  , height = 662 , x_cor = 40 , y_cor = 37 , folder_name = "grid", image_name = "background_grid.png")

#Buttoms
ready_for_battle = Button(x= 798 , y = 626,image_path= "start_battle.png" , image_hover_path= "start_battle_hover.png" , width= 408 , height = 61 , action = connect_to_fight)
random_place_ships = Button(x= 205 , y = 709,image_path= "random_place.png" , image_hover_path= "random_place_hover.png" , width= 318 , height = 48 , action = random_places_ships)

def ships_position_window():

    music_load_waiting.stop()
    music_load_main.play()

    for song in all_sounds:
        song.set_volume(save_data_volume[0])
        pygame.mixer.music.set_volume(save_data_volume[0])
    pygame.display.set_caption("Position Ships")
    run_game = True
    #generate grid with class
    grid_player.X_SCREEN = 81
    grid_player.Y_SCREEN = 76
    grid_player.generate_grid()
    check_connect_fight = 0
    for row in range(0, len(list_grid)):
        for col in range(0, len(list_grid[row])):
            list_grid[row][col] = 0
    for row in range(0, len(enemy_matrix)):
        for col in range(0, len(enemy_matrix[row])):
            enemy_matrix[row][col] = 0
    for ship in list_ships:
        ship.X_COR = ship.STASIC_X 
        ship.Y_COR = ship.STASIC_Y
        ship.ORIENTATION_SHIP = "horizontal"
        ship.WIDTH = 62
        ship.HEIGHT = 62
        ship.CHECK_ORIENTATION = "horizontal"
        ship.load_image()
        
    while run_game:
        module_screen.FPS.tick(60)
        if save_data_posistion_ships[0] == "fight" and check_can_connect_to_fight[1] == "fight":
            if check_connection_users[1] == True:
                apply_fade_effect(screen = main_screen)
                change_scene(fight_window)
                run_game = False
                break
        elif check_can_connect_to_fight[0] != True and save_data_posistion_ships[0] == "fight" and check_connection_users[1] == True:
            apply_fade_effect(screen = main_screen)
            change_scene(game_windows.waiting_window)
            run_game = False
            break
            
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

        #----------------------------------------------------------------
        # анимация потери соеденения
        if server_module.check_connection[0] == False:
            animation_connection_problem.animation(main_screen = main_screen, count_image = 5)
            if animation_connection_problem.COUNT_IMAGES >= 4:
                animation_connection_problem.clear_animation()
        #----------------------------------------------------------------

        if connection[0] == False:
            game_windows.fight_frame.reonnect_image.draw_image(screen = main_screen)

        for event in pygame.event.get():
            for ship in list_ships:
                ship.matrix_move(event = event, matrix_width = 620, matrix_height = 620, cell = 100)
                ship.rotate_ship(event = event)

            if event.type == pygame.QUIT:
                run_game = False  
                change_scene("END GAME")
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ready_for_battle.check_click(event = event)
                random_place_ships.check_click(event = event)
                
        pygame.display.flip()