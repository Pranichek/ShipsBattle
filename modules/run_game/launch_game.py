import pygame
import modules.screens.server_screen as server_module_screen
from ..json_functions import write_json , list_users
from ..screens import screen_server

# Ініціалізуємо всі модулі pygame для початку роботи
pygame.init()



def start_game():
    #змінна для зберігання тексту
    user_ip = ''
    #створення текстового поля
    font = pygame.font.SysFont('frenchsript', 40)
    #створюємо рамку нашого тексту
    text_box = pygame.Rect((1280 // 2) - (100 //2),(832 // 2) - (50 // 2),100,50)
    #змінная длі переврки чи зараз пишуть текст
    activa = False
    #цільова кольорова зміна тексту
    color = pygame.Color("Red")

    run_game = True
    while run_game:
        server_module_screen.FPS.tick(60)
        server_module_screen.screen_server.fill((255 , 192 , 203))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False
            #перевіряємо чи користувач натиснув мишку 
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Якщо натиснуто всередині текстового поля
                if text_box.collidepoint(event.pos):
                    activa = True
                #Якщо не натиснуто всередині текстового поля
                else:
                    activa = False

             #якщо натиснуто клавішу
            if event.type == pygame.KEYDOWN:
                #чи текстове поле активне
                if activa:
                    #якщо натиснуто клавішу backspace або у текстовому полі ще не так багато укв щоб можна було писати
                    if len(user_ip) < 10 or event.key == pygame.K_BACKSPACE:
                        print("get in")
                         #якщо натиснуто BACKSPACE
                        if event.key == pygame.K_BACKSPACE:
                            #видаляємо останній символ
                            #щоб отримати всі символи рядка user_ip, крім останнього, та перезаписуємо змінну
                            user_ip = user_ip[:-1]
                        #якщо користувач натиснув кнопку щоб писати
                        else:
                            #якщо натиснув ENTER коли писав текст то нічого не робимо
                            if event.key == pygame.K_RETURN:
                                pass
                            #додаємо введений символ до змінної тексту
                            else:
                                user_ip += event.unicode

                        #якщо натиснта клавіша ENTER 
                        if event.key == pygame.K_RETURN:
                            print(user_ip)
                            #якщо текстове поле не пусте та не знаходиться в списку користувачів
                            if len(user_ip) > 0:
                                if user_ip not in list_users:
                                    #додаємо нового користувача до списку та джейсон файлу
                                    list_users[user_ip] = {"points": 0}
                                    write_json(filename = "data_base.json")


                            # if len(user_ip) > 0:
                            #     write_json(filename = "data_base.json", object_to_load = user_ip)
                        
        #якщо натиснуте текстове поле то воно червоне            
        if activa:
            color = pygame.Color("red")
        #якщо ні, то біле
        else:
            color = pygame.Color("white")
        #малюємо текстове поле з заданим кольором та шириною
        pygame.draw.rect(surface = screen_server ,color = color ,rect =  text_box ,width = 4)
        #рендеримо текст з змінною user_ip та  чорним кольором
        surf = font.render(user_ip , True, "black")
        #Відображаємо текст в текстовому полі , + 5 щоб текст не був прижатий до країв
        screen_server.blit(surf , (text_box.x + 5 , text_box.y + 5))
        #змінюємо ширину текстового поля в залежності від розміру тексту
        #фугкція max робить так що текстове поле ніколи не буде меньшим ща 100 пікселів , але якщо текст буде стпноаитися більшим то текстове поле буде розтягуватись
        text_box.w = max(100 , surf.get_width() + 10)
        #оновлюємо екран
        pygame.display.flip()