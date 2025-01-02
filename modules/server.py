import socket , json , time , threading
from .screens import list_grid
# Импортируем классы
from .classes import input_port , input_ip_adress, input_nick , Animation
# Импортируем функцию записи в json файлы
from .json_functions import write_json , list_server_status , list_users , read_json
# from .shop import kept_all_ships_laive_for_five_turns , first_kill_four_decker , first_task , second_task , third_task , fourth_task , list_first_task , list_second_task , list_third_task , list_fourth_task
import modules.shop as shop

# чтобы у на ототбражались зачеркнутые клеточки вокргу корабля
our_miss_anim = []

# функция для болной загрузки данных
def recv_all(socket, buffer_size = 1024):
    data = b""
    while True:
        part = socket.recv(buffer_size)
        data += part
        if len(part) < buffer_size:  # Якщо менше buffer_size, це остання частина
            break
    return data

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
#сохранаяем координаты где должнны отображаться анимация зачеркивания клеточек,  когда враг убил У НАС КОРАБЛЬ
save_miss_coordinates = []
# сохраняем где отрисовываем анимацию зачеркания когда мы убили корабль
enemy_animation_miss_coord = []
# список где сохраняем баланс врага
enemy_balance = [0]
# словарь для зберігання інформаці про гравців
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

        # Бесконечный цикл для провери расстановки кораблей
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

                if data_connect.strip():  
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

    # бесконечный цикл для боя
    while True:
        try:
            for our_kill_ship_anim_miss in enemy_animation_miss_coord:
                animation_miss = Animation(
                                x_cor = our_kill_ship_anim_miss[0] - 637,
                                y_cor = our_kill_ship_anim_miss[1],
                                image_name="0.png",
                                width = 55,
                                height = 55,
                                need_clear = False,
                                name_folder = "animation_miss"
                            )
                if len(enemy_animation_miss_coord) > 0:
                    exit = False
                    for anim_miss in our_miss_anim:
                        if anim_miss.X_COR == animation_miss.X_COR and anim_miss.Y_COR == animation_miss.Y_COR:
                            exit= True
                    if not exit:
                        our_miss_anim.append(animation_miss)
                        enemy_matrix[0][our_kill_ship_anim_miss[2]][our_kill_ship_anim_miss[3]] = 5
            # робимо зупинку на 0.1 секунду , що сервер і клієент встигали обмінюватися данними
            time.sleep(0.1)
            check_ten_times.append(1)

            # счетчик кораблей сервера
            count_server_ships = 0
            # счетчик кораблей клиента
            count_client_ships = 0

            # делаем перебор матриц сервера и клиента, чтобы проверять ввыиграл уже кто то или нет
            for row_server in range(len(list_grid)):
                for cell_server in range(len(list_grid[row_server])):
                    # 5 - по клетке уже стреляли
                    # 0 - кораблей просто нет
                    # 7 - уже потопленный корабль
                    if list_grid[row_server][cell_server] != 0 and list_grid[row_server][cell_server] != 5 and list_grid[row_server][cell_server] != 7:
                        count_server_ships += 1

            for row_client in range(len(enemy_matrix[0])):
                for cell_client in range(len(enemy_matrix[0][row_client])):
                    # 5 - по клетке уже стреляли
                    # 0 - кораблей просто нет
                    # 7 - уже потопленный корабль
                    if enemy_matrix[0][row_client][cell_client] != 0 and enemy_matrix[0][row_client][cell_client] != 5 and enemy_matrix[0][row_client][cell_client] != 7:
                        count_client_ships += 1

            # если кораблей сервера не осталовь , то выиграл клиент
            if count_server_ships == 0 and count_client_ships > 0:
                # список для хранения кто выиграл
                list_check_win[0] = "win_client"
            # если кораблей клиента не осталось , то выиграл сервер
            elif count_client_ships == 0 and count_server_ships > 0:
                # список для хранения кто выиграл
                list_check_win[0] = "win_server"

            # список который сохраняет данные по поводу времени
            if check_ten_times.count(1) >= 10:
                check_ten_times.clear()
                check_time[0] += 1

            # turn[0] - список для хранения очереди 
            # check_time[0] - список который сохраняет данные по поводу времени
            # 'server_matrix' - матрица пользователя который играет за сервер
            # "new_for_client" - матрица в которой хранится матрица уже с нашими выстрелами(выстрелами сервера)
            # "check_end_game" - список который хранит данные о побидители игры
            #"first_kill_3deck" - список в котоором хранится сколько у игрока осталось трехпалубныъ кораблей , и за счет того понимаем кто первый убил трех палубный кораблик
            #"misses_coordinate" - координаты где должнна отображаться анимация зачеркивания клеточек,  когда враг убил У НАС КОРАБЛЬ
            # ""money_balance"" - баланс игрока
            # "check_ten_times" - счетчик чтобы каждые десять циклов отнималась одна секунда для хода игрока(так как у нас tim.sleep(0.1 секунда)) , значит 10 повторений одна секунда
            game_information = {
                'turn': turn[0],
                'time': check_time[0],
                'server_matrix': list_grid,
                "new_for_client": enemy_matrix[0],
                "check_end_game": list_check_win[0] ,
                "first_kill_3deck": shop.enemy_ships_3decker[0],
                "misses_coordinate": save_miss_coordinates,
                "money_balance":shop.money_list[0],
                "check_ten_times":check_ten_times.count(1)
            }

            # отправляем даныне на сервер , и делаем их джейсон строкой
            client_socket.send(json.dumps(game_information).encode())
            # settimeout(3) - ставит ожидания 3 секунды , и если за это время никакие данные от клиента не прийдут , то выдает ошибку
            client_socket.settimeout(3)
            # client_data = client_socket.recv(1024).decode()
            # ready_clinet_data = json.loads(client_data)

            # Отримання всіх даних
            client_data = recv_all(client_socket).decode()
            # Розбір JSON
            ready_clinet_data = json.loads(client_data)

            enemy_balance[0] = ready_clinet_data["money_balance"]

            for coord_miss in ready_clinet_data["misses_coordinate"]:
                if coord_miss not in enemy_animation_miss_coord:
                    enemy_animation_miss_coord.append(coord_miss)

            if check_repeat[0] == 0:
                enemy_matrix[0] = ready_clinet_data["client_matrix"]
            # обновляем матрицу сервера(ready_clinet_data["new_for_server"] - матрица в которой хранится пострелы клиента)
            if check_repeat[0] >= 1:
                for row in range(len(ready_clinet_data["new_for_server"])):
                        for cell in range(len(ready_clinet_data["new_for_server"][row])):
                            list_grid[row][cell] = ready_clinet_data["new_for_server"][row][cell]

            # проверяем стрелял ли клиент или нет
            if ready_clinet_data["need"] == "no":
                # если нет , то ничего не делаем
                pass
            # если клиент стерлял , записываем чья сейчас очерель(это зависит от того попал ли клиент или нет)
            elif ready_clinet_data["need"] == "yes":
                print("зашло сюда")
                turn[0] = ready_clinet_data["turn"]
                check_time[0] = 0
              
            # если прошло 30 сек , и никто не походил , то меняем очередь
            if check_time[0] >= 29:
                check_time[0] = 0
                if turn[0] == "server_turn":
                    turn[0] = "client_turn"
                elif turn[0] == "client_turn":
                    turn[0] = "server_turn"

            if turn[0] == "client_turn" and check_time[0] == 1 and check_ten_times.count(1) == 1:
                print(111)
                if shop.second_task.TEXT == shop.list_second_task[1]:
                    shop.kept_all_ships_alive_for_five_turns(grid = list_grid)
                

            # первым убить четрыех палбный кораблик
            if shop.third_task.TEXT == shop.list_third_task[0]:
                shop.first_kill_four_decker(grid = list_grid , enemy_grid = enemy_matrix)

            
            if shop.second_task.TEXT == shop.list_second_task[-1]:
                if ready_clinet_data["first_kill_3deck"] != "kill three-decker ship":
                    shop.first_kill_three_decker(grid = list_grid , enemy_grid = enemy_matrix)

            
            check_repeat[0] += 1

            
            # если кто то уже выиграл , то остонавливаем цикл игры
            # если в list_check_win[0] лежит пустота , то значит что еще никто не выиграл
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
server_thread = threading.Thread(target = start_server, daemon=True)