import pygame
from os.path import abspath, join

game_ico = abspath(join(__file__, "..", "..", "..", "static", "icons", "game_ico.png"))
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 832

FPS = pygame.time.Clock()
#створюємо екран для користувача який запускає сервер, та встановлюємо для цього екрану розміри
main_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_icon(pygame.image.load(game_ico))
