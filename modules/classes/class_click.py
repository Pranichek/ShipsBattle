import pygame
import os

class Sound:
     def __init__(self, name_sound):
        pygame.mixer.init()
        self.NAME_SOUND = name_sound  
        self.SOUND = pygame.mixer.Sound(__file__ + f"/../../../sounds/{self.NAME_SOUND}")
        # self.file_path = file_path
#викликаємо метод завантаження звуку
#         self.load_sound()
#         #створюємо метод для завантаження звуку з файлової системи
#      def load_sound(self):
#         #  #__file__ - хранит путь именно в нашем проекте , в файле котором мы его создали
#         # #/.. - выход из текущего пути на один шаг назад
#         sound_path = os.path.abspath(__file__ + f"/../../../sounds/{self.name_sound}")
#             #завантажуємо звук по вказаному шляху
#         pygame.mixer.music.load(sound_path)
              
     def play2(self, loops):
         self.SOUND.play(loops=0, maxtime=0, fade_ms=0)
         
#         sound_path_click = os.path.abspath(__file__ + f"/../../../sounds/{self.NAME_SOUND}")
# # Відтворення музики. Параметр loop визначає кількість повторень (-1 - безперервно).
        # pygame.mixer.Sound(sound_path_click)
        # pygame.mixer.Sound.play()
        # self.is_paused_click = False

#      def pause2(self):
# # Пауза музики.
#         if not self.is_paused_click:
#             pygame.mixer.pause()
#             self.is_paused_click = True

#      def unpause2(self):
# # Продовження відтворення з паузи.
#         if self.is_paused_click:
#             pygame.mixer.unpause()
#             self.is_paused_click = False

#      def stop2(self):
# # Зупинка музики.
#         self.sound.stop()
#         self.is_paused_click = False
music_click = Sound(name_sound="button_pressed.mp3")
