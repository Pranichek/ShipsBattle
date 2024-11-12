#імпортуємо усі необхідні компоненти проекту, щоб їх можна було легко використовувати в інших частинах програми, та також за межами папки modules 
from .server import start_server
from .client import connect_user
from .run_game import *
from .screens import *