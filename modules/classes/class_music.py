import pygame
<<<<<<< HEAD

class MusicPlayer:
    def __init__(self, file_path):
        pygame.mixer.init()  
        self.file_path = file_path
        self.is_paused = False
        self.load_music()

    def load_music(self):
        pygame.mixer.music.load(self.file_path)  # Завантаження музичного файлу

    def play(self, loop=-1):

# Відтворення музики. Параметр loop визначає кількість повторень (-1 - безперервно).

        pygame.mixer.music.play(loop)
        self.is_paused = False

    def pause(self):
=======
import os

class MusicPlayer:
     def __init__(self, name_sound):
        pygame.mixer.init()
        self.NAME_SOUND = name_sound  
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
              
     def play(self, loop=-1):
        sound_path = os.path.abspath(__file__ + f"/../../../sounds/{self.NAME_SOUND}")
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

    def set_volume(self, volume):
# Встановлення гучності (значення від 0 до 1).

        pygame.mixer.music.set_volume(volume)

def stop(self):
# Зупинка музики.
    pygame.mixer.music.stop()
    self.is_paused = False
music_load_main = MusicPlayer(name_sound= "main_screen_music.mp3")
music_load_waiting = MusicPlayer(name_sound="wait_music.mp3")



class VolumeDownButton:
    def __init__(self, x, y, width, height, font, volume_step=0.1, min_volume=0.0):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.text = "🔉"
        self.color = (200, 200, 200)
        self.hover_color = (150, 150, 150)
        self.text_color = (0, 0, 0)
        self.volume_step = volume_step
        self.min_volume = min_volume

    def draw(self, screen):
        # рисует кнопку
        mouse_pos = pygame.mouse.get_pos()
        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(screen, color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event, current_volume):
        # обробатывает события после нажатия на кнопку
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                # Уменьшаем громкость
                new_volume = max(self.min_volume, current_volume - self.volume_step)
                pygame.mixer.music.set_volume(new_volume)
                return new_volume
        return current_volume