import pygame, random
from os.path import abspath, join
from .shop_image import shop_item
from ..screens import FPS
from os.path import abspath, join
from ..classes import buy_product_sound
from ..volume_settings import turn_off_volume_func, volume_up_func, volume_down_func
from .shop_image import done_task_four, done_task_one, done_task_two, done_task_three, shop_item
from .text_shop import list_first_task, list_second_task, list_third_task, list_fourth_task, first_task, second_task, third_task,fourth_task, money_list


#класс для кнопки в магазині
class Button_Shop:
    #створюємо конструктор(__init__) кнопки
    def __init__(self, x, y, image_name, height,width,  target_y: int ,action = None):
        self.X_COR = x
        self.IMAGE_NAME = image_name
        self.Y_COR = y
        self.WIDTH = width
        self.HEIGHT = height
        #os.path.abspath(__file__ + f"/../../../static/images_button/shop_buttons/{self.IMAGE_NAME}")
        self.PATH_IMAGE1 = abspath(join(__file__, "..", "..", "..", "static", "images_button", "shop_buttons", f"{self.IMAGE_NAME}"))
        self.IMAGE = pygame.transform.scale(pygame.image.load(self.PATH_IMAGE1), (self.WIDTH , self.HEIGHT))
        self.RECT = self.IMAGE.get_rect(topleft=(self.X_COR, self.Y_COR))
        self.RECT.height -= 13
        self.ACTION = action
        self.ACTIVE = False 
        self.TURN = "Down"
        self.VISIBLE = 0
        self.TARGET_Y = target_y
        self.SPEED = 13


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
    # Кнопка може плавно переміщатися вниз (до цільової позиції) і назад
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
                    self.fade_in()
                    self.Y_COR += current_speed
                    self.RECT.y += current_speed
                    if self.Y_COR >= self.TARGET_Y:  
                        self.Y_COR = self.TARGET_Y
                        self.RECT.y == self.TARGET_Y
                        self.TURN = "Up"  

            elif self.TURN == "Up":
                if self.Y_COR > -(self.HEIGHT + (832- (self.TARGET_Y + self.HEIGHT))):  
                    self.Y_COR -= current_speed
                    self.RECT.y -= current_speed
                    self.VISIBLE = 0
                    if self.Y_COR <= -(self.HEIGHT + (832- (self.TARGET_Y + self.HEIGHT))):  
                        self.Y_COR = -(self.HEIGHT + (832- (self.TARGET_Y + self.HEIGHT)))
                        self.RECT.y = -(self.HEIGHT + (832- (self.TARGET_Y + self.HEIGHT)))
                        self.TURN = "Down"  

        # Сброс состояния только для завершенной анимации
        if self.Y_COR == self.TARGET_Y or self.Y_COR == -(self.HEIGHT + (832- (self.TARGET_Y + self.HEIGHT))):
            self.ACTIVE = False

# # копии списков с задниями чтоюы моэно было брать новые
first_tasks_copy = list_first_task.copy()
second_tasks_copy = list_second_task.copy()
third_tasks_copy = list_third_task.copy()
fourth_tasks_copy = list_fourth_task.copy()
# # def new_tasks():
# #     if done_task_three in shop_item:
# #         done_task_three.VISIBLE = 0
# #     if done_task_two in shop_item:
# #         done_task_two.VISIBLE = 0
# #     if done_task_one in shop_item:
# #         done_task_one.VISIBLE = 0
# #     if done_task_four in shop_item:
# #         done_task_four.VISIBLE = 0
# #     first_task.TEXT = random.choice(first_tasks_copy)
# #     first_task.update_text_for_task()
# #     second_task.TEXT = random.choice(second_tasks_copy)
# #     second_task.update_text_for_task()
# #     third_task.TEXT = random.choice(third_tasks_copy)
# #     third_task.update_text_for_task()
# #     fourth_task.TEXT = random.choice(fourth_tasks_copy)
# #     fourth_task.update_text_for_task()


def test():
    print("Hello world!") 

# список в котором храним сколько потртили монет
waste_money = [0]

flag_arson = ["no"]
flag_put_out_the_fire = ["no"]
def buy_fire_rocket():
    if money_list[0] >= 80:
        buy_product_sound.play2(loops = 1)
        waste_money[0] += 80
        flag_arson[0] = "yes"

def buy_fire_fighter():
    if flag_put_out_the_fire[0] == "no":
        if money_list[0] >= 50:
            buy_product_sound.play2(loops = 1)
            flag_put_out_the_fire[0] = "yes"
            waste_money[0] += 50

# флаг для проверки того , купил ли игрок бомбу.True - значиит что купил
check_buy_bomb_attack = [False]
def buy_bomb():
    if money_list[0] >= 150:
        if check_buy_bomb_attack[0] == False:
            buy_product_sound.play2(loops = 1)
            if check_buy_bomb_attack[0] == False:
                waste_money[0] += 150
                check_buy_bomb_attack[0] = True
                

flagbimb200=["no"]
cheak = [9,19,29,39,49,59,69,79,89,99,10,20,30,40,50,60,70,80,90,100]
check_2= [11,12,13,14,15,16,17,18,19,20]
def buy_auto_rocket():
    if money_list[0] >= 200:
        buy_product_sound.play2(loops = 1)
        if flagbimb200[0] == "no":
            waste_money[0] += 200
            flagbimb200[0] = "yes"
            
but_flag = [False]
def buy_restore_cell():
    if money_list[0] >= 75:
        buy_product_sound.play2(loops = 1)
        if but_flag[0] == False:
            waste_money[0] += 75
            but_flag[0] = True

flag_radar = [False]
def buy_radar():
    if money_list[0] >= 20:
        buy_product_sound.play2(loops = 1)
        if flag_radar[0] == False:
            waste_money[0] += 20
            flag_radar[0] = True

random_hits = [False]
def buy_random_hits():
    if money_list[0] >= 25:
        buy_product_sound.play2(loops = 1)
        if random_hits[0] == False:
            waste_money[0] += 25
            random_hits[0] = True
            

button_radar = Button_Shop(
    x = 472,
    y = -(35 + (832- (214 + 38))),
    width = 103,
    height = 38,
    image_name = "radar.png",
    action = buy_radar,
    target_y = 214
)
# створюємо елементи від цього класу
button_random_hits = Button_Shop(
    x = 600 ,
    y = -(98 + (832- (263 + 98))),
    width = 96 ,
    height = 98 ,
    image_name = "random_hits.png",
    target_y = 263,
    action = buy_random_hits,
)

button_stop_fire = Button_Shop(
    x = 710 ,
    y = -(98 + (832- (263 + 98))) ,
    width = 96 ,
    height = 98 ,
    image_name = "stop_fire.png",
    target_y = 263,
    action = buy_fire_fighter
)

button_restores_cell = Button_Shop(
    x = 820 ,
    y = -(105 + (832- (263 + 105))),
    width = 96 ,
    height = 105 ,
    image_name = "restore_one_cell.png",
    target_y = 263,
    action = buy_restore_cell
)

button_fire_rocket = Button_Shop(
    x = 930 ,
    y = -(98 + (832- (263 + 98))),
    width = 96 ,
    height = 98 ,
    image_name = "fire_rocket.png",
    target_y = 263,
    action = buy_fire_rocket
)

button_bomb = Button_Shop(
    x = 1040 ,
    y = -(97 + (832- (263 + 97))),
    width = 96 ,
    height = 97 ,
    image_name = "bomb.png",
    target_y = 263,
    action = buy_bomb
)

button_auto_attack = Button_Shop(
    x = 1150 ,
    y = -(105 + (832- (263 + 105))),
    width = 96 ,
    height = 105 ,
    image_name = "auto_rocket.png",
    target_y = 263,
    action = buy_auto_rocket
)

volume_up = Button_Shop(
    x = 1007, 
    y = -(71 + (832 - (8 + 71))), 
    width = 74, 
    height = 71, 
    image_name = "button_volue_up.png", 
    action = volume_up_func,
    target_y = 8
)

volume_down = Button_Shop(
    x = 1099, 
    y = -(71 + (832 - (8 + 71))), 
    width = 74, 
    height = 71, 
    image_name = "button_music_lower.png", 
    action = volume_down_func,
    target_y = 8
)

turn_off_button = Button_Shop(
    x = 1191,
    y = -(71 + (832 - (8 + 71))),
    width = 74, 
    height = 71, 
    image_name = "off_music_hover.png", 
    action = turn_off_volume_func,
    target_y = 8
)

# new_random_tasks = Button_Shop(
#     x = 331 ,
#     y = -(21 + (832 - (350 + 21))),
#     width = 80,
#     height = 21,
#     image_name = 'new_tasks.png',
#     target_y = 349,
#     action = new_tasks
# )



# додаємо кнопки до списку де збергіються елементи магазину , щоб можна було через цикл їх всіх відмалювати
shop_item.extend([button_restores_cell ,button_random_hits , button_auto_attack , button_bomb , button_fire_rocket , button_stop_fire, volume_up, volume_down,turn_off_button, button_radar])
