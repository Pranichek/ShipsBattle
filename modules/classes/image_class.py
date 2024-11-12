import pygame
import os

class CreateImage:
    def __init__(self , width , height, x_cor , y_cor, image_name , name_folder):
        self.width = width
        self.height = height
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.image_name = image_name
        self.name_folder = name_folder
        self.image = None
        self.load_image()
    def load_image(self):
        path = os.path.abspath(__file__ + f"/../../../images/{self.name_folder}/{self.image_name}")
        image = pygame.image.load(path)
        transformed_image = pygame.transform.scale(image , (self.width , self.height))
        self.image = transformed_image
    def draw(self , screen: pygame.Surface):
        screen.blit(self.image , (self.x_cor , self.y_cor))
