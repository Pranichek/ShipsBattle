import pygame
import random
import os
from os.path import abspath, join

class MusicPlayer:
     '''
     ### Класс для управления музикой в игре ###
     '''
     def __init__(self, name_sound):
        '''
        #### Метод конструктор, который позволит нам создавать `музыку` в `игре` ####
        - :mod:`NAME_SOUND`: Название музыкального файла, который будет воспроизводиться.
        - :mod:`is_paused`: Флаг, указывающий, находится ли музыка на паузе. (По умолчанию отсутствует в `__init__`, но создаётся в методах.)

        Пример использования : 
        ```python
        music_load_main = MusicPlayer(name_sound= "main_screen_music.mp3")
        ```
        '''
        pygame.mixer.init()
        self.NAME_SOUND = name_sound

     def random_play(self, loop=0):
        '''
        `Метод` который позволяет `включить` `музыку` 
        '''
        sound_folder = abspath(join(__file__, "..", "..", "..", "static", "sounds", "fight_music"))
        sound_files = [f for f in os.listdir(sound_folder) if f.endswith((".mp3", ".wav", ".ogg"))]


        random_sound = random.choice(sound_files)
        sound_path = join(sound_folder, random_sound)

# Відтворення музики. Параметр loop визначає кількість повторень (-1 - безперервно).
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(loop)
        self.is_paused = False
        pygame.mixer.music.set_endevent(pygame.USEREVENT + 1)

     def handle_music_event(self):
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT + 1:
                pygame.mixer.music.stop()
                self.random_play()   
                
     def play(self, loop=-1):
        '''
        `Метод` который позволяет `включить` `музыку` 
        '''
        #os.path.abspath(__file__ + f"/../../../static/sounds/{self.NAME_SOUND}")
        sound_path = abspath(join(__file__, "..", "..", "..", "static", "sounds", f"{self.NAME_SOUND}"))

# Відтворення музики. Параметр loop визначає кількість повторень (-1 - безперервно).
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(loop)
        self.is_paused = False

     def pause(self):
        '''
        `Метод` который позволяет `выключить` `музыку`
        '''
# Пауза музики.
        if not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True

     def unpause(self):
        '''
        `Метод` который позволяет `продолжить` `музикe` в том случае, если музыка была на паузе
        '''
# Продовження відтворення з паузи.
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False

     def stop(self):
        '''
        `Метод` который позволяет `закончить` `музыку`
        '''
# Зупинка музики.
        pygame.mixer.music.stop()
        self.is_paused = False




music_load_main = MusicPlayer(name_sound= "main_screen_music.mp3")
music_load_waiting = MusicPlayer(name_sound="wait_music.mp3")
fight_music = MusicPlayer(name_sound = "fight_music.mp3")

