from ...classes.class_click import music_click
from ...classes.class_input_text import input_port, input_ip_adress
from ...classes.class_image import DrawImage
from threading import Thread
from ...server import run_server

#список для відслуджування чи нажати кнопка заупску серверу чи ні
check_server_started = [False]
#фон який говорить про помилку, коли користувач пробує запистити сервер, але він це робить не правильно
fail_start_server = DrawImage(width = 901 , height = 283 , x_cor = 180 , y_cor = 273 , folder_name = "backgrounds" , image_name = "fail_server.png")


def start_server():
   #запускаємо звук кліку кнопки
    music_click.play2(0)
    # розділяем нашь айпі на числа , тобо якщо воно було таке 192.168.0.1 то стане таким 192 168 0 1
    # це для того щоб можна було перевірити кожне число окремо
    ip_address = input_ip_adress.user_text.split(".")            
    #якщо цих чисел не 4 , то користувач не правильно увів дані 
    if len(ip_address) != 4:
        # передаємо у список повідомлення про помилку шоб можна було вивести на екрані вікно помилки
        check_server_started[0] = "error_server"
        # якщо вже було це вікно , то робимо його видимим 
        if fail_start_server.visible == False:
            fail_start_server.visible = True
            print("error_server")
            return False
        # перевіряємо чи кожне число в межах допустимого діапазону
        for number in ip_address:
            # перевіряємо чи це взагалі числа а не наприклад літери
            if not number.isdigit():
                # якшо це не цифри, то передаємо у список повідомлення про помилку шоб можна було вивести на екрані вікно помилки
                check_server_started[0] = "error_server"
                print("зашло")
                # якщо вже було це вікно , то робимо його видимим 
                if fail_start_server.visible == False:
                    fail_start_server.visible = True
                    print("error_server")
                # return False - означає що сталася помилка ,та код не буде далі рухатися
                return False
            # якщо користувач увів числа але вони не підходять під рамки для нормального айпі, то виводимо окно про помилку
            if not 0 <= int(number) <= 255:
                check_server_started[0] = "error_server"
                print("зашло")
                if fail_start_server.visible == False:
                    fail_start_server.visible = True
                    print("error_server")
                # return False - означає що сталася помилка ,та код не буде далі рухатися
                return False
        try:
            # тепер перівіряємо на правильність порт 
            port = int(input_port.user_text)
            #  якщо користувач увів нічого або лише тільки одну цифру то виводимо окно с помилкою
            if len(ip_address) <= 1:
                    check_server_started[0] = "error_server"
                    print("зашло")
                    if fail_start_server.visible == False:
                        fail_start_server.visible = True
                        print("error_server")
                    # return False - означає що сталася помилка ,та код не буде далі рухатися
                    return False
            # якщо порт не підходить під рамки, то виводимо окно с помилкою
            elif not 1240 < port < 65553:
                check_server_started[0] = "error_server"
                print("зашло")
                if fail_start_server.visible == False:
                    fail_start_server.visible = True
                    print("error_server")
                # return False - означає що сталася помилка ,та код не буде далі рухатися
                return False
        except ValueError:
            #  якщо порт взагалі не цифри то також виводимо окно із помилкою
            check_server_started[0] = "error_server"
            print("зашло")
            if fail_start_server.visible == False:
                fail_start_server.visible = True
                print("error_server")
            # return False - означає що сталася помилка ,та код не буде далі рухатися
            return False
    print(113)
    server_thread = Thread(target=run_server, args=(str(input_ip_adress.user_text), (input_port.user_text)), daemon = True)
    server_thread.start()