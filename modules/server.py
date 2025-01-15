import socket 
import colorama
# Импортируем классы
from threading import Thread


# функция для болной загрузки данных
def recv_all(sock):
    data = b""
    while True:
        part = sock.recv(1024)  # Получаем данные порциями
        if not part:
            break
        data += part
    return data



responce = [1]
data_enemy = [0]
enemy_data = [""]
#где стоят корабли соперника
enemy_ships = [""]
player_ships_coord_len = []
# для восстановления клеточки
number_list = [100]
row_list = [100]
col_list = [100]
check_send_data_health = [0]
# счетчик чтобы взять новые данные про умершие корабли врага
get_new_killed_data = [0]
# список для того чтобы от времени отнималась ровно одна секунда
check_ten_times = []
# список для того чтобы мы получили матрицу соперника только один раз
check_repeat = [0]
# список для проверки перехода на фрейм боя
list_check_ready_to_fight = [None]
# лист очереди
turn = ["server_turn"]
# лист таймер времени
check_time = [0]
# Лист для проверки за кого мы играем(сервер или клиент)
list_player_role = [""]
# лист где храним матрицу врага
enemy_matrix = ["yes"]
# список куда сохраняем кто выиграл
list_check_win = [None]
# сохраняем где отрисовываем анимацию зачеркания когда мы убили корабль
enemy_animation_miss_coord = []
# список где сохраняем баланс врага
enemy_balance = [0]
# сохраняем координаты вражеских медалей
save_medals_coordinates = []
# список в котором храним какие корабли убили у игрока
player_died_ships = []
# список в коотором храним какие корабли убил игрок у врага
enemy_died_ships = []
#------------------------------------------------------------------------------------------------
flag_bomb_animation = [False]
#------------------------------------------------------------------------------------------------
# флаг в котором храним все ли впорядке с связью между игроками
check_connection = [True]


# словарь для зберігання інформаці про гравців
dict_save_information = {
    "player_nick": "",
    "player_points" : 0,
    "enemy_nick" : "",
    "enemy_points" : 0,
}

# #ліст для перевірки чи зайшов користувач на сервер
# list_server_status = {
#     "status": None
# }
# #зберігаємо інформацію про статус серверу у json файл , поки цей статус пустий тому що не запустили сервер
# write_json(filename= "utility.json" , object_dict =  list_server_status)

# dict_status_game = {
#     "status" : "places ships"
# }
# write_json(filename= "status_connect_game.json" , object_dict =  dict_status_game)
# #створємо функцію для запуску серверу
# def start_server():
#     #если игрок нажал запустить сервер и его еще нет в словаре игроков, то записываем его ник в джейсон
#     if input_nick.user_text not in list_users:
#         #создаем игрока с его ником и даем базовое количество баллов
#         list_users[input_nick.user_text] = {"points": 0,
#                                             "password": input_password.user_text
#                                             }
#         #зберігаємо інформацію у json файл
#         write_json(filename = "data_base.json" , object_dict = list_users)

#     #берем из поля ввода данные для запуска сервера(айпи и порт)
#     ip_address = input_ip_adress.user_text
#     port = int(input_port.user_text)
    
#     # Створюємо сокет з використанням протоколу IPv4 (AF_INET) та TCP (SOCK_STREAM)
#     with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as server_socket:
#         # Прив'язуємо сокет до порту що ввів користувач, та Прив'язуємо по якому айпі можуть до нього підключитися
#         server_socket.bind((ip_address, port))
#         #Ставимо сервер у режим очікування підключень
#         server_socket.listen()
#         print("connecting")
#         print(ip_address , "ip address")
#         print(port, "port")
#         player_ships_coord_len.clear()

#         #записуємо в словарь статус очікування підключення до серверу
#         #передаем в словарь файл статус ожидания
#         list_server_status = {
#             "status": "wait"
#         }
#         #зберігаємо інформацію про статус підлючення до серверу у json файл
#         write_json(filename= "utility.json" , object_dict = list_server_status)
        
#         #приймаємо користувача який під'єднується до серверу
#         client_socket, adress = server_socket.accept()


#         #записуємо у словарь статус того що до серверу під'єднався користувач
#         list_server_status = {
#             "status": "connect"
#         }
#         #зберігаємо інформацію про статус підлючення до серверу у json файл
#         write_json(filename= "utility.json" , object_dict = list_server_status)

      
#         list_player_role[0] = "server_player"  

#         # Отримуємо дані від клієнта(нікнейм та скільки у нього баллів), у виді джейсон строки
#         response_data = client_socket.recv(1024).decode()
#         #перетворюємо json сктроку , у словник
#         data_in_list = json.loads(response_data)
#         print(data_in_list, "from client")


#         #якщо нікнейма суперника ще немає у словарі то записуємо його нік у джейосн файл
#         if data_in_list["nick"] not in list_users:
#             list_users[data_in_list["nick"]] = {"points": data_in_list["points"], "password": data_in_list["password"]}
#             write_json(filename = "data_base.json" , object_dict = list_users)

#         #якщо його нікнейм вже є , тоді просто оновлюємо його кількість баллів 
#         elif data_in_list["nick"] in list_users:
#             list_users[data_in_list["nick"]]["points"] = data_in_list["points"]
#             write_json(filename = "data_base.json" , object_dict = list_users)

#         #отримуємо дані про користувачів з бази даних  (назва файла з базой даних)
#         data_for_client = read_json(name_file = "data_base.json")
#         #беремо кол-во баллів користувача який запсукає сервер, щоб відправати оновлену кількість 
#         points_for_client = data_for_client[input_nick.user_text]["points"]
#         password_for_client = data_for_client[input_nick.user_text]["password"]

#         print(points_for_client , "points for client")
        
#         #формуємо дані користувача який запустив сервер ,для відправки до клієнта який під'єднався
#         data_for_client = {
#             "nick": str(input_nick.user_text),
#             "points": points_for_client,
#             "status": list_server_status,
#             "password": password_for_client
#         }
#         #відправляємо дані на клієнта , dumps - перетворює словарь у джейсон строку 
#         client_socket.send(json.dumps(data_for_client).encode())
#         # Бесконечный цикл для провери расстановки кораблей
#         while True:
#             time.sleep(0.1)
#             try:
#                 if check_connection[0] != False and list_check_ready_to_fight[0] != "fight":
#                     check_connection[0] = True
#                     data_ready = read_json(name_file="status_connect_game.json")
#                     #нащи данные
#                     status_from_file = data_ready["status"]

#                     # Формуємо відповідь
                
#                     responce[0] = str(status_from_file)
                        
#                     client_socket.sendall(responce[0].encode()) 
#                     print(8989)
#                     # Отримуємо дані від клієнта
#                     # client_socket.settimeout(1)
#                     data_enemy[0] = client_socket.recv(1024).decode()
                    
#                     if list_check_ready_to_fight[0] == "fight":
#                         check_connection[0] = True
#                         print("Вышло")
                
#                     dict_save_information["player_nick"] = str(input_nick.user_text)
#                     dict_save_information["enemy_nick"] = data_in_list["nick"]
#                     dict_save_information["player_points"] = points_for_client
#                     dict_save_information["enemy_points"] = data_in_list["points"]
#                 elif check_connection[0] != False and list_check_ready_to_fight[0] == "fight":
#                     print(7878)
#                     check_connection[0] = True
#                     # # робимо зупинку на 0.1 секунду , що сервер і клієент встигали обмінюватися данними
#                     check_ten_times.append(1)
#                     # # список который сохраняет данные по поводу времени
#                     if check_ten_times.count(1) >= 10:
#                         check_ten_times.clear()
#                         check_time[0] += 1

#                     game_information = {
#                         'turn': turn[0],
#                         'time': check_time[0]
#                     }   
#                     # # отправляем даныне на сервер , и делаем их джейсон строкой
#                     # client_socket.sendall(pickle.dumps(game_information))
#                     try:
#                         client_data = recv_all(client_socket)
#                         enemy_data[0] = pickle.loads(client_data)
#                     except TimeoutError:
#                         print("Клиент не ответил вовремя. Пропускитть надо")
#                         continue
#                     print(8989)
#                     print(enemy_data[0]["turn"])
#                     # if check_time[0] >= 30:
#                     #     check_time[0] = 0
#                     #     if turn[0] == "server_turn":
#                     #         turn[0] = "client_turn"
#                     #     elif turn[0] == "client_turn":
#                     #         turn[0] = "server_turn"
#                 else:
#                     #Ставимо сервер у режим очікування підключень
#                     server_socket.listen()
#                     #приймаємо користувача який під'єднується до серверу
#                     client_socket, adress = server_socket.accept()
#                     check_connection[0] = True
#                     print(colorama.Fore.GREEN + "Connectcnion is restarted" + colorama.Fore.GREEN)
#                     continue
#             except Exception as error:
#                 print(f"Неизвестная ошибка: {error}")
#                 check_connection[0] = False
#                 continue
                    

                      
# #створюємо зміну потока, для запуску серверу
# server_thread = threading.Thread(target = start_server, daemon=True)
def listen_client(client, second_client):
    while True:
        try:
            data = client.recv(1024)
            if data:
                second_client.sendall(data)
        except ConnectionResetError:
            SERVER.RESTART = True
            break
        except Exception as error:
            print("Error occurred:", error)
            SERVER.RESTART = True
            break

class Server():
    def __init__(self):
        self.RESTART = False
    def start_server(self, ip_adress: str, port: int):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((str(ip_adress), int(port)))
        while True:
            try:
                print(f"Room ip_adress {colorama.Fore.GREEN} {ip_adress} {colorama.Style.RESET_ALL}")
                print(f"Room Port:{colorama.Fore.GREEN} {port} {colorama.Style.RESET_ALL}")
                self.server_socket.listen()
                print("Server started working")
                print("Waiting clients")
                client_socket, addr = self.server_socket.accept()
                client_socket.sendall("server_player".encode("utf-8"))
                print("First player is connected")
                client_socket_second, addr_second = self.server_socket.accept()
                client_socket_second.sendall("client_player".encode("utf-8"))
                print("Second player is connecter")

                thread1 = Thread(target = listen_client, args = (client_socket, client_socket_second))
                thread1.start()

                thread2 = Thread(target = listen_client, args = (client_socket_second, client_socket))
                thread2.start()
                print(3)
                if self.RESTART:
                    print("Server problemin")
                    self.RESTART = False
                    raise Exception("RESTART")
            except:
                print("Exception server")
                pass
SERVER = Server()

def run_server(input_ip_address, input_port):
    server = Server()
    server.start_server(input_ip_address, input_port)

