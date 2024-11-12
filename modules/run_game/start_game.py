#імпортуємо усі потрібні модулі
import pygame
from ..screens import screen ,  Button
import modules.screens.server_screen as module_screen_server
from ..server import server_thred
from ..classes import DrawImage
from ..game import input_texts
import sys


#ініціалізуємо pygame щоб можна було із ним працювати
pygame.init()

background_image = DrawImage(width = 1280,height= 832 , x_cor= 0 , y_cor= 0 ,folder_name= "images_background" , image_name= "main_background.jpg")
ice_image = DrawImage(width = 154,height= 68, x_cor =  563, y_cor= 552,folder_name= "decorations1lvl" , image_name= "ice.png")
input_text_font = DrawImage(width = 346 ,height= 68, x_cor = 467, y_cor= 518,folder_name= "images_background" , image_name= "input_text_font.png")


#створюємо функцію, яка викликається при запуску гри для користувача який запускає сервер
def server_window():
    global event
    #викликаємо функцію для запуску серверу
    server_thred.start()
    #встановлюємо назву вікна гри для сервера
    pygame.display.set_caption("Screen_Server")
    #створюжмо змінну для того щоб відстежувати коли треба закривати вікно
    run_game = True
    #основний цикл роботи вікна користувача
    
    while run_game:
        #встановлюємо із якою швидкістю буде оновлюватись екран
        module_screen_server.FPS.tick(60)
        #встановлюєм колір фону
        module_screen_server.screen.fill((255, 0 , 0))
        background_image.draw_image(screen= screen)
        ice_image.draw_image(screen= screen)
        input_text_font.draw_image(screen= screen)
        input_texts(screen_name = screen)
        #Обробляємо всі події у вікні
        for event in pygame.event.get():
            #якщо натиснута кнопка закриття вікна, завершуємо цикл
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                # #коли ми у змінну передаємо False, цикл перестає працювати та вікно закривається
                # run_game = False
            

        pygame.display.flip()


        


  


        
        


