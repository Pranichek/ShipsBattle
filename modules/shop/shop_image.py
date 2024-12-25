import pygame
import os

pygame.init()

# клас для відображення зображень у магазині
class Image_Shop:
    # конструктор (__init__) зображеннь у магазині
    def __init__(self, x_cor: int , y_cor: int , width: int , height: int, folder_name: str , image_name: str , target_y: int):
        self.FOLDER_NAME = folder_name
        self.IMAGE_NAME = image_name
        self.X_COR = x_cor
        self.Y_COR = y_cor
        self.WIDTH = width
        self.HEIGHT = height
        self.PATH = os.path.abspath(__file__ + f"/../../../media/{self.FOLDER_NAME}/{self.IMAGE_NAME}")
        self.IMAGE = pygame.transform.scale(pygame.image.load(self.PATH), (self.WIDTH, self.HEIGHT)).convert_alpha()
        self.SPEED = 4
        self.ACTIVE = False 
        self.TURN = "Down"
        self.TARGET_Y = target_y
        self.visible = 0  

    # Відображає зображення на екрані, враховуючи поточну прозорість (visible)
    def draw(self, screen: pygame.Surface):
        self.IMAGE.set_alpha(self.visible)
        screen.blit(self.IMAGE , (self.X_COR, self.Y_COR))

    # Плавно змінює прозорість зображення:fade_in() збільшує прозорість до 255 (повністю видимий стан)
    def fade_in(self):
        if self.visible < 255:
            self.visible += 5  
            if self.visible >= 255:
                self.visible = 255
     
    # fade_out() зменшує прозорість до 0 (невидимий стан)
    def fade_out(self):
        if self.visible > 0:
            self.visible -= 5  
            if self.visible <= 0:
                self.visible = 0
       
    # Зображення може плавно переміщатися вниз (до цільової позиції) і назад
    #Використовується прапорець turn, щоб визначити напрямок руху
    # Викликається fade_in() і fade_out() для плавного з’явлення чи зникнення
    def move(self):
        if self.ACTIVE:
            if self.TURN == "Down":
                if self.Y_COR < self.TARGET_Y: 
                    self.Y_COR += self.SPEED
                    self.fade_in()
                    if self.Y_COR >= self.TARGET_Y:  
                        self.Y_COR = self.TARGET_Y
                        self.TURN = "Up"  

            elif self.TURN == "Up":
                if self.Y_COR > -(self.HEIGHT + (422 - (self.TARGET_Y + self.HEIGHT))):  
                    self.Y_COR -= self.SPEED
                    self.fade_out()
                    if self.Y_COR <= -(self.HEIGHT + (422 - (self.TARGET_Y + self.HEIGHT))):  
                        self.Y_COR = -(self.HEIGHT + (422 - (self.TARGET_Y + self.HEIGHT)))
                        self.TURN = "Down"  

        # Сброс состояния только для завершенной анимации
        if self.Y_COR == self.TARGET_Y or self.Y_COR == -(self.HEIGHT + (422 - (self.TARGET_Y + self.HEIGHT))):
            self.ACTIVE = False



# стовюємо об'єтки зображень від цього класу
shop_bg = Image_Shop(
    x_cor = 0 ,
    y_cor = -416 ,
    width = 1280 ,
    height = 416 ,
    folder_name = "backgrounds" ,
    image_name = "shop_background.png" ,
    target_y = 0)

deer_img = Image_Shop(
    x_cor = 0 ,
    y_cor = -89 ,
    width = 164 , 
    height = 89 ,
    folder_name = "decorations" ,
    image_name = "deer.png" ,
    target_y = 328
)

items_bg = Image_Shop(
    x_cor = 583 ,
    y_cor = -333 ,
    width = 682 ,
    height = 295 ,
    folder_name = "backgrounds" ,
    image_name = "shop_item_bg.png" ,
    target_y = 89
)

tasks_bg = Image_Shop(
    x_cor = 9 , 
    y_cor = -333 , 
    width = 427 ,
    height = 291 ,
    folder_name = "backgrounds" ,
    image_name = "tasks_bg.png" ,
    target_y = 89
)

ten_coins = Image_Shop(
    x_cor = 620 ,
    y_cor = -(106 + (422 - (137 + 106))) ,
    width = 54 , 
    height = 106 ,
    folder_name = "prices" ,
    image_name = "10_coins.png" ,
    target_y = 137
)

twenty_five_coins = Image_Shop(
    x_cor = 729,
    y_cor = -(105 + (422 - (137 + 105))),
    width = 59,
    height = 105,
    folder_name = "prices",
    image_name = "25_coins.png",
    target_y = 137
)

fifty_coins = Image_Shop(
    x_cor = 831,
    y_cor = -(106 + (422 - (137 + 106))),
    width = 81 , 
    height = 106 ,
    folder_name = "prices",
    image_name = "50_coins.png",
    target_y = 137
)

eghty_coins = Image_Shop(
    x_cor = 942 ,
    y_cor = -(106 + (422 - (137 + 106))) ,
    width = 73 , 
    height = 106 ,
    folder_name = "prices",
    image_name = "80_coins.png",
    target_y = 137
)

hundred_fifty_coins = Image_Shop(
    x_cor = 1049,
    y_cor = -(110 + (422 - (137 + 110))) ,
    width = 78, 
    height = 110,
    folder_name = "prices",
    image_name = "150_coins.png",
    target_y = 137
)

two_hundred_coins = Image_Shop(
    x_cor = 1146 , 
    y_cor = -(107 + (422 - (137 + 107))) ,
    width = 97 , 
    height = 107 ,
    folder_name = "prices",
    image_name = "200_coins.png",
    target_y = 137
)

jar_coins = Image_Shop(
    x_cor = 431 , 
    y_cor = -(153 + (422 - (150 + 153))) ,
    width = 154 ,
    height = 153 ,
    folder_name = "decorations" ,
    image_name = "jar.png" ,
    target_y = 150
)

task_one = Image_Shop(
    x_cor = 33 ,
    y_cor = -(65 + (422 - (131 + 65))) ,
    width = 376 ,
    height = 65,
    folder_name = "backgrounds" ,
    image_name = "task_one.png" ,
    target_y = 131
)

task_two = Image_Shop(
    x_cor = 33 ,
    y_cor = -(65 + (422 - (186 + 65))) ,
    width = 376 ,
    height = 65,
    folder_name = "backgrounds" ,
    image_name = "task_two.png" ,
    target_y = 186
)

task_three = Image_Shop(
    x_cor = 33 ,
    y_cor = -(65 + (422 - (237 + 65))) ,
    width = 376 ,
    height = 65,
    folder_name = "backgrounds" ,
    image_name = "task_three.png" ,
    target_y = 237
)

task_four = Image_Shop(
    x_cor = 33 ,
    y_cor = -(43 + (422 - (293 + 43))) ,
    width = 376 ,
    height = 43,
    folder_name = "backgrounds" ,
    image_name = "task_four.png" ,
    target_y = 293
)


shop_item = []

# додаємо зображення до цього списку , щоб за допомогою циклу відмальовувати їх
shop_item.extend([shop_bg , items_bg , tasks_bg , deer_img , ten_coins , twenty_five_coins , fifty_coins , eghty_coins , hundred_fifty_coins , two_hundred_coins , jar_coins ,task_one ,task_two ,task_three , task_four])

