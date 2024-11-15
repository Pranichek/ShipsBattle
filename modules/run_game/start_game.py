#імпортуємо усі потрібні модулі
import pygame
from ..screens import main_screen
import modules.screens.screen as module_screen_server
from ..classes import DrawImage , Button , Font, InputText




#ініціалізуємо pygame щоб можна було із ним працювати
pygame.init()

input_text = InputText(width= 346 , height= 68 , x_cor= 467, y_cor= 239, font_name = "Jersey15.ttf" , screen_name = main_screen , base_text= "nickname", name_image= "button_image.png")

#створюємо текст за допомогою класу
createbutton_font = Font(size= 48 , name_font= "Jersey15.ttf" , text= "create" , screen= main_screen , x_cor= 220, y_cor= 655)

#список для проверки нажата ли кнопка
check_press_button = [None]

def button_action():
    check_press_button[0] = "button is pressed"

#функція для перезаписування яке зараз вікно активне
def change_scene(scene):
    list_current_scene[0] = scene

#створюємо кнопку перемикання за допомогою класу
button = Button(x= 113,y = 653,image_path= "button_image.png",image_hover_path= "image_hover.png",width= 346,height= 68,action= button_action)
#отримуємо потрібні зображення , за допомогою створення об'єкту класа DrawImage
background_image = DrawImage(width = 1280,height= 832 , x_cor= 0 , y_cor= 0 ,folder_name= "images_background" , image_name= "main_background.jpg")



#ліст для зберігання яке зараз вікно активне
list_current_scene = [None]
    
#створюємо функцію, яка викликається при запуску гри для користувача який запускає сервер
def main_window():
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
        createbutton_font.draw_font()
        input_text.draw_text()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False  
                change_scene(None)
            elif check_press_button[0] == "button is pressed":
                check_press_button[0] = None
                run_game = False
                change_scene(create_game_window())
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button.check_click()

            input_text.check_event(event)

        pygame.display.flip()
            
    
def create_game_window():
    #викликаємо функцію для запуску серверу
    #встановлюємо назву вікна гри для сервера
    pygame.display.set_caption("Create Game Window")
    #створюжмо змінну для того щоб відстежувати коли треба закривати вікно
    run_game = True
    #основний цикл роботи вікна користувача
    while run_game:
        #встановлюємо із якою швидкістю буде оновлюватись екран
        #встановлюєм колір фону
        #малюємо наші об'єкти зображеннь на екрані screen_server
        background_image.draw_image(screen= main_screen)
        button.draw(surface= main_screen)
        createbutton_font.draw_font()
        #Обробляємо всі події у вікні
        input_text.draw_text()
        #Обробляємо всі події у вікні
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False  
                change_scene(None)
            elif check_press_button[0] == "button is pressed":
                check_press_button[0] = None
                run_game = False
                change_scene(main_window())
            elif event.type == pygame.MOUSEBUTTONDOWN:
                button.check_click()

            input_text.check_event(event)
        
            
        #оновлюєио екран щоб можна було бачити зміни на ньому
        pygame.display.flip()