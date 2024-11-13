import socket
#підключаємо модуль для роботи із потоками
import threading
import json
from .json_functions import list_users

# def add_for_server(nickname : str, score : int):
#     user_data = {
#         "nickname" : list_users[0],
#         "score" : list_users[-1]
#     }
#     json_user_data = json.dumps(user_data)


#створюємо функцію підключення користувача до серверу
def connect_user():
    # створюємо сокет з використанням протоколу IPv4 (AF_INET) та TCP (SOCK_STREAM)
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as client_socket:
        # підключаємо користувача до сервера за Lan ip 192.168.0.4 та портом 6060
        client_socket.connect(("localhost", 7373))
        # відправляємо дані від користувача на сервер , та кодуємо їх у байти
        client_socket.send("-_-".encode())
        while event_user.is_set():
            if not event_user.is_set():
                break

event_user = threading.Event()
#створюємо зміну потока, із функцією підключення коритсувача до серверу
thread_user = threading.Thread(target = connect_user)