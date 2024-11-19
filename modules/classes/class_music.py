import pygame

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


