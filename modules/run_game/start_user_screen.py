import pygame
import modules.screens.user_screen as module_user_screen
from ..screens import user_screen
from ..client import connect_user

pygame.init()

def user_window():
   connect_user()

   start_user = True
   while start_user:  
    module_user_screen.FPS.tick(60)
    module_user_screen.screen_user.fill((255, 50 , 100))
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_user = False
    
    pygame.display.flip()
            
      