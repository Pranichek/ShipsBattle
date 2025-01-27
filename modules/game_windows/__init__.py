#імпортуємо функції запуску гри у __init__.py , щоб іх можна було використовувати у інших файлах
from .main_frame import main_window
from .create_game_frame import create_game_window
from .join_game_frame import join_game_window
from .waiting_frame import waiting_window 
from .ships_position_frame import ships_position_window
from .finish_frame import finish_window
from .fight_frame import fight_window
from .rules_frame import rules_window
from .change_window import change_scene, list_current_scene
