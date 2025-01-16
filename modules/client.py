import socket, json, time, pickle
from .classes import input_port, input_ip_adress, input_nick ,list_ships
from .json_functions import write_json , list_users 
from .json_functions.json_read import read_json
import modules.server as server_module
from .screens import list_grid
import modules.shop as shop
import modules.achievement as achievement
from .classes.class_input_text import input_password
from threading import Thread


# лист для клиента в котором храним надо ли что то изменять после его атаки
list_check_need_send = [False]
#список для відслуджування чи підключився користувач до серверу чи ні
list_check_connection = [False]
check_connection_users = [False, False]
# список в котором храним данные которые отправляем другому игроку
data_player_shot = []


def send_matrix():
    list_check_need_send[0] = True
    data_player_shot.append("enemy_matrix")
    for row in list_grid:
        for cell in row:
            data_player_shot.append(str(cell))


dict_status_game = {
    "status" : "places ships"
}
write_json(filename= "status_connect_game.json" , object_dict =  dict_status_game)

# Функция для получения всех данных
def recv_all(sock):
    data = b""
    while True:
        part = sock.recv(1024)
        if not part or b"END" in part:  # Условие завершения передачи
            data += part.split(b"END")[0]
            break
        data += part
    return data

def start_client():
    if input_nick.user_text not in list_users:
        #создаем игрока с его ником и даем базовое количество баллов
        list_users[input_nick.user_text] = {"points": 0,
                                            "password": input_password.user_text
                                            }
        #зберігаємо інформацію у json файл
        write_json(filename = "data_base.json" , object_dict = list_users)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((str(input_ip_adress.user_text), int(input_port.user_text)))  # Подключение к серверу
        print("Клиент подключён к серверу.")
        # Получение сообщения от сервера (роль клиента)
        role = client_socket.recv(1024).decode("utf-8")
        server_module.list_player_role[0] = role
        check_connection_users[0] = "wait"
        data_ready = read_json(name_file = "status_connect_game.json")
        status_ready_to_game = data_ready["status"] 
        # Бесконечный цикл для отправки и получения данных
        while status_ready_to_game != "fight" or check_connection_users[1] != 'fight':
            data_ready = read_json(name_file = "status_connect_game.json")
            status_ready_to_game = data_ready["status"] 
            try:
                if status_ready_to_game != "fight" or check_connection_users[1] != 'fight':
                    time.sleep(0.1)
                    print(1)
                    data_ready = read_json(name_file = "status_connect_game.json")
                    status_ready_to_game = data_ready["status"] 
                    client_socket.sendall(status_ready_to_game.encode("utf-8"))

                    data_enemy = client_socket.recv(1024).decode("utf-8")
                    check_connection_users[1] = data_enemy
                    check_connection_users[0] = "connect"
                    check_connection_users[1] = server_module.enemy_data[0]["check_connection_users"]
                    print(server_module.enemy_data[0])  
            except Exception as e:
                print("Ошибка клиента:", e)
                pass
        send_matrix()
        while True:
            try:
                print(2)
                time.sleep(0.5)
                # Перевірка значення в списку перед відправкою даних
                if list_check_need_send[0] == True:  # Перевірка на `True`
                    str_line = ""
                    for cell in data_player_shot:
                        str_line += str(cell) + " " # Переводимо список в строчку с пробелами
                    client_socket.sendall(str_line.encode("utf-8"))  # Відправка даних як список
                    data_player_shot.clear()  # Очищаем список перед новым входом
                    list_check_need_send[0] = False
                else:
                    client_socket.sendall("keep-alive".encode("utf-8"))

        
                enemy_data = client_socket.recv(1024)
                server_module.enemy_data[0] = enemy_data.decode("utf-8")
                print(server_module.enemy_data, "enemy_data") 

            except Exception as e:
                print("Ошибка клиента:", e)
                pass
    except Exception as e:
        print(f"Ошибка клиента: {e}")

connect_to_game = Thread(target = start_client, daemon = True)

# def connect_user():
#     #если игрок нажал запустить сервер и его еще нет в словаре игроков, то записываем его ник в джейсон
#     if input_nick.user_text not in list_users:
#         #создаем игрока с его ником и даем базовое количество баллов
#         list_users[input_nick.user_text] = {"points": 0,
#                                             "password": input_password.user_text
#                                             }
#         #зберігаємо інформацію у json файл
#         write_json(filename = "data_base.json" , object_dict = list_users)


#     #берем из поля ввода данные для запуска сервера(айпи и порт)
#     # ip_adress = input_ip_adress.user_text
#     # port = int(input_port.user_text)
   
#     # створюємо сокет з використанням протоколу IPv4 (AF_INET) та TCP (SOCK_STREAM)
#     with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as client_socket:
#         # підключаємо користувача до сервера за даними що ввів користувач
#         # client_socket.connect((ip_address, port))
#         # while list_server_status["status"] == None:
#         try:
#             if event_connect_to_server.is_set():
#                 ip_adress = input_ip_adress.user_text
#                 port = int(input_port.user_text)
#                 client_socket.settimeout(0.1)
#                 client_socket.connect((ip_adress, port))
#                 print("підключено до сервера")
#                 event_connect_to_server.clear()
#                 # break
#         except (socket.timeout, OSError):
#             print("server not found")
#             list_check_connection[0] = "error_connection"  # Сбрасываем событие
#             event_connect_to_server.clear()
#             print(event_connect_to_server)
#         server_module.player_ships_coord_len.clear()
#         print(ip_adress , "ip address")
#         print(port , "port")


#         #отримуємо дані користувачів з бази даних (назва файла з базой даних)
#         data_for_server = read_json(name_file = "data_base.json")
#         #беремо кількість балів користувача який приєднується до сервера , щоб користувач на сервері знав останнє їхнє значення
#         points_for_server = data_for_server[input_nick.user_text]["points"]
#         password_for_server = data_for_server[input_nick.user_text]["password"]
#         print(points_for_server , "points for client")
       
#         #формуємо дані для відправки на сервер , у виді словника, щоб можна було у одні строці їх відправити
#         data_for_server = {
#             "nick": str(input_nick.user_text),
#             "points": points_for_server,
#             "status": list_server_status,
#             "password": password_for_server
#         }
    
#         #dump - переводить словник , у джейсон строку(наш словник буде у вигляді звичайної строки, що полегшує відправку даних)
#         # відправляємо дані від користувача на сервер , та кодуємо їх у байти
#         client_socket.send(json.dumps(data_for_server).encode())

#         #отримуємовід сервера дані у вигляді байтів , та декодуємо їх
#         data = client_socket.recv(1024).decode()
#         #переводимо дані які отримали у виді строки у вигляд словаря, щоб модна було брати інйормацію по ключам
#         data_in_list = json.loads(data)

#         #виводимо отримані дані на консоль
#         print(data_in_list["nick"] , "nick from server")
#         print(data_in_list["status"] , "status from server")
#         print(data_in_list["points"] , "points from server")

#         #якщо нік користувача який отримали з серверу не існує в словарі, то додаємо його до словаря з базовими очками
#         if data_in_list["nick"] not in list_users:
#             list_users[data_in_list["nick"]] = {"points": data_in_list["points"], "password": data_in_list["password"]}
#             write_json(filename = "data_base.json" , object_dict = list_users)
#         #якщо його нікнейм вже є (тобто такий користувач вже є), тоді просто оновлюємо його кількість баллів
#         elif data_in_list["nick"] in list_users:
#             list_users[data_in_list["nick"]]["points"] = data_in_list["points"]
#             write_json(filename = "data_base.json" , object_dict = list_users)


#         #зберігаємо статус того що підключилися до серверу, у джейсон файл
#         write_json(filename= "utility.json" , object_dict = data_in_list["status"])


#         server_module.list_player_role[0] = "player_client"
#         while True:
#             try:
#                 time.sleep(0.1)
#                 if server_module.check_connection[0] != False:
#                     server_module.check_connection[0] = True
#                     # Зчитуємо дані з файлу
#                     data_ready = read_json(name_file="status_connect_game.json")
#                     #нащи данные
#                     status_from_file = data_ready["status"] 

#                     # Формуємо відповідь
#                     server_module.responce[0] = str(status_from_file)

#                     client_socket.sendall(server_module.responce[0].encode("utf-8")) 
#                     # Отримуємо дані від серверу
#                     client_socket.settimeout(1)
#                     server_module.data_enemy[0] = client_socket.recv(1024).decode()

#                     if server_module.list_check_check_connection_users[0] == "fight":
#                         break
#                 else:
#                     print(78787878)
#                     client_socket.close()     # Закрываем сокет
#                     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создаём новый
#                     client_socket.connect((ip_adress, port))
#                     server_module.check_connection[0] = True
#                     print(123)
#                     continue
#             except Exception as error:
#                 print(f"Неизвестная ошибка: {error}")
#                 server_module.check_connection[0] = False
#                 # client_socket.close()
#                 continue
#             server_module.dict_save_information["player_nick"] = str(input_nick.user_text)
#             server_module.dict_save_information["enemy_nick"] = data_in_list["nick"]
#             server_module.dict_save_information["player_points"] = points_for_server
#             server_module.dict_save_information["enemy_points"] = data_in_list["points"]
#         # створюємо цикл для бою(щоб робити обмін даними , до потрібного моменту)
#         while True:
#             try:
#                 time.sleep(0.1)  
#                 if server_module.check_connection[0] != False:
#                     server_module.check_connection[0] = True
                
#                     # Отримання всіх даних від серверу
#                     # list_check_need_sen - список который хранит флаг , по которому мы понимаем атакавал клиент или нет
#                     if list_check_need_send[0] == "no":
#                         # якщо не не атакував , то відправляємо дані , але ті які на ход ніяк не влияють(нам потрбіно завжди щось відправляти на севре , щоб не бцло помилки)
#                         client_dict = {
#                             "turn": "server_turn",
#                             "time": 0,
#                             "need" : "no",
#                             'client_matrix':list_grid,
#                             "new_for_server" : server_module.enemy_matrix[0],
#                             "money_balance":shop.money_list[0],
#                             "medals_coordinates":achievement.list_save_coords_achiv,
#                             "player_ships":server_module.player_ships_coord_len,
#                             "row":server_module.row_list[0],
#                             "col":server_module.col_list[0],
#                             "number":server_module.number_list[0],
#                         }
#                         data_list.clear()
#                         data_list.append(client_dict)
#                         client_socket.sendall(pickle.dumps(client_dict))
#                     # якщо клієнт зробив постріл , то перевіряємо чи потрібо змінювати чергу , чи ні
#                     elif list_check_need_send[0] == "yes":
#                         # print(1)
#                         print(server_module.turn[0])
#                         # якщо клієент зробив постріл , але схибив його , то змінюємо чергу за допмогою "turn": "server_turn"
#                         if server_module.turn[0] == "server_turn":
#                             print(2)
#                             client_dict = {
#                                 "turn": "server_turn",
#                                 "time": 0 ,
#                                 "need" : "yes",
#                                 'client_matrix':list_grid,
#                                 "new_for_server" : server_module.enemy_matrix[0],
#                                 "money_balance":shop.money_list[0],
#                                 "medals_coordinates":achievement.list_save_coords_achiv,
#                                 "player_ships":server_module.player_ships_coord_len,
#                                 "row":server_module.row_list[0],
#                                 "col":server_module.col_list[0],
#                                 "number":server_module.number_list[0],
#                             }
#                             # відправляємо дані , але перед цим словарь перетворюємо у строку за допомогою json.dumps
#                             data_list.clear()
#                             data_list.append(client_dict)
#                             client_socket.sendall(pickle.dumps(client_dict))
#                             list_check_need_send[0] = "no"
#                             server_module.check_time[0] = 0
#                             continue
#                         # якщо клієнт зробив постріл і потрапив по кораблю , то не змінюємо чергу , а просто обнуляємо час , оскільки клієнт потрпив
#                         if server_module.turn[0] == "client_turn":
#                             # print(3)
#                             client_dict = {
#                                 "turn": "client_turn",
#                                 "time": 0 ,
#                                 "need" : "yes",
#                                 'client_matrix':list_grid,
#                                 "new_for_server" : server_module.enemy_matrix[0],
#                                 "money_balance":shop.money_list[0],
#                                 "medals_coordinates":achievement.list_save_coords_achiv,
#                                 "player_ships":server_module.player_ships_coord_len,
#                                 "row":server_module.row_list[0],
#                                 "col":server_module.col_list[0],
#                                 "number":server_module.number_list[0],
#                             }
#                             data_list.clear()
#                             data_list.clear()
#                             data_list.append(client_dict)
#                             client_socket.sendall(pickle.dumps(client_dict))                    # перетворбємо дані від сереру у формат словарю(перед перетворенням це було json строкою)

#                             list_check_need_send[0] = "no"
#                             server_module.check_time[0] = 0
#                             continue
#                     # client_socket.settimeout(3)
#                     try:
#                         data_turn = server_module.recv_all(client_socket)                # перетворбємо дані від сереру у формат словарю(перед перетворенням це було json строкою)
#                     except socket.timeout:
#                         print("Слишком долгое ожидание от сервера")
#                         continue
#                     server_module.enemy_data[0] = pickle.loads(data_turn)                    # перетворбємо дані від сереру у формат словарю(перед перетворенням це було json строкою)
                     
#                     # записуємо у список збереження черги , із даних , що підправив сервер(оскільки він керує чия зараз черга)
#                     server_module.turn[0] = server_module.enemy_data[0]['turn']
#                     server_module.check_repeat[0] += 1

#                     if server_module.row_list[0] != 100 and server_module.check_send_data_health[0] <= 9:
#                         server_module.check_send_data_health[0] += 1
#                     # если кто то уже выиграл , то остонавливаем цикл игры
#                     # если в list_check_win[0] лежит пустота , то значит что еще никто не выиграл
#                     if server_module.enemy_data[0]["check_end_game"] != None:
#                         server_module.list_check_win[0] = server_module.enemy_data[0]["check_end_game"]
#                         break
#             except Exception as error:
#                 print(f"Неизвестная ошибка: {error}")
#                 # client_socket.close()
#                 continue
          

# #створюємо зміну потока, із функцією підключення коритсувача до серверу
# thread_connect = threading.Thread(target = connect_user ,daemon = True)