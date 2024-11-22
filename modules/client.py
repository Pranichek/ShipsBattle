import socket
#підключаємо модуль для роботи із потоками
import threading
import json
from .classes.class_input_text import input_port, input_ip_adress, input_nick
import json
from .json_functions import write_json , list_users , list_server_status 

#ліст для перевірки чи зайшов користувач на сервер
list_server_status = {
    "status": None
}
write_json(filename= "utility.json" , object_dict = list_server_status)

#створюємо функцію підключення користувача до серверу
def connect_user():
    if input_nick.user_text not in list_users:
        list_users[input_nick.user_text] = {"points": 0}
        write_json(filename = "data_base.json" , object_dict = list_users)
    ip_address = input_ip_adress.user_text
    port = int(input_port.user_text)
    print(1)
    # створюємо сокет з використанням протоколу IPv4 (AF_INET) та TCP (SOCK_STREAM)
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as client_socket:
        # підключаємо користувача до сервера за Lan ip 192.168.0.4 та портом 6060
        print(2)
        client_socket.connect((ip_address, port))

        encode_text = str(input_nick.user_text)
        # відправляємо дані від користувача на сервер , та кодуємо їх у байти
        client_socket.send(encode_text.encode())

        data = client_socket.recv(1024).decode()
        data_in_list = json.loads(data)
        print(data_in_list["nick"] , "nick from server")
        print(data_in_list["status"] , "status from server")
        if data_in_list["nick"] not in list_users:
            list_users[data_in_list["nick"]] = {"points": 0}
            write_json(filename = "data_base.json" , object_dict = list_users)

        write_json(filename= "utility.json" , object_dict = data_in_list["status"])
        
        
            

#створюємо зміну потока, із функцією підключення коритсувача до серверу
thread_connect = threading.Thread(target = connect_user, daemon=True)