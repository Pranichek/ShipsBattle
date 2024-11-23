import socket
#підключаємо модуль для роботи із потоками
import threading
# Импортируем классы
from .classes.class_input_text import input_port , input_ip_adress, input_nick
# Импортируем функцию записи в json файлы
from .json_functions.write_json import write_json , list_server_status , list_users
import json


#ліст для перевірки чи зайшов користувач на сервер
list_server_status = {
    "status": None
}
write_json(filename= "utility.json" , object_dict =  list_server_status)

        
if list_server_status == False:
    print("False")

#створємо функцію для запуску серверу
def start_server():
    #
    if input_nick.user_text not in list_users:
        list_users[input_nick.user_text] = {"points": 0}
        write_json(filename = "data_base.json" , object_dict = list_users)
                    
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
        list_server_status = {
            "status": "wait"
        }
        write_json(filename= "utility.json" , object_dict = list_server_status)

        client_socket, adress = server_socket.accept()
        list_server_status = {
            "status": "connect"
        }
        write_json(filename= "utility.json" , object_dict = list_server_status)

        with client_socket:  
            # Отримуємо дані від клієнта
            response_data = client_socket.recv(1024).decode()
            print(response_data , "from client")

            if response_data not in list_users:
                list_users[response_data] = {"points": 0}
                write_json(filename = "data_base.json" , object_dict = list_users)
            
            #формуємо дані для відправки від сервера до клієнта
            data_for_client = {
                "nick": str(input_nick.user_text),
                "status": list_server_status
            }
            #відправляємо дані на кліжента , dumps - перетворює словарь у звичайну строку 
            client_socket.send(json.dumps(data_for_client).encode())
           
        
            
#створюємо зміну потока, для запуску серверу
server_thread = threading.Thread(target = start_server, daemon=True)