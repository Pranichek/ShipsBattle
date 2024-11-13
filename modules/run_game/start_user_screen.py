#імпортуємо усі необхідні модулі
import pygame
import modules.screens.user_screen as module_user_screen
from ..screens import screen_user
from ..client import thread_user
from ..classes import DrawImage
from ..game import input_texts
import sys

#ініціалізуємо pygame щоб можна було із ним працювати
pygame.init()

#отримуємо потрібні зображення , за допомогою створення об'єкту класа DrawImage
backgroundd_image = DrawImage(width = 1280,height= 832 , x_cor= 0 , y_cor= 0 ,folder_name= "images_background" , image_name= "main_background.jpg")
iced_image = DrawImage(width = 154,height= 68, x_cor =  563, y_cor= 552,folder_name= "decorations1lvl" , image_name= "ice.png")
inputd_text_font = DrawImage(width = 346 ,height= 68, x_cor = 467, y_cor= 518,folder_name= "images_background" , image_name= "input_text_font.png")


#створюємо функцію, яка викликається при запуску гри для користувача який приєднується до серверу
def user_window():
   #викликаємо функцію для підключення користувача до серверу
   thread_user.start()
   #встановлюємо назву вікна гри для користувача
   pygame.display.set_caption("Screen_User")
   #створюжмо змінну для того щоб відстежувати коли треба закривати вікно
   start_user = True
   #основний цикл роботи вікна користувача
   while start_user:
        #встановлююємо із якою швидкістю буде оновлюватись екран
        module_user_screen.FPS.tick(60)
        #встановлюєм колір фону
        module_user_screen.screen_user.fill((255, 50 , 100))
        #малюємо наші об'єкти зображеннь на екрані screen_user
        backgroundd_image.draw_image(screen = screen_user)
        iced_image.draw_image(screen= screen_user)
        inputd_text_font.draw_image(screen= screen_user)
        #викликаємо функцію для вводу нікнейму на екрані screen_user
        input_texts(screen_name= screen_user)
        #Обробляємо всі події у вікні
        for event in pygame.event.get():
                # Якщо натиснута кнопка закриття вікна, завершуємо цикл
                if event.type == pygame.QUIT:
                    sys.exit()
                    pygame.quit()
                    # #коли ми у змінну передаємо False , цикл перестає працювати та вікно закривається
                    # start_user = False
        
        #оновлюєио екран щоб можна було бачити зміни на ньому
        pygame.display.flip()
            
        