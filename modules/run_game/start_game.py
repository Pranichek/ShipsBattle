#імпортуємо усі потрібні модулі
import pygame
from ..screens import screen ,  Button
import modules.screens.server_screen as module_screen_server
from ..server import start_server 
from threading import Thread



#ініціалізуємо pygame щоб можна було із ним працювати
pygame.init()


#створюємо функцію, яка викликається при запуску гри для користувача який запускає сервер
def server_window():
    # Создаём поток, target - это так сказать метод, в который надо записать функцию, которая будет использовать отдельный поток
    # в нашем случае это start server, daemon - это поток демон( сам офигел от название ), он не блокирует завершение программы , но когда все потоки
    # завершаются, он выключается автоматически
    server_thread = Thread(target = start_server, daemon = True)
    # Запускаем поток 
    server_thread.start()
    #викликаємо функцію для запуску серверу
    # Я удалил, и всё заработало, не знаю как так получается, но что есть то есть, 
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
