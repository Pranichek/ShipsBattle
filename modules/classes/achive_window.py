import pygame , os
from ..classes import music_achieve
pygame.init()


class Acievement:
    def __init__(self , achievement_image_name: str):
        self.IMAGE_NAME = achievement_image_name
        self.X_COR = 640
        self.Y_COR = 319
        self.X_MAX = 458
        self.WIDTH = 122
        self.HEIGHT = 97
        self.MAX_WIDTH = 354
        self.MAX_HEIGHT = 281
        self.PATH_BORDER_IMAGE = os.path.abspath(__file__ + f"/../../../media/achievement/{self.IMAGE_NAME}.png")
        self.BORDER_IMAGE = pygame.transform.scale(pygame.image.load(self.PATH_BORDER_IMAGE), (self.WIDTH, self.HEIGHT)).convert_alpha()
        # 
        self.ACTIVE = False 
        #
        self.CHECK_END_ANIM = False
        #
        self.DIRECTION = None
        self.VISIBLE = 0 
        self.COUNT_REPEAT = 0 
        self.COUNT_MOVE = 0
    # Плавно змінює прозорість зображення:fade_in() збільшує прозорість до 255 (повністю видимий стан)
    def fade_in(self):
        if self.VISIBLE < 311:
            self.VISIBLE += 5  
            if self.VISIBLE >= 311:
                self.VISIBLE = 311
     
    # fade_out() зменшує прозорість до 0 (невидимий стан)
    def fade_out(self):
        if self.VISIBLE > 0:
            self.VISIBLE -= 5  
            if self.VISIBLE <= 0:
                self.VISIBLE = 0
    def reset(self):
        self.X_COR = 640
        self.Y_COR = 319
        self.MAX_WIDTH = 354
        self.MAX_HEIGHT = 281
        self.ACTIVE = False 
        self.CHECK_END_ANIM = False
        self.DIRECTION = None
        self.VISIBLE = 0 
        self.COUNT_REPEAT = 0 
        self.COUNT_MOVE = 0

    def move(self):
        if self.ACTIVE == True:
            if self.COUNT_REPEAT == 0:
                music_achieve.play2(loops = 1)
            if self.COUNT_MOVE >= 155: 
                    # Перевіряємо кількість повторів
                    # Повертаємо вікно до початкової позиції
                    if self.X_COR < 640:
                        self.X_COR += 1    
                    if self.Y_COR > 100:
                        self.Y_COR -= 0.8
                    if self.WIDTH > 122:
                        self.WIDTH -= 5
                    if self.HEIGHT > 97:
                        self.HEIGHT -= 4

                    self.BORDER_IMAGE = pygame.transform.scale(pygame.image.load(self.PATH_BORDER_IMAGE), (self.WIDTH, self.HEIGHT)).convert_alpha()
                    self.fade_out()
                    if self.X_COR >= 540:
                        self.reset()
                    return False

            if not self.CHECK_END_ANIM:
                # Рух до початкової позиції (вліво)
                if self.X_COR > self.X_MAX:
                    self.X_COR -= 3.4
                if self.WIDTH < self.MAX_WIDTH:
                    self.WIDTH += 5
                    self.fade_in()
                else:
                    self.WIDTH = self.MAX_WIDTH
                if self.HEIGHT < self.MAX_HEIGHT:
                    self.HEIGHT += 4
                else:
                    self.HEIGHT = self.MAX_HEIGHT
                    self.CHECK_END_ANIM = True
            elif self.CHECK_END_ANIM:
                # Горизонтальний рух (вправо/вліво)
                if self.DIRECTION == "More":
                    if self.WIDTH > 337:
                        self.WIDTH -= 0.5
                    if self.HEIGHT > 265:
                        self.HEIGHT -= 0.5
                    if self.X_COR < self.X_MAX + 20:  # Рух вправо
                        self.X_COR += 1
                    if self.WIDTH <= 337 and self.HEIGHT <= 265:
                        self.DIRECTION = "Less"
                        self.COUNT_MOVE += 1
                elif self.DIRECTION == "Less":
                    if self.WIDTH < self.MAX_WIDTH:
                        self.WIDTH += 0.5
                    if self.HEIGHT < self.MAX_HEIGHT:
                        self.HEIGHT += 0.5
                    if self.X_COR > self.X_MAX:  # Рух вліво
                        self.X_COR -= 1
                    if self.WIDTH >= self.MAX_WIDTH and self.HEIGHT >= self.MAX_HEIGHT:
                        self.DIRECTION = "More"
                    self.COUNT_MOVE += 1
                else:
                    self.DIRECTION = "More"
            self.COUNT_REPEAT += 1
            self.BORDER_IMAGE = pygame.transform.scale(pygame.image.load(self.PATH_BORDER_IMAGE), (self.WIDTH, self.HEIGHT)).convert_alpha() 
            
                    


    def draw(self , screen: pygame.Surface):
        self.BORDER_IMAGE.set_alpha(self.VISIBLE)
        screen.blit(self.BORDER_IMAGE , (self.X_COR, self.Y_COR))

    
first_four_decker_achivment = Acievement(achievement_image_name = "four_decker_sniper")

ten_shoot_in_row_achievement = Acievement(achievement_image_name = "perfect_shooter")