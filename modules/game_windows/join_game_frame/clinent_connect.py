from ...classes.class_input_text import input_ip_adress , input_port, input_nick, input_password
from ...classes.class_image import DrawImage
from ...classes.class_click import music_click
from ...client import connect_to_game , list_check_connection, list_users, check_start_connect



#фон коли користувач пробує підключитися до серверу якого немає
fail_connect = DrawImage(width = 901 , height = 283 , x_cor = 180 , y_cor = 273 , folder_name = "backgrounds" , image_name = "fail_background.png")

def connect_to_server():
   #запускаємо звук кліку кнопки
    music_click.play2(0)
    # розділяем нашь айпі на числа , тобо якщо воно було таке 192.168.0.1 то стане таким 192 168 0 1
    # це для того щоб можна було перевірити кожне число окремо
    ip_address = input_ip_adress.user_text.split(".")
    
            
    # якщо цих чисел не 4 , то користувач не правильно увів дані 
    if len(ip_address) != 4:
        list_check_connection[0] = "error_connection"
        print("зашло")
        if fail_connect.visible == False:
            fail_connect.visible = True
            print("error_connection")
        # return False - означає що сталася помилка ,та код не буде далі рухатися
        return False
        # return False - означає що сталася помилка ,та код не буде далі рухатися
    if input_password.user_text == "password" or input_password.user_text == "" or  input_password.user_text == " " or input_nick.user_text == "" or input_nick.user_text == "nickname":
            list_check_connection[0] = "error_connection"
            print("зашло")
            if fail_connect.visible == False:
                fail_connect.visible = True
                print("error_connection")
            # return False - означає що сталася помилка ,та код не буде далі рухатися
            return False
    else:
        if input_nick.user_text in list_users:
            if list_users[input_nick.user_text]["password"] == "password":
                list_check_connection[0] = "error_connection"
                print("зашло")
                if fail_connect.visible == False:
                    fail_connect.visible = True
                    print("error_connection")
                # return False - означає що сталася помилка ,та код не буде далі рухатися
                return False
            if list_users[input_nick.user_text]["password"] == input_password.user_text:
                print("пароль подтвердил")
            if list_users[input_nick.user_text]["password"] != input_password.user_text:
                list_check_connection[0] = "error_connection"
                print("зашло")
                if fail_connect.visible == False:
                    fail_connect.visible = True
                    print("error_connection")
                # return False - означає що сталася помилка ,та код не буде далі рухатися
                return False
        
        elif input_nick.user_text not in list_users:
            print("первая игра")
    
        # перевіряємо чи кожне число в межах допустимого діапазону
        for number in ip_address:
            # перевіряємо чи це взагалі числа а не наприклад літери
            if not number.isdigit():
                # якшо це не цифри, то передаємо у список повідомлення про помилку шоб можна було вивести на екрані вікно помилки
                list_check_connection[0] = "error_connection"
                print("зашло")
                if fail_connect.visible == False:
                    fail_connect.visible = True
                    print("error_connection")
                # return False - означає що сталася помилка ,та код не буде далі рухатися
                return False
            # якщо користувач увів числа але вони не підходять під рамки для нормального айпі, то виводимо окно про помилку
            if not 0 <= int(number) <= 255:
                list_check_connection[0] = "error_connection"
                print("зашло")
                if fail_connect.visible == False:
                    fail_connect.visible = True
                    print("error_connection")
                # return False - означає що сталася помилка ,та код не буде далі рухатися
                return False
        try:
            # тепер перівіряємо на правильність порт 
            port = int(input_port.user_text)
            #  якщо користувач увів нічого або лише тільки одну цифру то виводимо окно с помилкою
            if len(ip_address) <= 1:
                    list_check_connection[0] = "error_connection"
                    print("зашло")
                    if fail_connect.visible == False:
                        fail_connect.visible = True
                        print("error_connection")
                    # return False - означає що сталася помилка ,та код не буде далі рухатися
                    return False
            # якщо порт не підходить під рамки, то виводимо окно с помилкою
            elif not 1240 < port < 65553:
                list_check_connection[0] = "error_connection"
                print("зашло")
                if fail_connect.visible == False:
                    fail_connect.visible = True
                    print("error_connection")
                # return False - означає що сталася помилка ,та код не буде далі рухатися
                return False
        except ValueError:
            #  якщо порт взагалі не цифри то також виводимо окно із помилкою
            list_check_connection[0] = "error_connection"
            print("зашло")
            if fail_connect.visible == False:
                fail_connect.visible = True
                print("error_connection")
            # return False - означає що сталася помилка ,та код не буде далі рухатися
            return False
        # якщо усі перевірки пройдені і користувач вперше натиснув на цю кнопку то запускаємо підключення до серверу
        # if event_connect_to_server.is_set():
        if check_start_connect[0] == False:
            check_start_connect[1] = True
            connect_to_game.start()
        else:
            check_start_connect[1] = True
            pass
        # якщо усі перевікри пройдені але це не перший запуск, наприклад перший раз увів айди сервера якого ще немає, а тепер такий сервер є 
        # то передаємо у  event_connect_to_server значення True за допомогою .set()
