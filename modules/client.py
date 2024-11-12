import socket


#створюємо функцію підключення користувача до серверу
def connect_user():
    # створюємо сокет з використанням протоколу IPv4 (AF_INET) та TCP (SOCK_STREAM)
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as client_socket:
        # підключаємо користувача до сервера за Lan ip 192.168.0.4 та портом 6060
        client_socket.connect(("192.168.0.4", 6060))
        # відправляємо дані від користувача на сервер , та кодуємо їх у байти
        client_socket.send("-_-".encode())
    


    

    
    