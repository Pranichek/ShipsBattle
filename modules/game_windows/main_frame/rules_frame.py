import pygame
import modules.game_windows as game_windows
import modules.screens.screen as module_screen
import modules.server as server_module
from ...screens import main_screen
from ...classes.class_image import DrawImage
from ...classes.class_button import Button
from ..change_window import change_scene
from ..button_pressed import button_action, check_press_button

#картинки
rules_bg = DrawImage(width = 1280,height = 832 , x_cor = 0 , y_cor = 0 ,folder_name= "backgrounds" , image_name= "rules_bg.png")

#кнопка кторая перекидывает на фрейм по созданию игры(запуска сервера)
back_window = Button(x= 32, y = 34,image_path= "back_button.png" , image_hover_path= "back_button_hover.png" , width= 138 , height = 40.98 , action = button_action)


#створюємо функцію 
def rules_window():
    pygame.display.set_caption("Rules_frame")    
    
    run_game = True
    
    while run_game:
        print("4444444444444444444444444444")
        module_screen.FPS.tick(60)
        mouse_x , mouse_y = pygame.mouse.get_pos()
        rules_bg.draw_image(screen= main_screen)
        
        back_window.draw(surface = main_screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False  
                change_scene(None)
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                back_window.check_click(event = event)
                
            elif check_press_button[0] == "button is pressed":
                x_pos , y_pos = pygame.mouse.get_pos()
                check_press_button[0] = None 
                run_game = False
                if x_pos >= back_window.x:
                    if x_pos <= back_window.x + back_window.width:
                        if y_pos >= back_window.y:
                            if y_pos <= back_window.y + back_window.height:
                                print("back_menu")
                                change_scene(game_windows.main_window())
        pygame.display.flip()
                
        