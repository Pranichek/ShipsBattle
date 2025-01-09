#імпортуємо весь вміст файлу class_image.py доступним для іншиї файів, щоб могли імпортувати не вводячи увесь шлях
from .class_image import DrawImage
from .class_button import Button
from .class_input_text import input_nick , input_ip_adress , input_port
from .class_text import Font
from .class_ship import list_ships 
from .class_click import music_click , music_achieve
from .class_music import music_load_main , music_load_waiting ,fight_music
from .animation import *
from .achive_window import *
from .class_medal import *
from .class_server_ip import *