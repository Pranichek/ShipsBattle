import os
import pygame

class Font:
    def __init__(self, size : int, name_font : str, text : str,x_cor : int, y_cor : int ,screen : pygame.Surface):
        self.size = size
        self.name_font = name_font
        self.path_to_font = os.path.abspath(__file__ + f"/../../../media/fonts/{self.name_font}")
        self.text = text
        self.screen = screen
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.font = pygame.font.Font(self.path_to_font, self.size)
        self.text_surface = self.font.render(self.text, True, "white")
    def draw_font(self):
        self.screen.blit(self.text_surface, (self.x_cor , self.y_cor))
    def update_text(self):
        self.text_surface = self.font.render(self.text, True, "white")




        