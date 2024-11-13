import pygame
#імопртуємо функцію запису інформації у джейсон файл, та словарь із користувачами
from ..json_functions import dump_json , list_users
import os


#іницілізація Pygame
pygame.init()
#path - шлях
#abspath - абсолютний шлях

path_to_font = os.path.abspath(__file__  +  f"/../../../fonts/Jersey15.ttf")

print(path_to_font)

#змінна для збереження тексту користувача, у вигляді списку
user_text = [""]
#створення тектсовго поля , та надаємо налаштування шрифта
font = pygame.font.SysFont(path_to_font ,size = 48)
#робимо рамку для нашого тексту
text_box = pygame.Rect(467 , 518, 346 , 68)
#змінна у вигляді списку, щоб відстежувати чи активне зараз поля для введення тексту
check_type = [False]
#колір рамки
color = pygame.Color("black")


#функція вводу тексту на екрані
def input_texts(screen_name):
    for event in pygame.event.get():
        #Перевіряємо, чи була натиснута кнопка миші
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Перевіряємо, чи курсор миші знаходиться в межах текстового поля
            if text_box.collidepoint(event.pos):
                # Якщо курсор миші знаходиться в текстовому полі, встановлюємо значення True для активності текстового поля
                check_type[0] = True
            else:
                # Якщо курсор миші поза текстовим полем, встановлюємо значення False
                check_type[0] = False

         #Перевіряємо, чи була натиснута будь-яка клавіша на клавіатурі
        if event.type == pygame.KEYDOWN:
            # Якщо клавіша натиснута, і текстове поле активно
            if check_type[0] == True:
                # Перевіряємо, чи не перевищив користувач ліміт символів у ніку
                if len(user_text[0]) < 10 or event.key == pygame.K_BACKSPACE:
                    #Якщо натиснута клавіша Backspace, видаляємо останній символ
                    if event.key == pygame.K_BACKSPACE:
                        user_text[0] = user_text[0][:-1]

                    # Якщо натиснута інша клавіша, крім Backspace
                    else:
                       # Якщо натиснута клавіша Enter, нічого не робимо, щоб не було зайвиї проміжков у ніку
                        if event.key == pygame.K_RETURN:
                            pass
                        # Інакше додаємо символ який нажатий на клавітаурі змінної де зберігається що натиснув користувач
                        else:
                            #unicode- функція яка додає символ, який ввів користувач, до змінної user_text[0]
                            user_text[0] += event.unicode
            # Якщо натиснута клавіша Enter
            if event.key == pygame.K_RETURN:
                #перевіряємо щоб був хочаб один символ у нику
                if len(user_text) > 0:
                    #перевіряємо чи такого ніку ще немає у словарюю із користувачами
                    if user_text[0] not in list_users:
                        #якщо ні, створюємо нового користувача з нулями очками
                        list_users[user_text[0]] = {"points": 0}
                        #зберігаємо інформацію у json файл
                        dump_json(filename= "data_base.json")
                    

    # Якщо текстове поле активне, очищаємо значення "nickname" у змінній user_text[0]
    if check_type[0] == True:
        if user_text[0] == "nickname":
            user_text[0] = ""
    # Якщо текстове поле неактивне, встановлюємо значення "nickname", якщо поле пусте
    elif check_type[0] == False:
        if len(user_text[0]) == 0:
            user_text[0] = "nickname"

    # Малюємо текстове поле з рамкою
    pygame.draw.rect(surface = screen_name, color = color, rect = text_box, width= 2)
     # Рендеримо введений текст білим кольором і відображаємо на екрані
     #True -  говорить за те що ми згладжуємо текст
    text = font.render(user_text[0], True , "white")
    #виводимо текст на екрані , text_box.x + 87, text_box.y + 12 - це щоб текст був по середині рамкидля тексту
    screen_name.blit(text, (text_box.x + 87, text_box.y + 12))

    #встановлюємо розмііри рамки тексту
    text_box.w = 346
    text_box.h = 68






