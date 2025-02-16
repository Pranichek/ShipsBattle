import socket, time, colorama
from .classes import input_port, input_ip_adress, input_nick ,list_ships
from .json_functions import write_json , list_users 
import modules.server as server_module
from .screens import list_grid, enemy_matrix
import modules.shop as shop
import modules.achievement as achievement
from .classes.class_input_text import input_password
from threading import Thread
from .server import SERVER, list_check_win

colorama.init(autoreset = True)
RED = colorama.Fore.RED

# лист для клиента в котором храним надо ли что то изменять после его атаки
list_check_need_send = [False]
#список для відслуджування чи підключився користувач до серверу чи ні
list_check_connection = [False]
check_connection_users = [False, False]
# список в котором храним данные которые отправляем другому игроку
data_player_shot = []
# список для того чтобы время было ровно по секундам
check_two_times = []
# список для подсчета сколько времени оба игрока расставели корабли, чтобы точно все успели прдклюючиться к бою
check_can_connect_to_fight = [0, False, False]
# список в котором сохраняем расставил ли игрок корабли
save_data_posistion_ships = ["start"]
connection = [True]
check_start_time_thread = [False]
your_turn = [0]

dict_save_information = {
    "player_nick": "",
    "player_points": 0,
    "enemy_nick": "",
    "enemy_points": 0,
    "enemy_password": ""
}


def send_matrix():
    data_player_shot.clear()  # Очищаем данные перед добавлением новых
    data_player_shot.append("enemy_matrix")
    for row in list_grid:  
        for cell in row:
            data_player_shot.append(str(cell))
    for ship in list_ships:
        data_player_shot.append(str(ship.row))
        data_player_shot.append(str(ship.col))
        data_player_shot.append(str(ship.LENGHT))
        data_player_shot.append(str(ship.ORIENTATION_SHIP))
    data_player_shot.append(input_nick.user_text)
    data_player_shot.append(input_password.user_text)
    try:
        data_player_shot.append(list_users[input_nick.user_text]["points"])
    except:
        data_player_shot.append(0)
    list_check_need_send[0] = True
    

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

check_start_connect = [False, False, False]
def start_client():
    check_start_connect[0] = True
    while True:
        try:
            if check_start_connect[1] == True:
                # Создание нового сокета при каждой попытке
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.settimeout(0.1)
                # Попытка подключения к серверу
                port_client = int(input_port.user_text)
                client_socket.connect((str(input_ip_adress.user_text), port_client))
                print("Успешное подключение!")
                client_socket.settimeout(None)
                break
        except Exception as error:
            check_start_connect[1] = False
            time.sleep(1)
            client_socket.settimeout(None)
            continue

    # Получение сообщения от сервера (роль клиента)
    role = client_socket.recv(1024).decode("utf-8")
    server_data = role.split(" ")
    server_module.list_player_role[0] = server_data[0]
    your_turn[0] = server_data[1]
    # Бесконечный цикл для отправки и получения данных
    while list_check_win[0] == None:
        if list_check_win[0] != None:
            break
        try:
            connection[0] = True
            if check_can_connect_to_fight[0] != True:
                time.sleep(0.1)
                check_connection_users[1] = False
                client_socket.sendall(save_data_posistion_ships[0].encode("utf-8"))
                try:
                    if check_can_connect_to_fight[2] != False:
                        client_socket.settimeout(3)
                    data_enemy = client_socket.recv(1024).decode("utf-8")
                except Exception as exception:
                    raise Exception("Reconnect", exception)
                check_connection_users[0] = True
                check_can_connect_to_fight[1] = data_enemy
                if save_data_posistion_ships[0] == "fight" and data_enemy == 'fight':
                    check_can_connect_to_fight[0] = True
                check_connection_users[1] = True
            else:
                time.sleep(0.3)
                # Перевірка значення в списку перед відправкою даних
                if list_check_need_send[0] == True:  # Перевірка на `True`
                    str_line = ""
                    for cell in data_player_shot:
                        str_line += str(cell) + " " # Переводимо список в строчку с пробелами
                    client_socket.sendall(str_line.encode("utf-8") + b"END")  # Відправка даних як список
                    data_player_shot.clear()  # Очищаем список перед новым входом
                    list_check_need_send[0] = False
                else:
                    data_player_shot.append("keep-alive")
                    str_line = ""
                    for row in range(len(enemy_matrix)):
                        for col in range(len(enemy_matrix[row])):
                            if enemy_matrix[row][col] == 7:
                                str_col = str(col)
                                number_cell = (row * 10) + int(str_col[-1])
                                data_player_shot.append(number_cell)
                    for cell in data_player_shot:
                        str_line += str(cell) + " "
                    client_socket.sendall(str_line.encode("utf-8") + b"END")
                    data_player_shot.clear()
                try:
                    if server_module.enemy_data[0] != "":
                        client_socket.settimeout(6)
                    enemy_data = recv_all(client_socket)
                except:
                    raise Exception("Reconnect")
                server_module.enemy_data[0] = enemy_data.decode("utf-8")

        except Exception as error:
            print(f"Error(client error): {RED}{error}")
            port_client += 1
            while True:
                if list_check_win[0] != None:
                    break
                try:
                    try:
                        client_socket.close()
                    except Exception as error:
                        print(f"Error(client_socket.close): {RED}{error}")
                    
                    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    connection[0] = False
                    print(port_client)
                    client_socket.connect((str(input_ip_adress.user_text), port_client)) 
                    break
                except:
                    time.sleep(1)
                    continue

                
def count_time():
    check_start_time_thread[0] = True
    while list_check_win[0] == None:
        if list_check_win[0] != None:
            break
        if connection[0] == True:
            check_two_times.append(3)
        time.sleep(0.5)
