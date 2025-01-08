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
        self.PATH_IMAGE = abspath(join(__file__, "..", "..", "..", "media", "achievement", "medals", f"{self.MEDAL_IMAGE_NAME}.png"))
        self.MEDAL_DESDESCRIPTION_PATH = abspath(join(__file__, "..", "..", "..", "media", "achievement", "description_medals",f"{self.MEDAL_IMAGE_DESCRIPTION}.png"))
        self.MEDAL_IMAGE = pygame.transform.scale(pygame.image.load(self.PATH_IMAGE), (self.WIDTH, self.HEIGHT))
        self.MEDAL_DESDESCRIPTION_IMAGE = pygame.transform.scale(pygame.image.load(self.MEDAL_DESDESCRIPTION_PATH), (self.WIDTH + 121, self.HEIGHT + 46))
        self.ACTIVE = False
        self.VISIBLE = 100
        self.DESCRIPRION_VISIBLE = 0
        self.RECT = self.MEDAL_IMAGE.get_rect(topleft=(self.X_COR - 10, self.Y_COR + 5))
        self.RECT = self.RECT.inflate(-20, -20)
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
            self.DESCRIPRION_VISIBLE += 20
            if self.DESCRIPRION_VISIBLE >= 255:
                self.DESCRIPRION_VISIBLE = 255  
    def fade_out_description(self):
        if self.DESCRIPRION_VISIBLE > 0:
            self.DESCRIPRION_VISIBLE -= 20
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
            screen.blit(self.MEDAL_DESDESCRIPTION_IMAGE , (self.X_COR - 60, self.Y_COR + 50))
        else:
            self.fade_out_description()
            self.MEDAL_DESDESCRIPTION_IMAGE.set_alpha(self.DESCRIPRION_VISIBLE)
            screen.blit(self.MEDAL_DESDESCRIPTION_IMAGE , (self.X_COR - 60, self.Y_COR + 50))

           
            
four_decker_sniper_medal = Medal(x_cor = 750, y_cor = 24, width = 60, height = 60, image_name = "medal_four_decker" , medal_image_description = "four_decker_sniper")
auto_sight_medal = Medal(x_cor = 900, y_cor = 24, width = 55, height = 55, image_name = "auto_sight_medal", medal_image_description = "auto_sight")
destroyer_medal = Medal(x_cor = 850, y_cor = 68, width = 60, height = 60, image_name = "destroyer", medal_image_description = "destroyer")
first_hit_medal = Medal(x_cor = 800, y_cor = 26, width = 60, height = 60, image_name = "first_hit_medal", medal_image_description = "first_shot")
lone_hunter_medal = Medal(x_cor = 850, y_cor = 24, width = 60, height = 60, image_name = "lone_hunter_medal", medal_image_description = "lone_hunter")
master_of_disguist_medal = Medal(x_cor = 800, y_cor = 64, width = 60, height = 60, image_name = "master_of_disguist_medal", medal_image_description = "master_of_diguise")
opening_battle_medal = Medal(x_cor = 900, y_cor = 64, width = 60, height = 60, image_name = "medal_opening_the_battle", medal_image_description = "opening_the_battle")
perfectionists_medal = Medal(x_cor = 1000, y_cor = 64, width = 60, height = 60, image_name = "medal_perfectionists", medal_image_description = "monster_of_perfections")
perfect_shooter_medal = Medal(x_cor = 995, y_cor = 24, width = 70, height = 60, image_name = "perfect_shooter_medal", medal_image_description = "perfect_shooter")
pioneer_medal = Medal(x_cor = 950, y_cor = 24, width = 60, height = 60, image_name = "pioneer_medal", medal_image_description = "pioneer")
strategist_medal = Medal(x_cor = 750, y_cor = 64, width = 60, height = 60, image_name = "strategist_medal", medal_image_description = "strategist")
target_attack_medal = Medal(x_cor = 950, y_cor = 64, width = 60, height = 60, image_name = "target_attack_medal", medal_image_description = "targeted_attack")
player_medal = [four_decker_sniper_medal, auto_sight_medal, destroyer_medal, first_hit_medal, lone_hunter_medal, master_of_disguist_medal, opening_battle_medal, perfectionists_medal, perfect_shooter_medal, pioneer_medal, strategist_medal, target_attack_medal]

enemy_four_decker_sniper_medal = Medal(x_cor = 220, y_cor = 24, width = 60, height = 60, image_name = "medal_four_decker" , medal_image_description = "four_decker_sniper")
enemy_auto_sight_medal = Medal(x_cor = 370, y_cor = 24, width = 55, height = 55, image_name = "auto_sight_medal", medal_image_description = "auto_sight")
enemy_destroyer_medal = Medal(x_cor = 320, y_cor = 68, width = 60, height = 60, image_name = "destroyer", medal_image_description = "destroyer")
enemy_first_hit_medal = Medal(x_cor = 270, y_cor = 26, width = 60, height = 60, image_name = "first_hit_medal", medal_image_description = "first_shot")
enemy_lone_hunter_medal = Medal(x_cor = 320, y_cor = 24, width = 60, height = 60, image_name = "lone_hunter_medal", medal_image_description = "lone_hunter")
enemy_master_of_disguist_medal = Medal(x_cor = 270, y_cor = 64, width = 60, height = 60, image_name = "master_of_disguist_medal", medal_image_description = "master_of_diguise")
enemy_opening_battle_medal = Medal(x_cor = 370, y_cor = 64, width = 60, height = 60, image_name = "medal_opening_the_battle", medal_image_description = "opening_the_battle")
enemy_perfectionists_medal = Medal(x_cor = 470, y_cor = 64, width = 60, height = 60, image_name = "medal_perfectionists", medal_image_description = "monster_of_perfections")
enemy_perfect_shooter_medal = Medal(x_cor = 465, y_cor = 24, width = 70, height = 60, image_name = "perfect_shooter_medal", medal_image_description = "perfect_shooter")
enemy_pioneer_medal = Medal(x_cor = 420, y_cor = 24, width = 60, height = 60, image_name = "pioneer_medal", medal_image_description = "pioneer")
enemy_strategist_medal = Medal(x_cor = 220, y_cor = 64, width = 60, height = 60, image_name = "strategist_medal", medal_image_description = "strategist")
enemy_target_attack_medal = Medal(x_cor = 420, y_cor = 64, width = 60, height = 60, image_name = "target_attack_medal", medal_image_description = "targeted_attack")
enemy_medals = [enemy_four_decker_sniper_medal,enemy_auto_sight_medal,enemy_destroyer_medal,enemy_first_hit_medal,enemy_lone_hunter_medal,enemy_master_of_disguist_medal,enemy_opening_battle_medal,enemy_perfectionists_medal,enemy_perfect_shooter_medal,enemy_pioneer_medal,enemy_strategist_medal,enemy_target_attack_medal]



