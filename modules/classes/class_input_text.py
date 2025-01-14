import pygame 
from os.path import abspath, join
from .class_click import del_letter_sound, typing_sound
from ..screens.screen import main_screen, FPS

pygame.init()

#створюємо клас
class InputText:
    #створюємо метод конструктор та додаємо параметри для нього 
    def __init__(self, width : int, height : int, x_cor : int, y_cor : int, base_text : str,name_image : str, screen_name : str, font_name : str):
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
        self.VISIBLE = 255

    def fade_in(self):
        fps = FPS.get_fps()
        if fps <= 0:
            fps = 0.01
        current_speed = (60 / fps)
        if self.VISIBLE < 311:
            self.VISIBLE += 5 * current_speed
            if self.VISIBLE >= 311:
                self.VISIBLE = 311
    # fade_out() зменшує прозорість до 0 (невидимий стан)
    def fade_out(self):
        fps = FPS.get_fps()
        if fps <= 0:
            fps = 0.01
        current_speed =  (60 / fps)
        if self.VISIBLE > 0:
            self.VISIBLE -= 10 * current_speed
            if self.VISIBLE <= 0:
                self.VISIBLE = 0
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
    def check_event(self, event: object):
        # Проверяем, активное ли поле
        if self.active:
            # Если поле активно и видно базовый текст, очищаем его
            if self.VISIBLE == 0 and self.user_text == self.base_text:
                self.user_text = ""
        else:  # Если поле неактивно
            # Если текст пустой и видимым остается базовый текст, возвращаем его
            if self.VISIBLE == 255 and self.user_text == "":
                self.user_text = self.base_text

        # Обработка события нажатия мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):  # Если кликнули на поле, активируем его
                self.active = True
            else:  # Если кликнули вне поля, деактивируем его
                self.active = False

        # Устанавливаем максимальную длину текста в зависимости от типа поля
        if self.base_text == "nickname":
            self.max_length = 8
        elif self.base_text == "ip adress":
            self.max_length = 15
        elif self.base_text == "port":
            self.max_length = 5
        else:
            self.max_length = 7

        # Обработка ввода текста, если поле активно
        if event.type == pygame.KEYDOWN and self.active:
            # Удаление последнего символа при нажатии Backspace
            if event.key == pygame.K_BACKSPACE:
                del_letter_sound.play2(loops=1)
                self.user_text = self.user_text[:-1]
            # Если базовый текст очищен, проверяем ввод
            elif self.user_text != self.base_text:
                # Для поля "ip adress" и "port" допускаем только цифры и точки
                if self.base_text in ["ip adress", "port"]:
                    if len(self.user_text) < self.max_length and (event.unicode.isdigit() or event.unicode == "."):
                        typing_sound.play2(loops=1)
                        self.user_text += event.unicode
                # Для других типов полей допускаем любой текст
                else:
                    if len(self.user_text) < self.max_length:
                        typing_sound.play2(loops=1)
                        self.user_text += event.unicode


    def draw_text(self):
         # Очистити базовий текст тільки при активаці
        text_surface = self.font.render(self.user_text, False, "white")
        text_surface.set_alpha(self.VISIBLE)

        self.screen_name.blit(self.image, (self.x_cor, self.y_cor))
        if self.base_text == "port":
                self.screen_name.blit(text_surface, (self.x_cor + 115, self.y_cor + 13))
        else:
            if self.user_text != self.base_text:
                if self.base_text == "ip adress":
                    self.screen_name.blit(text_surface, (self.x_cor + 45, self.y_cor + 13))
                elif self.base_text == "nickname":
                    self.screen_name.blit(text_surface, (self.x_cor + 100, self.y_cor + 13))
                elif self.base_text == "password":
                    self.screen_name.blit(text_surface, (self.x_cor + 100, self.y_cor + 13))
            else:
                self.screen_name.blit(text_surface, (self.x_cor + 90, self.y_cor + 13))


input_nick = InputText(width = 346 , height = 85 , x_cor = 470, y_cor = 297, font_name = "Jersey15.ttf" , screen_name = main_screen , base_text= "nickname", name_image= "input_area.png")
input_ip_adress = InputText(width = 346 , height = 85 , x_cor = 470, y_cor = 400, font_name = "Jersey15.ttf" , screen_name = main_screen , base_text= "ip adress", name_image= "input_area.png")
input_port = InputText(width = 346 , height = 85 , x_cor = 470, y_cor = 501, font_name = "Jersey15.ttf" , screen_name = main_screen , base_text= "port", name_image= "input_area.png")
input_password = InputText(width = 346 , height = 85 , x_cor = 470, y_cor= 195, font_name = "Jersey15.ttf" , screen_name = main_screen , base_text= "password", name_image= "input_area.png")