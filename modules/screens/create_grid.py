import os
import pygame
from .grid_list import list_grid


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
        image_path = os.path.abspath(__file__ + f"/../../../media/grid/{self.image_name}")
        image = pygame.image.load(image_path)
        transformed_image = pygame.transform.scale(image, (self.width, self.height))
        self.image = transformed_image
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))


#список для хранения объектов клеток сетки
list_object_map = []

list_object_map_enemy = []


#класс для создания сетки
class Grid:
    def __init__(self , x_screen: int , y_screen: int):
        self.X_SCREEN = x_screen
        self.Y_SCREEN = y_screen
    def generate_grid(self , width_cell = 62 , height_cell = 62):
        if self.X_SCREEN == 67:
                    list_object_map_enemy.clear()
        else:
             list_object_map.clear()
    
        x_screen , y_screen = self.X_SCREEN , self.Y_SCREEN
        for row in list_grid:
            for cell in row:
                # if cell == 0:
                empty_cell = Cell(x = x_screen , y = y_screen ,width = width_cell , height = height_cell , image_name = "empty_cell.png")
                if self.X_SCREEN == 67:
                    list_object_map_enemy.append(empty_cell)
                else:
                    list_object_map.append(empty_cell)
                    
                x_screen += width_cell
            y_screen += height_cell
            x_screen = self.X_SCREEN
    def snap_to_grid(self, x, y):
    # Рассчитываем индекс столбца сетки (grid_x), в который попадает точка (x)-координата корабля.
    # 1. Вычитаем координату начала сетки по X (self.X_SCREEN), чтобы получить относительное положение.
    # 2. Делим на ширину ячейки (62), чтобы определить, в какой столбец попадает точка.
    # 3. Округляем до ближайшего целого числа, чтобы привязать координату к ближайшему столбцу.
        grid_x = round((x - self.X_SCREEN) / 62)  
    
    # Рассчитываем индекс строки сетки (grid_y), в которую попадает точка (y)-координата корабля.
    # 1. Вычитаем координату начала сетки по Y (self.Y_SCREEN), чтобы получить относительное положение.
    # 2. Делим на высоту ячейки (62), чтобы определить, в какую строку попадает точка.
    # 3. Округляем до ближайшего целого числа, чтобы привязать координату к ближайшей строке.
        grid_y = round((y - self.Y_SCREEN) / 62)  
    
    # Ограничиваем индекс столбца (grid_x) в пределах от 0 до 8 (максимальное количество столбцов минус 1).
    # Если координата выходит за пределы сетки, она будет приведена к ближайшей границе.
        grid_x = max(0, min(10 - 1, grid_x))
    
    # Ограничиваем индекс строки (grid_y) в пределах от 0 до 8 (максимальное количество строк минус 1).
    # Если координата выходит за пределы сетки, она будет приведена к ближайшей границе.
        grid_y = max(0, min(10 - 1, grid_y))
    
    # Возвращаем координаты центра привязанной ячейки:
    # 1. Рассчитываем экранные координаты центра ячейки по X:
    #    - Умножаем индекс столбца (grid_x) на ширину ячейки (62) и добавляем смещение сетки (self.X_SCREEN).
    # 2. Аналогично, рассчитываем экранные координаты центра ячейки по Y.
        return self.X_SCREEN + grid_x * 62, self.Y_SCREEN + grid_y * 62
    
    
grid_player = Grid(x_screen = 81 , y_screen = 76)
enemy_grid = Grid(x_screen = 67 , y_screen = 257)

