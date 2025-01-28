from os.path import abspath, join
import pygame

class Font:
    '''
    ### Класс для работы с шрифтами ###
    '''
    def __init__(self, size : int, name_font : str, text : str,x_cor : int, y_cor : int , text_color:str ,screen : pygame.Surface):
        '''
        #### Метод конструктор, который позволит нам создавать `шрифты` для `текста` ####

        Атрибути:
        - :mod:`color_text`: Колір тексту
        - :mod:`size`: Розмір шрифту
        - :mod:`name_font`: Назва шрифту
        - :mod:`path_to_font`: Шлях до файлу шрифту
        - :mod:`text`: Текст для відображення
        - :mod:`screen`: Поверхня, на якій буде відображатись текст
        - :mod:`x_cor`: Координата X тексту
        - :mod:`y_cor`: Координата Y тексту
        - :mod:`font`: Об'єкт шрифту Pygame
        - :mod:`text_surface`: Поверхня з текстом для відображення
        '''
        self.color_text = text_color
        self.size = size
        self.name_font = name_font
        #f"/../../../media/fonts/{self.name_font}"
        self.path_to_font = abspath(join(__file__, "..", "..", "..", "media", "fonts", f"{self.name_font}"))
        self.text = text
        self.screen = screen
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.font = pygame.font.Font(self.path_to_font, self.size)
        self.text_surface = self.font.render(self.text, False, self.color_text)
    def draw_font(self):
        '''
        `Метод` который `отрисовывает` в `указанных` `атрибутах` на `указанном` `экране`
        '''
        self.screen.blit(self.text_surface, (self.x_cor , self.y_cor))
    def update_text(self):
        '''
        `Метод` который `обновляет` текст шрифта на `новый` `текст`
        '''
        self.text_surface = self.font.render(self.text, False, self.color_text)




        