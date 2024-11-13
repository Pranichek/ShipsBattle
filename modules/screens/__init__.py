# Імпортуємо основний екран сервера з модуля server_screen
from .server_screen import screen_server
# Імпортуємо екран користувача з модуля user_screen
from .user_screen import screen_user
from .button import Button

#файл __init__.py робить доступними для імпорту об’єкти screen, screen_user, і Button з відповідних файлів(модулів), щоб можна було використовувати їх у інших частинах проєкту.