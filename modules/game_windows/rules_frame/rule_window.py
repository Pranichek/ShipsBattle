import pygame, sys
from ...classes.class_image import DrawImage
import modules.game_windows as game_windows
from ...classes.class_button import Button
from ...screens import main_screen
from ..waiting_frame import apply_fade_effect
from ..change_window import change_scene
pygame.init()

rules = DrawImage(
    x_cor = 0,
    y_cor = 0,
    width = 1280,
    height = 832,
    folder_name = "backgrounds",
    image_name = "rules.png"
)

check_run_game = [False]
def change_on_main():
    apply_fade_effect(screen = main_screen)
    change_scene(game_windows.main_window)
    check_run_game[0] = True

back_to_main = Button(
    x = 8, 
    y = 7,
    image_path = "back_rules.png", 
    image_hover_path = "back_rules_hover.png", 
    width = 148, 
    height = 41, 
    action = change_on_main
)


def rules_window():
    pygame.display.set_caption("Rules window")
    run_game = True
    while run_game:
        rules.draw_image(screen = main_screen)
        back_to_main.draw(surface = main_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
                change_scene("END GAME")
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                back_to_main.check_click(event = event)
        if check_run_game[0] == True:
            check_run_game[0] = False
            run_game = False
        

        pygame.display.flip()