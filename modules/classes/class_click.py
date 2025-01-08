import pygame
from os.path import abspath, join

class Sound:
     def __init__(self, name_sound):
        pygame.mixer.init()
        self.NAME_SOUND = name_sound  
        #os.path.abspath(__file__ + f"/../../../static/sounds/{self.NAME_SOUND}")
        sound_path = abspath(join(__file__, "..", "..", "..", "static", "sounds", f"{self.NAME_SOUND}"))
        self.SOUND = pygame.mixer.Sound(sound_path)
              
     def play2(self, loops):
         self.SOUND.play(loops=0, maxtime=0, fade_ms=0)
         

music_click = Sound(name_sound = "button_pressed.mp3")
music_achieve = Sound(name_sound = "get_achievement.mp3")
death_ship_sound = Sound(name_sound = "death_ship.mp3")
miss_water_sound = Sound(name_sound = "miss_attack.mp3")