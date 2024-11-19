import socket
#підключаємо модуль для роботи із потоками
import threading
import json
from .classes.class_input_text import input_port, input_ip_adress


#створюємо функцію підключення користувача до серверу
def connect_user():
    ip_address = input_ip_adress.user_text
    port = int(input_port.user_text)
    # створюємо сокет з використанням протоколу IPv4 (AF_INET) та TCP (SOCK_STREAM)
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as client_socket:
        # підключаємо користувача до сервера за Lan ip 192.168.0.4 та портом 6060
        client_socket.connect((ip_address, port))
        # відправляємо дані від користувача на сервер , та кодуємо їх у байти
        client_socket.send("-_-".encode())
        
            

#створюємо зміну потока, із функцією підключення коритсувача до серверу
thread_connect = threading.Thread(target = connect_user, daemon=True)