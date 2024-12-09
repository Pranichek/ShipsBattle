import pygame
import os

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

    def load_image(self):
        image_path = os.path.abspath(__file__ + f"/../../../media/{self.folder_name}/{self.image_name}")
        load_image = pygame.image.load(image_path)
        transformed_image = pygame.transform.scale(load_image, (self.width, self.height))
        self.image = transformed_image
        self.rect = self.image.get_rect(topleft=(self.x_cor, self.y_cor))

    def draw_image(self, screen: pygame.Surface):
        # Відображаємо тільки якщо картинка видима
        if self.visible:
            screen.blit(self.image, (self.x_cor, self.y_cor))

    def check_touch(self):
        # Отримуємо позицію миші
        mouse_pos = pygame.mouse.get_pos()
        # Якщо мишка наводиться на картинку, робимо її невидимою
        if self.rect.collidepoint(mouse_pos):
            # False -  значить шо змінюємо стан на невидимий
            self.visible = False  
