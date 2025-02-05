import socket, json, time, pickle
from .classes import input_port, input_ip_adress, input_nick ,list_ships
from .json_functions import write_json , list_users 
import modules.server as server_module
from .screens import list_grid
import modules.shop as shop
import modules.achievement as achievement
from .classes.class_input_text import input_password
from threading import Thread
from .server import SERVER, list_check_win


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

dict_save_information = {
    "player_nick": "",
    "player_points" : 0,
    "enemy_nick" : "",
    "enemy_points" : 0,
}


def send_matrix():
    data_player_shot.clear()  # Очищаем данные перед добавлением новых
    data_player_shot.append("enemy_matrix")
    for row in list_grid:  # Предполагается, что list_grid соответствует enemy_matrix
        for cell in row:
            data_player_shot.append(str(cell))
    for ship in list_ships:
        data_player_shot.append(str(ship.row))
        data_player_shot.append(str(ship.col))
        data_player_shot.append(str(ship.LENGHT))
        data_player_shot.append(str(ship.ORIENTATION_SHIP))
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
    print("Запуска клиента происходит")
    if input_nick.user_text not in list_users:
        #создаем игрока с его ником и даем базовое количество баллов
        list_users[input_nick.user_text] = {"points": 0,
                                            "password": input_password.user_text
                                            }
        #зберігаємо інформацію у json файл
        write_json(filename = "data_base.json" , object_dict = list_users)
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
            print("Неправильные данные", error)
            time.sleep(0.1)
            client_socket.settimeout(None)
            continue

    print("Клиент подключён к серверу.")
    # Получение сообщения от сервера (роль клиента)
    role = client_socket.recv(1024).decode("utf-8")
    server_module.list_player_role[0] = role
    # Бесконечный цикл для отправки и получения данных
    while list_check_win[0] == None:
        if list_check_win[0] != None:
            break
        try:
            connection[0] = True
            if check_can_connect_to_fight[2] != 'True':
                time.sleep(0.1)
                status_game = [save_data_posistion_ships[0], input_nick.user_text, input_password.user_text, list_users[input_nick.user_text]["points"],check_can_connect_to_fight[0]]
                str_data = ""
                for data in status_game:
                    str_data += f"{str(data)} "
                client_socket.sendall(str_data.encode("utf-8"))
                try:
                    if check_can_connect_to_fight[2] != False:
                        client_socket.settimeout(3)
                    data_enemy = client_socket.recv(1024).decode("utf-8")
                except Exception as exception:
                    raise Exception("Reconnect", exception)
                print(data_enemy)
                data = data_enemy.split(" ")
                check_connection_users[0] = save_data_posistion_ships[0]
                if len(data) >= 4:
                    check_can_connect_to_fight[2] = data[4]
                    if data[1] not in list_users:
                        list_users[data[1]] = {"points": int(data[3]), "password": data[2]}
                        write_json(filename = "data_base.json" , object_dict = list_users)
                    #якщо його нікнейм вже є , тоді просто оновлюємо його кількість баллів 
                    elif data[1] in list_users:
                        list_users[data[1]]["points"] = int(data[3])
                        write_json(filename = "data_base.json" , object_dict = list_users)

                    if save_data_posistion_ships[0] == "fight" and data[0] == 'fight':
                        check_can_connect_to_fight[0] = True
                    try:
                        dict_save_information["player_nick"] = input_nick.user_text
                        dict_save_information["enemy_nick"] = data[1]
                        dict_save_information["player_points"] = int(list_users[input_nick.user_text]["points"])
                        dict_save_information["enemy_points"] = int(data[3])
                    except:
                        pass
                else:
                    print("Index error")
                    if save_data_posistion_ships[0] == "fight":
                        check_can_connect_to_fight[2] = 'True'
            else:
                time.sleep(0.5)
                # Перевірка значення в списку перед відправкою даних
                if list_check_need_send[0] == True:  # Перевірка на `True`
                    str_line = ""
                    for cell in data_player_shot:
                        str_line += str(cell) + " " # Переводимо список в строчку с пробелами
                    client_socket.sendall(str_line.encode("utf-8") + b"END")  # Відправка даних як список
                    data_player_shot.clear()  # Очищаем список перед новым входом
                    list_check_need_send[0] = False
                else:
                    client_socket.sendall("keep-alive".encode("utf-8") + b"END")
                try:
                    if server_module.enemy_data[0] != "":
                        client_socket.settimeout(3)
                    enemy_data = recv_all(client_socket)
                except:
                    raise Exception("Reconnect")
                server_module.enemy_data[0] = enemy_data.decode("utf-8")
                
                # print(server_module.enemy_data, "enemy_data") 
        except Exception as e:
            print(e)
            port_client += 1
            while True:
                if list_check_win[0] != None:
                    break
                try:
                    try:
                        client_socket.close()
                    except:
                        pass
                    print(2)
                    connection[0] = False
                    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    print(3)
                    print(port_client)
                    client_socket.connect((str(input_ip_adress.user_text), port_client)) 
                    print(5)
                    break
                except:
                    time.sleep(1)
                    continue
    print("Клиент отключён от сервера.")
    client_socket.close()
                
# connect_to_game = Thread(target = start_client, daemon = True)

def count_time():
    check_start_time_thread[0] = True
    while list_check_win[0] == None:
        if list_check_win[0] != None:
            break
        if connection[0] == True:
            check_two_times.append(3)
        time.sleep(0.5)
# count_time_thread = Thread(target = count_time, daemon = True)
