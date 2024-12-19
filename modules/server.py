import socket
from .screens import list_grid
#підключаємо модуль для роботи із потоками
import threading
# Импортируем классы
from .classes.class_input_text import input_port , input_ip_adress, input_nick
# Импортируем функцию записи в json файлы
from .json_functions.write_json import write_json , list_server_status , list_users
from .json_functions.json_read import read_json
import json
import time

# список для того чтобы мы получили матрицу соперника только один раз
check_repeat = [0]

# список для проверки перезода на фрейм боя
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

dict_save_information = {
    "player_nick": "",
    "player_points" : 0,
    "enemy_nick" : "",
    "enemy_points" : 0,
}

#ліст для перевірки чи зайшов користувач на сервер
list_server_status = {
    "status": None
}
#зберігаємо інформацію про статус серверу у json файл , поки цей статус пустий тому що не запустили сервер
write_json(filename= "utility.json" , object_dict =  list_server_status)

dict_status_game = {
    "status" : "places ships"
}
write_json(filename= "status_connect_game.json" , object_dict =  dict_status_game)


#створємо функцію для запуску серверу
def start_server(list_grid):
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
        print(ip_address , "ip address")
        print(port, "port")

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

        # 
        list_player_role[0] = "server_player"  

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
        
        #формуємо дані користувача який запустив сервер ,для відправки до клієнта який під'єднався
        data_for_client = {
            "nick": str(input_nick.user_text),
            "points": points_for_client,
            "status": list_server_status
        }
        #відправляємо дані на клієнта , dumps - перетворює словарь у джейсон строку 
        client_socket.send(json.dumps(data_for_client).encode())

    
        while True:
            try:
                time.sleep(1)
                # Зчитуємо дані з файлу
                data_ready = read_json(name_file="status_connect_game.json")
                #нащи данные
                status_from_file = data_ready["status"]

                # Формуємо відповідь
                response = {
                    "status": status_from_file
                    }
                client_socket.send(json.dumps(response).encode())
        
                client_socket.settimeout(3)
                # Отримуємо дані від клієнта
                data_connect = client_socket.recv(1024).decode()
                if data_connect.strip():  # Перевірка, чи є дані
                    data_in_dict = json.loads(data_connect)
                else:
                    print("Почему то данных нет , и рядок пустой")
        
                print(status_from_file)
                print(data_in_dict["status"])

                # Перевірка завершення
                if status_from_file == data_in_dict["status"] and status_from_file != "places ships":
                    list_check_ready_to_fight[0] = "fight"
                    break
                elif status_from_file == "You can connect to the game" and status_from_file != data_in_dict["status"]:
                    list_check_ready_to_fight[0] = "wait"
            except TimeoutError:
                print("Слишком долгое ожидание")
                continue
            except json.JSONDecodeError:
                print("Не получилось декодировать данные/")
                continue
            except Exception as error:
                print(f"Тупая ошибка: {error}")
                continue


        dict_save_information["player_nick"] = str(input_nick.user_text)
        dict_save_information["enemy_nick"] = data_in_list["nick"]
        dict_save_information["player_points"] = points_for_client
        dict_save_information["enemy_points"] = data_in_list["points"]


    while True:
        try:
            time.sleep(1)
            count_server_ships = 0
            count_client_ships = 0

            for row_server in range(len(list_grid)):
                for cell_server in range(len(list_grid[row_server])):
                    if list_grid[row_server][cell_server] != 0 and list_grid[row_server][cell_server] != 5 and list_grid[row_server][cell_server] != 7:
                        count_server_ships += 1

            for row_client in range(len(enemy_matrix[0])):
                for cell_client in range(len(enemy_matrix[0][row_client])):
                    if enemy_matrix[0][row_client][cell_client] != 0 and enemy_matrix[0][row_client][cell_client] != 5 and enemy_matrix[0][row_client][cell_client] != 7:
                        count_client_ships += 1

            if count_server_ships == 0 and count_client_ships > 0:
                list_check_win[0] = "win_client"
                
            elif count_client_ships == 0 and count_server_ships > 0:
                list_check_win[0] = "win_server"

            # список который сохраняет данные по поводу времени
            check_time[0] += 1
            game_information = {
                'turn': turn[0],
                'time': check_time[0],
                'server_matrix': list_grid,
                "new_for_client": enemy_matrix[0],
                "check_end_game": list_check_win[0]
            }

            client_socket.send(json.dumps(game_information).encode())
            client_socket.settimeout(3)
            client_data = client_socket.recv(1024).decode()
            ready_clinet_data = json.loads(client_data)

            if check_repeat[0] == 0:
                enemy_matrix[0] = ready_clinet_data["client_matrix"]
            # обновляем матрицу сервера
            if check_repeat[0] >= 1:
                list_grid = list(ready_clinet_data["new_for_server"])

            if ready_clinet_data["need"] == "no":
                print("nothing")
            elif ready_clinet_data["need"] == "yes":
                print("зашло сюда")
                turn[0] = ready_clinet_data["turn"]
                check_time[0] = 0
                # print(turn[0])
            
            if check_time[0] >= 29:
                check_time[0] = 0
                if turn[0] == "server_turn":
                    turn[0] = "client_turn"
                elif turn[0] == "client_turn":
                    turn[0] = "server_turn"
        
            check_repeat[0] += 1
            print(list_grid)

            if list_check_win[0] != None:
                break


                
        except TimeoutError:
                print("Слишком долгое ожидание")
                continue
        except json.JSONDecodeError:
            print("Не получилось декодировать данные/")
            continue
        except Exception as error:
            print(f"Тупая ошибка: {error}")
            continue

        
        

        
           
        
            
#створюємо зміну потока, для запуску серверу
server_thread = threading.Thread(target = start_server,args=(list_grid,), daemon=True)