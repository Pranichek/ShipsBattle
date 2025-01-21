import pygame
from os.path import abspath, join
import modules.screens as screen_module


class Animation():
    def __init__(self, image_name: str , width: int , height: int , x_cor: int , y_cor: int , need_clear: bool , name_folder: str ,animation_speed: int):
        self.ANIMATION_SPEED = animation_speed
        self.IMAGE_NAME = image_name
        self.LIST_IMAGES = []
        self.COUNT_IMAGES = 0
        self.COUNT_MAIN_LOOP = 0
        self.WIDTH = width
        self.HEIGHT = height  
        self.IMAGE = None
        self.X_COR = x_cor
        self.Y_COR = y_cor 
        self.NEED_CLEAR = need_clear  # Нужно ли очищать анимацию после ее проигрывания
        self.NAME_FOLDER = name_folder
        self.IS_ANIMATION_DONE = False  # Флаг который будет отслеживать завершение анимации
    def load_images(self):
        path = abspath(join(__file__, f"{self.IMAGE_NAME}"))
        image = pygame.image.load(path)
        transformed_image = pygame.transform.scale(image, (self.WIDTH, self.HEIGHT))
        self.IMAGE = transformed_image
    def animation(self, count_image: int, main_screen: pygame.Surface):
        fps = screen_module.FPS.get_fps()
        if screen_module.FPS.get_fps() <= 0:
            fps = 0.01
        current_speed = self.ANIMATION_SPEED * ((fps + 10) / 60)
        if len(self.LIST_IMAGES) == 0:
            for number in range(count_image):
                self.IMAGE_NAME = abspath(join(__file__, "..", "..", "..", "media", f"{self.NAME_FOLDER}", f"{number}.png"))
                self.load_images()
                self.LIST_IMAGES.append(self.IMAGE)

        if self.IS_ANIMATION_DONE and self.NEED_CLEAR == True:
            # Если анимация закончена, ничего не рисуем   
            return True

        self.IMAGE = self.LIST_IMAGES[self.COUNT_IMAGES]
        self.draw(screen=main_screen)

        if self.COUNT_MAIN_LOOP >= current_speed:
            if self.COUNT_IMAGES < count_image - 1:  # Проверяем, не конец ли анимации
                self.COUNT_IMAGES += 1
            else:
                self.IS_ANIMATION_DONE = True
                return True 
            self.COUNT_MAIN_LOOP = 0

        self.COUNT_MAIN_LOOP += 1

    def draw(self, screen: pygame.Surface):
        screen.blit(self.IMAGE, (self.X_COR, self.Y_COR))
    def clear_animation(self):
        self.LIST_IMAGES = []
        self.COUNT_IMAGES = 0
        self.COUNT_MAIN_LOOP = 0
        self.IS_ANIMATION_DONE = False

# анимация промаха ракетой
miss_rocket_animation = Animation(
    image_name = "0.png" , 
    width = 311, 
    height = 100, 
    x_cor = 311, 
    y_cor = 311, 
    need_clear = True, 
    name_folder = "animation_rocket",
    animation_speed = 3
)

#просто полет ракетой
rocket_animation = Animation(
    image_name = "0.png", 
    width = 311, 
    height = 100, 
    x_cor = 311, 
    y_cor = 311, 
    need_clear = True,
    name_folder = "animation_rocket",
    animation_speed = 3
)
# промах ракеты
miss_rocket = Animation(
    image_name = "0.png" , 
    width = 270, 
    height = 85, 
    x_cor = 311, 
    y_cor = 311, 
    need_clear = True, 
    name_folder = "animation_miss_rocket",
    animation_speed = 4
)
# анимация взрыва после ракеты
animation_boom = Animation(
    image_name = "0.png" , 
    width = 100, 
    height = 100, 
    x_cor = 500, 
    y_cor = 500, 
    need_clear = True, 
    name_folder = "animation_boom",
    animation_speed = 3
)

# анимация бомбы
bomb_animation = Animation(
    image_name = "0.png",
    width = 321,
    height = 120,
    x_cor = 500,
    y_cor = 500,
    need_clear = True,
    name_folder = "bomb_animation",
    animation_speed = 3
)
# анимация взрыва после бомбы
animation_bomb_boom = Animation(
    image_name = "0.png" , 
    width = 220, 
    height = 220, 
    x_cor = 500, 
    y_cor = 500, 
    need_clear = True, 
    name_folder = "bomb_boom",
    animation_speed = 4
)

# анимация аптечки
animation_health = Animation(
    image_name = "0.png",
    width = 60,
    height = 60,
    x_cor = 500,
    y_cor = 500,
    need_clear = True,
    name_folder = "animation_medical",
    animation_speed = 4
)

# когда проблемы с соеденением
animation_connection_problem = Animation(
    image_name = "0.png",
    width = 901,
    height = 284,
    x_cor = 210,
    y_cor = 274,
    need_clear = False,
    name_folder = "error_connection_animation",
    animation_speed = 31
)


# анимации типо рандомного выбора игрока кто первый ходит
animation_random_player = Animation(
    image_name = "0.png",
    width = 414,
    height = 118,
    x_cor = 415,
    y_cor = 185,
    need_clear = True,
    name_folder = "animation_choice",
    animation_speed = 6
)

# анимация полета авторакеты
animation_auto_rocket = Animation(
    image_name = "0.png",
    width = 250,
    height = 70,
    x_cor = 415,
    y_cor = 185,
    need_clear = True,
    name_folder = "animation_auto_rocket",
    animation_speed = 4
)

# промах авто ракетой
miss_auto_rocket = Animation(
    image_name = "0.png",
    width = 250,
    height = 70,
    x_cor = 415,
    y_cor = 185,
    need_clear = True,
    name_folder = "animation_miss_auto_rocket",
    animation_speed = 4
)

# анимация радара
radar_animation = Animation(
    image_name = "0.png",
    width = 165,
    height = 165,
    x_cor = 415,
    y_cor = 185,
    need_clear = True,
    name_folder = "animation_radar",
    animation_speed = 4
)

# fire_rocket_animation
fire_rocket_animation = Animation(
    image_name = "0.png",
    width = 250,
    height = 131,
    x_cor = 415,
    y_cor = 185,
    need_clear = True,
    name_folder = "animation_fire_rocket",
    animation_speed = 4
)

fire_fighter_animation = Animation(
    image_name = "0.png",
    width = 250,
    height = 70,
    x_cor = 415,
    y_cor = 185,
    need_clear = True,
    name_folder = "fire_fighter_animation",
    animation_speed = 4
)

fire_animation = Animation(
    image_name = "0.png",
    width = 250,
    height = 70,
    x_cor = 415,
    y_cor = 185,
    need_clear = True,
    name_folder = "fire_animation",
    animation_speed = 4
)

