# Імпортуємо основний екран сервера з модуля server_screen
from .screen import main_screen
from .create_grid import *
from .list_grid import *


#файл __init__.py робить доступними для імпорту об’єкти screen, screen_user, і Button з відповідних файлів(модулів), щоб можна було використовувати їх у інших частинах проєкту.