import pygame
from os.path import abspath, join
from .class_click import music_click

# создаем класс кнопки
class Button:
    '''
    ### Класс для создания кнопок на экране ###
    '''
    # создаем метод конструктор этого класса, в который приниамем следущие парамтеры
    #x: int, y: int, image_path:str, image_hover_path:str, height:int,width:int, action=None)
    def __init__(self, x: int, y: int, image_path:str, image_hover_path:str, height:int,width:int, action=None):
        '''
        #### Метод конструктор, который позволит нам создавать `кнопки` ####
        Атрибуты:

        - :mod:`ANIMATION_SPEED`: скорость анимации (определяет, как быстро будет сменяться кадр).
        - :mod:`IMAGE_NAME`: имя исходного изображения для анимации.
        - :mod:`LIST_IMAGES`: список изображений, составляющих анимацию.
        - :mod:`COUNT_IMAGES`: индекс текущего изображения в списке.
        - :mod:`COUNT_MAIN_LOOP`: счётчик для управления темпом анимации.
        - :mod:`WIDTH`: ширина изображения.
        - :mod:`HEIGHT`: высота изображения.
        - :mod:`IMAGE`: текущее изображение для отображения.
        - :mod:`X_COR`: горизонтальная координата для рисования изображения.
        - :mod:`Y_COR`: вертикальная координата для рисования изображения.
        - :mod:`NEED_CLEAR`: флаг, указывающий, нужно ли очищать анимацию после её окончания.
        - :mod:`NAME_FOLDER`: имя папки с изображениями для анимации.
        - :mod:`IS_ANIMATION_DONE`: флаг, показывающий завершение анимации.

        Пример использования : 
        ```python
        shop_and_tasks = Button(x= 33 , y = 32,image_path= "show_shop.png" , image_hover_path= "show_shop_hover.png" , width = 36, height = 31 , action = show_shop)
        ```
        '''
        # создаем свойства для класса кнопки
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image1 = abspath(join(__file__, "..", "..", "..", "static", "images_button", f"{image_path}"))
        self.image2 = abspath(join(__file__, "..", "..", "..", "static", "images_button", f"{image_hover_path}"))
        self.image = pygame.transform.scale(pygame.image.load(self.image1), (self.width, self.height))
        self.image_hover = pygame.transform.scale(pygame.image.load(self.image2), (self.width, self.height))
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.action = action
    # создаем метод который отрисовывает кнопку
    def draw(self, surface):
        '''
        `Метод` который позволит нам `отрисовывать` `кнопку`, на `указанном` `экране` - `surface`
        '''
        # получаем текущую позицию мыши
        mouse_pos = pygame.mouse.get_pos()
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        # если курсор мыши находится внутри области кнопки, отрисовываем кнопку с изображением наведения
        if self.rect.collidepoint(mouse_pos):
            surface.blit(self.image_hover, self.rect.topleft)
        # если курсор мыши не находится внутри области кнопки, отрисовываем кнопку с изображением изначального состояния
        else:
            surface.blit(self.image, self.rect.topleft)
    # метод который проверяет нажали ли на кнопку, и если да, то запускаем функцию которая должна отрабатывать при нажатии на кнопку
    def check_click(self, event):
        '''
        - :mod:`event`: `События` в `pygame`
        
        `Метод` который позволит нам `проверить`, была ли `нажата` `кнопка`, и если да, то `запускать` `функцию` - `action` ,
        так же `проигрывать` `звук` `нажатия`
        '''
        # проверяем если событие было нажатие мыши и кнопка была нажата(кнопка левая кнопка мыши)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  
            # получаем текущую позицию мыши
            mouse = pygame.mouse.get_pos()
            # если курсор мыши находится внутри области кнопки, запускаем функцию action, которая должна отрабатывать при нажатии на кнопку
            if self.rect.collidepoint(mouse):
                if self.action:
                    music_click.play2(loops = 1)
                    self.action()