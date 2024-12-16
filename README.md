<h1>Ships Battle</h1>

---

<a name="articles"><h3>Table of contents</h3></a>

# Project Description  
[Project description](#headers)

# Getting Started  
[Getting started](#getting_started)

# Modules Description  
[Modules description](#modules)

# Project Scheme  
[Scheme of project](#scheme)

# Package Description  
-   [Package description](#package_description)
    -[Main __init__.py of package modules](#main_init)
    - [client.py package modules](#client)
    - [server.py package modules](#server)
    -   [Classes package](#classes_discription)
        -  [__init__.py of package modules](#classes_init)
        - [class_button.py](#class_button)
        - [class_click.py](#class_click)
        - [class_font.py](#class_font)
        - [class_image.py](#class_image)
        - [class_input_text.py](#class_input_text)
        - [class_sounds.py](#class_sounds)
    -   [game package](#game_description)
        -  [__init__.py of package game](#game_init)
        -  [input_text.py of package game](#game_input_text)
    -   [json_functions package](#json_functions_description)
        -  [__init__.py of package json_functions](#json_functions_init)
        -  [read_json.py of package json_functions](#read_json)
        -  [write_json.py of package json_functions](#write_json)
    -   [run_game package](#run_game_description)
        -  [__init__.py of package run_game](#run_game_init)
        -  [start_game.py of package run_game](#start_game)
    -   [screens package](#screens_description)
        -  [__init__.py of package screens](#creens_init)
        -  [create_grid.py of package screens](#create_grid)
        -  [list_grid.py of package screens](#list_grid)
        -  [screen.py of package screens](#screen)
    -   [static package](#static)
        -  [data_base.json of package static](#data_base)
        -  [utility.json of package static](#utility)
    -    [Main file main.py](#main)

# Sources of information
[Links to sources of information](#links_of_informations)

# Problems when creating a project
[Problems during development](#prbl_project)

# Working on mistakes
[Mistakes during development](#work_mistakes)

# Conclusion
[Conlusion](#conclusions)

---


<a name="headers"><h1>Project description</h1></a>
Основна мета цього проєкту - закріпити навички роботи з клієнтом, сервером та передача данних. 
Ships Battle - гра у морський бій у сучасному світі. За допомогою ip ви маєте можливість створити чи доєднатися до гри з другом, під час гри заробити бали та в кінці побачити результат гри. 
Щоб створити гру, потрібно:
 1. Ввести свій нікнейм 
 2. ip-адресу, яка приймає запрос від будь-якого користувача(0.0.0.0), або локальну адресу
 3. Ввести порт
Щоб доєднатись до гри, потрібно:
 1. Ввести свій нікнейм 
 2. Публічну ip-адресу, яку ви можете дізнатись у свого провайдера
 3. Ввести порт
<details>
<summary> English version </summary>
The main goal of this project is to consolidate the skills of working with the client, server and data transfer.
Ships Battle - a game of naval battle in the modern world. Using ip you have the opportunity to create or join a game with a friend, earn points during the game and at the end see the result of the game.
To create a game, you need:
1. Enter your nickname
2. ip-address that accepts requests from any user (0.0.0.0), or a local address
3. Enter the port
To join the game, you need:
1. Enter your nickname
2. Public ip-address, which you can find out from your provider
3. Enter the port
</details>

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
* **io** - working with bytes

<a name="scheme"><h1>Scheme of the project</h1></a>

[⬆️Table of contents](#articles)


[https://www.figma.com/board/db61SCQLwAnOtFgqTjsIGn/Untitled?node-id=0-1&t=tG7hTz55wsvVlP7L-1]

<a name="package_description"><h1>Package description</h1></a>

<a name="main_init"><h2>__init__.py</h2></a>

Цей файл ініціалізує всі модулі, функції, класи та змінні з пакету modules.
Зручно,для отримання доступу до всіх елементів пакета.
<details>
<summary>English version</summary>
This file initializes all modules, functions, classes, and variables from the modules package. 
This approach is convenient for accessing all elements of the package.
</details>

```python
#імпортуємо усі необхідні компоненти проекту, щоб їх можна було легко використовувати в інших частинах програми, та також за межами папки modules 
from .server import server_thread
from .client import thread_connect
from .run_game import *
from .screens import *

```


<a name="client"><h2>client.py</h2></a>
Цей файл використовуємо для передачі данних між користувачами, коли користувач доєднується до гри.
<details>
<summary>English version</summary>
This file is used to transfer data between users when a user is logged in to the game.
</details>

```python
import socket
#підключаємо модуль для роботи із потоками
import threading
import json
from .classes.class_input_text import input_port, input_ip_adress, input_nick
import json
from .json_functions import write_json , list_users , list_server_status 

#ліст для перевірки чи зайшов користувач на сервер
list_server_status = {
    "status": None
}
write_json(filename= "utility.json" , object_dict = list_server_status)

#створюємо функцію підключення користувача до серверу
def connect_user():
    if input_nick.user_text not in list_users:
        list_users[input_nick.user_text] = {"points": 0}
        write_json(filename = "data_base.json" , object_dict = list_users)
    ip_address = input_ip_adress.user_text
    port = int(input_port.user_text)
    print(1)
    # створюємо сокет з використанням протоколу IPv4 (AF_INET) та TCP (SOCK_STREAM)
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as client_socket:
        # підключаємо користувача до сервера за Lan ip 192.168.0.4 та портом 6060
        print(2)
        client_socket.connect((ip_address, port))

        encode_text = str(input_nick.user_text)
        # відправляємо дані від користувача на сервер , та кодуємо їх у байти
        client_socket.send(encode_text.encode())

        data = client_socket.recv(1024).decode()
        data_in_list = json.loads(data)
        print(data_in_list["nick"] , "nick from server")
        print(data_in_list["status"] , "status from server")
        if data_in_list["nick"] not in list_users:
            list_users[data_in_list["nick"]] = {"points": 0}
            write_json(filename = "data_base.json" , object_dict = list_users)

        write_json(filename= "utility.json" , object_dict = data_in_list["status"])
        
        
            

#створюємо зміну потока, із функцією підключення коритсувача до серверу
thread_connect = threading.Thread(target = connect_user, daemon=True)
```

<a name="server"><h2>server.py</h2></a>
Цей файл використовуємо для передачі данних між користувачами, коли користувач створює гру.
<details>
<summary>English version</summary>
We use this file to transfer data between users when a user creates a game.
</details>

```python
import socket
#підключаємо модуль для роботи із потоками
import threading
# Импортируем классы
from .classes.class_input_text import input_port , input_ip_adress, input_nick
# Импортируем функцию записи в json файлы
from .json_functions.write_json import write_json , list_server_status , list_users
import json


#ліст для перевірки чи зайшов користувач на сервер
list_server_status = {
    "status": None
}
write_json(filename= "utility.json" , object_dict =  list_server_status)

        
if list_server_status == False:
    print("False")

#створємо функцію для запуску серверу
def start_server():
    #
    if input_nick.user_text not in list_users:
        list_users[input_nick.user_text] = {"points": 0}
        write_json(filename = "data_base.json" , object_dict = list_users)
                    
    ip_address = input_ip_adress.user_text
    port = int(input_port.user_text)
    print(ip_address , port)
    # Створюємо сокет з використанням протоколу IPv4 (AF_INET) та TCP (SOCK_STREAM)
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as server_socket:
        # Прив'язуємо сокет до порту 6060 , та робимо так щоб до нього могли підключатися користувачи із різних мереж
        server_socket.bind((ip_address, port))
        #Ставимо сервер у режим очікування підключень
        server_socket.listen()
        print("connecting")
        list_server_status = {
            "status": "wait"
        }
        write_json(filename= "utility.json" , object_dict = list_server_status)

        client_socket, adress = server_socket.accept()
        list_server_status = {
            "status": "connect"
        }
        write_json(filename= "utility.json" , object_dict = list_server_status)

        with client_socket:  
            # Отримуємо дані від клієнта
            response_data = client_socket.recv(1024).decode()
            print(response_data , "from client")

            if response_data not in list_users:
                list_users[response_data] = {"points": 0}
                write_json(filename = "data_base.json" , object_dict = list_users)
            
            #формуємо дані для відправки від сервера до клієнта
            data_for_client = {
                "nick": str(input_nick.user_text),
                "status": list_server_status
            }
            #відправляємо дані на кліжента , dumps - перетворює словарь у звичайну строку 
            client_socket.send(json.dumps(data_for_client).encode())
           
        
            
#створюємо зміну потока, для запуску серверу
server_thread = threading.Thread(target = start_server, daemon=True)
```


<a name="classes_discription"><h2>classes_discription</h2></a>


<a name="classes_init"><h2>classes_init.py</h2></a>

Цей файл ініціалізує всі модулі, функції, класи та змінні з пакету classes.
Зручно,для отримання доступу до всіх елементів пакета.
<details>
<summary>English version</summary>
This file initializes all modules, functions, classes, and variables from the classes package. 
This approach is convenient for accessing all elements of the package.
</details>

```python
#імпортуємо весь вміст файлу class_image.py доступним для іншиї файів, щоб могли імпортувати не вводячи увесь шлях
from .class_image import *
from .class_button import *
from .class_input_text import *
from .class_font import *
from .class_sounds import*
```

<a name="class_button"><h2>class_button.py</h2></a>
У цьому файлі створюємо клас для кнопок, які будемо вікористовувати у майбутньому.
<details>
<summary>English version</summary>
In this file, we create a class for the buttons that we will use in the future.
</details>

```python
import pygame
import os 


class Button:
    def __init__(self, x, y, image_path, image_hover_path, height,width, action=None):
        self.image1 = os.path.abspath(__file__ + f"/../../../images/images_button/{image_path}")
        self.image2 = os.path.abspath(__file__ + f"/../../../images/images_button/{image_hover_path}")
        self.image = pygame.transform.scale(pygame.image.load(self.image1), (width, height))
        self.image_hover = pygame.transform.scale(pygame.image.load(self.image2), (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.action = action

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            surface.blit(self.image_hover, self.rect.topleft)
        else:
            surface.blit(self.image, self.rect.topleft)

    def check_click(self):
        mouse = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse):
            if self.action:
                    self.action()
```


<a name="class_click"><h2>class_click.py</h2></a>

Створюємо класс для звуку натискання, зручно через те, що музика не перетинається з основною мелодією.
<details>
<summary>English version</summary>
We create a class for the click sound, which is convenient because the music does not overlap with the main melody.
</details>

```python
import pygame
import os

class Sound:
     def __init__(self, name_sound):
        pygame.mixer.init()
        self.NAME_SOUND = name_sound  
        self.SOUND = pygame.mixer.Sound(__file__ + f"/../../../sounds/{self.NAME_SOUND}")
              
     def play2(self, loops):
         self.SOUND.play(loops=0, maxtime=0, fade_ms=0)
 
music_click = Sound(name_sound="button_pressed.mp3")
```

<a name="class_font"><h2>class_font.py</h2></a>

Створюємо класс для стилю шрифтів, також імпортуючи їх.
<details>
<summary>English version</summary>
We create a class for the font style, also importing them.
</details>

```python
import os
import pygame

class Font:
    def __init__(self, size : int, name_font : str, text : str,x_cor : int, y_cor : int ,screen : pygame.Surface):
        self.size = size
        self.name_font = name_font
        self.path_to_font = os.path.abspath(__file__ + f"/../../../fonts/{self.name_font}")
        self.text = text
        self.screen = screen
        self.x_cor = x_cor
        self.y_cor = y_cor
    def draw_font(self):
        font = pygame.font.Font(self.path_to_font, self.size)
        text = font.render(self.text, True, "white")
        self.screen.blit(text, (self.x_cor , self.y_cor))

```

<a name="class_image"><h2>class_image.py</h2></a>

Створюємо класс для додавання фотографій на фон.
<details>
<summary>English version</summary>
We create a class for adding photos to the background.
</details>

```python
import pygame
import os

#створюємо клас , для зручного та швидкого додавання картинки на екран
class DrawImage:
        #Створюємо метод конструктор класу ,з параметрами зображення: розміри, координати, папка де зберігається зображення та назва зображення.
        def __init__(self,width:int , height:int , x_cor:int , y_cor:str , folder_name:str , image_name:str):
              #задаємо значения властивостям класу
              self.width = width
              self.height = height
              self.x_cor = x_cor
              self.y_cor = y_cor
              self.folder_name = folder_name
              self.image_name = image_name
              #створюємо властивість для збереження загруженого зображення
              self.image = None
              #викликаємо метод завантаження зображення
              self.load_image()
        #створюємо метод для завантаження зображення з файлової системи
        def load_image(self):
            #__file__ - хранит путь именно в нашем проекте , в файле котором мы его создали
            #/.. - выход из текущего пути на один шаг назад
            image_path = os.path.abspath(__file__ + f"/../../../images/{self.folder_name}/{self.image_name}")
            #завантажуємо зображення по вказаному шляху
            load_image = pygame.image.load(image_path)
            #змінюємо зображення яке отримали у 25 рядку, по потрібному розміру
            transformed_image = pygame.transform.scale(load_image, (self.width,self.height))
            # Зберігаємо трансформоване зображення у властивість self.image, щоб його можна було використовувати далі.
            self.image = transformed_image
        #Метод draw_image відповідає за відображення зображення на екрані
        def draw_image(self, screen:pygame.Surface):
              #blit — метод(функція), що дозволяє відображати зображення на вказаній поверхні(екрані)
              # Ми передаємо об'єкт зображення (self.image) та координати, на яких воно з'явиться
              screen.blit(self.image, (self.x_cor, self.y_cor))

```


<a name="class_input_text"><h2>class_input_text.py</h2></a>

Класс для вводу тексту нійкнейму, ip-адреси та порту.
<details>
<summary>English version</summary>
Class for entering nickname, IP address and port text.
</details>

```python
import pygame 
import os
from ..screens.screen import main_screen

pygame.init()

#створюємо клас
class InputText:
    #створюємо метод конструктор та додаємо параметри для нього 
    def __init__(self, width : int, height : int, x_cor : int, y_cor : int, base_text : str,name_image : str,
                screen_name : str, font_name : str):
        #створюємо властивості класа , для того щоб динамічно передавати різні дані
        self.width = width
        self.height = height
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.base_text = base_text
        self.screen_name = screen_name
        self.font_name = font_name
        self.user_text = f"{self.base_text}"
        self.active = False
        self.name_image = name_image
        self.font = None
        self.max_length = 13
        self.rect = pygame.Rect(self.x_cor, self.y_cor, self.width, self.height)
        self.load_image()
        self.load_font(font_name)
    #створюємо метод завантаження картинки
    def load_image(self):
        #знаходимо путь по якому завантажуємо картинку
        image_path = os.path.abspath(__file__ + f"/../../../images/images_background/{self.name_image}")
        self.image = pygame.image.load(image_path)
        #завантажуємо картинку зі шляху який ми знайшли та змінюємо по розмірам
        transform_image = pygame.transform.scale(self.image , (self.width, self.height))
        #зберігаємо картинку до властивості
        self.image = transform_image    
    
    #завантажуємо шрифт який ми будемо використовувати коли пишемо 
    def load_font(self, font_name : str): 
            #отримуємо шрифт по шляху та передаємо назву його(font_name)
            font_path = os.path.abspath(__file__ + f"/../../../fonts/{font_name}")
            #ствоюємо текст зі шрифтом який ми отримали
            self.font = pygame.font.Font(font_path, size = 48)

    #створюємо метод який обробляє все що проісходить із поля воду тексту
    def check_event(self, event : object):

        if self.active == True:
            if self.user_text == self.base_text:
                self.user_text = ""
        # Якщо текстове поле неактивне, встановлюємо значення "nickname", якщо поле пусте
        elif self.active == False:
            if self.user_text == "":
                self.user_text = self.base_text
        # Обработка событий
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                self.active = True
            elif not self.rect.collidepoint(pos):
                self.active = False


        if self.base_text == "nickname":
            self.max_length = 10
        else:
            self.max_length = 13

        if event.type == pygame.KEYDOWN and self.active == True:
            # Если поле активно, обрабатываем ввод текста
            if event.key == pygame.K_BACKSPACE:
                self.user_text = self.user_text[:-1]
            elif len(self.user_text) < self.max_length:
                self.user_text += event.unicode

    def draw_text(self):
         # Очистити базовий текст тільки при активаці
        text_surface = self.font.render(self.user_text, True, "white")
        self.screen_name.blit(self.image, (self.x_cor, self.y_cor))
        if self.user_text == "port":
            self.screen_name.blit(text_surface, (self.x_cor + 125, self.y_cor + 13))
        else:
            self.screen_name.blit(text_surface, (self.x_cor + 90, self.y_cor + 13))


input_nick = InputText(width= 346 , height= 80 , x_cor= 467, y_cor= 239, font_name = "Jersey15.ttf" , screen_name = main_screen , base_text= "nickname", name_image= "input_area.png")
input_ip_adress = InputText(width= 346 , height= 80 , x_cor= 467, y_cor= 372, font_name = "Jersey15.ttf" , screen_name = main_screen , base_text= "ip adress", name_image= "input_area.png")
input_port = InputText(width= 346 , height= 80 , x_cor= 467, y_cor= 501, font_name = "Jersey15.ttf" , screen_name = main_screen , base_text= "port", name_image= "input_area.png")

```

<a name="class_sounds"><h2>class_sounds.py</h2></a>

Створюємо класс для додавння музику, за потреби можемо ставити її на паузу, потім відновлювати, але у своєму проєкті ми вимикаємо музику, а потім вмикаємо її заново. Використовуємо mixer.
<details>
<summary>English version</summary>
We create a class to add music, if necessary we can pause it, then resume it, but in our project we turn off the music, and then turn it on again. We use mixer.
</details>

```python
import pygame
import os

class MusicPlayer:
     def __init__(self, name_sound):
        pygame.mixer.init()
        self.name_sound = name_sound  
        # self.file_path = file_path
#викликаємо метод завантаження звуку
        self.load_sound()
        #створюємо метод для завантаження звуку з файлової системи
     def load_sound(self):
        #  #__file__ - хранит путь именно в нашем проекте , в файле котором мы его создали
        # #/.. - выход из текущего пути на один шаг назад
        sound_path = os.path.abspath(__file__ + f"/../../../sounds/{self.name_sound}")
            #завантажуємо звук по вказаному шляху
        pygame.mixer.music.load(sound_path)
              
     def play(self, loop=-1):

# Відтворення музики. Параметр loop визначає кількість повторень (-1 - безперервно).

        pygame.mixer.music.play(loop)
        self.is_paused = False

     def pause(self):
# Пауза музики.
        if not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True

     def unpause(self):
# Продовження відтворення з паузи.
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False

     def stop(self):
# Зупинка музики.
        pygame.mixer.music.stop()
        self.is_paused = False
music_load_main = MusicPlayer(name_sound= "main_screen_music.mp3")
music_load_waiting = MusicPlayer(name_sound="waiting.mp3")

```
<a name="game package"><h2>Game package</h2></a>


