import pygame
from os.path import abspath, join
from ..screens.screen import FPS

class DrawImage:
    def __init__(self, width: int, height: int, x_cor: int, y_cor: int, folder_name: str, image_name: str):
        self.width = width
        self.height = height
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.folder_name = folder_name
        self.image_name = image_name
        self.image = None
        self.visible = True  # Видима картинка спочатку
        self.rect = None
        self.load_image()
        self.visible = 255

    def load_image(self):
        #"/../../../media/{self.folder_name}/{self.image_name}
        image_path = abspath(join(__file__, "..", "..", "..", "media", f"{self.folder_name}", f"{self.image_name}"))
        load_image = pygame.image.load(image_path)
        transformed_image = pygame.transform.scale(load_image, (self.width, self.height)).convert_alpha()
        self.image = transformed_image
        self.rect = self.image.get_rect(topleft=(self.x_cor, self.y_cor))

    def draw_image(self, screen: pygame.Surface):
        # Відображаємо тільки якщо картинка видима
        self.image.set_alpha(self.visible)  
        if self.visible:
            screen.blit(self.image, (self.x_cor, self.y_cor))

    def check_touch(self):
        # Отримуємо позицію миші
        mouse_pos = pygame.mouse.get_pos()
        # Якщо мишка наводиться на картинку, робимо її невидимою
        if self.rect.collidepoint(mouse_pos):
            # False -  значить шо змінюємо стан на невидимий
            self.visible = False  

    def fade_out(self):
        fps = FPS.get_fps()
        if fps <= 0:
            fps = 0.01
        current_speed = (60 / fps)
        if self.visible > 0:
            self.visible -= 10 * current_speed
            if self.visible <= 0:
                self.visible = 0
    def fade_in(self):
        fps = FPS.get_fps()
        if fps <= 0:
            fps = 0.01
        if self.visible < 255:
            self.visible += 1 * (60 / fps)
            if self.visible >= 255:
                self.visible = 255
