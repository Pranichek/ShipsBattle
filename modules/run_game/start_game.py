#імпортуємо усі потрібні модулі
import pygame
from ..screens import screen_server ,  Button
import modules.screens.server_screen as module_screen_server
from ..classes import DrawImage
from ..game import input_texts
from ..server import  server_thread , event_t
import sys


#ініціалізуємо pygame щоб можна було із ним працювати
pygame.init()


#отримуємо потрібні зображення , за допомогою створення об'єкту класа DrawImage
background_image = DrawImage(width = 1280,height= 832 , x_cor= 0 , y_cor= 0 ,folder_name= "images_background" , image_name= "main_background.jpg")
ice_image = DrawImage(width = 154,height= 68, x_cor =  563, y_cor= 552,folder_name= "decorations1lvl" , image_name= "ice.png")
input_text_font = DrawImage(width = 346 ,height= 68, x_cor = 467, y_cor= 518,folder_name= "images_background" , image_name= "input_text_font.png")


#створюємо функцію, яка викликається при запуску гри для користувача який запускає сервер
def server_window():
    #викликаємо функцію для запуску серверу
    #встановлюємо назву вікна гри для сервера
    pygame.display.set_caption("Screen_Server")
    server_thread.start()
    #створюжмо змінну для того щоб відстежувати коли треба закривати вікно
    run_game = True
    #основний цикл роботи вікна користувача
    while run_game:
        #встановлюємо із якою швидкістю буде оновлюватись екран
        module_screen_server.FPS.tick(60)
        #встановлюєм колір фону
        #малюємо наші об'єкти зображеннь на екрані screen_server
        background_image.draw_image(screen= screen_server)
        ice_image.draw_image(screen= screen_server)
        input_text_font.draw_image(screen= screen_server)
        #викликаємо функцію для вводу нікнейму на екрані screen_server
        # input_texts(screen_name = screen_server)
        #Обробляємо всі події у вікні
        
        for event in pygame.event.get():
            print(1)
            if event.type == pygame.QUIT:
                run_game = False  
                # event_t.set()
        
   

                # установим False для выхода из цикла 
                # #коли ми у змінну передаємо False, цикл перестає працювати та вікно закривається
                # run_game = False
            
        #оновлюєио екран щоб можна було бачити зміни на ньому
        pygame.display.flip()
    # Дожидаемся завершения потока сервера
    # server_thread.join()
    # pygame.quit()
    # sys.exit()


        


  


        
        


