import socket
import threading

#створємо функцію для запуску серверу
def start_server():
    # Створюємо сокет з використанням протоколу IPv4 (AF_INET) та TCP (SOCK_STREAM)
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as server_socket:
        # Прив'язуємо сокет до порту 6060 , та робимо так щоб до нього могли підключатися користувачи із різних мереж
        server_socket.bind(("0.0.0.0", 7322))
        #Ставимо сервер у режим очікування підключень
        server_socket.listen()
        print("connecting")
        #Приймаємо користувача який приєднався і отримуємо сокет та його адресу
        client_soket, adress = server_socket.accept()
        print("connected: ", adress)
        #Отримуємо дані від клієнта (максимум 1240 байт) і декодуємо їх у текст
        response_data = client_soket.recv(1240).decode()
        #Виводимо отримані дані у консоль
        print(response_data)

server_thred = threading.Thread(target = start_server)



 
