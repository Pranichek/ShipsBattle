import pygame
import os

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
        self.RECT = self.READY_IMAGE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))#прямоугольник для того чтобы могли отслеживать курсор ли на кораблике или нет
    
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




ship = Ship(
    x_cor = 80 , 
    y_cor = 80 , 
    width = 62 , 
    height=62 , 
    image_ship = "ship_three.png", 
    image_rotate_ship = "rotate_ship_three.png", 
    length=3 , 
    position_ship = "horizontal"
)
         
