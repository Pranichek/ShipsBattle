import pygame
from ..json_functions import dump_json , list_users

pygame.init()

#переменная для сохранения текста
user_text = [""]
#создание текстового поля
font = pygame.font.SysFont("Jersey 15" , 48)
#рамка для нашего текста
text_box = pygame.Rect(467 , 518, 346 , 68)
#создаем переменную для отслеживания пишет ли пользователь сейчас , елси находится False то значит что поле текста не активно
check_type = [False]
#цвет рамки 
color = pygame.Color("black")

def input_texts(screen_name):
    for event in pygame.event.get():
        #проверяем ли нажата кнопка мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            #проверяем, находится ли курсор мыши в рамке текстового поля
            if text_box.collidepoint(event.pos):
                #если мышка нажата и курсор находится в диапазоне текстового поля, то передаем значение True
                check_type[0] = True
            else:
                #если мышка не нажата, то передаем значение False
                check_type[0] = False

        #нажата ли любая кнопка на нашей клавиатуре
        if event.type == pygame.KEYDOWN:
            #если кнопка была нажата и текстовое поле активно
            if check_type[0] == True:
                #проверяем ли пользователь не привысил лимит букв в нике
                if len(user_text[0]) <= 10 or event.key == pygame.K_BACKSPACE:
                    #если нажата клавиша удаления буквы то удаляем последнюю букву
                    if event.key == pygame.K_BACKSPACE:
                        user_text[0] = user_text[0][:-1]

                    #если нажата любая другая кнопка кроме удаления 
                    else:
                        #првоеряем ли нажата кнопка ENTER , если да то ничего не записываем
                        if event.key == pygame.K_RETURN:
                            pass
                        #иначе записываем в переменную для хранения текста, все кнопки которые нажаты
                        else:
                            user_text[0] += event.unicode
            if event.key == pygame.K_RETURN:
                if len(user_text) > 0:
                    if user_text[0] not in list_users:
                        list_users[user_text[0]] = {"points": 0}
                        dump_json(filename= "data_base.json")
                    


    if check_type[0] == True:
        if user_text[0] == "nickname":
            user_text[0] = ""
    elif check_type[0] == False:
        if len(user_text[0]) == 0:
            user_text[0] = "nickname"

    pygame.draw.rect(surface = screen_name, color = color, rect = text_box, width= 2)
    text = font.render(user_text[0], True , "white")
    screen_name.blit(text, (text_box.x + 87, text_box.y + 12))

    text_box.w = 346
    text_box.h = 68






