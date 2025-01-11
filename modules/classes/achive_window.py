import pygame 
from os.path import abspath, join
from ..classes import music_achieve
from ..screens import FPS
pygame.init()

list_achieves = []

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
        self.PATH_BORDER_IMAGE = abspath(join(__file__, "..", "..", "..", "media", "achievement", "achievement_windows", f"{self.IMAGE_NAME}.png"))
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
        self.CHECK_END_ANIM = False
        self.DIRECTION = None
        self.VISIBLE = 0 
        self.COUNT_REPEAT = 0 
        self.COUNT_MOVE = 0

    def move(self):
        current_procent = 60 / (FPS.get_fps() + 10)
        if self.ACTIVE == True:
            if self.COUNT_REPEAT == 0:
                music_achieve.play2(loops = 1)
            if self.COUNT_MOVE >= 50: 
                    # Перевіряємо кількість повторів
                    # Повертаємо вікно до початкової позиції
                    if self.X_COR < 640:
                        self.X_COR += 1 * current_procent  
                    if self.Y_COR > 100:
                        self.Y_COR -= 0.8 * current_procent  
                    if self.WIDTH > 122:
                        self.WIDTH -= 5 * current_procent  
                    if self.HEIGHT > 97:
                        self.HEIGHT -= 4 * current_procent  
                    self.BORDER_IMAGE = pygame.transform.scale(pygame.image.load(self.PATH_BORDER_IMAGE), (self.WIDTH, self.HEIGHT)).convert_alpha()
                    self.fade_out()
                    if self.X_COR >= 540:
                        self.reset()
                        self.ACTIVE = False 
                    return False

            if not self.CHECK_END_ANIM:
                # Рух до початкової позиції (вліво)
                if self.X_COR > self.X_MAX:
                    self.X_COR -= 3.4 * current_procent  
                if self.WIDTH < self.MAX_WIDTH:
                    self.WIDTH += 5 * current_procent  
                    self.fade_in()
                else:
                    self.WIDTH = self.MAX_WIDTH
                if self.HEIGHT < self.MAX_HEIGHT:
                    self.HEIGHT += 4 * current_procent  
                else:
                    self.HEIGHT = self.MAX_HEIGHT
                    self.CHECK_END_ANIM = True
            elif self.CHECK_END_ANIM:
                # Горизонтальний рух (вправо/вліво)
                if self.DIRECTION == "More":
                    if self.WIDTH > 337:
                        self.WIDTH -= 0.7 * current_procent  
                    if self.HEIGHT > 265:
                        self.HEIGHT -= 0.7 * current_procent  
                    if self.X_COR < self.X_MAX + 20:  # Рух вправо
                        self.X_COR += 0.1 * current_procent  
                    if self.WIDTH <= 337 and self.HEIGHT <= 265:
                        self.DIRECTION = "Less"
                        self.COUNT_MOVE += 1 
                elif self.DIRECTION == "Less":
                    if self.WIDTH < self.MAX_WIDTH:
                        self.WIDTH += 0.7 * current_procent  
                    if self.HEIGHT < self.MAX_HEIGHT:
                        self.HEIGHT += 0.7 * current_procent  
                    if self.X_COR > self.X_MAX:  # Рух вліво
                        self.X_COR -= 0.1 * current_procent  
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

strategist_achievement = Acievement(achievement_image_name = "strategist")

first_hit_achievement = Acievement(achievement_image_name = "first_hit")

master_of_disguist_achievement = Acievement(achievement_image_name = "master_of_disguise")

piooner_achievement = Acievement(achievement_image_name = "pioneer")

lone_hunter_achievement = Acievement(achievement_image_name = "lone_hunter")

opening_the_battle_achievement = Acievement(achievement_image_name = "opening_the_battle")

perfictionists_achiement = Acievement(achievement_image_name = "perfictionists_achiv")

target_attack_achievement = Acievement(achievement_image_name = "target_attack")

destroyer_achievement = Acievement(achievement_image_name = "destroyer_window")

list_achieves.extend([first_four_decker_achivment , ten_shoot_in_row_achievement , strategist_achievement , first_hit_achievement , master_of_disguist_achievement , piooner_achievement ,lone_hunter_achievement , opening_the_battle_achievement , perfictionists_achiement , target_attack_achievement, destroyer_achievement])


