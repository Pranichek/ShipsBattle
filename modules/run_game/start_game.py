#імпортуємо усі потрібні модулі
import pygame
from ..screens import main_screen
import modules.screens.screen as module_screen_server
from ..classes import DrawImage , Button , Font, InputText


#ініціалізуємо pygame щоб можна було із ним працювати
pygame.init()

#input_texts
input_nick = InputText(width= 346 , height= 80 , x_cor= 467, y_cor= 239, font_name = "Jersey15.ttf" , screen_name = main_screen , base_text= "nickname", name_image= "button_image.png")
input_ip_adress = InputText(width= 346 , height= 80 , x_cor= 467, y_cor= 372, font_name = "Jersey15.ttf" , screen_name = main_screen , base_text= "ip adress", name_image= "button_image.png")
input_port = InputText(width= 346 , height= 80 , x_cor= 467, y_cor= 501, font_name = "Jersey15.ttf" , screen_name = main_screen , base_text= "port", name_image= "button_image.png")


#fonts(text)
createbutton_font = Font(size= 48 , name_font= "Jersey15.ttf" , text= "create" , screen= main_screen , x_cor= 218, y_cor= 663)
join_game_fonts = Font(size= 48 , name_font= "Jersey15.ttf" , text= "join" , screen= main_screen , x_cor= 978 , y_cor= 663)



#список для проверки нажата ли кнопка
check_press_button = [None]

def test():
    print(1)

def button_action():
    check_press_button[0] = "button is pressed"

#функція для перезаписування яке зараз вікно активне
def change_scene(scene):
    list_current_scene[0] = scene

#ліст для зберігання яке зараз вікно активне
list_current_scene = [None]

#buttons
#кнопка кторая перекидывает на фрейм по созданию игры(запуска сервера)
create_game_frame = Button(x= 113, y = 653,image_path= "button_image.png" , image_hover_path= "image_hover.png" , width= 346 , height= 80 , action= button_action)
#кнопка кторая перекидывает на фрейм по присоеденению к игре(серверу)
join_game_frame = Button(x= 832 , y = 653,image_path= "button_image.png" , image_hover_path= "image_hover.png" , width= 346 , height= 80 , action= button_action)
#кнопка которая возвращает назад к главному окну
back_to_menu = Button(x= 30 , y = 41 ,image_path= "back_to_menu.png" , image_hover_path= "back_to_menu2.png" , width= 155 , height= 62 , action= button_action)
#кнопка которая запускает сервер(игру)
start_game_button = Button(x= 352 , y = 642,image_path= "create_game_button.png" , image_hover_path= "create_game_button2.png" , width= 575 , height= 80 , action= test)
#кнопка которая подключается к игре
join_game_button = Button(x= 352 , y = 642,image_path= "join_to_game.png" , image_hover_path= "join_to_game2.png" , width= 575 , height= 80 , action= test)


#images decoration
cold_image = DrawImage(width= 152 , height= 68 , x_cor= 207 , y_cor= 716 , folder_name= "decorations" , image_name= "ice.png")
second_cold_image = DrawImage(width= 152 , height= 68 , x_cor= 940, y_cor= 716 , folder_name= "decorations" , image_name= "ice.png")
third_cold_image = DrawImage(width=  150, height= 68 , x_cor= 536 , y_cor= 705 , folder_name= "decorations" , image_name= "ice.png")
fourth_cold_image = DrawImage(width= 150, height= 68 , x_cor= 686 , y_cor= 705 , folder_name= "decorations" , image_name= "ice.png")
back_text = DrawImage(width= 131 , height= 41 , x_cor= 54, y_cor= 52 , folder_name= "decorations" , image_name= "back_text.png")



#backgrounds
main_bg = DrawImage(width = 1280,height= 832 , x_cor= 0 , y_cor= 0 ,folder_name= "images_background" , image_name= "main_background.jpg")
create_game_bg = DrawImage(width = 1280,height= 832 , x_cor= 0 , y_cor= 0 ,folder_name= "images_background" , image_name= "create_game_bg.png")




#створюємо функцію, яка викликається при запуску гри для користувача який запускає сервер
def main_window():
    #викликаємо функцію для запуску серверу
    #встановлюємо назву вікна гри для сервера
    pygame.display.set_caption("BattleShips")
    #створюжмо змінну для того щоб відстежувати коли треба закривати вікно
    run_game = True
    #основний цикл роботи вікна користувача
    while run_game:
        module_screen_server.FPS.tick(60)
        main_bg.draw_image(screen= main_screen)

        cold_image.draw_image(screen= main_screen)  
        create_game_frame.draw(surface= main_screen)
        createbutton_font.draw_font()
        
        second_cold_image.draw_image(screen= main_screen)
        join_game_frame.draw(surface= main_screen)
        join_game_fonts.draw_font()
        # input_text.draw_text()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False  
                change_scene(None)
            elif check_press_button[0] == "button is pressed":
                check_press_button[0] = None
                run_game = False
                x_pos , y_pos = pygame.mouse.get_pos()
                if x_pos > 600:
                    change_scene(join_game_window())
                elif x_pos < 600:
                    change_scene(create_game_window())
            elif event.type == pygame.MOUSEBUTTONDOWN:
                create_game_frame.check_click()
                join_game_frame.check_click()

            # input_text.check_event(event)

        pygame.display.flip()
            
    
def create_game_window():
    #викликаємо функцію для запуску серверу
    #встановлюємо назву вікна гри для сервера
    pygame.display.set_caption("Create Game Window")
    #створюжмо змінну для того щоб відстежувати коли треба закривати вікно
    run_game = True
    #основний цикл роботи вікна користувача
    while run_game:
        module_screen_server.FPS.tick(60)
        create_game_bg.draw_image(screen= main_screen)

        input_nick.draw_text()
        input_ip_adress.draw_text()
        input_port.draw_text()

        back_to_menu.draw(surface= main_screen)
        back_text.draw_image(screen= main_screen)

        third_cold_image.draw_image(screen= main_screen)
        fourth_cold_image.draw_image(screen= main_screen)
        start_game_button.draw(surface= main_screen)
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
                back_to_menu.check_click()
                start_game_button.check_click()

            input_nick.check_event(event)
            input_ip_adress.check_event(event)
            input_port.check_event(event)  

        #оновлюєио екран щоб можна було бачити зміни на ньому
        pygame.display.flip()


def join_game_window():
    #викликаємо функцію для запуску серверу
    #встановлюємо назву вікна гри для сервера
    pygame.display.set_caption("Join to Game Window")
    #створюжмо змінну для того щоб відстежувати коли треба закривати вікно
    run_game = True
    #основний цикл роботи вікна користувача
    while run_game:
        module_screen_server.FPS.tick(60)
        create_game_bg.draw_image(screen= main_screen)

        input_nick.draw_text()
        input_ip_adress.draw_text()
        input_port.draw_text()

        back_to_menu.draw(surface= main_screen)
        back_text.draw_image(screen= main_screen)

        third_cold_image.draw_image(screen= main_screen)
        fourth_cold_image.draw_image(screen= main_screen)
        join_game_button.draw(surface= main_screen)
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
                back_to_menu.check_click()
                join_game_button.check_click()
               

            input_nick.check_event(event)
            input_ip_adress.check_event(event)
            input_port.check_event(event)  

        #оновлюєио екран щоб можна було бачити зміни на ньому
        pygame.display.flip()