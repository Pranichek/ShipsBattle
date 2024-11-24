import socket
#підключаємо модуль для роботи із потоками
import threading
# Импортируем классы
from .classes.class_input_text import input_port , input_ip_adress, input_nick
# Импортируем функцию записи в json файлы
from .json_functions.write_json import write_json , list_server_status , list_users
from .json_functions.read_json import read_json
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

        #записуємо в словарь статус очікування підключення до серверу
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

        # Отримуємо дані від клієнта(нікнейм та скільки у нього баллів), у виді джейсон строки
        response_data = client_socket.recv(1024).decode()
        #перетворюємо json сктроку , у словник
        data_in_list = json.loads(response_data)
        print(data_in_list, "from client")

        #якщо нікнейма суперника ще немає у словарі то записуємо його нік у джейосн файл
        if data_in_list["nick"] not in list_users:
            list_users[data_in_list["nick"]] = {"points": data_in_list["points"]}
            write_json(filename = "data_base.json" , object_dict = list_users)
        #якщо його нікнейм вже є , тоді просто оновлюємо його кількість баллів 
        elif data_in_list["nick"] in list_users:
            list_users[data_in_list["nick"]]["points"] = data_in_list["points"]
            write_json(filename = "data_base.json" , object_dict = list_users)

        #отримуємо дані про користувачів з бази даних  (назва файла з базой даних)
        data_for_client = read_json(name_file = "data_base.json")
        #беремо кол-во баллів користувача який запсукає сервер, щоб відправати оновлену кількість 
        points_for_client = data_for_client[input_nick.user_text]["points"]
        print(points_for_client , "points for client")
        
        #формуємо дані користувача який запустив серве ,для відправки до клієнта який під'єднався
        data_for_client = {
            "nick": str(input_nick.user_text),
            "points": points_for_client,
            "status": list_server_status
        }
        #відправляємо дані на клієнта , dumps - перетворює словарь у джейсон строку 
        client_socket.send(json.dumps(data_for_client).encode())
           
        
            
#створюємо зміну потока, для запуску серверу
server_thread = threading.Thread(target = start_server, daemon=True)