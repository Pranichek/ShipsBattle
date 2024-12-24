import pygame
import os 


class Button:
    def __init__(self, x, y, image_path, image_hover_path, height,width, action=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image1 = os.path.abspath(__file__ + f"/../../../static/images_button/{image_path}")
        self.image2 = os.path.abspath(__file__ + f"/../../../static/images_button/{image_hover_path}")
        self.image = pygame.transform.scale(pygame.image.load(self.image1), (self.width, self.height))
        self.image_hover = pygame.transform.scale(pygame.image.load(self.image2), (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.action = action

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            surface.blit(self.image_hover, self.rect.topleft)
        else:
            surface.blit(self.image, self.rect.topleft)

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            mouse = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse):
                if self.action:
                    self.action()
                    
