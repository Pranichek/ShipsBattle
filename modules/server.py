import socket
#підключаємо модуль для роботи із потоками
import threading

event_t = threading.Event()


#створємо функцію для запуску серверу
def start_server():
    # Створюємо сокет з використанням протоколу IPv4 (AF_INET) та TCP (SOCK_STREAM)
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as server_socket:
        # Прив'язуємо сокет до порту 6060 , та робимо так щоб до нього могли підключатися користувачи із різних мереж
        server_socket.bind(("0.0.0.0", 7111))
        #Ставимо сервер у режим очікування підключень
        server_socket.listen()
        print("connecting")
        while not event_t.is_set():
            client_socket, adress = server_socket.accept()
            print("connected: ", adress)
            response_data = client_socket.recv(1024).decode()
            print(response_data)
            #Отримуємо дані від клієнта (максимум 1240 байт) і декодуємо їх у текст
            if event_t.is_set():
                print("kfjvjdfnvndjfvjkndfv")
                break


    

#створюємо зміну потока, для запуску серверу
server_thread = threading.Thread(target = start_server)