import socket
#підключаємо модуль для роботи із потоками
import threading
from .classes.class_input_text import input_port , input_ip_adress



#створємо функцію для запуску серверу
def start_server():
    ip_address = input_ip_adress.user_text
    port = int(input_port.user_text)
    print(ip_address , port)
    # Створюємо сокет з використанням протоколу IPv4 (AF_INET) та TCP (SOCK_STREAM)
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as server_socket:
        # Прив'язуємо сокет до порту 6060 , та робимо так щоб до нього могли підключатися користувачи із різних мереж
        server_socket.bind((ip_address, port))
        #Ставимо сервер у режим очікування підключень
        server_socket.listen()
        print("connecting")
        client_socket, adress = server_socket.accept()
        print("connected: ", adress)
        #Отримуємо дані від клієнта (максимум 1240 байт) і декодуємо їх у текст
        response_data = client_socket.recv(1024).decode()
        print(response_data)
            

#створюємо зміну потока, для запуску серверу
server_thread = threading.Thread(target = start_server, daemon=True)



 
