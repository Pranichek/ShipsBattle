import socket , json , time , threading, pickle
from .screens import list_grid
# Импортируем классы
from .classes import input_port , input_ip_adress, input_nick, list_ships
# Импортируем функцию записи в json файлы
from .json_functions import write_json , list_server_status , list_users , read_json
import modules.shop as shop
import modules.achievement as achievement
from .classes.class_input_text import input_password


# функция для болной загрузки данных
def recv_all(socket, buffer_size = 1024):
    data = b""
    while True:
        part = socket.recv(buffer_size)
        data += part
        if len(part) < buffer_size:  # Якщо менше buffer_size, це остання частина
            break
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
        list_users[input_nick.user_text] = {"points": 0,
                                            "password": input_password.user_text
                                            }
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
        player_ships_coord_len.clear()

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
            list_users[data_in_list["nick"]] = {"points": data_in_list["points"], "password": data_in_list["password"]}
            write_json(filename = "data_base.json" , object_dict = list_users)

        #якщо його нікнейм вже є , тоді просто оновлюємо його кількість баллів 
        elif data_in_list["nick"] in list_users:
            list_users[data_in_list["nick"]]["points"] = data_in_list["points"]
            write_json(filename = "data_base.json" , object_dict = list_users)

        #отримуємо дані про користувачів з бази даних  (назва файла з базой даних)
        data_for_client = read_json(name_file = "data_base.json")
        #беремо кол-во баллів користувача який запсукає сервер, щоб відправати оновлену кількість 
        points_for_client = data_for_client[input_nick.user_text]["points"]
        password_for_client = data_for_client[input_nick.user_text]["password"]

        print(points_for_client , "points for client")
        
        #формуємо дані користувача який запустив сервер ,для відправки до клієнта який під'єднався
        data_for_client = {
            "nick": str(input_nick.user_text),
            "points": points_for_client,
            "status": list_server_status,
            "password": password_for_client
        }
        #відправляємо дані на клієнта , dumps - перетворює словарь у джейсон строку 
        client_socket.send(json.dumps(data_for_client).encode())
        # Бесконечный цикл для провери расстановки кораблей
        while True:
            try:
                time.sleep(0.1)
                if check_connection[0] != False:
                    check_connection[0] = True
                    data_ready = read_json(name_file="status_connect_game.json")
                    #нащи данные
                    status_from_file = data_ready["status"]

                    # Формуємо відповідь
                
                    responce[0] = str(status_from_file)
                        
                    client_socket.sendall(responce[0].encode("utf-8")) 
                    print(8989)
                    # Отримуємо дані від клієнта
                    client_socket.settimeout(1)
                    data_enemy[0] = client_socket.recv(1024).decode()
                    
                    if list_check_ready_to_fight[0] == "fight":
                        check_connection[0] = True
                        break
                else:
                    #Ставимо сервер у режим очікування підключень
                    server_socket.listen()
                    #приймаємо користувача який під'єднується до серверу
                    client_socket, adress = server_socket.accept()
                    check_connection[0] = True
                    print(123)
                    continue
            except Exception as error:
                print(f"Неизвестная ошибка: {error}")
                check_connection[0] = False
                continue


        dict_save_information["player_nick"] = str(input_nick.user_text)
        dict_save_information["enemy_nick"] = data_in_list["nick"]
        dict_save_information["player_points"] = points_for_client
        dict_save_information["enemy_points"] = data_in_list["points"]
        client_socket.close()
        # бесконечный цикл для боя
        while True:
            try:
                time.sleep(0.1)  
                if check_connection[0] != False:
                    check_connection[0] = True

                    # # робимо зупинку на 0.1 секунду , що сервер і клієент встигали обмінюватися данними
                    check_ten_times.append(1)
                    
                    # # список который сохраняет данные по поводу времени
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
                    # "medals_coordinates" - координаты медалей которые нужно отобразить на экране(для врага) , я как игрок получил медаль , и у врага должно это отобразится
                    # "plyer_died_ships" - корабли которые убмлм у игрока 
                    game_information = {
                        'turn': turn[0],
                        'time': check_time[0],
                        'server_matrix': list_grid,
                        "new_for_client": enemy_matrix[0],
                        "check_end_game": list_check_win[0],
                        "money_balance":shop.money_list[0],
                        "check_ten_times":check_ten_times.count(1),
                        "medals_coordinates":achievement.list_save_coords_achiv,
                        "player_ships":player_ships_coord_len,
                        "row":row_list[0],
                        "col":col_list[0],
                        "number":number_list[0]
                    }   


                    # отправляем даныне на сервер , и делаем их джейсон строкой
                    client_socket.sendall(pickle.dumps(game_information))
                    # settimeout(3) - ставит ожидания 3 секунды , и если за это время никакие данные от клиента не прийдут , то выдает ошибку
                    # Отримання всіх даних
                    # client_socket.settimeout(1)
                    try:
                        client_data = recv_all(client_socket)
                    except TimeoutError:
                        print("Клиент не ответил вовремя. Пропускитть надо")
                        continue
                    enemy_data[0] = pickle.loads(client_data)
  
                
                    
                    # # если прошло 30 сек , и никто не походил , то меняем очередь
                    if check_time[0] >= 29:
                        check_time[0] = 0
                        if turn[0] == "server_turn":
                            turn[0] = "client_turn"
                        elif turn[0] == "client_turn":
                            turn[0] = "server_turn"


                    check_repeat[0] += 1

                    if row_list[0] != 100 and check_send_data_health[0] <= 9:
                        check_send_data_health[0] += 1
                    # если кто то уже выиграл , то остонавливаем цикл игры
                    # если в list_check_win[0] лежит пустота , то значит что еще никто не выиграл
                    if list_check_win[0] != None:
                        break
                else:
                    #Ставимо сервер у режим очікування підключень
                    server_socket.listen()
                    #приймаємо користувача який під'єднується до серверу
                    client_socket, adress = server_socket.accept()
                    check_connection[0] = True
                    print(123)
                    continue
            except Exception as error:
                print(f"Неизвестная ошибка: {error}")
                check_connection[0] = False
                continue
           
           
           
#створюємо зміну потока, для запуску серверу
server_thread = threading.Thread(target = start_server, daemon=True)