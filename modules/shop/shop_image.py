import pygame
from os.path import abspath, join
from ..screens import FPS



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
        #"/../../../media/{self.FOLDER_NAME}/{self.IMAGE_NAME}"
        self.PATH = abspath(join(__file__, "..", "..", "..", "media", f"{self.FOLDER_NAME}", f"{self.IMAGE_NAME}"))
        self.IMAGE = pygame.transform.scale(pygame.image.load(self.PATH), (self.WIDTH, self.HEIGHT)).convert_alpha()
        self.SPEED = 13
        self.ACTIVE = False 
        self.TURN = "Down"
        self.TARGET_Y = target_y
        self.VISIBLE = 0 

    # Відображає зображення на екрані, враховуючи поточну прозорість (visible)
    def draw(self, screen: pygame.Surface):
        self.IMAGE.set_alpha(self.VISIBLE)
        screen.blit(self.IMAGE , (self.X_COR, self.Y_COR))

    # Плавно змінює прозорість зображення:fade_in() збільшує прозорість до 255 (повністю видимий стан)
    def fade_in(self):
        fps = FPS.get_fps()
        if fps <= 0:
            fps = 0.01
        if self.VISIBLE < 255:
            self.VISIBLE += 5 * (60 / fps)
            if self.VISIBLE >= 255:
                self.VISIBLE = 255
    # fade_out() зменшує прозорість до 0 (невидимий стан)
    def fade_out(self):
        fps = FPS.get_fps()
        if fps <= 0:
            fps = 0.01
        if self.VISIBLE > 0:
            self.VISIBLE -= 5 * (60 / fps)
            if self.VISIBLE <= 0:
                self.VISIBLE = 0
       
    # Зображення може плавно переміщатися вниз (до цільової позиції) і назад
    #Використовується прапорець turn, щоб визначити напрямок руху
    # Викликається fade_in() і fade_out() для плавного з’явлення чи зникнення
    def move(self):
        fps = FPS.get_fps()
        if fps <= 0:
            fps = 0.01
        current_speed = self.SPEED * (60 / fps)
        if self.ACTIVE:
            if self.TURN == "Down":
                if self.Y_COR < self.TARGET_Y: 
                    self.Y_COR += current_speed
                    self.fade_in()
                    if self.Y_COR >= self.TARGET_Y:  
                        self.Y_COR = self.TARGET_Y
                        self.TURN = "Up"  

            elif self.TURN == "Up":
                if self.Y_COR > -(self.HEIGHT + (832 - (self.TARGET_Y + self.HEIGHT))):  
                    self.Y_COR -= current_speed
                    self.fade_out()
                    if self.Y_COR <= -(self.HEIGHT + (832 - (self.TARGET_Y + self.HEIGHT))):  
                        self.Y_COR = -(self.HEIGHT + (832 - (self.TARGET_Y + self.HEIGHT)))
                        self.TURN = "Down"  

        # Сброс состояния только для завершенной анимации
        if self.Y_COR == self.TARGET_Y or self.Y_COR == -(self.HEIGHT + (832 - (self.TARGET_Y + self.HEIGHT))):
            self.ACTIVE = False



# стовюємо об'єтки зображень від цього класу
shop_bg = Image_Shop(
    x_cor = 0 ,
    y_cor = -832 ,
    width = 1280 ,
    height = 832 ,
    folder_name = "backgrounds" ,
    image_name = "shop_background.png" ,
    target_y = 0)

deer_img = Image_Shop(
    x_cor = 0 ,
    y_cor = -(89 + (832 - (328 + 89))) ,
    width = 164 , 
    height = 89 ,
    folder_name = "decorations" ,
    image_name = "deer.png" ,
    target_y = 328
)

items_bg = Image_Shop(
    x_cor = 583 ,
    y_cor = -(295 + (832 - (89 + 295))),
    width = 682 ,
    height = 295 ,
    folder_name = "backgrounds" ,
    image_name = "shop_item_bg.png" ,
    target_y = 89
)

tasks_bg = Image_Shop(
    x_cor = 9 , 
    y_cor = -(291 + (832 - (89 + 291))), 
    width = 427 ,
    height = 291 ,
    folder_name = "backgrounds" ,
    image_name = "tasks_bg.png" ,
    target_y = 89
)

price = Image_Shop(
    x_cor = 612 ,
    y_cor = -(152 + (832 - (100 + 152))),
    width = 634,
    height = 152 ,
    folder_name = "prices",
    image_name = "price.png",
    target_y = 100
)

jar_coins = Image_Shop(
    x_cor = 431 , 
    y_cor = -(153 + (832 - (150 + 153))) ,
    width = 154 ,
    height = 153 ,
    folder_name = "decorations" ,
    image_name = "jar.png" ,
    target_y = 150
)

task_one = Image_Shop(
    x_cor = 33 ,
    y_cor = -(65 + (832 - (131 + 65))) ,
    width = 376 ,
    height = 65,
    folder_name = "backgrounds" ,
    image_name = "task_one.png" ,
    target_y = 131
)

task_two = Image_Shop(
    x_cor = 33 ,
    y_cor = -(65 + (832 - (186 + 65))) ,
    width = 376 ,
    height = 65,
    folder_name = "backgrounds" ,
    image_name = "task_two.png" ,
    target_y = 186
)

task_three = Image_Shop(
    x_cor = 33 ,
    y_cor = -(65 + (832 - (237 + 65))) ,
    width = 376 ,
    height = 65,
    folder_name = "backgrounds" ,
    image_name = "task_three.png" ,
    target_y = 237
)

task_four = Image_Shop(
    x_cor = 33 ,
    y_cor = -(43 + (832 - (293 + 43))) ,
    width = 376 ,
    height = 43,
    folder_name = "backgrounds" ,
    image_name = "task_four.png" ,
    target_y = 293
)

# awars_description = Image_Shop(
#     x_cor = 0 ,
#     y_cor = -(357 + (832 - (431 + 357))),
#     width = 1280 ,
#     height = 357 ,
#     folder_name = "backgrounds" ,
#     image_name = "awars_description.png" ,
#     target_y = 431
# )


shop_item = []

# додаємо зображення до цього списку , щоб за допомогою циклу відмальовувати їх
shop_item.extend([shop_bg , items_bg , tasks_bg , deer_img , price , jar_coins ,task_one ,task_two ,task_three , task_four])

