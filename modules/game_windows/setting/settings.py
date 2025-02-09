import pygame, sys
from ...classes.class_image import DrawImage
import modules.game_windows as game_windows
from ...classes.class_button import Button
from ...screens import main_screen
from ..waiting_frame import apply_fade_effect
from ..change_window import change_scene

pygame.init()

settings_image = DrawImage(
    x_cor=0,
    y_cor=0,
    width=1280,
    height=832,
    folder_name="backgrounds",
    image_name="win_game_bg.png"
)

check_run_game = [False]

def change_on_main():
    apply_fade_effect(screen=main_screen)
    change_scene(game_windows.main_window)
    check_run_game[0] = True

def change_cursor(path_to_cursor: str = None): 
    if path_to_cursor:
        cursor_image = pygame.image.load(path_to_cursor)  
        cursor_image = pygame.transform.scale(cursor_image, (32, 32))  
        cursor_data = pygame.cursors.Cursor((0, 0), cursor_image)
        pygame.mouse.set_cursor(cursor_data)
    else:
        pygame.mouse.set_visible(False) 
        pygame.mouse.set_cursor(pygame.cursors.diamond)
        pygame.mouse.set_visible(True) 

back_to_main = Button(
    x=0, 
    y=7,
    image_path="back_rules.png", 
    image_hover_path="back_rules_hover.png", 
    width=50, 
    height=51, 
    action=change_on_main
)

change_cursor_button = Button(
    x=50, 
    y=50,
    image_path="button_volue_up.png", 
    image_hover_path="button_volue_up_hover.png", 
    width=148, 
    height=41, 
    action=lambda: change_cursor("3771695.png")
)

def settings():
    pygame.display.set_caption("Settings window")
    run_game = True
    while run_game:
        settings_image.draw_image(screen=main_screen)
        back_to_main.draw(surface=main_screen)
        change_cursor_button.draw(surface=main_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                change_scene("END GAME")
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                back_to_main.check_click(event=event)
                change_cursor_button.check_click(event=event)

        if check_run_game[0]:
            check_run_game[0] = False
            run_game = False

        pygame.display.flip()
