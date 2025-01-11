import pygame
from os.path import abspath, join

class MusicPlayer:
     def __init__(self, name_sound):
        pygame.mixer.init()
        self.NAME_SOUND = name_sound  
       
     def play(self, loop=-1):
        #os.path.abspath(__file__ + f"/../../../static/sounds/{self.NAME_SOUND}")
        sound_path = abspath(join(__file__, "..", "..", "..", "static", "sounds", f"{self.NAME_SOUND}"))
# Відтворення музики. Параметр loop визначає кількість повторень (-1 - безперервно).
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play(loop)
        self.is_paused = False

     def pause(self):
# Пауза музики.
        if not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True

     def unpause(self):
# Продовження відтворення з паузи.
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False

     def stop(self):
# Зупинка музики.
        pygame.mixer.music.stop()
        self.is_paused = False


music_load_main = MusicPlayer(name_sound= "main_screen_music.mp3")
music_load_waiting = MusicPlayer(name_sound="wait_music.mp3")
fight_music = MusicPlayer(name_sound = "fight_music.mp3")


