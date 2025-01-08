import pygame
from os.path import abspath, join

pygame.init()
#координаты  x y , width , height , active , image_name
class Medal:
    def __init__(self, x_cor: int, y_cor: int, width: int, height: int, image_name: str , medal_image_description: str):
        self.X_COR = x_cor
        self.Y_COR = y_cor
        self.WIDTH = width
        self.HEIGHT = height
        self.MEDAL_IMAGE_NAME = image_name
        self.MEDAL_IMAGE_DESCRIPTION = medal_image_description
        #__file__ - хранит до файла в котором она находится
        # .. = ".."
        self.PATH_IMAGE = abspath(join(__file__, "..", "..", "..", "media", "achievement", f"{self.MEDAL_IMAGE_NAME}.png"))
        self.MEDAL_DESDESCRIPTION_PATH = abspath(join(__file__, "..", "..", "..", "media", "achievement", f"{self.MEDAL_IMAGE_DESCRIPTION}.png"))
        self.MEDAL_IMAGE = pygame.transform.scale(pygame.image.load(self.PATH_IMAGE), (self.WIDTH, self.HEIGHT))
        self.MEDAL_DESDESCRIPTION_IMAGE = pygame.transform.scale(pygame.image.load(self.MEDAL_DESDESCRIPTION_PATH), (self.WIDTH + 100, self.HEIGHT + 80))
        self.ACTIVE = False
        self.VISIBLE = 100
        self.DESCRIPRION_VISIBLE = 0
        self.RECT = self.MEDAL_IMAGE.get_rect(topleft=(self.X_COR, self.Y_COR))
    def draw_medals(self, screen: pygame.Surface):
        self.MEDAL_IMAGE.set_alpha(self.VISIBLE)
        screen.blit(self.MEDAL_IMAGE , (self.X_COR, self.Y_COR))
    #для самой медали
    def fade_in(self):
        if self.VISIBLE < 255:
            self.VISIBLE += 5  
            if self.VISIBLE >= 255:
                self.VISIBLE = 255  
    # для окошка под медлью
    def fade_in_descriprion(self):
        if self.DESCRIPRION_VISIBLE < 255:
            self.DESCRIPRION_VISIBLE += 5  
            if self.DESCRIPRION_VISIBLE >= 255:
                self.DESCRIPRION_VISIBLE = 255  
    def fade_out_description(self):
        if self.DESCRIPRION_VISIBLE > 0:
            self.DESCRIPRION_VISIBLE -= 5  
            if self.DESCRIPRION_VISIBLE <= 0:
                self.DESCRIPRION_VISIBLE = 0

    def completed_task(self):
        if self.ACTIVE == True:
            self.fade_in()
            
    def show_descriptions(self, screen: pygame.Surface):
        mouse = pygame.mouse.get_pos()
        if self.RECT.collidepoint(mouse):
            self.fade_in_descriprion()
            self.MEDAL_DESDESCRIPTION_IMAGE.set_alpha(self.DESCRIPRION_VISIBLE)
            screen.blit(self.MEDAL_DESDESCRIPTION_IMAGE , (self.X_COR - 50, self.Y_COR + 40))
        else:
            self.fade_out_description()
            self.MEDAL_DESDESCRIPTION_IMAGE.set_alpha(self.DESCRIPRION_VISIBLE)
            screen.blit(self.MEDAL_DESDESCRIPTION_IMAGE , (self.X_COR - 50, self.Y_COR + 40))

           
    

            
test_medal = Medal(x_cor = 100, y_cor = 131, width = 50, height = 50, image_name = "medal_four_decker" , medal_image_description = "auto_sight")

    # def fade_out_description(self):
    #     if self.VISIBLE > 0:
    #         self.VISIBLE -= 5  
    #         if self.VISIBLE <= 0:
    #             self.VISIBLE = 0