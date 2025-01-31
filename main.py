import modules
import pygame
import sys


if __name__ == '__main__':
    modules.list_current_scene[0] = modules.main_window#передаем функцию отображения первого окна
    while modules.list_current_scene[0] != None:
        modules.list_current_scene[0]()#вызываем функцию которая тут запущен
    print("None")
pygame.quit()
sys.exit()

