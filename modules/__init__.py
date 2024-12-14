#імпортуємо усі необхідні компоненти проекту, щоб їх можна було легко використовувати в інших частинах програми, та також за межами папки modules 
from .run_game import list_current_scene ,change_scene , main_window 
from .screens import *
from .server import start_server , server_thread , turn , list_player_role 
from .client import thread_connect , connect_user , list_check_need_send

