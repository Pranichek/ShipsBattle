#імпортуємо усі потрібні модулі
import pygame
from ..screens import main_screen
import modules.screens.screen as module_screen_server
from ..classes import DrawImage , Button
from ..game import input_texts


#ініціалізуємо pygame щоб можна було із ним працювати
pygame.init()

#832 653
def button_action():
    list_current_scene[0] = "button is pressed"

button = Button(x= 113,y = 653,image_path= "button_image.jpg",image_hover_path= "image_hover.jpg",width= 346,height= 68,action= button_action)
#отримуємо потрібні зображення , за допомогою створення об'єкту класа DrawImage
background_image = DrawImage(width = 1280,height= 832 , x_cor= 0 , y_cor= 0 ,folder_name= "images_background" , image_name= "main_background.jpg")

def change_scene(scene):
    list_current_scene[0] = scene


list_current_scene = [None]

    
#створюємо функцію, яка викликається при запуску гри для користувача який запускає сервер
def window():
    #викликаємо функцію для запуску серверу
    #встановлюємо назву вікна гри для сервера
    pygame.display.set_caption("BattleShips")
    #створюжмо змінну для того щоб відстежувати коли треба закривати вікно
    run_game = True
    #основний цикл роботи вікна користувача
    while run_game:
        #встановлюємо із якою швидкістю буде оновлюватись екран
        #встановлюєм колір фону
        #малюємо наші об'єкти зображеннь на екрані screen_server
        background_image.draw_image(screen= main_screen)
        button.draw(surface= main_screen)
        #викликаємо функцію для вводу нікнейму на екрані screen_server
        # input_texts(screen_name = main_screen)
        #Обробляємо всі події у вікні
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("into")
                run_game = False  
                change_scene(None)
                # установим False для выхода из цикла 
                # #коли ми у змінну передаємо False, цикл перестає працювати та вікно закривається
                # run_game = False
            elif list_current_scene[0] == "button is pressed":
                run_game = False
                change_scene(second_window)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button.check_click()
        #оновлюєио екран щоб можна було бачити зміни на ньому
        pygame.display.flip()
    
def second_window():
    #викликаємо функцію для запуску серверу
    #встановлюємо назву вікна гри для сервера
    pygame.display.set_caption("Second_window")
    #створюжмо змінну для того щоб відстежувати коли треба закривати вікно
    run_game = True
    #основний цикл роботи вікна користувача
    while run_game:
        #встановлюємо із якою швидкістю буде оновлюватись екран
        #встановлюєм колір фону
        #малюємо наші об'єкти зображеннь на екрані screen_server
        background_image.draw_image(screen= main_screen)
        #викликаємо функцію для вводу нікнейму на екрані screen_server
        # input_texts(screen_name = main_screen)
        #Обробляємо всі події у вікні
        button.draw(surface= main_screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("into1")
                run_game = False  
                change_scene(None)
            elif list_current_scene[0] == "button is pressed":
                run_game = False
                change_scene(window)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button.check_click()
            
                # установим False для выхода из цикла 
                # #коли ми у змінну передаємо False, цикл перестає працювати та вікно закривається
                # run_game = False
            
        #оновлюєио екран щоб можна було бачити зміни на ньому
        pygame.display.flip()



    





  


        
        


