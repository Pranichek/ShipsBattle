<h1>Ships Battle</h1>

---

<a name="articles"><h3>Table of contents</h3></a>

# Project Description  
[Project description](#headers)

# Information about our team 
[Information about our team](#team)

# Figma
[Figma](#figmaa)

# Our project structure  
[structure of project](#structure)

# Getting Started  
[Getting started](#getting_started)

# Modules Description  
[Modules description](#modules)

# Package Description  
-   [Package description](#package_description)
    - [describe achievment package](#achievment)
    - [describe classes package](#classes)
    - [describe game_tools package](#game_tools)
    - [describe game_windows package](#game_windows)
    - [describe json_functions package](#json_functions)
    - [describe screens package](#screens)
    - [describe shop package](#shop)
    - [describe volume_settings package](#volume_settings)

- [client.py package modules](#client)
- [server.py package modules](#server)
- [class_ship.py modules](#class_ship)


# Problems when creating a project
[Problems during development](#prbl_project)

# Conclusion
[Conlusion](#conclusions)

---


<a name="headers"><h1>Project description</h1></a>
Основна мета цього проєкту - закріпити навички роботи з клієнтом, сервером та обміном данних. 
Ships Battle - це гра морський бій для двох людей з можливістю підключитися віддалено або в одній мережі. 
За допомогою введення ip адреса та порту ви можете підключитися та грати спільно з іншим гравцем. Під час гри ви маєте можливість отримати монети за попадання по кораблям, а потім витратити їх на зброю з магазину, але якщо ви хочете заробити більше монет можна виконати завдання, які є в магазині, а також, якщо заробити медаль "Магнат", то кількість монет за попадання по кораблю буде більшою. 

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
The main goal of this project is to consolidate skills in working with the client, server and data exchange.
Ships Battle is a naval battle game for two people with the ability to connect remotely or on the same network.
By entering the IP address and port, you can connect and play together with another player. During the game, you have the opportunity to get coins for hitting ships, and then spend them on weapons from the store, but if you want to earn more coins, you can complete the tasks that are in the store, and also, if you earn the "Tycoon" medal, the number of coins for hitting the ship will be greater.

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
1. GitHub - [Vova - Developer](https://github.com/Pranichek)
2. GitHub - [David - Developer](https://github.com/Zixtherc)
3. GitHub - [Nazar - Developer](https://github.com/Nazickj2023)
4. GitHub - [Mykhailo - Developer](https://github.com/DeKlain4ik)
4. GitHub - [Lena - Developer, Designer](https://github.com/LenaFedchenko)
4. GitHub - [Kamilla - Developer, Designer](https://github.com/KamillaKrupina?tab=repositories)

[⬆️Table of contents](#articles) 


<a name="figmaa"><h1>Figma</h1></a>

[Link to Figma](https://www.figma.com/community/file/1463238329116517584)



<a name="structure"><h1>Structure of project</h1></a>

[Link to project structure](https://www.figma.com/board/SnEIS3t6Ro3rcaxTK6nRDq/Untitled?node-id=0-1&p=f&t=8ecpCJNVmgIVfyh5-0)

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

<a name="achievment"><h1>describe achievment package</h1></a>
У цій папці ми маємо файли, які відповідають за нагороди гравців, тут прораховуються усі можливі попадання по кораблям, наприклад, якщо гравець попав по кораблю за перший хід, то гравець отримує свою першу нагороду.
<details>
<summary>English version</summary>
In this folder we have files that are responsible for player rewards, all possible hits on ships are calculated here, for example, if a player hits a ship on the first turn, then the player receives his first reward.
</details>

[⬆️Table of contents](#articles)

<a name="classes"><h1>describe classes package</h1></a>
У даній папці ми маємо файли з класами, такими як, клас анімацій, клас кнопок, клас з відображенням малюнків, клас вводу тексту, клас нагород, два різні класи музики, один для фонової музики MusicPlayer, а інший для різних кліків Sound, а також клас кораблів, у якому ми створюємо та відмальовуємо кораблі. У кожному класі створюємо об'єкт класу, а потім використовуємо його.
<details>
<summary>English version</summary>
In this folder we have files with classes such as, animation class, button class, image display class, text input class, awards class, two different music classes, one for background music MusicPlayer and another for different Sound clicks, and also a ship class in which we create and draw ships. In each class we create an object of the class and then use it.
</details>

[⬆️Table of contents](#articles)

<a name="game_tools"><h1>describe game_tools package</h1></a>
У папці game_tools файли у яких ми перевіряємо вбиті кораблі ворога, зароблені монети, які гравець може витратити на зброю, ефект затемнення, який ми використовуємо для того, щоб екрани перемикалися плавно, а також файл, який відповідає за визначення меж знищеного корабля, додавання анімації промахів навколо знищеного корабля, а також за ведення обліку знищених кораблів.
<details>
<summary>English version</summary>
The game_tools folder has files that we check for crashed ships, coins that can be spent on armor, a darkening effect that we use to ensure that the screens switch smoothly, and also a file that Indicates the value between a disabled ship, adding animation of misses around a disabled ship, as well as the appearance of disabled ships.
</details>

[⬆️Table of contents](#articles)

<a name="game_windows"><h1>describe game_windows package</h1></a>
У папці game_windows ми маємо файли, які відповідають за натискання кнопки та зміну вікна, а також папки з різними вікнами гри, такими як головне вікно(вікно створення гри), вікно доєднання до гри, розтавлення кораблів, саме вікно бою, частину коду якого можна побачити нижче, та вікно результату гри.

Частина функції вікна бою
<details>
<summary>English version</summary>
In the game_windows folder we have files that indicate pressing the button and changing the window, as well as folders with different game windows, such as the head window, which is always added to the game, The deployment of ships depends on the battle itself, some of the code can be lowered, but the result will be affected.

Part of the functions in battle
</details>

```python
    def fight_window():
    # зупиняємо музику яка грала перед боєм
    music_load_waiting.stop()
    # вмикаємо музику для бою
    fight_music.play()
    # задаємо назву вікну
    pygame.display.set_caption("Battle Screen")
    # створюємо змінну для нескінченого циклу гри
    run_game = True

    # створюємо дві сітки для гри(нашу та ворога) , ці сітки просто як звичайний малюнок
    enemy_grid.X_SCREEN = 67
    enemy_grid.Y_SCREEN = 257
    enemy_grid.generate_grid(width_cell=55, height_cell=55)

    grid_player.X_SCREEN = 705
    grid_player.Y_SCREEN = 257
    grid_player.generate_grid(width_cell=55, height_cell=55)


    # оновлюємо координати кораблів , та їхній розмір , щоб можна було відмалювати на сітці
    for num , ship  in enumerate(list_ships):
        grid_x = list_ships[num].col
        grid_y = list_ships[num].row
        list_ships[num].X_COR = grid_player.X_SCREEN + grid_x * 55
        list_ships[num].Y_COR = grid_player.Y_SCREEN + grid_y * 55
        list_ships[num].WIDTH = 55
        list_ships[num].HEIGHT = 55
        list_ships[num].load_image()

    # Завантажуємо картинку для сітки , по якій можемо ореєнутватися куди бити(тобто A1 , B9 і тд)
    grid_image.width = 597
    grid_image.height = 597
    grid_image.x_cor = 659
    grid_image.y_cor = 211
    grid_image.load_image()

    # оновлюємо дані про нік та бали гравців
    player_nick.text = dict_save_information["player_nick"]
    enemy_nick.text = dict_save_information["enemy_nick"]
    player_points.text = str(dict_save_information["player_points"])
    enemy_points.text = str(dict_save_information["enemy_points"])
    player_nick.update_text()
    enemy_nick.update_text()
    player_points.update_text()
    enemy_points.update_text()
    send_matrix()
    random_first_choice_sound.play2(loops = 1)
    while run_game:
        module_screen.FPS.tick(60)
        #----------------------------------------------------------------
        ship_border()
        #----------------------------------------------------------------
        kill_enemy_ships()
        if len(server_module.enemy_died_ships) > 0:
            achievement.player_died_ships_for_achiv[0] = server_module.player_died_ships
            achievement.enemy_dies_ships_for_ahiv[0] = server_module.enemy_died_ships
        for medal in range(0 , len(server_module.save_medals_coordinates)):
            if server_module.save_medals_coordinates[medal] == 1:
                class_medal.enemy_four_decker_sniper_medal.ACTIVE = True
            elif server_module.save_medals_coordinates[medal] == 2:
                class_medal.enemy_perfect_shooter_medal.ACTIVE = True
            elif server_module.save_medals_coordinates[medal] == 3:
                class_medal.enemy_strategist_medal.ACTIVE = True
            elif server_module.save_medals_coordinates[medal] == 4:
                class_medal.enemy_first_hit_medal.ACTIVE= True
            elif server_module.save_medals_coordinates[medal] == 5:
                class_medal.enemy_magnat_medal.ACTIVE = True
            elif server_module.save_medals_coordinates[medal] == 6:
                class_medal.enemy_master_of_disguist_medal.ACTIVE = True
            elif server_module.save_medals_coordinates[medal] == 7:
                class_medal.enemy_lone_hunter_medal.ACTIVE = True
            elif server_module.save_medals_coordinates[medal] == 8:
                class_medal.enemy_pioneer_medal.ACTIVE = True
            elif server_module.save_medals_coordinates[medal] == 9:
                class_medal.enemy_destroyer_medal.ACTIVE = True
            elif server_module.save_medals_coordinates[medal] == 10:
                class_medal.enemy_opening_battle_medal.ACTIVE = True
            elif server_module.save_medals_coordinates[medal] == 11:
                class_medal.enemy_target_attack_medal.ACTIVE = True
            elif server_module.save_medals_coordinates[medal] == 12:
                class_medal.enemy_collector_medal = True

        if animation_random_player.COUNT_IMAGES >= 5 and animation_random_player.COUNT_IMAGES <= 10:
            animation_random_player.ANIMATION_SPEED = 3.2
        elif animation_random_player.COUNT_IMAGES >= 11 and animation_random_player.COUNT_IMAGES <= 16:
            animation_random_player.ANIMATION_SPEED = 4.2
        elif animation_random_player.COUNT_IMAGES >= 17 and animation_random_player.COUNT_IMAGES <= 22:
            animation_random_player.ANIMATION_SPEED = 5.2
        elif animation_random_player.COUNT_IMAGES >= 23 and animation_random_player.COUNT_IMAGES <= 27:
            animation_random_player.ANIMATION_SPEED = 8.2
        if server_module.list_player_role[0] == "server_player":
            if animation_random_player.COUNT_IMAGES >= 28 and animation_random_player.COUNT_IMAGES <= 31:
                animation_random_player.ANIMATION_SPEED = 120
        elif server_module.list_player_role[0] == "client_player":
             if animation_random_player.COUNT_IMAGES >= 29 and animation_random_player.COUNT_IMAGES <= 31:
                animation_random_player.ANIMATION_SPEED = 120



        if server_module.list_player_role[0] != "server_player" and animation_random_player.COUNT_IMAGES >= 29 and count_sound_time[0] == 0:
            enemy_turn_sound.play2(loops = 1)
            count_sound_time[0] = 1
        elif animation_random_player.COUNT_IMAGES >= 28 and count_sound_time[0] == 0 and server_module.list_player_role[0] != "client_player":
            player_turn_sound.play2(loops = 1)
            count_sound_time[0] = 1
    


        if animation_random_player.IS_ANIMATION_DONE == True:
            if check_two_times.count(3) >= 2:
                server_module.check_time[0] += 1
                check_two_times.clear()

        if len(server_module.enemy_data) > 0:
            check_data = server_module.enemy_data[0].split(' ')
            #"rocket_shot 3 1"
            #["rocket_shot", "3", "1" , " "]
            if check_data[0] == "enemy_matrix":
                check_list = server_module.enemy_data[0].split(' ')
                row = 0
                column = 0
                for str_number in check_list[1:101]:
                    enemy_matrix[row][column] = int(str_number)
                    column += 1
                    if column == 10:
                        row += 1
                        column = 0
                for data_ship in range(101, len(check_list) - 1, 4):
                    server_module.enemy_ships.append((int(check_list[data_ship]), int(check_list[data_ship + 1]), int(check_list[data_ship + 2]), (check_list[data_ship + 3])))
            else:
                try:
                    if check_data[0] == "enemy_turn":
                        if server_module.list_player_role[0] == "server_player":
                            server_module.turn[0] = "server_turn"
                        elif server_module.list_player_role[0] == "client_player":
                            server_module.turn[0] = "client_turn"
                    if check_data[0] == "player_turn":
                        if server_module.list_player_role[0] == "server_player":
                            server_module.turn[0] = "client_turn"
                        elif server_module.list_player_role[0] == "client_player":
                            server_module.turn[0] = "server_turn"
                    for data_enemy in check_data:
                        if data_enemy == "shot":
                            server_module.check_time[0] = 0
                            count_hit = 0
                            for data_enemy in range(1, len(check_data) - 1, 2): 
                                if list_grid[int(check_data[1])][int(check_data[2])] in [1, 2, 3, 4, 7]:
                                    if list_grid[int(check_data[1])][int(check_data[2])] == 7:
                                        pass
                                    else:
                                        list_grid[int(check_data[1])][int(check_data[2])] = 7
                                        server_module.check_time[0] = 0
                                    data_player_shot.append("enemy_turn")
                                    list_check_need_send[0] = True
                                    if server_module.list_player_role[0] == "server_player":
                                        server_module.turn[0] = "client_turn"
                                    elif server_module.list_player_role[0] == "client_player":
                                        server_module.turn[0] = "server_turn"
                                else:
                                    list_grid[int(check_data[1])][int(check_data[2])] = 5
                                    server_module.check_time[0] = 0
                                    if server_module.list_player_role[0] == "server_player":
                                        server_module.turn[0] = "server_turn"
                                    elif server_module.list_player_role[0] == "client_player":
                                        server_module.turn[0] = "client_turn"
                        elif data_enemy == "auto_rocket":
                            index_cell = 1
                            count_hit = 0
                            for cell in check_data[1:-1]:
                                if index_cell % 2 == 0:
                                    if list_grid[int(check_data[index_cell - 1])][int(check_data[index_cell])] in [1, 2, 3, 4, 7]:
                                        count_hit += 1
                                        if list_grid[int(check_data[index_cell - 1])][int(check_data[index_cell])] == 7:
                                            pass
                                        else:
                                            list_grid[int(check_data[index_cell - 1])][int(check_data[index_cell])] = 7
                                    elif list_grid[int(check_data[index_cell - 1])][int(check_data[index_cell])] in [0, 5]:
                                        list_grid[int(check_data[index_cell - 1])][int(check_data[index_cell])] = 5
                                index_cell += 1
                            if count_hit == 0:
                                if server_module.list_player_role[0] == "server_player":
                                    server_module.turn[0] = "server_turn"
                                elif server_module.list_player_role[0] == "client_player":
                                    server_module.turn[0] = "client_turn"
                            elif count_hit >= 1:
                                data_player_shot.append("enemy_turn")
                                list_check_need_send[0] = True
                                if server_module.list_player_role[0] == "server_player":
                                    server_module.turn[0] = "client_turn"
                                elif server_module.list_player_role[0] == "client_player":
                                    server_module.turn[0] = "server_turn"
                            server_module.check_time[0] = 0
                        elif data_enemy == "bomb":
                            for cell in range(1 , 19):
                                print("bomb")
                                try:
                                    if cell % 2 == 0:
                                        if list_grid[int(check_data[cell - 1])][int(check_data[cell])] in [1, 2, 3, 4, 7]:
                                            if list_grid[int(check_data[cell - 1])][int(check_data[cell])] == 7:
                                                pass
                                            else:
                                                list_grid[int(check_data[cell - 1])][int(check_data[cell])] = 7
                                        elif list_grid[int(check_data[cell - 1])][int(check_data[cell])] in [0, 5]:
                                            list_grid[int(check_data[cell - 1])][int(check_data[cell])] = 5
                                except:
                                    continue
                            if int(check_data[-3]) == 0:
                                if server_module.list_player_role[0] == "server_player":
                                    server_module.turn[0] = "server_turn"
                                elif server_module.list_player_role[0] == "client_player":
                                    server_module.turn[0] = "client_turn"
                            else:
                                data_player_shot.append("enemy_turn")
                                list_check_need_send[0] = True
                                if server_module.list_player_role[0] == "server_player":
                                    server_module.turn[0] = "client_turn"
                                elif server_module.list_player_role[0] == "client_player":
                                    server_module.turn[0] = "server_turn"
                            server_module.check_time[0] = 0
                except:
                    continue
                if check_data[0] == "restore_cell":
                    enemy_matrix[int(check_data[2])][int(check_data[3])] = int(check_data[1])
                if check_data[0] == "medal":
                    for medal in check_data[1:-1]:
                        print(check_data[1:-1])
                        if int(medal) not in server_module.save_medals_coordinates:
                            server_module.save_medals_coordinates.append(int(medal))
                elif check_data[0] == "money":
                    server_module.enemy_balance[0] = int(check_data[1])
                    enemy_balance_in_jar.update_text()

```

[⬆️Table of contents](#articles)

<a name="json_functions"><h1>describe json_functions package</h1></a>
У цій папці ми маємо файли, які записують нікнейм та пароль користувачів.
<details>
<summary>English version</summary>
In this folder we have files that record the nickname and password of users.
</details>

[⬆️Table of contents](#articles)

<a name="screens"><h1>describe screens package</h1></a>
Створюємо у папці screens ми відмальовуємо розміри екрану гри, також зберігаємо початковий список кораблів та у файлі create_grid відображаємо поле бою, код можна побачити нижче.
<details>
<summary>English version</summary>
We create in the screens folder, we draw the dimensions of the game screen, we also save the initial list of ships and display the battlefield in the create_grid file, the code can be seen below.
</details>

```python
    #класс для створення однієї порожньої клітинки
    class Cell:
        def __init__(self, x: int , y: int , width: int , height:int , image_name: str):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.image_name = image_name
            self.image = None
            self.load_image()
        def load_image(self):
            #"/../../../media/grid/{self.image_name}
            image_path = abspath(join(__file__, "..", "..", "..", "media", "grid", f"{self.image_name}"))
            image = pygame.image.load(image_path)
            transformed_image = pygame.transform.scale(image, (self.width, self.height))
            self.image = transformed_image
        def draw(self, screen: pygame.Surface):
            screen.blit(self.image, (self.x, self.y))


    #список для зберігання об'єктів сітки
    list_object_map = []

    list_object_map_enemy = []


    #класс для створення сітки
    class Grid:
        def __init__(self , x_screen: int , y_screen: int):
            self.X_SCREEN = x_screen
            self.Y_SCREEN = y_screen
        def generate_grid(self , width_cell = 62 , height_cell = 62):
            if self.X_SCREEN == 67:
                        list_object_map_enemy.clear()
            else:
                list_object_map.clear()
        
            x_screen , y_screen = self.X_SCREEN , self.Y_SCREEN
            for row in list_grid:
                for cell in row:
                    # if cell == 0:
                    empty_cell = Cell(x = x_screen , y = y_screen ,width = width_cell , height = height_cell , image_name = "empty_cell.png")
                    if self.X_SCREEN == 67:
                        list_object_map_enemy.append(empty_cell)
                    else:
                        list_object_map.append(empty_cell)
                        
                    x_screen += width_cell
                y_screen += height_cell
                x_screen = self.X_SCREEN

        def snap_to_grid(self, x, y):
        # Розраховуємо індекс стовпця сітки (grid_x), який потрапляє точка (x)-координата корабля.
        # 1. Віднімаємо координату початку сітки по X (self.X_SCREEN), щоб отримати відносне положення.
        # 2. Ділимо на ширину комірки (62), щоб визначити, в який стовпець потрапляє крапка.
        # 3. Округлюємо до найближчого цілого числа, щоб прив'язати координату до найближчого стовпця.
            grid_x = round((x - self.X_SCREEN) / 62)  
        
        # Розраховуємо індекс рядка сітки (grid_y), до якого потрапляє точка (y)-координата корабля.
        # 1. Віднімаємо координату початку сітки по Y (self.Y_SCREEN), щоб отримати відносне положення.
        # 2. Ділимо на висоту комірки (62), щоб визначити, в який рядок потрапляє крапка.
        # 3. Округлюємо до найближчого цілого числа, щоб прив'язати координату до найближчого рядка.
            grid_y = round((y - self.Y_SCREEN) / 62)  
        
        # Обмежуємо індекс стовпця (grid_x) у межах від 0 до 8 (максимальна кількість стовпців мінус 1).
        # Якщо координата виходить за межі сітки, вона буде приведена до найближчого кордону.
            grid_x = max(0, min(10 - 1, grid_x))
        
        # Обмежуємо індекс рядка (grid_y) у межах від 0 до 8 (максимальна кількість рядків мінус 1).
        # Якщо координата виходить за межі сітки, вона буде приведена до найближчого кордону.
            grid_y = max(0, min(10 - 1, grid_y))
        
        # Повертаємо координати центру прив'язаного осередку:
        # 1. Розраховуємо екранні координати центру осередку по X:
        # - Помножуємо індекс стовпця (grid_x) на ширину комірки (62) і додаємо усунення сітки (self.X_SCREEN).
        # 2. Аналогічно, розраховуємо екранні координати центру осередку Y.
            return self.X_SCREEN + grid_x * 62, self.Y_SCREEN + grid_y * 62
        
        def snap_to_grid_enemy(self, x, y):

            grid_x = round((x - self.X_SCREEN) / 55)  

            grid_y = round((y - self.Y_SCREEN) / 55)  

            grid_x = max(0, min(10 - 1, grid_x))
    
            grid_y = max(0, min(10 - 1, grid_y))
    
            return self.X_SCREEN + grid_x * 55, self.Y_SCREEN + grid_y * 55
        
        def cell_number_to_coordinates(self, cell_number):
            # Перетворимо номер клітини на екранні координати
            # cell_number - це номер клітини, який починається з 1 (наприклад, 1, 2, 3,...)
            grid_x = (cell_number ) % 10  # Перетворюємо у стовпець
            grid_y = (cell_number ) // 10  # Перетворюємо у рядок
            x_coord = self.X_SCREEN + grid_x * 55
            y_coord = self.Y_SCREEN + grid_y * 55
            return x_coord, y_coord
        def coordinates_to_number(self, x_coord, y_coord):
            # Перетворимо екранні координати на номер клітини
            # x_coord та y_coord - це екранні координати точки
            grid_x = (x_coord - self.X_SCREEN) // 55  # Розраховуємо стовпець
            grid_y = (y_coord - self.Y_SCREEN) // 55  # Розраховуємо рядок
            cell_number = grid_y * 10 + grid_x + 1  # Перетворюємо в номер клітинки
            return cell_number
        

        
    grid_player = Grid(x_screen = 81 , y_screen = 76)
    enemy_grid = Grid(x_screen = 67 , y_screen = 257)
```

[⬆️Table of contents](#articles)

<a name="shop"><h1>describe shop package</h1></a>
У цій папці файли, які відповідають за кнопки у нашій крамниці, усі зображення, а також увесь текст з крамниці. Ще є папка з файлами усіх завдань, які можна виконати та отримати додаткові монети.
<details>
<summary>English version</summary>
This folder contains the files responsible for the buttons in our store, all the images, and all the text from the store. There is also a folder with files for all the tasks that can be completed to get additional coins.
</details>

[⬆️Table of contents](#articles)

<a name="volume_settings"><h1>describe volume_settings package</h1></a>
У папці volume_settings файли з функціями, які відповідають за гучність музики, маємо змогу налаштовувати гучність, або вимкнути звук зовсім.
<details>
<summary>English version</summary>
In the volume_settings folder, there are files with functions that are responsible for the music volume, allowing us to adjust the volume or turn off the sound altogether.
</details>

[⬆️Table of contents](#articles)


<a name="client"><h1>Client.py package modules</h1></a>
Частина коду client, де ми віправляємо матрицю через список, отримуємо дані, а також цикл для безпреревного обміну даними.

```python
        def send_matrix():
        list_check_need_send[0] = True
        data_player_shot.clear()  # Очищаємо дані перед додаванням нових
        data_player_shot.append("enemy_matrix")
        for row in list_grid:  # Передбачається, що list_grid відповідає enemy_matrix
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

    # Функція для отримання усіх данних
    def recv_all(sock):
        data = b""
        while True:
            part = sock.recv(1024)
            if not part or b"END" in part:  # Умова завершення передачі
                data += part.split(b"END")[0]
                break
            data += part
        return data

    def start_client():
        if input_nick.user_text not in list_users:
            #створюємо гравця з його ніком та даємо базову кількість балів
            list_users[input_nick.user_text] = {"points": 0,
                                                "password": input_password.user_text
                                                }
            #зберігаємо інформацію у json файл
            write_json(filename = "data_base.json" , object_dict = list_users)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            # try:
            port_client = int(input_port.user_text)
            client_socket.connect((str(input_ip_adress.user_text), port_client))  # Підключення до серверу
            print("Клиент подключён к серверу.")
            # Отримання повідомлення від сервера (роль клієнта)
            role = client_socket.recv(1024).decode("utf-8")
            server_module.list_player_role[0] = role
            # Бескінечний цикл для відправки та отримання даних
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
                                str_line += str(cell) + " " # Переводимо список в рядок з пробілами
                            client_socket.sendall(str_line.encode("utf-8") + b"END")  # Відправка даних як список
                            data_player_shot.clear()  # Очищаєємо список перед новим входом
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
```
[⬆️Table of contents](#articles)

<a name="server"><h1>Server.py package modules</h1></a>
Частина коду server, де ми створюємо зміну потока, для запуску серверу.

```python
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
Головний клас кораблів, який створює об'єкти класів.

```python
    class Ship:
    def __init__(self, x_cor: int, y_cor: int, width: int, height: int, image_ship: str, image_rotate_ship: str , length: int, position_ship: str):
        r'''
        :mod:`метод` ``__init__``, яка створює об'єкти класів, встановлює координати, розмір, позицію кораблів.

        Приклад застосування: 
        >>> self.X_COR, self.Y_COR = grid_player.snap_to_grid(self.X_COR, self.Y_COR) 
        '''
        self.X_COR = x_cor#місце де стоятиме корабель за іксом
        self.Y_COR = y_cor#місце де стоятиме корабель за греком
        self.WIDTH = width#ширина корабля
        self.HEIGHT = height#висота корабля
        self.IMAGE_SHIP = image_ship#картинка звичайного корабля
        self.ROTATE_SHIP = image_rotate_ship#картинка поверненого корабля
        self.LENGHT = length#довжина корабля у клітинах
        self.ORIENTATION_SHIP = position_ship#горизонтально чи вертикально зараз стоїть корабель
        self.CHEK_ROTATION = self.ORIENTATION_SHIP#для перевірки горизонтально чи вертикально зараз стоїть корабель
        self.READY_IMAGE_SHIP = None#відмаштобована та готова картина нормального корабля
        self.IMAGE_ROTATE_SHIP = None#відмаштобована та готова кратинка поверненого корабля
        self.load_image()#викликаємо метод завантаження картинки
        self.CHECK_MOVE = None # Прапор для перевірки рухів миші
        self.RECT = self.READY_IMAGE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))#прямокутник для того, щоб могли відстежувати курсор чи на кораблику чи ні
        self.STASIC_X = self.X_COR # Static_x = це початкові координати
        self.STASIC_Y = self.Y_COR # Static_y = це початкові координати
        # це світло де зберігається нова клітина де стоїть корабель
        self.number_cell = 0
        # це властивість де зберігається стара клітина де стояв корабель
        self.number_ship_cell = 0
        # номер рядка в матриці де він стоїть
        self.row = 0
        # номер клітини де він стоїть
        self.col = 0
        # прапор для перевірки зіткнення з кораблями (колізії)
        self.check_collision = None
        self.check_after_random = None
```

Функції, які создають прилипання та розраховує індекс клітинки.

```python
    def snap_to_grid(self): 
        r'''
        :mod:`Метод` ``snap_to_grid``, за допомогою коорднинат прив'язуємо корабель дло сітки.
        Приклад застосування: 
        >>> snapped_x, snapped_y = grid.snap_to_grid(mouse_x, mouse_y)
        '''       
        # Прив'язати координати до сітки, щоб корабель не йшов на саму сітку
        self.X_COR, self.Y_COR = grid_player.snap_to_grid(self.X_COR, self.Y_COR) 
    def center_to_cell_number(self, x, y):
        r'''
        :mod:`Метод` ``center_to_cell_number``, яка розраховує індекс клітинки: Номер клітки = (строка * кількість стовбців) + (стовбець) + 1.
        Приклад застосування: 
        >>>  self.number_ship_cell = self.center_to_cell_number(x = self.X_COR,y = self.Y_COR)
        '''        
        #Розраховуємо індекс стовпця та рядки, в які потрапляє корабель.
        # grid_player.X_SCREEN - координати сітки за іксом
        # grid_player.Y_SCREEN - координати сітки за гріком
        # x - координати корабли за позовом
        # y - координати корабля за гріком
        col = (x - grid_player.X_SCREEN) // 62  # Индекс столбца 
        row = (y - grid_player.Y_SCREEN) // 62  # Индекс строки 

        # Враховуємо, що клітини нумеруються з 1, тому:
        # Номер клітини = (рядок * кількість стовпців) + (стовпець) + 1.
        cell_number = row * 10 + col + 1

        # Повертаємо номер клітинки
        return cell_number
```

Методи для розтавлення кораблів

```python
    def rotate_ship(self, event: pygame.event):
        r'''
        :mod:`Метод` ``rotate_ship``, повертає корабель горизонтально чи вертикально, натиснувши клавішу R  корабель повертається.
        Приклад застосування: 
        >>>  self.RECT = self.IMAGE_ROTATE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
        '''  
        self.RECT.topleft = (self.X_COR, self.Y_COR)
        # Створюємо змінну мишки, і отримуємо координати мишки гравця
        mouse = pygame.mouse.get_pos()
        # Якщо координати мишки дорівнюють координатам корабля
        if self.RECT.collidepoint(mouse):
            # Якщо клавіша відпущена
            if event.type == pygame.KEYDOWN:
                # якщо натиснуто R клавіша
                if event.key == pygame.K_r and self.CHECK_MOVE == True: 
                    # Якщо корабель horizontal
                    if self.CHEK_ROTATION == "horizontal":
                        self.ORIENTATION_SHIP = "vertical"
                        self.CHEK_ROTATION = self.ORIENTATION_SHIP
                        self.load_image()
                        self.RECT = self.IMAGE_ROTATE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
    
                        # Обновляємо прямокутник
                    
                    elif self.CHEK_ROTATION == "vertical":
                        self.ORIENTATION_SHIP = "horizontal"
                        self.CHEK_ROTATION = self.ORIENTATION_SHIP
                        self.load_image()
                        self.RECT = self.READY_IMAGE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
                        
                        
                    self.X_COR = mouse[0] - self.RECT.width // 2
                    self.Y_COR = mouse[1] - self.RECT.height // 2

                    
                    

    # метод який чистити положення корабля на матриці якщо його пересунули
    def clear_matrix(self):
        r'''
        :mod:`Метод` ``clear_matrix``, який очищає попереденє розтавлення корабля.
        Приклад застосування: 
        >>>  self.clear_matrix()
        '''  
        # список для перевірки розставлення кораблів
        if check_for_shipsmoving[0] == 0:
            # список для перевірки попереднього розтавлення кораблів
            check_prev_pos = 0

            for index_col in range(0 , 2):
                # Додавання до клітинки
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
       

    # метод, який телепортує корабель на початкову точку і повертається в положення по горизонталі
    def return_start_code(self):
        r'''
        :mod:`Метод` ``return_start_code``, для повернення корабля на початкому точку, якщо корабель не відповідає потрібним координатам ,та повертає корабель в горизонтальнеп положення.
        >>>  self.return_start_code()
        '''  
        self.X_COR, self.Y_COR = self.STASIC_X, self.STASIC_Y
        self.RECT = self.IMAGE_ROTATE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
        self.ORIENTATION_SHIP = "horizontal"
        # Записуємо у змінну для перевірки
        self.CHEK_ROTATION = self.ORIENTATION_SHIP
        # Малюємо зображення за допомогою методу
        self.load_image()
        # Записуємо в змінну змінену позицію
        self.RECT = self.READY_IMAGE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
            
       

    def matrix_move(self, event: pygame.event, matrix_width: int, matrix_height: int, cell: int):
        r'''
        :mod:`Метод` ``matrix_move``, перевіряє, щоб кораблі не накладалися один на одний та щоб кораблі були щонайменше на одну клітинку один від одного.
        >>>  ship.matrix_move(event = event, matrix_width = 620, matrix_height = 620, cell = 100)
        '''
        # Отримуємо координати миші
        mouse = pygame.mouse.get_pos() 

        if event.type == pygame.MOUSEBUTTONDOWN and self.RECT.collidepoint(event.pos):
            # Початок переміщення
            self.CHECK_MOVE = True

        # Якщо ми рухаємо курсором по екрану і вже натискали на корабель
        elif event.type == pygame.MOUSEMOTION and self.CHECK_MOVE:

            self.X_COR = mouse[0] - self.RECT.width // 2
            self.Y_COR = mouse[1] - self.RECT.height // 2


            # Обмежуємо рух корабля межами матриці
            self.X_COR = max(0, min(self.X_COR, matrix_width * cell - self.RECT.width))
            self.Y_COR = max(0, min(self.Y_COR, matrix_height * cell - self.RECT.height))
            # Обновляємопрямокутник тільки при русі
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

            # Перевірка перетину з іншими кораблями
            # робимо перебір списку з кораблями, щоб модно було перевіряти чи не намагається поставити користувач корабель на корабель
            for ship in list_ships:
                # Перевіряємо ship != self - це щоб не перевіряти кораблик сам із собою
                # self.RECT.colliderect(ship.RECT) - перевіримо кожен корабель зі списку з поточним кораблем, якщо їх прямокутники (колізії) перетинаються, то ставимо кораблик на початкові координати
                if ship != self and self.RECT.colliderect(ship.RECT):
                    print("пересекается")
                    self.return_start_code()
                    # self.number_cell = self.number_ship_cell
                    # # Переробляємо значення клітини в рядок щоб можна було легко дізнатися в колонці він стоїть
                    # str_col = str (self.number_cell)
                    # # Обчислюємо номер рядка де стоїть корабель (наприклад 23, ділимо на 10 без залишку і отримуємо 2, ось наш стовпець)
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

                    # Перераховуємо номер клітини, де стоїть корабель для старих координат
                    self.number_ship_cell = self.center_to_cell_number(x = self.X_COR,y = self.Y_COR)


                    print(list_grid)
                    print("------------------------------------------------------------------------------------------------")
                    for cell in list_object_map: 
                            if cell.x <= self.X_COR and self.X_COR < cell.x + 62:
                                if cell.y <= self.Y_COR and self.Y_COR < cell.y + 62:
                                    # Дізнаємсь номер клітинки де стоїть корабель
                                    self.number_cell = list_object_map.index(cell)
                                    # Перераховуємо номер клітини, де стоїть корабель для старих координат
                                    str_col = str(self.number_cell) 
                                    # Обчислюємо номер рядка де стоїть корабель (наприклад 23, ділимо на 10 без залишку і отримуємо 2, ось наш стовпець)
                                    self.row = self.number_cell // 10  
                                    #Колонку кораблика обчислюємо за таким принципом
                                    # Наприклад знову 23 число номер колонки де стоїть корабель , тоді за допомогою -1 ми беремо останнє число тобто трійку, і ось так отримуємо номер колонки
                                    self.col = int(str_col[-1])

                                    # Встановлюємо значення де стоїть корабель у матриці
                                    if self.ORIENTATION_SHIP == "horizontal":
                                        for index_column in range(0 , self.LENGHT):
                                            list_grid[self.row][self.col + index_column] = self.LENGHT
                                    elif self.ORIENTATION_SHIP == "vertical":
                                        for index_row in range(0 , self.LENGHT):
                                            list_grid[self.row + index_row][self.col] = self.LENGHT
                    
                     
                    for shiper in list_ships:
                        # перевірка щоб корабель який рухаємо не порівнювали із самим собою
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
