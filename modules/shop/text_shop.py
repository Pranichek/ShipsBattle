# import pygame , os , random
# from .shop_image import shop_item

# class Font_Shop:
#     def __init__(self, size : int, name_font : str, text : str,x_cor : int, y_cor : int , target_y: int):
#         self.SIZE = size
#         self.NAME_FONT = name_font
#         self.PATH_TO_FONT = os.path.abspath(__file__ + f"/../../../media/fonts/{self.NAME_FONT}")
#         self.TEXT = text
#         self.X_COR = x_cor
#         self.Y_COR = y_cor
#         self.TARGET_Y = target_y
#         self.SPEED = 4
#         self.VISIBLE = 0
#         self.TURN = "Down"
#         self.ACTIVE = False

#         self.font = pygame.font.Font(self.PATH_TO_FONT, self.SIZE)
#         self.text_surface = self.font.render(self.TEXT, True, "white")
#         self.text_surface = self.text_surface.convert_alpha()  

#     def draw(self, screen: pygame.Surface):
#         self.text_surface.set_alpha(self.VISIBLE)  
#         screen.blit(self.text_surface, (self.X_COR, self.Y_COR))
#         # print(self.font.size(self.TEXT))

#     def fade_in(self):
#         if self.VISIBLE < 255:
#             self.VISIBLE += 5  
#             if self.VISIBLE >= 255:
#                 self.VISIBLE = 255
         
#     def fade_out(self):
#         if self.VISIBLE > 0:
#             self.VISIBLE -= 5  
#             if self.VISIBLE <= 0:
#                 self.VISIBLE = 0
#     def move(self):
#         if self.ACTIVE:
#             if self.TURN == "Down":
#                 if self.Y_COR < self.TARGET_Y: 
#                     self.Y_COR += self.SPEED
#                     self.fade_in()
#                     if self.Y_COR >= self.TARGET_Y:  
#                         self.Y_COR = self.TARGET_Y
#                         self.TURN = "Up"  

#             elif self.TURN == "Up":
#                 if self.Y_COR > -(self.SIZE + (422 - (self.TARGET_Y + self.SIZE))):  
#                     self.Y_COR -= self.SPEED
#                     self.fade_out()
#                     if self.Y_COR <= -(self.SIZE + (422 - (self.TARGET_Y + self.SIZE))):  
#                         self.Y_COR = -(self.SIZE + (422 - (self.TARGET_Y + self.SIZE)))
#                         self.TURN = "Down"  
     
#         if self.Y_COR == self.TARGET_Y or self.Y_COR == -(self.SIZE + (422 - (self.TARGET_Y + self.SIZE))):
#             self.ACTIVE = False

import pygame , os , random
from .shop_image import shop_item

class Font_Shop:
    def __init__(self, size: int, name_font: str, text: str, x_cor: int, y_cor: int, target_y: int , max_width: int, max_height: int):
        self.SIZE = size
        self.NAME_FONT = name_font
        self.PATH_TO_FONT = os.path.abspath(__file__ + f"/../../../media/fonts/{self.NAME_FONT}")
        self.TEXT = text
        self.X_COR = x_cor
        self.Y_COR = y_cor
        self.TARGET_Y = target_y
        self.MAX_WIDTH = max_width
        self.MAX_HEIGHT = max_height
        self.SPEED = 4
        self.VISIBLE = 0
        self.TURN = "Down"
        self.ACTIVE = False
        # Создаем шрифт
        self.font = pygame.font.Font(self.PATH_TO_FONT, self.SIZE)
        # Рендер текста
        text_surface = self.font.render(self.TEXT, True, "white")
        width , height = text_surface.get_size()
        # Масштабирование текста до заданных размеров
        self.text_surface = pygame.transform.scale(text_surface,(self.MAX_WIDTH, self.MAX_HEIGHT))
        self.text_surface = self.text_surface.convert_alpha()

    def draw(self, screen: pygame.Surface):
        self.text_surface.set_alpha(self.VISIBLE)
        screen.blit(self.text_surface, (self.X_COR, self.Y_COR))

    def fade_in(self):
        if self.VISIBLE < 255:
            self.VISIBLE += 5
            if self.VISIBLE >= 255:
                self.VISIBLE = 255

    def fade_out(self):
        if self.VISIBLE > 0:
            self.VISIBLE -= 5
            if self.VISIBLE <= 0:
                self.VISIBLE = 0

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
                if self.Y_COR > -(self.SIZE + (422 - (self.TARGET_Y + self.SIZE))):
                    self.Y_COR -= self.SPEED
                    self.fade_out()
                    if self.Y_COR <= -(self.SIZE + (422 - (self.TARGET_Y + self.SIZE))):
                        self.Y_COR = -(self.SIZE + (422 - (self.TARGET_Y + self.SIZE)))
                        self.TURN = "Down"

        if self.Y_COR == self.TARGET_Y or self.Y_COR == -(self.SIZE + (422 - (self.TARGET_Y + self.SIZE))):
            self.ACTIVE = False

list_first_task = ["2 hits in a row" , "4 hits in a row" , "Kill one three-decker ship"]
list_second_task = ["Kill 3 double-decker ships in a row" , "Kept all ships alive for 5 turns" , "Kill two ships in a row"]
list_third_task = ["The first to kill a 4 deck ship"  , "Kill 4 single-deck ships in a row", "Buy one bonus from the store"]
list_fourth_task = ["The first step is murder" , "Killed three ships in a row" , "Completed the first three tasks"]

first_task = Font_Shop(
    x_cor = 52 ,
    y_cor = -(45 + (422 - (136 + 45))),
    size = 45 ,
    name_font = "Jersey15.ttf",
    text = random.choice(list_first_task),
    target_y = 136 , 
    max_width = 161 ,
    max_height = 31
)

second_task = Font_Shop(
    x_cor = 52 ,
    y_cor = -(25 + (422 - (192 + 25))),
    size = 25 ,
    name_font = "Jersey15.ttf",
    text = random.choice(list_second_task),
    target_y = 192 , 
    max_width = 220 ,
    max_height = 28

)

third_task = Font_Shop(
    x_cor = 52 ,
    y_cor = -(25 + (422 - (244 + 25))),
    size = 25 ,
    name_font = "Jersey15.ttf",
    text = random.choice(list_third_task),
    target_y = 244 ,
    max_width = 180 ,
    max_height = 28
)

fourth_task = Font_Shop(
    x_cor = 52 ,
    y_cor = - (25 + (422 - (298 + 25))),
    size = 25 ,
    name_font = "Jersey15.ttf",
    text = random.choice(list_fourth_task),
    target_y = 298 ,
    max_width = 225 ,
    max_height = 31
)

shop_item.extend([first_task , second_task , third_task , fourth_task])

    