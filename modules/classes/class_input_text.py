import pygame 
from os.path import abspath, join
from ..screens.screen import main_screen

pygame.init()

#створюємо клас
class InputText:
    #створюємо метод конструктор та додаємо параметри для нього 
    def __init__(self, width : int, height : int, x_cor : int, y_cor : int, base_text : str,name_image : str,
                screen_name : str, font_name : str):
        #створюємо властивості класа , для того щоб динамічно передавати різні дані
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
    #створюємо метод завантаження картинки
    def load_image(self):
        #знаходимо путь по якому завантажуємо картинку
        #"/../../../media/backgrounds/{self.name_image}
        image_path = abspath(join(__file__, "..", "..", "..", "media", "backgrounds", f"{self.name_image}"))
        self.image = pygame.image.load(image_path)
        #завантажуємо картинку зі шляху який ми знайшли та змінюємо по розмірам
        transform_image = pygame.transform.scale(self.image , (self.width, self.height))
        #зберігаємо картинку до властивості
        self.image = transform_image    
    
    #завантажуємо шрифт який ми будемо використовувати коли пишемо 
    def load_font(self, font_name : str): 
            #отримуємо шрифт по шляху та передаємо назву його(font_name)
            # "/../../../media/fonts/{font_name}
            font_path = abspath(join(__file__, "..", "..", "..", "media", "fonts", f"{font_name}"))
            #ствоюємо текст зі шрифтом який ми отримали
            self.font = pygame.font.Font(font_path, size = 48)

    #створюємо метод який обробляє все що проісходить із поля воду тексту
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
        text_surface = self.font.render(self.user_text, False, "white")
        self.screen_name.blit(self.image, (self.x_cor, self.y_cor))
        if self.user_text == "port":
            self.screen_name.blit(text_surface, (self.x_cor + 125, self.y_cor + 13))
        else:
            self.screen_name.blit(text_surface, (self.x_cor + 90, self.y_cor + 13))


input_nick = InputText(width= 346 , height= 80 , x_cor= 467, y_cor= 239, font_name = "Jersey15.ttf" , screen_name = main_screen , base_text= "nickname", name_image= "input_area.png")
input_ip_adress = InputText(width= 346 , height= 80 , x_cor= 467, y_cor= 372, font_name = "Jersey15.ttf" , screen_name = main_screen , base_text= "ip adress", name_image= "input_area.png")
input_port = InputText(width= 346 , height= 80 , x_cor= 467, y_cor= 501, font_name = "Jersey15.ttf" , screen_name = main_screen , base_text= "port", name_image= "input_area.png")