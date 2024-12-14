#імпортуємо функції запуску гри у __init__.py , щоб іх можна було використовувати у інших файлах
from .start_game import change_scene , main_window , list_current_scene 
from .random_placing import random_places_ships
from .launch_server import start_server , check_server_started , fail_start_server
from .clinent_connect import connect_to_server , fail_connect