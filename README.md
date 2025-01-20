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
