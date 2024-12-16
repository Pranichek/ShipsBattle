import pygame
import os

class Sound:
     def __init__(self, name_sound):
        pygame.mixer.init()
        self.NAME_SOUND = name_sound  
        self.SOUND = pygame.mixer.Sound(__file__ + f"/../../../sounds/{self.NAME_SOUND}")
              
     def play2(self, loops):
         self.SOUND.play(loops=0, maxtime=0, fade_ms=0)
 
music_click = Sound(name_sound="button_pressed.mp3")
