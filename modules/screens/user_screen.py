#імпортуємо модуль для створення ігор
import pygame


#встановлюємо розмір екрану
SCREEN_WIDTH = 1280
SCREEN_HEIGH = 832


#встановлюємо FPS для оновлення екрану
FPS = pygame.time.Clock()
#створюємо екран для користувача який прижднується до серверу, та встановлюємо для цього екрану розміри
screen_user = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGH))


