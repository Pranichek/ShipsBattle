import pygame
import modules.game_windows as game_windows
import modules.screens.screen as module_screen
import modules.server as server_module
from ...screens import main_screen
from ...classes.class_music import music_load_main
from ...classes.class_image import DrawImage
from ...classes.class_button import Button
from ..change_window import change_scene
from ..button_pressed import button_action, check_press_button


#картинки
main_bg = DrawImage(width = 1280,height = 832 , x_cor = 0 , y_cor = 0 ,folder_name= "backgrounds" , image_name= "main_background.png")
cold_image = DrawImage(width= 152 , height= 68 , x_cor= 207 , y_cor= 716 , folder_name= "decorations" , image_name= "ice.png")
second_cold_image = DrawImage(width= 152 , height= 68 , x_cor= 940, y_cor= 716 , folder_name= "decorations" , image_name= "ice.png")

# кнопки
#кнопка кторая перекидывает на фрейм по созданию игры(запуска сервера)
create_game_frame = Button(x= 113, y = 653,image_path= "button_create.png" , image_hover_path= "create_button_hover.png" , width= 346 , height = 80 , action = button_action)
#кнопка кторая перекидывает на фрейм по присоеденению к игре(серверу)
join_game_frame = Button(x= 832 , y = 653,image_path= "join_button.png" , image_hover_path= "join_button_hover.png" , width= 346 , height = 80 , action = button_action)
# список для того чтобы гланая музыка играла тоьлко один раз
once_play_music = [0]


#створюємо функцію, яка викликається при запуску гри для користувача який запускає сервер
def main_window():
    pygame.display.set_caption("BattleShips")
    server_module.list_check_ready_to_fight[0] = None
    #викликаємо функцію для запуску серверу
    #встановлюємо назву вікна гри для сервера
    #створюжмо змінну для того щоб відстежувати коли треба закривати вікно
    run_game = True
    if once_play_music[0] < 1:
        music_load_main.play()

    once_play_music[0] += 1

    while run_game:
        module_screen.FPS.tick(60)
        mouse_x , mouse_y = pygame.mouse.get_pos()
        main_bg.draw_image(screen= main_screen)

        cold_image.draw_image(screen= main_screen)  
        create_game_frame.draw(surface= main_screen)
        second_cold_image.draw_image(screen= main_screen)
        join_game_frame.draw(surface= main_screen)        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False  
                change_scene(None)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                create_game_frame.check_click(event = event)
                join_game_frame.check_click(event = event)

                
            elif check_press_button[0] == "button is pressed":
                x_pos , y_pos = pygame.mouse.get_pos()
                check_press_button[0] = None 
                run_game = False
                if x_pos >= join_game_frame.x:
                    if x_pos <= join_game_frame.x + join_game_frame.width:
                        if y_pos >= join_game_frame.y:
                            if y_pos <= join_game_frame.y + join_game_frame.height:
                                print("Join windo")
                                change_scene(game_windows.join_game_window())
                elif x_pos >= create_game_frame.x:
                    if x_pos <= create_game_frame.x + create_game_frame.width:
                        if y_pos >= create_game_frame.y:
                            if y_pos <= create_game_frame.y + create_game_frame.height:
                                print("Create window")
                                change_scene(game_windows.create_game_window())
        pygame.display.flip()