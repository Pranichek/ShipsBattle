import socket ,threading , json , pygame , time
from .classes import input_port, input_ip_adress, input_nick , Animation
from .json_functions import write_json , list_users , list_server_status
from .json_functions.json_read import read_json
from .server import enemy_balance , list_check_ready_to_fight , dict_save_information, turn , check_time , list_player_role , enemy_matrix , check_repeat , list_check_win , enemy_animation_miss_coord , recv_all , save_miss_coordinates , our_miss_anim , save_medals_coordinates , player_died_ships , enemy_died_ships
from .screens import list_grid
import modules.shop as shop
import modules.achievement as achievement

list_check_need_send = ["no"]


pygame.init()


#список для відслуджування чи підключився користувач до серверу чи ні
list_check_connection = [False]

# список для отрисовки ачивки
# achiv_img = [False]


#ліст для перевірки чи зайшов користувач на сервер
list_server_status = {
    "status": None
}
#зберігаємо інформацію про статус серверу у json файл , поки цей статус пустий тому що не під'єднуємося до серверу
write_json(filename= "utility.json" , object_dict = list_server_status)


dict_status_game = {
    "status" : "places ships"
}
write_json(filename= "status_connect_game.json" , object_dict =  dict_status_game)


event_connect_to_server = threading.Event()
event_connect_to_server.set()


#створюємо функцію підключення користувача до серверу
def connect_user():
    #если игрок нажал запустить сервер и его еще нет в словаре игроков, то записываем его ник в джейсон
    if input_nick.user_text not in list_users:
        #создаем игрока с его ником и даем базовое количество баллов
        list_users[input_nick.user_text] = {"points": 0}
        #зберігаємо інформацію у json файл
        write_json(filename = "data_base.json" , object_dict = list_users)


    #берем из поля ввода данные для запуска сервера(айпи и порт)
    # ip_adress = input_ip_adress.user_text
    # port = int(input_port.user_text)
   
    # створюємо сокет з використанням протоколу IPv4 (AF_INET) та TCP (SOCK_STREAM)
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as client_socket:
        # підключаємо користувача до сервера за даними що ввів користувач
        # client_socket.connect((ip_address, port))
        # while list_server_status["status"] == None:
        try:
            if event_connect_to_server.is_set():
                ip_adress = input_ip_adress.user_text
                port = int(input_port.user_text)
                client_socket.settimeout(0.1)
                client_socket.connect((ip_adress, port))
                print("підключено до сервера")
                event_connect_to_server.clear()
                # break
        except (socket.timeout, OSError):
            print("server not found")
            list_check_connection[0] = "error_connection"  # Сбрасываем событие
            event_connect_to_server.clear()
            print(event_connect_to_server)
       
        print(ip_adress , "ip address")
        print(port , "port")


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


        list_player_role[0] = "player_client"
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
        dict_save_information["player_points"] = points_for_server
        dict_save_information["enemy_points"] = data_in_list["points"]

       # створюємо цикл для бою(щоб робити обмін даними , до потрібного моменту)
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

                # win game without losing a ship
                achievement.strategist(grid = list_grid , enemy_grid = enemy_matrix)


                # робимо зупинку на 0.1 секунду , що сервер і клієент встигали обмінюватися данними
                time.sleep(0.1)
                # settimeout(3) - говорить про те що , якщо за три секундни клієнт не отримав ніяких даних то тільки потім буде виводити помилку
                client_socket.settimeout(3)

                # Отримання всіх даних від серверу
                data_turn = recv_all(client_socket).decode()
                # перетворбємо дані від сереру у формат словарю(перед перетворенням це було json строкою)
                server_data = json.loads(data_turn)

                enemy_balance[0] = server_data["money_balance"]

                # какие корабли убил игрок
                for ship in server_data["plyer_died_ships"]:
                    if ship not in enemy_died_ships:
                        enemy_died_ships.append(ship)
                # для медалей
                for medal in server_data["medals_coordinates"]:
                    if medal not in save_medals_coordinates:
                        save_medals_coordinates.append(medal)

                # для зачерканных клеточек
                for coord_miss in server_data["misses_coordinate"]:
                    if coord_miss not in enemy_animation_miss_coord:
                        enemy_animation_miss_coord.append(coord_miss)
                
                # у список для відслідження скільки час на ход залишилось , записуємо дані про час від сервера(оскільки сервер контролює скільки прошло часу)
                check_time[0] = server_data['time']

                if turn[0] == "server_turn" and check_time[0] == 1 and server_data["check_ten_times"] == 1:
                    if shop.second_task.TEXT == shop.list_second_task[1]:
                        shop.kept_all_ships_alive_for_five_turns(grid = list_grid)

                if turn[0] == "server_turn" and check_time[0] == 1 and server_data["check_ten_times"] == 1:
                    print(133)
                    achievement.kept_all_ships_alive_for_ten_turns(grid = list_grid)

                # list_check_need_sen - список который хранит флаг , по которому мы понимаем атакавал клиент или нет
                if list_check_need_send[0] == "no":
                    # якщо не не атакував , то відправляємо дані , але ті які на ход ніяк не влияють(нам потрбіно завжди щось відправляти на севре , щоб не бцло помилки)
                    client_dict = {
                        "turn": "server_turn",
                        "time": 0 ,
                        "need" : "no",
                        'client_matrix':list_grid,
                        "new_for_server" : enemy_matrix[0],
                        "first_kill_3deck": shop.enemy_ships_3decker[0], 
                        "misses_coordinate": save_miss_coordinates,
                        "money_balance":shop.money_list[0],
                        "medals_coordinates":achievement.list_save_coords_achiv,
                        "plyer_died_ships":player_died_ships
                    }
                    client_socket.send(json.dumps(client_dict).encode())
                # якщо клієнт зробив постріл , то перевіряємо чи потрібо змінювати чергу , чи ні
                elif list_check_need_send[0] == "yes":
                    # print(1)
                    print(turn[0])
                    # якщо клієент зробив постріл , але схибив його , то змінюємо чергу за допмогою "turn": "server_turn"
                    if turn[0] == "server_turn":
                        print(2)
                        client_dict = {
                            "turn": "server_turn",
                            "time": 0 ,
                            "need" : "yes",
                            'client_matrix':list_grid,
                            "new_for_server" : enemy_matrix[0],
                            "first_kill_3deck": shop.enemy_ships_3decker[0],
                            "misses_coordinate": save_miss_coordinates,
                            "money_balance":shop.money_list[0],
                            "medals_coordinates":achievement.list_save_coords_achiv,
                            "plyer_died_ships":player_died_ships
                        }
                        # відправляємо дані , але перед цим словарь перетворюємо у строку за допомогою json.dumps
                        client_socket.send(json.dumps(client_dict).encode())
                        list_check_need_send[0] = "no"
                        check_time[0] = 0
                        continue
                    # якщо клієнт зробив постріл і потрапив по кораблю , то не змінюємо чергу , а просто обнуляємо час , оскільки клієнт потрпив
                    if turn[0] == "client_turn":
                        # print(3)
                        client_dict = {
                            "turn": "client_turn",
                            "time": 0 ,
                            "need" : "yes",
                            'client_matrix':list_grid,
                            "new_for_server" : enemy_matrix[0],
                            "first_kill_3deck": shop.enemy_ships_3decker[0],
                            "misses_coordinate": save_miss_coordinates,
                            "money_balance":shop.money_list[0],
                            "medals_coordinates":achievement.list_save_coords_achiv,
                            "plyer_died_ships":player_died_ships
                        }
                        client_socket.send(json.dumps(client_dict).encode())
                        list_check_need_send[0] = "no"
                        check_time[0] = 0
                        continue


                if check_repeat[0] == 0:
                    # сохраняем матрицу сервера
                    enemy_matrix[0] = server_data["server_matrix"]
                
                # записуємо у список збереження черги , із даних , що підправив сервер(оскільки він керує чия зараз черга)
                turn[0] = server_data['turn']


                # обновляем матрицу клиента , на матрицу с пострелами сервера
                if check_repeat[0] >= 1:
                    for row in range(len(server_data["new_for_client"])):
                        for cell in range(len(server_data["new_for_client"][row])):
                            list_grid[row][cell] = server_data["new_for_client"][row][cell]

                if shop.third_task.TEXT == shop.list_third_task[0]:
                    shop.first_kill_four_decker(grid = list_grid , enemy_grid = enemy_matrix)


                if shop.second_task.TEXT == shop.list_second_task[-1]:
                    if server_data["first_kill_3deck"] != "kill three-decker ship":
                        shop.first_kill_three_decker(grid = list_grid , enemy_grid = enemy_matrix)

                achievement.first_kill_four_decker_achivment(grid = list_grid , enemy_grid = enemy_matrix)
                achievement.opening_the_battle(grid = list_grid , enemy_grid = enemy_matrix)

                check_repeat[0] += 1

                # если кто то уже выиграл , то остонавливаем цикл игры
                # если в list_check_win[0] лежит пустота , то значит что еще никто не выиграл
                if server_data["check_end_game"] != None:
                    list_check_win[0] = server_data["check_end_game"]
                    print("end")
                    break

            except TimeoutError:
                print("Час очікування відповіді сервера вичерпано")
                continue
            except json.JSONDecodeError:
                print("Помилка декодування даних")
                if server_data["check_end_game"] != None:
                    break
                else:
                    continue
            except Exception as e:
                print(f"Несподівана помилка: {e}")
                continue




        #створюємо зміну потока, із функцією підключення коритсувача до серверу
thread_connect = threading.Thread(target = connect_user ,daemon=True)