import modules
import pygame
import sys


if __name__ == '__main__':
    modules.list_current_scene[0] = modules.main_window#передаем функцию отображения первого окна
    while modules.list_current_scene[0] is not None:
        modules.list_current_scene[0]()#вызываем функцию которая тут запущена
        
pygame.quit()
sys.exit()

  
print(1)
