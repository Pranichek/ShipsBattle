import pygame
import os
from .shop_image import shop_item


#класс для кнопки в магазині
class Button_Shop:
    #створюємо конструктор(__init__) кнопки
    def __init__(self, x, y, image_name, height,width,  target_y: int ,action = None):
        self.X_COR = x
        self.IMAGE_NAME = image_name
        self.Y_COR = y
        self.WIDTH = width
        self.HEIGHT = height
        self.PTATH_IMAGE1 = os.path.abspath(__file__ + f"/../../../static/images_button/shop_buttons/{self.IMAGE_NAME}")
        self.IMAGE = pygame.transform.scale(pygame.image.load(self.PTATH_IMAGE1), (self.WIDTH , self.HEIGHT))
        self.RECT = self.IMAGE.get_rect(topleft=(self.X_COR, self.Y_COR))
        self.ACTION = action
        self.ACTIVE = False 
        self.TURN = "Down"
        self.VISIBLE = 0
        self.TARGET_Y = target_y
        self.SPEED = 10

    # створюємо метод кнопки , який буде перевиряти чи натиснута кнопка , якщо так , то виконуємо дії яка прив'язана до кнопки
    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            mouse = pygame.mouse.get_pos()
            if self.RECT.collidepoint(mouse):
                if self.ACTION:
                    self.ACTION()
    
    # Відображає кнопку на екрані , та змінюємо прозорість (visible) залежно від стану
    def draw(self, screen: pygame.Surface):
        self.IMAGE.set_alpha(self.VISIBLE)
        screen.blit(self.IMAGE , (self.X_COR, self.Y_COR))
        mouse_pos = pygame.mouse.get_pos()
        if self.TURN == "Down":
            screen.blit(self.IMAGE , (self.X_COR, self.Y_COR))
    # Плавно змінює прозорість кнопки:fade_in() збільшує прозорість до 255 (повністю видимий стан)
    def fade_in(self):
        if self.VISIBLE < 255:
            self.VISIBLE += 5  
            if self.VISIBLE >= 255:
                self.VISIBLE = 255
    # fade_out() зменшує прозорість до 0 (невидимий стан)
    def fade_out(self):
        if self.VISIBLE > 0:
            self.VISIBLE -= 5  
            if self.VISIBLE <= 0:
                self.VISIBLE = 0
    # Кнопка може плавно переміщатися вниз (до цільової позиції) і назад
    #Використовується прапорець turn, щоб визначити напрямок руху
    # Викликається fade_in() і fade_out() для плавного з’явлення чи зникнення
    def move(self):
        if self.ACTIVE:
            if self.TURN == "Down":
                if self.Y_COR < self.TARGET_Y: 
                    self.Y_COR += self.SPEED
                    self.RECT.y += self.SPEED
                    self.fade_in()
                    if self.Y_COR >= self.TARGET_Y:  
                        self.Y_COR = self.TARGET_Y
                        self.RECT.y == self.TARGET_Y
                        self.TURN = "Up"  

            elif self.TURN == "Up":
                if self.Y_COR > -(self.HEIGHT + (832- (self.TARGET_Y + self.HEIGHT))):  
                    self.Y_COR -= self.SPEED
                    self.RECT.y -= self.SPEED
                    self.fade_out()
                    if self.Y_COR <= -(self.HEIGHT + (832- (self.TARGET_Y + self.HEIGHT))):  
                        self.Y_COR = -(self.HEIGHT + (832- (self.TARGET_Y + self.HEIGHT)))
                        self.RECT.y = -(self.HEIGHT + (832- (self.TARGET_Y + self.HEIGHT)))
                        self.TURN = "Down"  

        # Сброс состояния только для завершенной анимации
        if self.Y_COR == self.TARGET_Y or self.Y_COR == -(self.HEIGHT + (832- (self.TARGET_Y + self.HEIGHT))):
            self.ACTIVE = False


def test():
    print("Hello world!") 

# створюємо елементи від цього класу
button_armor_for_ship = Button_Shop(
    x = 600 ,
    y = -(98 + (832- (263 + 98))),
    width = 96 ,
    height = 98 ,
    image_name = "armor_for_ship.png",
    target_y = 263,
    action = test,
)

button_stop_fire = Button_Shop(
    x = 710 ,
    y = -(98 + (832- (263 + 98))) ,
    width = 96 ,
    height = 98 ,
    image_name = "stop_fire.png",
    target_y = 263,
    action = test
)

button_restores_cell = Button_Shop(
    x = 820 ,
    y = -(105 + (832- (263 + 105))),
    width = 96 ,
    height = 105 ,
    image_name = "restore_one_cell.png",
    target_y = 263,
    action = test
)

button_fire_rocket = Button_Shop(
    x = 930 ,
    y = -(98 + (832- (263 + 98))),
    width = 96 ,
    height = 98 ,
    image_name = "fire_rocket.png",
    target_y = 263,
    action = test
)

button_bomb = Button_Shop(
    x = 1040 ,
    y = -(97 + (832- (263 + 97))),
    width = 96 ,
    height = 97 ,
    image_name = "bomb.png",
    target_y = 263,
    action = test
)

button_auto_attack = Button_Shop(
    x = 1150 ,
    y = -(105 + (832- (263 + 105))),
    width = 96 ,
    height = 105 ,
    image_name = "auto_rocket.png",
    target_y = 263,
    action = test
)

# додаємо кнопки до списку де збергіються елементи магазину , щоб можна було через цикл їх всіх відмалювати
shop_item.extend([button_restores_cell ,button_armor_for_ship , button_auto_attack , button_bomb , button_fire_rocket , button_stop_fire])
