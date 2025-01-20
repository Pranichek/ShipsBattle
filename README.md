<h1>Ships Battle</h1>

---

<a name="articles"><h3>Table of contents</h3></a>

# Project Description  
[Project description](#headers)

# Information about our team 
[Information about our team](#team)

# Figma
[Figma](#figma)

# Our project structure  
[structure of project](#structure)

# Getting Started  
[Getting started](#getting_started)

# Modules Description  
[Modules description](#modules)

# Package Description  
-   [Package description](#package_description)
    - [client.py package modules](#client)
    - [server.py package modules](#server)
    - [class_ship.py modules](#class_ship)


# Problems when creating a project
[Problems during development](#prbl_project)

# Conclusion
[Conlusion](#conclusions)

---


<a name="headers"><h1>Project description</h1></a>
Основна мета цього проєкту - закріпити навички роботи з клієнтом, сервером та передача данних. 
Ships Battle - це гра морський бій для двох людей з можливістю підключитися віддалено або в одній мережі. 
За допомогою введення ip адреса та порту ви можете підключитися та грати спільно з іншим гравцем.
Щоб створити гру, потрібно:
 1. ip-адресу, яка приймає запрос від будь-якого користувача(0.0.0.0), або локальну адресу
 2. Ввести порт
 3. ввести пароль
 4. доєднатися до серверу
Щоб доєднатись до гри, потрібно:
 1. Ввести свій нікнейм 
 2. Публічну ip-адресу, яку ви можете дізнатись у свого провайдера
 3. Ввести порт
 4. ввести пароль
<details>
<summary> English version </summary>
The main goal of this project is to consolidate the skills of working with the client, server and data transfer.
Ships Battle is a naval battle game for two people with the ability to connect remotely or on the same network.
By entering the IP address and port, you can connect and play together with another player.
To create a game, you need:
 1. an ip address that accepts a request from any user (0.0.0.0), or a local address
 2. Enter the port
 3. enter the password
 4. join the server
To join the game, you need:
 1. Enter your nickname
 2. Public IP address, which you can find out from your provider
 3. Enter the port
 4. enter the password
</details>

[⬆️Table of contents](#articles) 

<a name="team"><h1>Information about our team</h1></a>
1. GitHub - [Vova](https://github.com/Pranichek)
2. GitHub - [David](https://github.com/Zixtherc)
3. GitHub - [Nazar](https://github.com/Nazickj2023)
4. GitHub - [Mykhailo](https://github.com/DeKlain4ik)
4. GitHub - [Lena](https://github.com/LenaFedchenko)
4. GitHub - [Kamilla](https://github.com/KamillaKrupina?tab=repositories)

[⬆️Table of contents](#articles) 


<a name="figma"><h1>Figma</h1></a>

[https://www.figma.com/design/A9pJOVv6brCiSAgOAxhizL/Untitled?node-id=722-2&t=zHQJ3nDrGuaLgYEX-0]



<a name="structure"><h1>Structure of project</h1></a>

[https://www.figma.com/board/db61SCQLwAnOtFgqTjsIGn/Untitled?node-id=0-1&p=f&t=63Vl5Ibc18dUVsOJ-0]

[⬆️Table of contents](#articles)


<a name="getting_started"><h1>Getting started</h1></a>
Нижче наведена інструкція, як встановити гру.

## Installing python
Це приклад того, як встановити python, якщо ви ніколи ним не користуєтесь
- Завантажте інсталятор Python
 - Перейдіть на офіційний [Python website](https://www.python.org)
 - Перейдіть до розділу "Завантаження". Веб-сайт автоматично визначає вашу операційну систему та відображає відповідну версію.
- Виберіть правильну версію
 - Для більшості користувачів рекомендується остання стабільна версія. Але якщо у вас немає останньої версії, спробуйте завантажити іншу.
- Завантажте інсталятор
 - Натисніть кнопку Завантажити Python. Ця кнопка буде у верхньому правому куті екрана.
- Налаштувати параметри встановлення
 - Поставте прапорець «Додати Python до PATH» у нижній частині вікна інсталятора. Цей крок є ключовим для запуску Python з командного рядка
 - Клацніть «Налаштувати інсталяцію», якщо ви хочете вибрати додаткові параметри, але налаштування за замовчуванням добре працюють для більшості користувачів.
- Встановити python
 - Нарешті ви можете натиснути кнопку «Встановити зараз» і дочекатися завершення встановлення.
- Перевірте інсталяцію
    - Після встановлення відкрийте термінал або командний рядок.
        <details>
        <summary> Operating system</summary>
        - On Windows: Press Win + R, type cmd, and press Enter.
        - On macOS/Linux: Open the Terminal application.
        </details>
    - Тип ```python --version``` or ```python3 --version``` та натисніть Enter.
- Якщо Python встановлено правильно, ви побачите встановлену версію

Якщо ви все ще не розумієте, як встановити Python, можете подивитися [тут](https://www.youtube.com/watch?v=YKSpANU8jPE)

[⬆️Table of contents](#articles)

## Installing this project
1. Клонуйте проект
 - Перейшов на головну сторінку проекту на github.
 - Натисніть зелену кнопку «Код», розташовану вгорі праворуч.
 - Виберіть параметр HTTPS і скопіюйте URL-адресу проекту.
2. Відкрийте проект у IDE
 - Запустіть бажану IDE (Vscode, PyCharm або іншу)
 - Відкрийте його та виберіть опцію «Відкрити папку», щоб перейти та відкрити каталог, де було клоновано проект.
 - Натисніть Control + J або просто створіть новий термінал і напишіть це:
    ```python
    git clone <repository_url>
    ```
3. Підготуйте проект до використання
 - Перейдіть до головної папки проекту
    ```python  
    cd ShipsBattle
    ```
4. Створіть віртуальне середовище

    Для macOS/Linux:

        python3 -m venv venv
    Для Windows:

        python -m venv venv
5. Активуйте віртуальне середовище

    На macOS/Linux:

        source venv\Scripts\activate
    На Windows:

        venv\Scripts\activate
6. Встановити модулі проекту
 - Коли віртуальне середовище стане активним, інсталюйте необхідні бібліотеки, виконавши:

        ```python 
        pip install -r requirements.txt 
        ```
7. Запуск програми
 - Щоб запустити музичний плеєр, використовуйте таку команду:

        ```python
        python main.py
        ```


[⬆️Table of contents](#articles)


<a name="modules"><h1>MODULES FOR PROGRAM</h1></a>

### MODULES FOR DOWNLOADING
* **pillow** - image handler/Робота зі створенням зображень з байт коду
* **pygame** - create a game and transform the image/бібліотека для програмування ігор на Python

### BASE MODULES PYTHON

* **socket** - making server and client connections
* **os** - searching absolute path


<a name="client"><h1>Client.py package modules</h1></a>

```python
    import socket, json, time, pickle
            from .classes import input_port, input_ip_adress, input_nick ,list_ships
            from .json_functions import write_json , list_users 
            import modules.server as server_module
            from .screens import list_grid
            import modules.shop as shop
            import modules.achievement as achievement
            from .classes.class_input_text import input_password
            from threading import Thread
            from .server import SERVER


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
            save_data_posistion_ships = [""]
            TARGET_COUNT = 0


            dict_save_information = {
                "player_nick": "",
                "player_points" : 0,
                "enemy_nick" : "",
                "enemy_points" : 0,
            }


            def send_matrix():
                list_check_need_send[0] = True
                data_player_shot.clear()  # Очищаем данные перед добавлением новых
                data_player_shot.append("enemy_matrix")
                for row in list_grid:  # Предполагается, что list_grid соответствует enemy_matrix
                    for cell in row:
                        data_player_shot.append(str(cell))
                for ship in list_ships:
                    data_player_shot.append(str(ship.X_COR))
                    data_player_shot.append(str(ship.Y_COR))
                    data_player_shot.append(str(ship.LENGHT))
                    data_player_shot.append(str(ship.ORIENTATION_SHIP))

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
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                    # try:
                    port_client = int(input_port.user_text)
                    client_socket.connect((str(input_ip_adress.user_text), port_client))  # Подключение к серверу
                    print("Клиент подключён к серверу.")
                    # Получение сообщения от сервера (роль клиента)
                    role = client_socket.recv(1024).decode("utf-8")
                    server_module.list_player_role[0] = role
                    # Бесконечный цикл для отправки и получения данных
                    while True:
                        try:
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
                                except:
                                    raise Exception("Reconnect")
                                print(data_enemy)
                                data = data_enemy.split(" ")
                                check_connection_users[0] = save_data_posistion_ships[0]
                                if len(data) > 4:
                                    check_can_connect_to_fight[2] = data[4]
                                    if data[1] not in list_users:
                                        list_users[data[1]] = {"points": data[3], "password": data[2]}
                                        write_json(filename = "data_base.json" , object_dict = list_users)
                                    #якщо його нікнейм вже є , тоді просто оновлюємо його кількість баллів 
                                    elif data[1] in list_users:
                                        list_users[data[1]]["points"] = data[3]
                                        write_json(filename = "data_base.json" , object_dict = list_users)

                                    if save_data_posistion_ships[0] == "fight" and data[0] == 'fight':
                                        check_can_connect_to_fight[0] = True

                                    dict_save_information["player_nick"] = input_nick.user_text
                                    dict_save_information["enemy_nick"] = data[1]
                                    dict_save_information["player_points"] = int(list_users[input_nick.user_text]["points"])
                                    dict_save_information["enemy_points"] = int(list_users[data[1]]["points"])
                                else:
                                    print("Index error")
                            else:
                                time.sleep(0.5)
                                check_two_times.append(3)
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
                        except Exception as e:
                            port_client += 1
                            while True:
                                try:
                                    try:
                                        client_socket.close()
                                    except:
                                        pass
                                    print(2)
                                    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                    print(3)
                                    print(port_client)
                                    client_socket.connect((str(input_ip_adress.user_text), port_client)) 
                                    print(5)
                                    break
                                except:
                                    time.sleep(1)
                                    continue
                            
                connect_to_game = Thread(target = start_client, daemon = True)
                # #створюємо зміну потока, для запуску серверу
    # server_thread = threading.Thread(target = start_server, daemon=True)
    def listen_client(client, second_client):
        while True:
            try:
                if SERVER.clients >= 1:
                    client.settimeout(5)
                data = client.recv(1024)
                if data:
                    second_client.sendall(data)
            except ConnectionResetError:
                SERVER.RESTART = True
                SERVER.clients = 0
                SERVER.server_socket.close()
                client.close()
                second_client.close()
                break
            except Exception as error:
                SERVER.RESTART = True
                SERVER.clients = 0
                SERVER.server_socket.close()
                client.close()
                second_client.close()
                break

    players = ["server_player", "client_player"]
    class Server():
        def __init__(self):
            self.RESTART = False
            self.START_CONNECT = False
            self.clients = 0
            self.PORT = 0
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        def start_server(self, ip_adress: str, port: int):
            self.PORT = int(port) 
            while True:
                try:
                    if not self.RESTART:
                        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        self.server_socket.bind((str(ip_adress), self.PORT))
                        copy_list_player = players.copy()
                        player_one = random.choice(copy_list_player)
                        copy_list_player.remove(player_one)
                        player_two = copy_list_player[0]
                        print(f"Room ip_adress {colorama.Fore.GREEN} {ip_adress} {colorama.Style.RESET_ALL}")
                        print(f"Room Port:{colorama.Fore.GREEN} {self.PORT} {colorama.Style.RESET_ALL}")
                        print(self.PORT)
                        self.server_socket.listen()
                        self.START_CONNECT = True
                        client_socket, addr = self.server_socket.accept()
                        client_socket.sendall(player_one.encode("utf-8"))
                        print("First player is connected")
                        client_socket_second, addr_second = self.server_socket.accept()
                        client_socket_second.sendall(player_two.encode("utf-8"))
                        print("Second player is connecter")
                        self.RESTART = False

                        print(client_socket , client_socket_second)

                        thread1 = Thread(target = listen_client, args = (client_socket, client_socket_second))
                        thread1.start()
                        self.clients += 1

                        thread2 = Thread(target = listen_client, args = (client_socket_second, client_socket))
                        thread2.start()
                        self.clients += 1

                        thread1.join()
                        thread2.join()
                        print("Congratulations")
                        self.PORT += 1
                    if self.RESTART:
                        self.server_socket.close()
                        self.RESTART = False
                        continue
                except Exception as error:
                    pass

    SERVER = Server()

    def run_server(input_ip_address, input_port):
        SERVER.start_server(input_ip_address, input_port)
```
[⬆️Table of contents](#articles)

<a name="server"><h1>Server.py package modules</h1></a>

```python
    import socket 
    import colorama
    import random
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

    enemy_data = [""]
    #где стоят корабли соперника
    enemy_ships = []
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
    # #створюємо зміну потока, для запуску серверу
    # server_thread = threading.Thread(target = start_server, daemon=True)
    def listen_client(client, second_client):
        while True:
            try:
                if SERVER.clients >= 1:
                    client.settimeout(5)
                data = client.recv(1024)
                if data:
                    second_client.sendall(data)
            except ConnectionResetError:
                SERVER.RESTART = True
                SERVER.clients = 0
                SERVER.server_socket.close()
                client.close()
                second_client.close()
                break
            except Exception as error:
                SERVER.RESTART = True
                SERVER.clients = 0
                SERVER.server_socket.close()
                client.close()
                second_client.close()
                break

    players = ["server_player", "client_player"]
    class Server():
        def __init__(self):
            self.RESTART = False
            self.START_CONNECT = False
            self.clients = 0
            self.PORT = 0
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        def start_server(self, ip_adress: str, port: int):
            self.PORT = int(port) 
            while True:
                try:
                    if not self.RESTART:
                        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        self.server_socket.bind((str(ip_adress), self.PORT))
                        copy_list_player = players.copy()
                        player_one = random.choice(copy_list_player)
                        copy_list_player.remove(player_one)
                        player_two = copy_list_player[0]
                        print(f"Room ip_adress {colorama.Fore.GREEN} {ip_adress} {colorama.Style.RESET_ALL}")
                        print(f"Room Port:{colorama.Fore.GREEN} {self.PORT} {colorama.Style.RESET_ALL}")
                        print(self.PORT)
                        self.server_socket.listen()
                        self.START_CONNECT = True
                        client_socket, addr = self.server_socket.accept()
                        client_socket.sendall(player_one.encode("utf-8"))
                        print("First player is connected")
                        client_socket_second, addr_second = self.server_socket.accept()
                        client_socket_second.sendall(player_two.encode("utf-8"))
                        print("Second player is connecter")
                        self.RESTART = False

                        print(client_socket , client_socket_second)

                        thread1 = Thread(target = listen_client, args = (client_socket, client_socket_second))
                        thread1.start()
                        self.clients += 1

                        thread2 = Thread(target = listen_client, args = (client_socket_second, client_socket))
                        thread2.start()
                        self.clients += 1

                        thread1.join()
                        thread2.join()
                        print("Congratulations")
                        self.PORT += 1
                    if self.RESTART:
                        self.server_socket.close()
                        self.RESTART = False
                        continue
                except Exception as error:
                    pass

    SERVER = Server()

    def run_server(input_ip_address, input_port):
        SERVER.start_server(input_ip_address, input_port)
```
[⬆️Table of contents](#articles)

<a name="class_ship"><h1>Class_ship.py modules</h1></a>

```python
    r'''
            У модулі створено клас ``Ship``, який відмальовує кораблі, відповідає за розтавлення, "прилипання" 
            однопалубних, двопалубних, трьохбалубних та чотирьохпалубних кораблів .
        '''
        import pygame
        from os.path import abspath, join
        from ..screens import grid_player , list_grid , list_object_map 

        # Лист для проверки когда накладываем корабль на корабль
        check_for_shipsmoving = [0]

        class Ship:
            def __init__(self, x_cor: int, y_cor: int, width: int, height: int, image_ship: str, image_rotate_ship: str , length: int, position_ship: str):
                r'''
                :mod:`метод` ``__init__``, яка створює об'єкти класів, встановлює координати, розмір, позицію кораблів.

                Приклад застосування: 
                >>> self.X_COR, self.Y_COR = grid_player.snap_to_grid(self.X_COR, self.Y_COR) 
                '''
                self.X_COR = x_cor#место где будет стоять корабыль по иксу
                self.Y_COR = y_cor#место где будет стоять корабль по игреку
                self.WIDTH = width#ширина корабля
                self.HEIGHT = height#высота корабля
                self.IMAGE_SHIP = image_ship#картинка обычного корабля
                self.ROTATE_SHIP = image_rotate_ship#картинка повернутого корабля
                self.LENGHT = length#длина корабля в клеточках
                self.ORIENTATION_SHIP = position_ship#горизонтально или вертикально сейчас стоит корабль
                self.CHEK_ROTATION = self.ORIENTATION_SHIP#для проверки оризонтально или вертикально сейчас стоит корабль
                self.READY_IMAGE_SHIP = None#отмаштобированная и готовая кратинка норамльного корабля
                self.IMAGE_ROTATE_SHIP = None#отмаштобированная и готовая кратинка повернутого корабля
                self.load_image()#вызываем метод загрузки картинки
                self.CHECK_MOVE = None # Флаг для проверки движений мыши
                self.RECT = self.READY_IMAGE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))#прямоугольник для того чтобы могли отслеживать курсор ли на кораблике или нет
                self.STASIC_X = self.X_COR # Static_x = это начальные координаты
                self.STASIC_Y = self.Y_COR # Static_y = это начальные координаты
                # это свйоство где хранится новая клетка где стоит корабль 
                self.number_cell = 0
                # это свойство где хранится стараяя клетка где стоял корабль
                self.number_ship_cell = 0
                # номер рядка в матрице где он стоит
                self.row = 0
                # номер клетки где он стоит
                self.col = 0
                # флаг для проверки столкновения с кораблями(коллизиями)
                self.check_collision = None
                self.check_after_random = None
            
            # Метод загрузки картинок кораблей
            def load_image(self):
                r'''
                :mod:`Метод` ``load_image``, яка завантажує зображення з абсолютним шляхом та перевіряє як корабель розташован, вертикально чи горизонтально.

                Приклад застосування: 
                >>> enemy_face.load_image()
                '''
                # Переменная с абсолютным путём, до папки картинок кораблей ( абсолютный путь строится через модуль os.path.abspath()
                #"/../../../media/ships/{self.IMAGE_SHIP}"
                ship = abspath(join(__file__,"..", "..", "..", "media", "ships", f"{self.IMAGE_SHIP}"))
                # Переменная с абсолютным путём, до папки перевёрнутых кораблей 
                #"/../../../media/ships/{self.ROTATE_SHIP}"
                rotate_ship = abspath(join(__file__, "..", "..", "..", "media", "ships", f"{self.ROTATE_SHIP}"))
                # Загружаем картинку при помощи метода load
                image_ship = pygame.image.load(ship)
                # Загружаем картинку повернутого корабля при
                image_rotate_ship = pygame.image.load(rotate_ship)
                
                # Размер корабля зависит от ориентации
                if self.ORIENTATION_SHIP == "horizontal":
                    size_ship = (self.WIDTH * self.LENGHT, self.HEIGHT)
                    # self.RECT = self.READY_IMAGE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
                elif self.ORIENTATION_SHIP == "vertical":
                    size_ship = (self.WIDTH, self.HEIGHT * self.LENGHT)
                    # self.RECT = self.IMAGE_ROTATE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
                self.READY_IMAGE_SHIP = pygame.transform.scale(image_ship, size_ship)
                self.IMAGE_ROTATE_SHIP = pygame.transform.scale(image_rotate_ship, size_ship)
            
            # Создаём метод "прилепания" корабля к сетке 
            def snap_to_grid(self): 
                r'''
                :mod:`Метод` ``snap_to_grid``, за допомогою коорднинат прив'язуємо корабель дло сітки.
                Приклад застосування: 
                >>> snapped_x, snapped_y = grid.snap_to_grid(mouse_x, mouse_y)
                '''       
                # Привязываем координаты к сетке, это что бы корабль не уходил на саму сетку
                self.X_COR, self.Y_COR = grid_player.snap_to_grid(self.X_COR, self.Y_COR) 
            def center_to_cell_number(self, x, y):
                r'''
                :mod:`Метод` ``center_to_cell_number``, яка розраховує індекс клітинки: Номер клітки = (строка * кількість стовбців) + (стовбець) + 1.
                Приклад застосування: 
                >>>  self.number_ship_cell = self.center_to_cell_number(x = self.X_COR,y = self.Y_COR)
                '''        
                #Рассчитываем индекс столбца и строки, в которые попадает корабль.
                # grid_player.X_SCREEN - координаты сетки по иксу
                # grid_player.Y_SCREEN - координаты сетки по игреку
                # x - координаты кораблы по иску
                # y - координаты корабля по игреку
                col = (x - grid_player.X_SCREEN) // 62  # Индекс столбца 
                row = (y - grid_player.Y_SCREEN) // 62  # Индекс строки 

                # Учитываем, что клетки нумеруются с 1, поэтому:
                # Номер клетки = (строка * количество столбцов) + (столбец) + 1.
                cell_number = row * 10 + col + 1

                # Возвращаем номер клетки
                return cell_number


            # Cоздаём метод отрисовки корабля, параметр screen - там где он у нас будет отрисовываться 
            def draw_sheep(self, screen: pygame.Surface):
                r'''
                :mod:`Метод` ``draw_sheep``, який перевіряє як розташован корабель,а потім його відмальовує.
                Приклад застосування: 
                >>>  list_ships[num].draw_sheep(screen = module_screen.main_screen)
                '''  
                # Отрисовываем корабль на экране, зависит от ориентации
                if self.ORIENTATION_SHIP == "horizontal":
                    screen.blit(self.READY_IMAGE_SHIP, (self.X_COR, self.Y_COR))
                # Отрисовываем корабль на экране, зависит от ориентации
                elif self.ORIENTATION_SHIP == "vertical":
                    screen.blit(self.IMAGE_ROTATE_SHIP, (self.X_COR, self.Y_COR))
            # Создаём метод разворота корабля 
            def rotate_ship(self, event: pygame.event):
                r'''
                :mod:`Метод` ``rotate_ship``, повертає корабель горизонтально чи вертикально, натиснувши клавішу R  корабель повертається.
                Приклад застосування: 
                >>>  self.RECT = self.IMAGE_ROTATE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
                '''  
                self.RECT.topleft = (self.X_COR, self.Y_COR)
                # Создаём переменную мышки, и получаем координаты мышки игрока
                mouse = pygame.mouse.get_pos()
                # Если координаты мышки равняются координатам корабля
                if self.RECT.collidepoint(mouse):
                    # И если клавиша отпущена 
                    if event.type == pygame.KEYDOWN:
                        # И если клавиша R нажата
                        if event.key == pygame.K_r and self.CHECK_MOVE == True: 
                            # Если ориентация корабля horizontal
                            if self.CHEK_ROTATION == "horizontal":
                                self.ORIENTATION_SHIP = "vertical"
                                self.CHEK_ROTATION = self.ORIENTATION_SHIP
                                self.load_image()
                                self.RECT = self.IMAGE_ROTATE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
            
                                # Обновляем прямоугольник только при движении
                            
                            elif self.CHEK_ROTATION == "vertical":
                                self.ORIENTATION_SHIP = "horizontal"
                                self.CHEK_ROTATION = self.ORIENTATION_SHIP
                                self.load_image()
                                self.RECT = self.READY_IMAGE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
                                
                                
                            self.X_COR = mouse[0] - self.RECT.width // 2
                            self.Y_COR = mouse[1] - self.RECT.height // 2

                            
                            

            # метод який чистить положення корабля на матриці якщо його передвинули
            def clear_matrix(self):
                r'''
                :mod:`Метод` ``clear_matrix``, який очищає попереденє розтавлення корабля.
                Приклад застосування: 
                >>>  self.clear_matrix()
                '''  
                # список для перевірки розтавленння кораблів
                if check_for_shipsmoving[0] == 0:
                    # список для перевірки попереднього розтавлення кораблів
                    check_prev_pos = 0

                    for index_col in range(0 , 2):
                        # Добалвяем к ячейке 
                        try:
                            # print(list_grid[self.row][self.col + index_col])
                            if list_grid[self.row][self.col + index_col] == 0:
                                check_prev_pos += 1
                        except Exception as e:
                            check_prev_pos = 1


                    if self.check_collision != True:
                        # перевірка чи очищений список
                        if check_prev_pos == 0:
                            print("clear col")
                            if list_grid[self.row][self.col] == 0:
                                print("already clear")
                            else:
                                for index_col in range(0 , self.LENGHT):
                                    list_grid[self.row][self.col + index_col] = 0
                                    # return False
                        # якщо список не очищенно, то очищаємо його
                        elif check_prev_pos > 0:
                            print("cler row")
                            if list_grid[self.row][self.col] == 0:
                                print("already clear")
                            else:
                                print(self.row , self.col)
                                print(list_grid[self.row][self.col])
                                for index_row in range(0 , self.LENGHT):
                                    print(self.LENGHT , "length")
                                    print(list_grid[self.row + index_row][self.col])
                                    list_grid[self.row + index_row][self.col] = 0
                                    # return False
                    elif self.check_collision == True:
                        print("banana")
                        if self.ORIENTATION_SHIP == "vertical":
                            print("clean row")
                            if list_grid[self.row][self.col] == 0:
                                print("already clear")
                            else:
                                for index_row in range(0 , self.LENGHT):
                                    list_grid[self.row + index_row][self.col] = 0
                                    # return False
                        elif self.ORIENTATION_SHIP == "horizontal":
                            print("clean col")
                            if list_grid[self.row][self.col] == 0:
                                print("already clear")
                            else:
                                for index_col in range(0 , self.LENGHT):
                                    list_grid[self.row][self.col + index_col] = 0
                                    # return False
                check_for_shipsmoving[0] = 0
            

            # метод который телепортирует коарбль на начальную точку  и поворачивает в положение по горизонатали
            def return_start_code(self):
                r'''
                :mod:`Метод` ``return_start_code``, для повернення корабля на початкому точку, якщо корабель не відповідає потрібним координатам ,та повертає корабель в горизонтальнеп положення.
                >>>  self.return_start_code()
                '''  
                self.X_COR, self.Y_COR = self.STASIC_X, self.STASIC_Y
                self.RECT = self.IMAGE_ROTATE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
                self.ORIENTATION_SHIP = "horizontal"
                # Записываем в переменную для проверки
                self.CHEK_ROTATION = self.ORIENTATION_SHIP
                # Отрисовываем изображение при помощи метода
                self.load_image()
                # Записываем в переменную изменённую позицию
                self.RECT = self.READY_IMAGE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
                    
            

            def matrix_move(self, event: pygame.event, matrix_width: int, matrix_height: int, cell: int):
                r'''
                :mod:`Метод` ``matrix_move``, перевіряє, щоб кораблі не накладалися один на одний та щоб кораблі були щонайменше на одну клітинку один від одного.
                >>>  ship.matrix_move(event = event, matrix_width = 620, matrix_height = 620, cell = 100)
                '''
                # Получаем текущие координаты мыши
                mouse = pygame.mouse.get_pos() 

                if event.type == pygame.MOUSEBUTTONDOWN and self.RECT.collidepoint(event.pos):
                    # Начало перемещения
                    self.CHECK_MOVE = True

                # Если мы двигаем курсором по экрану , и уже нажимали на корабль
                elif event.type == pygame.MOUSEMOTION and self.CHECK_MOVE:

                    self.X_COR = mouse[0] - self.RECT.width // 2
                    self.Y_COR = mouse[1] - self.RECT.height // 2


                    # Ограничиваем движение корабля границами матрицы
                    self.X_COR = max(0, min(self.X_COR, matrix_width * cell - self.RECT.width))
                    self.Y_COR = max(0, min(self.Y_COR, matrix_height * cell - self.RECT.height))
                    # Обновляем прямоугольник только при движении
                    self.RECT.topleft = (self.X_COR, self.Y_COR)

                elif event.type == pygame.MOUSEBUTTONUP and self.CHECK_MOVE:
                    self.CHECK_MOVE = False
                    print(self.WIDTH , "self_width")
                    print(self.RECT.width , "self_rect")

                    if self.check_after_random == True:
                        print("Зашло")
                        self.clear_matrix()
                        self.check_after_random = None
                        print(list_grid)

                    # Проверка пересечения с другими кораблями
                    # делаем перебор списка с кораблями , чтобы модно было проверять не пытается ли поставить пользователь корабль на корабль
                    for ship in list_ships:
                        # Проверяем ship != self - это для того чтобы не проверять кораблик сам с собой
                        # self.RECT.colliderect(ship.RECT) - проверям каждый корабль из списка с текущим кораблем, если ихние прямоугольники(колизии) пересекаются то ставим кораблик на начальные координаты
                        if ship != self and self.RECT.colliderect(ship.RECT):
                            print("пересекается")
                            self.return_start_code()
                            # self.number_cell = self.number_ship_cell
                            # # Переделываем значение клетки в строку чтобы можно было лекго узнать в калоночке он стоит
                            # str_col = str(self.number_cell) 
                            # # Вычисляем номер рядка где стоит корабль(например 23 , делим на 10 без остатка и получаем 2 , вот нашь столбец)
                            # self.row = self.number_cell // 10  
                            if ship.col == self.col and ship.row == self.row:
                                check_for_shipsmoving[0] += 1
                            else:
                                check_for_shipsmoving[0] = 0
                            self.clear_matrix()
                            print(list_grid)
                            return False
        
                    if grid_player.X_SCREEN - 30 <= self.X_COR and self.X_COR + self.RECT.width <= grid_player.X_SCREEN + 650:
                        if grid_player.Y_SCREEN - 30 <= self.Y_COR and self.Y_COR + self.RECT.height <= grid_player.Y_SCREEN + 650:
                            self.snap_to_grid()

            
                            if self.number_ship_cell != self.number_cell and self.check_collision != True:
                                self.clear_matrix()

                            self.check_collision = None

                            # Пересчитываем номер клетки где стоит корабль для старых координат
                            self.number_ship_cell = self.center_to_cell_number(x = self.X_COR,y = self.Y_COR)


                            print(list_grid)
                            print("------------------------------------------------------------------------------------------------")
                            for cell in list_object_map: 
                                    if cell.x <= self.X_COR and self.X_COR < cell.x + 62:
                                        if cell.y <= self.Y_COR and self.Y_COR < cell.y + 62:
                                            # Узнаем номер клетки где стоит кораблик
                                            self.number_cell = list_object_map.index(cell)
                                            # Переделываем значение клетки в строку чтобы можно было лекго узнать в калоночке он стоит
                                            str_col = str(self.number_cell) 
                                            # Вычисляем номер рядка где стоит корабль(например 23 , делим на 10 без остатка и получаем 2 , вот нашь столбец)
                                            self.row = self.number_cell // 10  
                                            #Колонку кораблика вычисляем по такому принципу
                                            # Например опять 23 число номер колонки где стоит корабль , тогда с помощью -1 мы берем последнее число тоесть тройку, и вот так получаем номер колонки
                                            self.col = int(str_col[-1])

                                            # Устанавливаем значение где стоит корабль в матрице
                                            if self.ORIENTATION_SHIP == "horizontal":
                                                for index_column in range(0 , self.LENGHT):
                                                    list_grid[self.row][self.col + index_column] = self.LENGHT
                                            elif self.ORIENTATION_SHIP == "vertical":
                                                for index_row in range(0 , self.LENGHT):
                                                    list_grid[self.row + index_row][self.col] = self.LENGHT
                            
                            
                            for shiper in list_ships:
                                # проверка чтобы корабль который двигаем не сравнивали с самим собой
                                if list_ships.index(shiper) != list_ships.index(self):
                                    if shiper.ORIENTATION_SHIP == "horizontal":
                                        if self.X_COR >= shiper.X_COR - 62:
                                            if self.X_COR < shiper.X_COR + shiper.RECT.width + 62:
                                                if self.Y_COR >= shiper.Y_COR - 62:
                                                    if self.Y_COR < shiper.Y_COR + 124:
                                                        self.X_COR = self.STASIC_X
                                                        self.Y_COR = self.STASIC_Y
                                                        print(self.row , self.col)
                                                        self.check_collision = True
                                                        self.clear_matrix()
                                                        self.return_start_code()
                                                        break
                                                
                                        
                                        if self.X_COR + self.RECT.width > shiper.X_COR - 62:
                                            if self.X_COR + self.RECT.width <= shiper.X_COR + shiper.RECT.width + 62:
                                                    if self.ORIENTATION_SHIP == "horizontal":
                                                        if self.Y_COR >= shiper.Y_COR - 62:
                                                            if self.Y_COR < shiper.Y_COR + 124:
                                                                    
                                                                    self.X_COR = self.STASIC_X
                                                                    self.Y_COR = self.STASIC_Y
                                                                    print(self.row , self.col)
                                                                    self.check_collision = True
                                                                    self.clear_matrix()
                                                                    self.return_start_code()
                                                                    break
                                                        
                                                    elif self.ORIENTATION_SHIP == "vertical":
                                                        if self.Y_COR + self.RECT.height > shiper.Y_COR - 62:
                                                            if self.Y_COR + self.RECT.height <= shiper.Y_COR + 124:
                                                                    print("HAAHAHAHAHHAHA")
                                                                    self.X_COR = self.STASIC_X
                                                                    self.Y_COR = self.STASIC_Y
                                                                    print(self.row , self.col)
                                                                    self.check_collision = True
                                                                    self.clear_matrix()
                                                                    self.return_start_code()
                                                                    break
                                                            

                                    elif shiper.ORIENTATION_SHIP == "vertical":
                                        if self.X_COR >= shiper.X_COR - 62:
                                            if self.X_COR < shiper.X_COR + shiper.RECT.width + 62:
                                                if self.Y_COR >= shiper.Y_COR - 62:
                                                    if self.Y_COR < shiper.Y_COR + shiper.RECT.height + 62:
                                                            self.X_COR = self.STASIC_X
                                                            self.Y_COR = self.STASIC_Y
                                                            print(self.row , self.col)
                                                            self.check_collision = True
                                                            self.clear_matrix()
                                                            self.return_start_code()
                                                            break
                                                    

                                        if self.X_COR + self.RECT.width > shiper.X_COR - 62:
                                            if self.X_COR + self.RECT.width <= shiper.X_COR + shiper.RECT.width + 62:
                                                    if self.Y_COR + self.RECT.height > shiper.Y_COR - 62:
                                                        if self.Y_COR + self.RECT.height <= shiper.Y_COR + shiper.RECT.height + 62:
                                                                self.X_COR = self.STASIC_X
                                                                self.Y_COR = self.STASIC_Y
                                                                print(self.row , self.col)
                                                                self.check_collision = True
                                                                self.clear_matrix()
                                                                self.return_start_code()
                                                                break
                                
                    
                            print("------------------------------------------------------------------------------------------------")
                            print(list_grid)
                        else:
                            self.clear_matrix()
                            self.return_start_code()
                            print(list_grid)
            
                    else:
                        self.clear_matrix()
                        self.return_start_code()
                        print(list_grid)
                        
        
                    # Обновляем прямоугольник в конце
                    self.RECT.topleft = (self.X_COR, self.Y_COR)
            


        # Тут мы создаём сами корабли, цифры в словах, типа: three, two, one , это деления корабля, на сколько клеточек он задуман
        # Чотирипалубний корабель
        ship_four = Ship(
            x_cor = 882,  # x кордината для чотирипалубного корабля
            y_cor = 475,   # y кордината для першого ряду
            width = 62,
            height = 62,
            image_ship = "ship_four.png", 
            image_rotate_ship = "rotate_ship_four.png", 
            length = 4, 
            position_ship = "horizontal"
        )

        # Тріпалубні кораблі (перший ряд)
        ship_three = Ship(
            x_cor = 773, 
            y_cor = 350,  # y кордината для другого ряду
            width = 62,
            height = 62,
            image_ship = "ship_three.png", 
            image_rotate_ship = "rotate_ship_three.png", 
            length = 3, 
            position_ship = "horizontal"
        )

        # Тріпалубні кораблі (другий ряд)
        ship_three2 = Ship(
            x_cor = 1038,  # зміщення по x
            y_cor = 350,
            width = 62,
            height = 62,
            image_ship = "ship_three.png", 
            image_rotate_ship = "rotate_ship_three.png", 
            length = 3, 
            position_ship = "horizontal"
        )

        # Двопалубні кораблі (перший ряд)
        ship_two = Ship(
            x_cor = 783, 
            y_cor = 215,  # y кордината для третього ряду
            width = 62,
            height = 62,
            image_ship = "ship_two.png", 
            image_rotate_ship = "rotate_ship_two.png", 
            length = 2, 
            position_ship = "horizontal"
        )

        # Двопалубні кораблі (другий ряд)
        ship_two2 = Ship(
            x_cor = 933,  # зміщення по x
            y_cor = 215,
            width = 62,
            height = 62,
            image_ship = "ship_two.png", 
            image_rotate_ship = "rotate_ship_two.png", 
            length = 2, 
            position_ship = "horizontal"
        )

        # Двопалубні кораблі (третій ряд)
        ship_two3 = Ship(
            x_cor = 1082,  # зміщення по x
            y_cor = 215,
            width = 62,
            height = 62,
            image_ship = "ship_two.png", 
            image_rotate_ship = "rotate_ship_two.png", 
            length = 2, 
            position_ship = "horizontal"
        )

        # Однопалубні кораблі (перший ряд)
        ship_one = Ship(
            x_cor = 814, 
            y_cor = 80,  # y кордината для четвертого ряду
            width = 62,
            height = 62,
            image_ship = "ship_one.png", 
            image_rotate_ship = "rotate_ship_one.png", 
            length = 1, 
            position_ship = "horizontal"
        )

        # Однопалубні кораблі (другий ряд)
        ship_one2 = Ship(
            x_cor = 918,  # зміщення по x
            y_cor = 80,
            width = 62,
            height = 62,
            image_ship = "ship_one.png", 
            image_rotate_ship = "rotate_ship_one.png", 
            length = 1, 
            position_ship = "horizontal"
        )

        # Однопалубні кораблі (третій ряд)
        ship_one3 = Ship(
            x_cor = 1022,  # зміщення по x
            y_cor = 80,
            width = 62,
            height = 62,
            image_ship = "ship_one.png", 
            image_rotate_ship = "rotate_ship_one.png", 
            length = 1, 
            position_ship = "horizontal"
        )

        # Однопалубні кораблі (четвертий ряд)
        ship_one4 = Ship(
            x_cor = 1126,  # зміщення по x
            y_cor = 80,
            width = 62,
            height = 62,
            image_ship = "ship_one.png", 
            image_rotate_ship = "rotate_ship_one.png", 
            length = 1, 
            position_ship = "horizontal"
        )







        # Создаём всех список кораблей
        list_ships = []

        # Добавляем В КОНЕЦ СПИСКА все корабли
        list_ships.append(ship_four)
        list_ships.extend([ship_three , ship_three2])
        list_ships.extend([ship_two , ship_two2 , ship_two3])
        list_ships.extend([ship_one , ship_one2 , ship_one3, ship_one4])    
```
[⬆️Table of contents](#articles)

<a name="prbl_project"><h2>Problems during development</h2></a>
Під час написання коду, ми зіштовхнулись з деякими труднощами. Наприклад ми не можемо ще раз запускати сервер, якщо його вже запустили, на жаль цю проблему ми не змогли вирішити, але це в перспективі. Однією з наших проблем стало розташування кораблів, складно було зробити так, щоб не можна було ставити корабель один на інший, також треба було зробити так, щоб користувач міг ставити корабель лише через одну клітинку, як зазначено в правилах гри. Наразі цю проблему вирішено. 
Найголовнішою проблемою було працювання з клієнтом та сервером, з самого початку ми мали іншу структуру коду, через що, згодом ми мали баг з перепідключенням клієнта та сервера, а також з обміном данних. Також через те, що ми відправляли усю матрицю одразу, були постійні перепідключення, що заважало грі, наразі ми змінили структуру, тепер інформація відправляється через список відразу та частково. Однією з проблем стало те, що не вся гра написана через класи, замість них ми маємо функції(наші вікна). 
Під час напсиання коду, ми мали погану структуру коду, тому ми її змінили, розподілили файли по фреймам.
<details>
<summary>English version</summary>
While writing the code, we encountered some difficulties. For example, we cannot restart the server if it has already been started, unfortunately we could not solve this problem, but it is in the future. One of our problems was the location of the ships, it was difficult to make it so that it was not possible to place a ship on top of another, it was also necessary to make it so that the user could place a ship only through one cell, as stated in the game rules. Currently, this problem has been solved.
The most important problem was working with the client and server, from the very beginning we had a different code structure, because of which, later we had a bug with the client and server reconnecting, as well as with data exchange. Also, because we sent the entire matrix at once, there were constant reconnections, which interfered with the game, now we have changed the structure, now the information is sent through the list immediately and partially. One of the problems was that not the entire game is written through classes, instead we have functions (our windows).
When writing the code, we had a bad code structure, so we changed it and distributed the files across frames.
</details>


<a name="conclusions"><h2>Conclusion</h2></a>
Під час реалізації проєкту ми отримали цінний досвід роботи в команді. Нам вдалося покращити свою дисципліну, організовуючи зустрічі для обговорення проблем та розподілу завдань. Ми вдосконалили навички роботи з модулем pygame, а першокурсники вперше ознайомилися з ним. Дійшли висновку, що це не найпростіший рушій для Python.
Також першокурсники ознайомилися з матрицями, а старшокурсники поглибили свої знання в цій темі. Ми успішно освоїли роботу з Figma, зокрема створення анімацій та їх використання у грі. Навчилися правильно структурувати файли в проєкті й створювати віртуальне середовище.
Ми розібралися в основах обміну даними між користувачами за допомогою IP-адрес та портів. Навчилися вирішувати проблеми, пов'язані з цим процесом, а також отримали знання про інтернет-протоколи IPv4 та IPv6. Вивчили їх основні характеристики: кількість символів, систему адресації (32-бітна для IPv4 та 128-бітна для IPv6) та цілі застосування.
За допомогою транспортного протоколу TCP ми змогли забезпечити безпечний обмін даними завдяки шифруванню. Освоїли роботу з бібліотекою socket для створення та підключення між клієнтом і сервером. Під час тестування гри, зіштовхнулися з проблемами та навчились вирішувати їх(зокрема проблеми зі з'єднанням). Зробили висновки, що завдяки бібліотеки socket маємо можливість підключитись до пристрою іншного користувача, без його відома. 
<details>
<summary>English version</summary>
During the project implementation, we gained valuable experience working in a team. We managed to improve our discipline by organizing meetings to discuss problems and distribute tasks. We improved our skills in working with the pygame module, and the freshmen got acquainted with it for the first time. We came to the conclusion that it is not the easiest engine for Python.
The freshmen also got acquainted with matrices, and the seniors deepened their knowledge in this topic. We successfully mastered working with Figma, in particular, creating animations and using them in the game. We learned how to properly structure files in a project and create a virtual environment.
We understood the basics of data exchange between users using IP addresses and ports. We learned to solve problems related to this process, and also gained knowledge about the Internet protocols IPv4 and IPv6. We studied their main characteristics: the number of characters, the addressing system (32-bit for IPv4 and 128-bit for IPv6), and the purposes of application.
Using the TCP transport protocol, we were able to ensure secure data exchange through encryption. We mastered working with the socket library to create and connect between the client and the server. While testing the game, we encountered problems and learned how to solve them (including connection problems). We concluded that thanks to the socket library, we have the ability to connect to another user's device without their knowledge.
</details>
 
[⬆️Table of contents](#articles)
