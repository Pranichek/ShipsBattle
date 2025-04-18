from ...classes.class_click import music_click
from ...classes.class_input_text import input_port, input_ip_adress, input_nick, input_password
from ...classes.class_image import DrawImage
from threading import Thread
from ...server import run_server, SERVER
from ...client import start_client, check_start_connect
from ...json_functions import list_users, write_json

#список для відслуджування чи нажати кнопка заупску серверу чи ні
check_server_started = [False]
#фон який говорить про помилку, коли користувач пробує запистити сервер, але він це робить не правильно
fail_start_server = DrawImage(width = 901 , height = 283 , x_cor = 180 , y_cor = 273 , folder_name = "backgrounds" , image_name = "fail_server.png")

list_serv = [False]
count_music = [False]
def start_server():
   #запускаємо звук кліку кнопки
    music_click.play2(0)
    # розділяем нашь айпі на числа , тобо якщо воно було таке 192.168.0.1 то стане таким 192 168 0 1
    # це для того щоб можна було перевірити кожне число окремо
    ip_address = input_ip_adress.user_text.split(".")            
    #якщо цих чисел не 4 , то користувач не правильно увів дані 
    if len(ip_address) != 4:
        list_serv[0] = False
        # передаємо у список повідомлення про помилку шоб можна було вивести на екрані вікно помилки
        check_server_started[0] = "error_server"
        # якщо вже було це вікно , то робимо його видимим 
        if fail_start_server.check_show == False:
            fail_start_server.check_show = True
            print("error_server")
            return False
        
    if input_password.user_text == "password" or input_password.user_text == "" or  input_password.user_text == " " or input_nick.user_text == "" or input_nick.user_text == "nickname":
        check_server_started[0] = "error_server"
        list_serv[0] = False
        if fail_start_server.check_show == False:
            fail_start_server.check_show = True
            print("error_connection")
        # return False - означає що сталася помилка ,та код не буде далі рухатися
        return False
    
    if input_nick.user_text in list_users:
        if list_users[input_nick.user_text]["password"] == "password":
            check_server_started[0] = "error_server"
            list_serv[0] = False
            if fail_start_server.check_show == False:
                fail_start_server.check_show = True
                print("error_connection")
            # return False - означає що сталася помилка ,та код не буде далі рухатися
            return False
        if list_users[input_nick.user_text]["password"] != input_password.user_text:
            check_server_started[0] = "error_server"
            list_serv[0] = False
            if fail_start_server.check_show == False:
                fail_start_server.check_show = True
                print("error_connection")
            # return False - означає що сталася помилка ,та код не буде далі рухатися
            return False
    
    # перевіряємо чи кожне число в межах допустимого діапазону
    for number in ip_address:
        # перевіряємо чи це взагалі числа а не наприклад літери
        if not number.isdigit():
            # якшо це не цифри, то передаємо у список повідомлення про помилку шоб можна було вивести на екрані вікно помилки
            check_server_started[0] = "error_server"
            list_serv[0] = False
            # якщо вже було це вікно , то робимо його видимим 
            if fail_start_server.check_show == False:
                fail_start_server.check_show = True
                print("error_server")
            # return False - означає що сталася помилка ,та код не буде далі рухатися
            return False
        # якщо користувач увів числа але вони не підходять під рамки для нормального айпі, то виводимо окно про помилку
        if int(number) >= 255 or int(number) < 0:
            check_server_started[0] = "error_server"
            list_serv[0] = False
            if fail_start_server.check_show == False:
                fail_start_server.check_show = True
                print("error_server")
            # return False - означає що сталася помилка ,та код не буде далі рухатися
            return False
    try:
        # тепер перівіряємо на правильність порт 
        port = int(input_port.user_text)
        #  якщо користувач увів нічого або лише тільки одну цифру то виводимо окно с помилкою
        if len(ip_address) <= 1:
                check_server_started[0] = "error_server"
                list_serv[0] = False
                if fail_start_server.check_show == False:
                    fail_start_server.check_show = True
                    print("error_server")
                # return False - означає що сталася помилка ,та код не буде далі рухатися
                return False
        # якщо порт не підходить під рамки, то виводимо окно с помилкою
        if port > 65553 or port < 1240:
            check_server_started[0] = "error_server"
            print("ERROR PORT")
            list_serv[0] = False
            if fail_start_server.check_show == False:
                fail_start_server.check_show = True
                print("error_server")
            # return False - означає що сталася помилка ,та код не буде далі рухатися
            return False
    except ValueError:
        #  якщо порт взагалі не цифри то також виводимо окно із помилкою
        check_server_started[0] = "error_server"
        list_serv[0] = False
        if fail_start_server.check_show == False:
            fail_start_server.check_show = True
            print("error_server")
        # return False - означає що сталася помилка ,та код не буде далі рухатися
        return False
    list_serv[0] = True
    count_music[0] = True
    if int(input_port.user_text) != SERVER.PORT:
        SERVER.run = True
        if input_nick.user_text not in list_users:
            #создаем игрока с его ником и даем базовое количество баллов
            list_users[input_nick.user_text] = {
                "points": 0,
                "password": input_password.user_text
            }
            #зберігаємо інформацію у json файл
            write_json(filename = "data_base.json" , object_dict = list_users)
        server_thread = Thread(target = run_server, args=(str(input_ip_adress.user_text), (input_port.user_text)), daemon = True)
        server_thread.start()
        check_start_connect[1] = True
        check_start_connect[2] = True
        connect_to_game = Thread(target = start_client, daemon = True)
        connect_to_game.start()

