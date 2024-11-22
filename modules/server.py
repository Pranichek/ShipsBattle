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
#зберігаємо інформацію про статус серверу у json файл , поки цей статус пустий тому що не запустили сервер
write_json(filename= "utility.json" , object_dict =  list_server_status)


#створємо функцію для запуску серверу
def start_server():
    #если игрок нажал запустить сервер и его еще нет в словаре игроков, то записываем его ник в джейсон
    if input_nick.user_text not in list_users:
        #создаем игрока с его ником и даем базовое количество баллов
        list_users[input_nick.user_text] = {"points": 0}
        #зберігаємо інформацію у json файл
        write_json(filename = "data_base.json" , object_dict = list_users)

    #берем из поля ввода данные для запуска сервера(айпи и порт)
    ip_address = input_ip_adress.user_text
    port = int(input_port.user_text)
    
    # Створюємо сокет з використанням протоколу IPv4 (AF_INET) та TCP (SOCK_STREAM)
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as server_socket:
        # Прив'язуємо сокет до порту що ввів користувач, та Прив'язуємо по якому айпі можуть до нього підключитися
        server_socket.bind((ip_address, port))
        #Ставимо сервер у режим очікування підключень
        server_socket.listen()
        print("connecting")
        #передаем в словарь файл статус ожидания
        list_server_status = {
            "status": "wait"
        }
        #зберігаємо інформацію про статус підлючення до серверу у json файл
        write_json(filename= "utility.json" , object_dict = list_server_status)
        
        #приймаємо користувача який під'єднується до серверу
        client_socket, adress = server_socket.accept()

        #записуємо у словарь статус того що до серверу під'єднався користувач
        list_server_status = {
            "status": "connect"
        }
        #зберігаємо інформацію про статус підлючення до серверу у json файл
        write_json(filename= "utility.json" , object_dict = list_server_status)

        # with client_socket:  
        # Отримуємо дані від клієнта(а саме його нікнейм)
        response_data = client_socket.recv(1024).decode()
        print(response_data , "from client")

        #якщо нікнейма суперника ще немає у словарі то записуємо його нік у джейосн файл
        if response_data not in list_users:
            list_users[response_data] = {"points": 0}
            write_json(filename = "data_base.json" , object_dict = list_users)
        
        #формуємо дані для відправки від сервера до клієнта
        data_for_client = {
            "nick": str(input_nick.user_text),
            "status": list_server_status
        }
        #відправляємо дані на клієнта , dumps - перетворює словарь у звичайну строку 
        client_socket.send(json.dumps(data_for_client).encode())
           
        
            
#створюємо зміну потока, для запуску серверу
server_thread = threading.Thread(target = start_server, daemon=True)