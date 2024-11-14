import pygame 
import os


class InputText:
    def __init__(self, width : int, height : int, x_cor : int, y_cor : int, base_text : str, image : str, screen_name : str, font : str):
        self.width = width,
        self.height = height,
        self.x_cor = x_cor,
        self.y_cor = y_cor,
        self.base_text = base_text,
        self.image = image,
        self.screen_name = screen_name,
        self.font = font
        self.user_text = []
    def load_image(self):
        image_path = os.path.abspath(__file__ + f"/../../../images/{self.image}")
        self.image = pygame.image.load(image_path)
        transform_image = pygame.transform.scale(self.image(self.width, self.height))
        self.image = transform_image

    def load_font(self, font : str):
            
            font_path = os.path.abspath(__file__ + f"/../../../fonts/{font}")
            font = pygame.font.Font(font_path, size = 44)


    def draw_input_text(self, user_text : str, screen_name : str):
        
        screen_name.blit(self.image(self.x_cor, self.y_cor))