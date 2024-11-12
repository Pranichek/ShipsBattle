#імпортуємо усі потрібні модулі
import pygame
from ..screens import screen ,  Button
import modules.screens.server_screen as module_screen_server
from ..server import start_server 



#ініціалізуємо pygame щоб можна було із ним працювати
pygame.init()


#створюємо функцію, яка викликається при запуску гри для користувача який запускає сервер
def server_window():
    #викликаємо функцію для запуску серверу
    start_server()
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
        #Обробляємо всі події у вікні
        for event in pygame.event.get():
            #якщо натиснута кнопка закриття вікна, завершуємо цикл
            if event.type == pygame.QUIT:
                #коли ми у змінну передаємо False, цикл перестає працювати та вікно закривається
                run_game = False

        pygame.display.flip()
        


                





        
        


