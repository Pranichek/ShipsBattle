import modules
import pygame

if __name__ == '__main__':
    modules.change_scene(modules.window)#передаем функцию отображения первого окна
    while modules.list_current_scene[0] is not None:
        modules.list_current_scene[0]()#вызываем функцию которая тут запущена

pygame.quit()
    
  

