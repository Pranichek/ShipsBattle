import pygame
import os

class MusicPlayer:
     def __init__(self, name_sound):
        pygame.mixer.init()
        self.name_sound = name_sound  
        # self.file_path = file_path
#викликаємо метод завантаження звуку
        self.load_sound()
        #створюємо метод для завантаження звуку з файлової системи
     def load_sound(self):
        #  #__file__ - хранит путь именно в нашем проекте , в файле котором мы его создали
        # #/.. - выход из текущего пути на один шаг назад
        sound_path = os.path.abspath(__file__ + f"/../../../sounds/{self.name_sound}")
            #завантажуємо звук по вказаному шляху
        pygame.mixer.music.load(sound_path)
              
     def play(self, loop=-1):

# Відтворення музики. Параметр loop визначає кількість повторень (-1 - безперервно).

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
music_load = MusicPlayer(name_sound= "main_screen_music.mp3")
#      def set_volume(self, volume):
# # Встановлення гучності (значення від 0 до 1).

#         pygame.mixer.music.set_volume(volume)