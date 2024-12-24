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
        -  [__init__.py of package screens](#screens_init)
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

<a name="game_init"><h2>game_init</h2></a>
Цей файл ініціалізує всі модулі, функції, класи та змінні з пакету game package.
Зручно,для отримання доступу до всіх елементів пакета.
<details>
<summary>English version</summary>
This file initializes all modules, functions, classes and variables from the game package.
Convenient for accessing all elements of the package.
</details>

```python
#імпортуємо весь вміст файлу input_text.py доступним для іншиї файів, щоб могли імпортувати не вводячи увесь шлях
from .input_text import *
```

<a name="input_text"><h2>input_text</h2></a>
Файл для відображення вводу тексту, функції для вводу та перевірка введених символів користувачем, якщо знак буде некорректим, то він не буде відображатись.

<details>
<summary>English version</summary>
A file for displaying text input, functions for input and checking the characters entered by the user; if the character is incorrect, it will not be displayed.
</details>

```python
import pygame
#імопртуємо функцію запису інформації у джейсон файл, та словарь із користувачами
from ..json_functions import dump_json , list_users
import os


#іницілізація Pygame
pygame.init()
#path - шлях
#abspath - абсолютний шлях

path_to_font = os.path.abspath(__file__  +  f"/../../../fonts/Jersey15.ttf")

print(path_to_font)

#змінна для збереження тексту користувача, у вигляді списку
user_text = [""]
#створення тектсовго поля , та надаємо налаштування шрифта
font = pygame.font.Font(path_to_font ,size = 48)
#робимо рамку для нашого тексту
text_box = pygame.Rect(467 , 518, 346 , 68)
#змінна у вигляді списку, щоб відстежувати чи активне зараз поля для введення тексту
check_type = [False]
#колір рамки
color = pygame.Color("black")


#функція вводу тексту на екрані
def input_texts(screen_name):
    for event in pygame.event.get():
        #Перевіряємо, чи була натиснута кнопка миші
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Перевіряємо, чи курсор миші знаходиться в межах текстового поля
            if text_box.collidepoint(event.pos):
                # Якщо курсор миші знаходиться в текстовому полі, встановлюємо значення True для активності текстового поля
                check_type[0] = True
            else:
                # Якщо курсор миші поза текстовим полем, встановлюємо значення False
                check_type[0] = False

         #Перевіряємо, чи була натиснута будь-яка клавіша на клавіатурі
        if event.type == pygame.KEYDOWN:
            # Якщо клавіша натиснута, і текстове поле активно
            if check_type[0] == True:
                # Перевіряємо, чи не перевищив користувач ліміт символів у ніку
                if len(user_text[0]) < 10 or event.key == pygame.K_BACKSPACE:
                    #Якщо натиснута клавіша Backspace, видаляємо останній символ
                    if event.key == pygame.K_BACKSPACE:
                        user_text[0] = user_text[0][:-1]

                    # Якщо натиснута інша клавіша, крім Backspace
                    else:
                       # Якщо натиснута клавіша Enter, нічого не робимо, щоб не було зайвиї проміжков у ніку
                        if event.key == pygame.K_RETURN:
                            pass
                        # Інакше додаємо символ який нажатий на клавітаурі змінної де зберігається що натиснув користувач
                        else:
                            #unicode- функція яка додає символ, який ввів користувач, до змінної user_text[0]
                            user_text[0] += event.unicode
            # Якщо натиснута клавіша Enter
            if event.key == pygame.K_RETURN:
                #перевіряємо щоб був хочаб один символ у нику
                if len(user_text) > 0:
                    #перевіряємо чи такого ніку ще немає у словарюю із користувачами
                    if user_text[0] not in list_users:
                        #якщо ні, створюємо нового користувача з нулями очками
                        list_users[user_text[0]] = {"points": 0}
                        #зберігаємо інформацію у json файл
                        dump_json(filename= "data_base.json")
                    

    # Якщо текстове поле активне, очищаємо значення "nickname" у змінній user_text[0]
    if check_type[0] == True:
        if user_text[0] == "nickname":
            user_text[0] = ""
    # Якщо текстове поле неактивне, встановлюємо значення "nickname", якщо поле пусте
    elif check_type[0] == False:
        if len(user_text[0]) == 0:
            user_text[0] = "nickname"

    # Малюємо текстове поле з рамкою
    pygame.draw.rect(surface = screen_name, color = color, rect = text_box, width= 2)
     # Рендеримо введений текст білим кольором і відображаємо на екрані
     #True -  говорить за те що ми згладжуємо текст
    text = font.render(user_text[0], True , "white")
    #виводимо текст на екрані , text_box.x + 87, text_box.y + 12 - це щоб текст був по середині рамкидля тексту
    screen_name.blit(text, (text_box.x + 87, text_box.y + 12))

    #встановлюємо розмііри рамки тексту
    text_box.w = 346
    text_box.h = 68

```

<a name="json_function_description"><h2>json_function_description</h2></a>

<a name="json_functions_init"><h2>json_functions_init</h2></a>
Цей файл ініціалізує всі модулі, функції, класи та змінні з пакету json_function.
Зручно,для отримання доступу до всіх елементів пакета.
<details>
<summary>English version</summary>
This file initializes all modules, functions, classes, and variables from the json_function package.
Convenient for accessing all elements of the package.
</details>

```python
#імпортуємо весь вміст файлу write_json.py доступним для іншиї файів, щоб могли імпортувати не вводячи увесь шлях
from .write_json import *
```

<a name="read_json"><h2>read_json</h2></a>
Файл для зчитування інформації, яку ввів користувач.

<details>
<summary>English version</summary>
A file for reading information entered by the user.
</details>

```python
import json 
import os

def read_json(name_file: str):
    search_abs_path = os.path.abspath(__file__ + f"/../../../static/{name_file}")
    with open(file= search_abs_path, mode= 'r') as file_json:
        return json.load(file_json)
```

<a name="write_json"><h2>write_json</h2></a>
Файл для запису та збереження інформації, яку ввів користувач.

<details>
<summary>English version</summary>
A file for recording and storing information entered by the user.
</details>

```python
import os, json

#створюємо словарь для збереження нікнеймів та балів користувачів
list_users = {}

list_server_status = {}


#отримуємо дані з бази даних, яка знаходиться в папці static та у файлі data_base.json
with open(file = os.path.abspath(__file__ + "/../../../static/utility.json")) as file:
    #загружаємо дані з json-файла в наш словник list_users
    list_server_status = json.load(file)

#отримуємо дані з бази даних, яка знаходиться в папці static та у файлі data_base.json
with open(file = os.path.abspath(__file__ + "/../../../static/data_base.json")) as file:
    #загружаємо дані з json-файла в наш словник list_users
    list_users = json.load(file)


#функція для збереження даних  із словаря list_users у потрібний файл, у нашому випадку filename = "data_base.json"
def write_json(filename:str, object_dict: object):
    #Формуємо абсолютний шлях до файлу, який знаходиться в папці static
    path_to_file = os.path.abspath(__file__ + f"/../../../static/{filename}")
    #Відкриваємо файл у режимі запису ("w"), щоб зберегти в нього дані
    with open(path_to_file, "w") as file:
        json.dump(
            obj = object_dict,#Дані, які треба записати у нашому випадку, змінна словарь із користувачами list_users
            fp = file,#файл, куди будуть записані дані
            indent= 4, # Встановлюємо відступ у 4 пробіли для зручності читання у json файлі
            ensure_ascii= False#робимо так щоб окрім англ літер , могли записувати кирилицю
        )
```

<a name="run_game_description"><h2>run_game</h2></a>

<a name="run_game_init"><h2>run_game_init</h2></a>
Цей файл ініціалізує всі модулі, функції, класи та змінні з пакету run_game.
Зручно,для отримання доступу до всіх елементів пакета.
<details>
<summary>English version</summary>
This file initializes all modules, functions, classes, and variables from the run_game package.
Convenient for accessing all elements of the package.
</details>

```python
#імпортуємо функції запуску гри у __init__.py , щоб іх можна було використовувати у інших файлах
from .start_game import *
```
<a name="start_game"><h2>start_game</h2></a>
Цей файл містить усі зібрані функції та класи всього проєкту.
<details>
<summary>English version</summary>
This file contains all the compiled functions and classes for the entire project.
</details>

```python
#імпортуємо усі потрібні модулі
import pygame
from ..screens import main_screen , Grid , list_object_map
import modules.screens.screen as module_screen_server
from ..classes import DrawImage , Button , Font, InputText
from ..server import server_thread 
from ..client import thread_connect
from ..classes.class_input_text import input_ip_adress ,input_nick ,input_port
from ..json_functions.read_json import read_json
from ..classes.class_sounds import music_load_main , music_load_waiting
from ..classes.class_click import music_click


#ініціалізуємо pygame щоб можна було із ним працювати
pygame.init()


#fonts(text)
createbutton_font = Font(size= 48 , name_font= "Jersey15.ttf" , text= "create" , screen= main_screen , x_cor= 218, y_cor= 663)
join_game_fonts = Font(size= 48 , name_font= "Jersey15.ttf" , text= "join" , screen= main_screen , x_cor= 974 , y_cor= 663)

def test():
    print(1)

#список для проверки нажата ли кнопка
check_press_button = [None]

#список для відслуджування чи нажати кнопка заупску серверу чи ні
check_server_started = [False]
#список для відслужування чи нажата кнопка підключення до серверу чи ні
check_client_connected = [False]

def start_server():
    if check_server_started[0] == False:
        if input_port.user_text == "port" or input_ip_adress.user_text == "ip adress" or input_nick.user_text == "nick":
            print("Fill text in the input boxes")
        else:
            server_thread.start()
            check_server_started[0] = True
    elif check_server_started[0] == True:
        print("Server has been started")

def connect_to_server():
    if check_client_connected[0] == False:
        if input_port.user_text == "port" or input_ip_adress.user_text == "ip adress" or input_nick.user_text == "nick":
            print("Fill text in the input boxes")
        else:
            thread_connect.start()
            check_client_connected[0] = True
    elif check_client_connected[0] == True:
        print("You are already tried connected to the server")

def button_action():
    check_press_button[0] = "button is pressed"
    music_click.play2(0)

#функція для перезаписування яке зараз вікно активне
def change_scene(scene):
    list_current_scene[0] = scene

#ліст для зберігання яке зараз вікно активне
list_current_scene = [None]

#buttons
#кнопка кторая перекидывает на фрейм по созданию игры(запуска сервера)
create_game_frame = Button(x= 113, y = 653,image_path= "button_create.png" , image_hover_path= "create_button_hover.png" , width= 346 , height= 80 , action= button_action)
#кнопка кторая перекидывает на фрейм по присоеденению к игре(серверу)
join_game_frame = Button(x= 832 , y = 653,image_path= "join_button.png" , image_hover_path= "join_button_hover.png" , width= 346 , height= 80 , action= button_action)
#кнопка которая возвращает назад к главному окну
back_to_menu = Button(x= 33 , y = 41 ,image_path= "back_button.png" , image_hover_path= "back_button_hover.png" , width= 158 , height= 41 , action= button_action)
#кнопка которая запускает сервер(игру)
start_game_button = Button(x= 352 , y = 642,image_path= "create_game_button.png" , image_hover_path= "create_game_button_hover.png" , width= 575 , height= 80 , action= start_server)
#кнопка которая подключается к игре
join_game_button = Button(x= 352 , y = 642,image_path= "join_to_game.png" , image_hover_path= "joint_to_game_hover.png" , width= 575 , height= 80 , action= connect_to_server)
#кнопка коли розставив кораблі та підлючаєшься до бою
ready_for_battle = Button(x= 799 , y = 678,image_path= "start_battle.png" , image_hover_path= "start_battle_hover.png" , width= 408 , height= 61 , action= test)
#кнопка яка будеть розставляти кораблі у ранломному положені
random_place_ships = Button(x= 205 , y = 709,image_path= "random_place.png" , image_hover_path= "random_place_hover.png" , width= 318 , height= 48 , action= test)

#images decoration
cold_image = DrawImage(width= 152 , height= 68 , x_cor= 207 , y_cor= 716 , folder_name= "decorations" , image_name= "ice.png")
second_cold_image = DrawImage(width= 152 , height= 68 , x_cor= 940, y_cor= 716 , folder_name= "decorations" , image_name= "ice.png")
third_cold_image = DrawImage(width=  150, height= 68 , x_cor= 536 , y_cor= 705 , folder_name= "decorations" , image_name= "ice.png")
fourth_cold_image = DrawImage(width= 150, height= 68 , x_cor= 686 , y_cor= 705 , folder_name= "decorations" , image_name= "ice.png")
#image for the grid
grid_image = DrawImage(width = 600 , height = 597 , x_cor = 40 , y_cor = 89 , folder_name = "grid", image_name = "background_grid.png")

#backgrounds
main_bg = DrawImage(width = 1280,height= 832 , x_cor= 0 , y_cor= 0 ,folder_name= "images_background" , image_name= "main_background.jpg")
#фон для окон д=где вводим данные для запуска сервера и подключение к нему
input_data_bg= DrawImage(width = 1280,height= 832 , x_cor= 0 , y_cor= 0 ,folder_name= "images_background" , image_name= "input_data.png")
#фон для очікування користувача
waiting_background = DrawImage(width = 1280,height= 832 , x_cor= 0 , y_cor= 0 ,folder_name= "images_background" , image_name= "waiting_background.png")
#фон для розташування кораблів перед ігрою
ships_position_bg = DrawImage(width = 1280,height= 832 , x_cor= 0 , y_cor= 0 ,folder_name= "images_background" , image_name= "position_ships_bg.png")




#створюємо функцію, яка викликається при запуску гри для користувача який запускає сервер
def main_window():
    #викликаємо функцію для запуску серверу
    #встановлюємо назву вікна гри для сервера
    pygame.display.set_caption("BattleShips")
    #створюжмо змінну для того щоб відстежувати коли треба закривати вікно
    run_game = True
    
    music_load_main.play()

    #основний цикл роботи вікна користувача
    while run_game:
        module_screen_server.FPS.tick(60)
        main_bg.draw_image(screen= main_screen)

        cold_image.draw_image(screen= main_screen)  
        create_game_frame.draw(surface= main_screen)
        # createbutton_font.draw_font()
        
        second_cold_image.draw_image(screen= main_screen)
        join_game_frame.draw(surface= main_screen)
        # join_game_fonts.draw_font()
        # input_text.draw_text()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False  
                change_scene(None)
            elif check_press_button[0] == "button is pressed":
                music_click.play2(0)
                check_press_button[0] = None
                run_game = False
                x_pos , y_pos = pygame.mouse.get_pos()
                if x_pos > 600:
                    change_scene(join_game_window())
                elif x_pos < 600:
                    change_scene(create_game_window()) 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                create_game_frame.check_click()
                join_game_frame.check_click()
            # input_text.check_event(event)
        pygame.display.flip()
            
    

def create_game_window():
    #викликаємо функцію для запуску серверу
    #встановлюємо назву вікна гри для сервера
    pygame.display.set_caption("Create Game Window")
    #створюжмо змінну для того щоб відстежувати коли треба закривати вікно
    run_game = True
    #основний цикл роботи вікна користувача
    while run_game:
        module_screen_server.FPS.tick(60)
        input_data_bg.draw_image(screen= main_screen)
        data = read_json(name_file = "utility.json")
        status_server = data["status"]


        input_nick.draw_text()
        input_ip_adress.draw_text()
        input_port.draw_text()

        back_to_menu.draw(surface= main_screen)


        third_cold_image.draw_image(screen= main_screen)
        fourth_cold_image.draw_image(screen= main_screen)
        start_game_button.draw(surface= main_screen)

        if status_server == "wait":
                    run_game = False
                    change_scene(waiting_window())
                    check_press_button[0] = None
        #Обробляємо всі події у вікні
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False  
                change_scene(None)
            elif check_press_button[0] == "button is pressed":
                music_click.play2(0)
                check_press_button[0] = None
                input_nick.user_text =  input_nick.base_text
                input_ip_adress.user_text = input_ip_adress.base_text
                input_port.user_text = input_port.base_text
                run_game = False
                change_scene(main_window())
            elif event.type == pygame.MOUSEBUTTONDOWN:
                back_to_menu.check_click()
                start_game_button.check_click()
                
            input_nick.check_event(event)
            input_ip_adress.check_event(event)
            input_port.check_event(event)  

        #оновлюєио екран щоб можна було бачити зміни на ньому
        pygame.display.flip()



def join_game_window():
    #викликаємо функцію для запуску серверу
    #встановлюємо назву вікна гри для сервера
    pygame.display.set_caption("Join to Game Window")
    #створюжмо змінну для того щоб відстежувати коли треба закривати вікно
    run_game = True
    #основний цикл роботи вікна користувача
    while run_game:
        data = read_json(name_file = "utility.json")
        status_server = data["status"]
        module_screen_server.FPS.tick(60)
        input_data_bg.draw_image(screen= main_screen)

        input_nick.draw_text()
        input_ip_adress.draw_text()
        input_port.draw_text()

        back_to_menu.draw(surface= main_screen)


        third_cold_image.draw_image(screen= main_screen)
        fourth_cold_image.draw_image(screen= main_screen)
        join_game_button.draw(surface= main_screen)

        if status_server == "connect":
            change_scene(ships_position_window())
            check_press_button[0] = None
            run_game = False
        #Обробляємо всі події у вікні
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False  
                change_scene(None)
            elif check_press_button[0] == "button is pressed":
                music_click.play2(0)
                check_press_button[0] = None
                input_nick.user_text =  input_nick.base_text
                input_ip_adress.user_text = input_ip_adress.base_text
                input_port.user_text = input_port.base_text
                run_game = False
                change_scene(main_window())
            elif event.type == pygame.MOUSEBUTTONDOWN:
                back_to_menu.check_click()
                
                join_game_button.check_click()
               

            input_nick.check_event(event)
            input_ip_adress.check_event(event)
            input_port.check_event(event)  
            
        #оновлюєио екран щоб можна було бачити зміни на ньому
        pygame.display.flip()


def waiting_window():
    pygame.display.set_caption("Waiting window")
    run_game = True
    music_load_main.stop()
    music_load_waiting.play()
    while run_game:
        data = read_json(name_file = "utility.json")
        status_server = data["status"]
        module_screen_server.FPS.tick(60)
        waiting_background.draw_image(screen = main_screen)

        if status_server == "connect":
            change_scene(ships_position_window())
            check_press_button[0] = None
            run_game = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False  
                change_scene(None)
        
        pygame.display.flip()

def ships_position_window():
    pygame.display.set_caption("Position Ships")
    run_game = True
    # music_load_waiting.stop()
    #generate grid with class
    grid_player = Grid(x_screen = 81 , y_screen = 127)
    grid_player.generate_grid()
    while run_game:
        module_screen_server.FPS.tick(60)
        ships_position_bg.draw_image(screen = main_screen)

        #отрисовка картинки цифер и букв для поля
        grid_image.draw_image(screen = main_screen)
        #отрисовка обьектов(пустых клеток) который хранятся в списке обьектов
        for object in list_object_map:
            object.draw(screen = main_screen) 

        #draw buttons
        ready_for_battle.draw(surface= main_screen)
        random_place_ships.draw(surface= main_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False  
                change_scene(None)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                ready_for_battle.check_click()
                random_place_ships.check_click()
        
        pygame.display.flip()
        
```


<a name="screens_description"><h2>screens_description</h2></a>

<a name="screens_init"><h2>screens_init</h2></a>
Цей файл ініціалізує всі модулі, функції, класи та змінні з пакету screens.
Зручно,для отримання доступу до всіх елементів пакета.
<details>
<summary>English version</summary>
This file initializes all modules, functions, classes and variables from the screens package.
Convenient for accessing all elements of the package.
</details>

```python
# Імпортуємо основний екран сервера з модуля server_screen
from .screen import main_screen
from .create_grid import *
from .list_grid import *


#файл __init__.py робить доступними для імпорту об’єкти screen, screen_user, і Button з відповідних файлів(модулів), щоб можна було використовувати їх у інших частинах проєкту.
```
<a name="create_grid"><h2>create_grid</h2></a>
Файл, який містить класи та функції для відображення поля гри.
<details>
<summary>English version</summary>
A file that contains classes and functions for displaying the game field.
</details>

```python
import os
import pygame
from .list_grid import list_grid


#класс для создания одной пустой клетки 
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
        image_path = os.path.abspath(__file__ + f"/../../../images/grid/{self.image_name}")
        image = pygame.image.load(image_path)
        transformed_image = pygame.transform.scale(image, (self.width, self.height))
        self.image = transformed_image
    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, (self.x, self.y))


#список для хранения объектов клеток сетки
list_object_map = []


#класс для создания сетки
class Grid:
    def __init__(self , x_screen: int , y_screen: int):
        self.X_SCREEN = x_screen
        self.Y_SCREEN = y_screen
    def generate_grid(self):
        x_screen , y_screen = self.X_SCREEN , self.Y_SCREEN
        for row in list_grid:
            for cell in row:
                if cell == "c":
                    empty_cell = Cell(x = x_screen , y = y_screen ,width = 62 , height = 62 , image_name = "empty_cell.png")
                    list_object_map.append(empty_cell)
                x_screen += 62
            y_screen += 62
            x_screen = 80
    
```
<a name="list_grid"><h2>list_grid</h2></a>
Матриця для кораблів. За допомогою неї, ми згодом бачим де стоїть корабель, в який корабель попали та де промах.
<details>
<summary>English version</summary>
A matrix for ships. With its help, we later see where the ship is, which ship we hit, and where we missed.
</details>

```python
list_grid = [
    ['c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c'],
    ['c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c'],
    ['c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c'],
    ['c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c'],
    ['c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c'],
    ['c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c'],
    ['c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c'],
    ['c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c'],
    ['c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c' , 'c']
]

#c - cell(пуста клітинка)
```
<a name="screen"><h2>screen</h2></a>
Файл, в якому задаємо розміри усіх екранів для гри.
<details>
<summary>English version</summary>
A file in which we specify the sizes of all screens for the game.
</details>

```python
import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 832

FPS = pygame.time.Clock()
#створюємо екран для користувача який запускає сервер, та встановлюємо для цього екрану розміри
main_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
```

<a name="static"><h2>static</h2></a>

<a name="data_base"><h2>data_base</h2></a>
Файл, в якому записуються та зберігаються бали гравців впродовж гри.
<details>
<summary>English version</summary>
A file that records and stores player scores throughout a game. Приклад бачимо нижче
</details>

```python
{
    "vova": {
        "points": 0
    },
    "katya": {
        "points": 0
    },
    "ura": {
        "points": 0
    },
    "nickname": {
        "points": 0
    },
    "krivopopka": {
        "points": 0
    },
    "katuha": {
        "points": 0
    },
    "�����ghj": {
        "points": 0
    },
    "fghjkm": {
        "points": 0
    },
    "fghu": {
        "points": 0
    },
    "dvc": {
        "points": 0
    },
    "gjkbn": {
        "points": 0
    },
    "jnfknbdj": {
        "points": 0
    },
    "jhngek": {
        "points": 0
    },
    "dfghj": {
        "points": 0
    },
    "bhjjk": {
        "points": 0
    }
}
```

<a name="utility"><h2>utility</h2></a>
Файл, в якому записується статус для потоків, тобто під час запуску гри статус змінюється, після чого, також змінюється екран на наступний фрейм. 
<details>
<summary>English version</summary>
A file that records the status for streams, i.e. when the game starts, the status changes, after which the screen also changes to the next frame.
</details>

```python
{
    "status": "wait"
}
```

<a name="main"><h2>main</h2></a>
Файл, в якому імпортуються усі файли та ми можемо запустити гру.
<details>
<summary>English version</summary>
The file in which all files are imported and we can run the game.
</details>

```python
import modules
import pygame
import sys

if __name__ == '__main__':
    modules.change_scene(modules.main_window)#передаем функцию отображения первого окна
    while modules.list_current_scene[0] is not None:
        modules.list_current_scene[0]()#вызываем функцию которая тут запущена

pygame.quit()
sys.exit()
```
<a name="prbl_project"><h2>Problems during development</h2></a>
Під час написання коду, ми зіштовхнулись з жеякими труднощами. Наприклад ми не можемо ще раз запускати сервер, якщо його вже запустили, на жаль цю проблему ми не змогли вирішити, але це в перспективі. Найголовнішою нашою проблемою стало розташування кораблів, складно було зробити так, щоб не можна було ставити корабель один на інший, також треба було зробити так, щоб користувач міг ставити корабель лише через одну клітинку, як зазначено в правилах гри. Після розстановки кораблів, багато часу зайняла передача кораблів з client на server та з server на client. Наразі ці проблеми вирішено. 
Також в майбутньмоу можливо додавання кнопки відміни запуску серверу, додання деяких анімацій, а також гра з розширеною версією.
<details>
<summary>English version</summary>
While writing the code, we encountered some difficulties. For example, we cannot restart the server if it has already been started, unfortunately we could not solve this problem, but it is in the future. Our main problem was the location of the ships, it was difficult to make it so that it was not possible to place a ship on top of another, it was also necessary to make it so that the user could place a ship only through one cell, as specified in the game rules. After placing the ships, it took a lot of time to transfer the ships from client to server and from server to client. These problems have now been solved.
Also in the future it is possible to add a button to cancel the server launch, add some animations, and also play with an extended version.
</details>


<a name="conclusions"><h2>Conclusion</h2></a>
Підведемо підсумки, під час створення цього проєкту, ми навчились з'єднувати двух користувачів за допомогою ip-адреси, покращили свої навички роботи з pygame, навчилися працювати з потоками, а також отримали досвід працювати в команді.
<details>
<summary>English version</summary>
To summarize, while creating this project, we learned how to connect two users using an IP address, improved our skills with pygame, learned how to work with streams, and also gained experience working in a team.
</details>
