import pygame
import modules.screens as module_screen
import modules.game_windows as game_windows
import modules.server as server_module
from ...classes.animation import animation_connection_problem
from ...screens import grid_player, main_screen, list_object_map
from ...server import list_check_ready_to_fight
from ...classes.class_music import music_load_main, music_load_waiting
from ...classes.class_ship import list_ships
from ...classes.class_image import DrawImage
from ...classes.class_button import Button
from ...game_tools import apply_fade_effect
from ..change_window import change_scene
from ..button_pressed import check_press_button
from .check_placing_ships import connect_to_fight
from .random_placing import random_places_ships
from ...json_functions import read_json

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
    pygame.display.set_caption("Position Ships")
    run_game = True
    
    #generate grid with class
    grid_player.generate_grid()

    while run_game:
        module_screen.FPS.tick(60)
        data_ready = read_json(name_file = "status_connect_game.json")
        status_ready_to_game = data_ready["status"] 

        if status_ready_to_game == "fight" and server_module.list_check_ready_to_fight[0] != "fight":
            server_module.list_check_ready_to_fight[0] = "fight"
            apply_fade_effect(screen = main_screen)
            run_game = False
            change_scene(None)
            change_scene(game_windows.fight_window())
            check_press_button[0] = None
        elif status_ready_to_game == "wait window" and  server_module.list_check_ready_to_fight[0] != "wait":
            server_module.list_check_ready_to_fight[0] = "wait"
            apply_fade_effect(screen = main_screen)
            run_game = False
            change_scene(None)
            change_scene(scene = game_windows.waiting_window())
            check_press_button[0] = None

        
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

        for event in pygame.event.get():
            for ship in list_ships:
                ship.matrix_move(event = event, matrix_width = 620, matrix_height = 620, cell = 100)
                ship.rotate_ship(event = event)

            if event.type == pygame.QUIT:
                run_game = False  
                change_scene(None)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ready_for_battle.check_click(event = event)
                random_place_ships.check_click(event = event)
                
        pygame.display.flip()