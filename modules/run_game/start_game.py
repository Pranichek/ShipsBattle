import pygame
from ..screens import screen , screen_name , Button
import modules.screens.server_screen as module_screen_server
from ..server import start_server 
import sys
import os


pygame.init()



def server_window():
    start_server()

    start = True
    while start:
        module_screen_server.FPS.tick(60)
        module_screen_server.screen.fill((255, 0 , 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        


                





        
        


