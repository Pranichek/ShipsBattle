import pygame
import os

class Sound:
     def __init__(self, name_sound):
        pygame.mixer.init()
        self.NAME_SOUND = name_sound  
        sound_path = os.path.abspath(__file__ + f"/../../../static/sounds/{self.NAME_SOUND}")
        self.SOUND = pygame.mixer.Sound(sound_path)
              
     def play2(self, loops):
         self.SOUND.play(loops=0, maxtime=0, fade_ms=0)
         
     def get_busy(self):
        return pygame.mixer.get_busy()
         

music_click = Sound(name_sound="button_pressed.mp3")
time_sound = Sound(name_sound="tick2.mp3")
