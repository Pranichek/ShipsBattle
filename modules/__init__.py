#імпортуємо усі необхідні компоненти проекту, щоб їх можна було легко використовувати в інших частинах програми, та також за межами папки modules 
from .screens import *
from .game_windows import main_window, list_current_scene, fight_window
from .server import *
from .client import list_check_need_send, count_time, start_client, check_connection_users

