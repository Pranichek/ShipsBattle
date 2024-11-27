import os
import pygame
from .list_grid import list_grid


#класс для создания одной пустой клетки 
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


#список для хранения объектов клеток сетки
list_object_map = []


#класс для создания сетки
class Grid:
    def __init__(self , x_screen: int , y_screen: int):
        self.X_SCREEN = x_screen
        self.Y_SCREEN = y_screen
    def generate_grid(self):
        x_screen , y_screen = self.X_SCREEN , self.Y_SCREEN
        for row in list_grid:
            for cell in row:
                if cell == "c":
                    empty_cell = Cell(x = x_screen , y = y_screen ,width = 62 , height = 62 , image_name = "empty_cell.png")
                    list_object_map.append(empty_cell)
                x_screen += 62
            y_screen += 62
            x_screen = 80
    def snap_to_grid(self, x, y):
        grid_x = round((x - self.X_SCREEN) / 62)  
        grid_y = round((y - self.Y_SCREEN) / 62)  
        # Ограничиваем координаты индексами сетки
        grid_x = max(0, min(9 - 1, grid_x))
        grid_y = max(0, min(9 - 1, grid_y))
        # Возвращаем координаты центра привязанной клетки
        return self.X_SCREEN + grid_x * 62, self.Y_SCREEN + grid_y * 62
    
grid_player = Grid(x_screen = 81 , y_screen = 127)