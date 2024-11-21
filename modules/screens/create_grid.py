import os
import pygame
from .list_grid import list_grid

class Cell:
    def __init__(self, x: int , y: int , width: int , height:int , image_name: str):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image_name = image_name
        self.image = None
        self.load_image()
    def load_image(self):
        image_path = os.path.abspath(__file__ + f"/../../../images/grid/{self.image_name}")
        image = pygame.image.load(image_path)
        transformed_image = pygame.transform.scale(image, (self.width, self.height))
        self.image = transformed_image
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))

list_object_map = []

def generate_grid():
    x_screen , y_screen = 80 , 128
    for row in list_grid:
        for cell in row:
            if cell == "c":
                empty_cell = Cell(x = x_screen , y = y_screen ,width = 62 , height = 62 , image_name = "empty_cell.png")
                list_object_map.append(empty_cell)
            x_screen += 62
        y_screen += 62
        x_screen = 80
    
    