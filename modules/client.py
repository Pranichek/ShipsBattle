import socket
#підключаємо модуль для роботи із потоками
import threading
import json
import pygame
from .classes.class_input_text import input_port, input_ip_adress, input_nick
import json
from .json_functions import write_json , list_users , list_server_status 
from .json_functions.read_json import read_json
from .screens import main_screen

pygame.init()



#ліст для перевірки чи зайшов користувач на сервер
list_server_status = {
    "status": None
}
#зберігаємо інформацію про статус серверу у json файл , поки цей статус пустий тому що не під'єднуємося до серверу
write_json(filename= "utility.json" , object_dict = list_server_status)

list_check_connection = [None]

def check_server_status(ip_adress : int , port : int): 
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(5)
            sock.connect((ip_adress, port))
            list_check_connection[0] = True
    except (socket.timeout, OSError):
        print("server not found")
        list_check_connection[0] =  False

    
#створюємо функцію підключення користувача до серверу
def connect_user():
    #если игрок нажал запустить сервер и его еще нет в словаре игроков, то записываем его ник в джейсон
    if input_nick.user_text not in list_users:
        #создаем игрока с его ником и даем базовое количество баллов
        list_users[input_nick.user_text] = {"points": 0}
        #зберігаємо інформацію у json файл
        write_json(filename = "data_base.json" , object_dict = list_users)

    #берем из поля ввода данные для запуска сервера(айпи и порт)
        ip_address = input_ip_adress.user_text
        port = int(input_port.user_text)
        
        server_status = check_server_status(ip_adress = ip_address, port = port)
            
        if server_status == False:
                print("Server not found!")
            
        elif server_status == True:
            # створюємо сокет з використанням протоколу IPv4 (AF_INET) та TCP (SOCK_STREAM)
            with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as client_socket:
                # підключаємо користувача до сервера за даними що ввів користувач
                client_socket.connect((ip_address, port))

                
                #отримуємо дані користувачів з бази даних (назва файла з базой даних)
                data_for_server = read_json(name_file = "data_base.json")
                #беремо кількість балів користувача який приєднується до сервера , щоб користувач на сервері знав останнє їхнє значення
                points_for_server = data_for_server[input_nick.user_text]["points"]
                print(points_for_server , "points for client")

                #формуємо дані для відправки на сервер , у виді словника, щоб можна було у одні строці їх відправити
                data_for_server = {
                    "nick": str(input_nick.user_text),
                    "points": points_for_server,
                    "status": list_server_status
                }
                
                #dump - переводить словник , у джейсон строку(наш словник буде у вигляді звичайної строки, що полегшує відправку даних)
                # відправляємо дані від користувача на сервер , та кодуємо їх у байти
                client_socket.send(json.dumps(data_for_server).encode())

                #отримуємовід сервера дані у вигляді байтів , та декодуємо їх
                data = client_socket.recv(1024).decode()
                #переводимо дані які отримали у виді строки у вигляд словаря, щоб модна було брати інйормацію по ключам
                data_in_list = json.loads(data)

                #виводимо отримані дані на консоль
                print(data_in_list["nick"] , "nick from server")
                print(data_in_list["status"] , "status from server")
                print(data_in_list["points"] , "points from server")

                #якщо нік користувача який отримали з серверу не існує в словарі, то додаємо його до словаря з базовими очками
                if data_in_list["nick"] not in list_users:
                    list_users[data_in_list["nick"]] = {"points": data_in_list["points"]}
                    write_json(filename = "data_base.json" , object_dict = list_users)
                #якщо його нікнейм вже є (тобто такий користувач вже є), тоді просто оновлюємо його кількість баллів 
                elif data_in_list["nick"] in list_users:
                    list_users[data_in_list["nick"]]["points"] = data_in_list["points"]
                    write_json(filename = "data_base.json" , object_dict = list_users)

                #зберігаємо статус того що підключилися до серверу, у джейсон файл
                write_json(filename= "utility.json" , object_dict = data_in_list["status"])
                
                
                    

        #створюємо зміну потока, із функцією підключення коритсувача до серверу
thread_connect = threading.Thread(target = connect_user, daemon=True)