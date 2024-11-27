import pygame
import os
from ..screens import grid_player


 

class Ship:
    def __init__(self, x_cor: int, y_cor: int, width: int, height: int, image_ship: str, image_rotate_ship: str , length: int, position_ship: str):
        self.X_COR = x_cor#место где будет стоять корабыль по иксу
        self.Y_COR = y_cor#место где будет стоять корабль по игреку
        self.WIDTH = width#ширина корабля
        self.HEIGHT = height#высота корабля
        self.IMAGE_SHIP = image_ship#картинка обычного корабля
        self.ROTATE_SHIP = image_rotate_ship#картинка повернутого корабля
        self.LENGHT = length#длина корабля в клеточках
        self.ORIENTATION_SHIP = position_ship#горизонтально или вертикально сейчас стоит корабль
        self.CHEK_ROTATION = self.ORIENTATION_SHIP#для проверки оризонтально или вертикально сейчас стоит корабль
        self.READY_IMAGE_SHIP = None#отмаштобированная и готовая кратинка норамльного корабля
        self.IMAGE_ROTATE_SHIP = None#отмаштобированная и готовая кратинка повернутого корабля
        self.load_image()#вызываем метод загрузки картинки
        self.FLAG = None
        self.RECT = self.READY_IMAGE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))#прямоугольник для того чтобы могли отслеживать курсор ли на кораблике или нет
        self.STASIC_X = self.X_COR
        self.STASIC_Y = self.Y_COR
    
    def load_image(self):
        ship = os.path.abspath(__file__ + f"/../../../images/ships/{self.IMAGE_SHIP}")
        rotate_ship = os.path.abspath(__file__ + f"/../../../images/ships/{self.ROTATE_SHIP}")
        image_ship = pygame.image.load(ship)
        image_rotate_ship = pygame.image.load(rotate_ship)
        
        # Размер корабля зависит от ориентации
        if self.ORIENTATION_SHIP == "horizontal":
            size_ship = (self.WIDTH * self.LENGHT, self.HEIGHT)
            # self.RECT = self.READY_IMAGE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
        elif self.ORIENTATION_SHIP == "vertical":
            size_ship = (self.WIDTH, self.HEIGHT * self.LENGHT)
            # self.RECT = self.IMAGE_ROTATE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
        self.READY_IMAGE_SHIP = pygame.transform.scale(image_ship, size_ship)
        self.IMAGE_ROTATE_SHIP = pygame.transform.scale(image_rotate_ship, size_ship)
    def snap_to_grid(self): 
        self.X_COR, self.Y_COR = grid_player.snap_to_grid(self.X_COR, self.Y_COR) 

    def draw_sheep(self, screen: pygame.Surface):
        if self.ORIENTATION_SHIP == "horizontal":
            screen.blit(self.READY_IMAGE_SHIP, (self.X_COR, self.Y_COR))
        elif self.ORIENTATION_SHIP == "vertical":
            screen.blit(self.IMAGE_ROTATE_SHIP, (self.X_COR, self.Y_COR))
      
    def rotate_ship(self, event: pygame.event):
        mouse = pygame.mouse.get_pos()
        if self.RECT.collidepoint(mouse):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: 
                    if self.CHEK_ROTATION == "horizontal":
                        self.ORIENTATION_SHIP = "vertical"
                        self.CHEK_ROTATION = self.ORIENTATION_SHIP
                        self.load_image()
                        self.RECT = self.IMAGE_ROTATE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
                    elif self.CHEK_ROTATION == "vertical":
                        self.ORIENTATION_SHIP = "horizontal"
                        self.CHEK_ROTATION = self.ORIENTATION_SHIP
                        self.load_image()
                        self.RECT = self.READY_IMAGE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
    def matrix_move(self, event: pygame.event, matrix_width: int, matrix_height: int, cell: int):
        mouse = pygame.mouse.get_pos()
        if self.RECT.collidepoint(mouse):  # Проверяем, что курсор находится над кораблем
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Проверяем, что клик был по кораблю
                if self.RECT.collidepoint(event.pos):
                    self.FLAG = True  # Устанавливаем флаг, что можно двигать корабль

            elif event.type == pygame.MOUSEMOTION and self.FLAG:
                # тут мы бновлем координаты корабля при движении мыши
                #делим на два чтобы курсор был по центру корабля
                self.X_COR = mouse[0] - self.RECT.width // 2  
                self.Y_COR = mouse[1] - self.RECT.height // 2

                # Проверка выхода за границы по X и Y
                if self.X_COR < 0:
                    self.X_COR = 0
                if self.Y_COR < 0:
                    self.Y_COR = 0
                if self.X_COR + self.RECT.width > matrix_width * cell:
                    self.X_COR = matrix_width * cell - self.RECT.width
                if self.Y_COR + self.RECT.height > matrix_height * cell:
                    self.Y_COR = matrix_height * cell - self.RECT.height
                # Обновляем прямоугольник с новым положением
                self.RECT = self.READY_IMAGE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))

            elif event.type == pygame.MOUSEBUTTONUP and self.FLAG:
                # Привязываем корабль к сетке 
                if self.X_COR >= grid_player.X_SCREEN  - 50 and self.X_COR <= grid_player.X_SCREEN + 558:
                    self.snap_to_grid()  
                else:
                    self.X_COR = self.STASIC_X  
                    self.Y_COR = self.STASIC_Y

                # Проверяем пересечение с другими кораблями 
                for ship in list_ships: 
                    if ship != self and self.RECT.colliderect(ship.RECT): 
                        # Если пересечение найдено, возвращаем корабль на исходную позицию 
                        self.X_COR = self.STASIC_X  
                        self.Y_COR = self.STASIC_Y 
                        break 
                    
                # Проверяем, чтобы корабль не вышел за границы матрицы
                if self.X_COR < 0:
                    self.X_COR = 0
                if self.Y_COR < 0:
                    self.Y_COR = 0

                # Корректируем позицию в зависимости от ориентации корабля
                if self.ORIENTATION_SHIP == "horizontal" and self.X_COR + self.LENGHT * cell > matrix_width * cell:
                    self.X_COR = (matrix_width - self.LENGHT) * cell
                if self.ORIENTATION_SHIP == "vertical" and self.Y_COR + self.LENGHT * cell > matrix_height * cell:
                    self.Y_COR = (matrix_height - self.LENGHT) * cell

                # Обновляем прямоугольник с финальной позицией
                self.RECT = self.READY_IMAGE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
                # Сбрасываем флаг, чтобы прекратить движение
                self.FLAG = False




ship_three = Ship(
    x_cor = 900 , 
    y_cor = 80 , 
    width = 62 , 
    height=62 , 
    image_ship = "ship_three.png", 
    image_rotate_ship = "rotate_ship_three.png", 
    length=3 , 
    position_ship = "horizontal"
)

ship_two = Ship(
    x_cor = 900,
    y_cor =  200,
    width= 62,
    height= 62,
    image_ship= "ship_two.png",
    image_rotate_ship= "rotate_ship_two.png",
    length = 2,
    position_ship= "horizontal"
)

list_ships = []

list_ships.append(ship_three)
list_ships.append(ship_two)