import pygame 
import os

pygame.init()


class InputText:
    def __init__(self, width : int, height : int, x_cor : int, y_cor : int, base_text : str,name_image : str,
                screen_name : str, font_name : str):
        self.width = width
        self.height = height
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.base_text = base_text
        self.screen_name = screen_name
        self.font_name = font_name
        self.user_text = f"{self.base_text}"
        self.active = False
        self.name_image = name_image
        self.font = None
        self.max_length = 13
        self.rect = pygame.Rect(self.x_cor, self.y_cor, self.width, self.height)
        self.load_image()
        self.load_font(font_name)
    def load_image(self):
        image_path = os.path.abspath(__file__ + f"/../../../images/images_button/{self.name_image}")
        self.image = pygame.image.load(image_path)
        transform_image = pygame.transform.scale(self.image , (self.width, self.height))
        self.image = transform_image    
    
    def load_font(self, font_name : str): 
            font_path = os.path.abspath(__file__ + f"/../../../fonts/{font_name}")
            self.font = pygame.font.Font(font_path, size = 48)

    def check_event(self, event : object):
        if self.active == True:
            if self.user_text == self.base_text:
                self.user_text = ""
    # Якщо текстове поле неактивне, встановлюємо значення "nickname", якщо поле пусте
        elif self.active == False:
            if self.user_text == "":
                self.user_text = self.base_text
        # Обработка событий
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                self.active = True
            elif not self.rect.collidepoint(pos):
                self.active = False


        if self.base_text == "nickname":
                self.max_length = 10
        else:
                self.max_length = 13

        if event.type == pygame.KEYDOWN and self.active == True:
            # Если поле активно, обрабатываем ввод текста
            if event.key == pygame.K_BACKSPACE:
                self.user_text = self.user_text[:-1]
            elif len(self.user_text) < self.max_length:
                self.user_text += event.unicode

    def draw_text(self):
       
         # Очистити базовий текст тільки при активаці

        text_surface = self.font.render(self.user_text, True, "white")
        self.screen_name.blit(self.image, (self.x_cor, self.y_cor))
        if self.user_text == "port":
            self.screen_name.blit(text_surface, (self.x_cor + 125, self.y_cor + 13))
        else:
            self.screen_name.blit(text_surface, (self.x_cor + 90, self.y_cor + 13))
