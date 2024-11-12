#імпортуємо усі необхідні модулі
import pygame
import modules.screens.user_screen as module_user_screen
from ..screens import user_screen
from ..client import connect_user


#ініціалізуємо pygame щоб можна було із ним працювати
pygame.init()


#створюємо функцію, яка викликається при запуску гри для користувача який приєднується до серверу
def user_window():
   #викликаємо функцію для підключення користувача до серверу
   connect_user()
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
        #Обробляємо всі події у вікні
        for event in pygame.event.get():
                # Якщо натиснута кнопка закриття вікна, завершуємо цикл
                if event.type == pygame.QUIT:
                    #коли ми у змінну передаємо False , цикл перестає працювати та вікно закривається
                    start_user = False
        
        #обновляємо екран щоб можна було бачити зміни на ньому
        pygame.display.flip()
            
      