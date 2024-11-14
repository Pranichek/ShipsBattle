import os
import pygame

class Font:
    def __init__(self, size : int, name_font : str, text : str,x_cor : int, y_cor : int ,screen : pygame.Surface):
        self.size = size
        self.name_font = name_font
        self.path_to_font = os.path.abspath(__file__ + f"/../../../fonts/{self.name_font}")
        self.text = text
        self.screen = screen
        self.x_cor = x_cor
        self.y_cor = y_cor
    def draw_font(self):
        font = pygame.font.Font(self.path_to_font, self.size)
        text = font.render(self.text, True, "white")
        self.screen.blit(text, (self.x_cor , self.y_cor))


        