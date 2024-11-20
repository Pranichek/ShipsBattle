import socket
#підключаємо модуль для роботи із потоками
import threading
# Импортируем классы
from .classes.class_input_text import input_port , input_ip_adress, input_nick
# Импортируем функцию записи в json файлы
from .json_functions.write_json import write_json , check_server_status


#ліст для перевірки чи зайшов користувач на сервер
dict_check_server = {
    "status": None
}
write_json(filename= "utility.json" , object_dict = dict_check_server)

        
if dict_check_server == False:
    print("False")

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
        dict_check_server = "wait"

        check_server_status = {
            "status": dict_check_server
        }
        write_json(filename= "utility.json" , object_dict = check_server_status)

        client_socket, adress = server_socket.accept()
        dict_check_server = "connect"

        check_server_status = {
            "status": dict_check_server
        }
        write_json(filename= "utility.json" , object_dict = check_server_status)

        with client_socket:  # Використовуємо контекстний менеджер для клієнтського сокета
            # Отримуємо дані від клієнта
            response_data = client_socket.recv(1024).decode()
            print(response_data , "from client")
          
            # Відправляємо відповідь клієнту
            encode_text = str(input_nick.user_text)
            client_socket.send(encode_text.encode())
        
            
#створюємо зміну потока, для запуску серверу
server_thread = threading.Thread(target = start_server, daemon=True)