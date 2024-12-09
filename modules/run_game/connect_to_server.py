from ..classes.class_input_text import input_ip_adress , input_port
from..classes.class_image import DrawImage
from ..classes.class_click import music_click
from ..client import thread_connect , event_connect_to_server , list_check_connection


#фон коли користувач пробує підключитися до серверу якого немає
fail_connect = DrawImage(width = 901 , height = 283 , x_cor = 180 , y_cor = 273 , folder_name = "backgrounds" , image_name = "fail_background.png")

def connect_to_server():
    #запускаємо звук кліку кнопки
    music_click.play2(0)
    # розділяем нашь айпі на числа , тобо якщо воно було таке 192.168.0.1 то стане таким 192 168 0 1
    # це для того щоб можна було перевірити кожне число окремо
    ip_address = input_ip_adress.user_text.split(".")
    # якщо воно має більше чисел ніж 4 або менш ніж 4 чисел, то такий айпі не є вірним , і виводимо помилку
    if len(ip_address) != 4:
        list_check_connection[0] = "error_connection"
        print("зашло")
        if fail_connect.visible == False:
            fail_connect.visible = True
            print("error_connection")
        # return False - означає що сталася помилка ,та код не буде далі рухатися
        return False
    
    # перевіряємо чи кожне число в межах допустимого діапазону
    for number in ip_address:
        # перевіряємо чи це взагалі числа а не наприклад літери
        if not number.isdigit():
            # якшо це не цифри, то передаємо у список повідомлення про помилку шоб можна було вивести на екрані вікно помилки
            list_check_connection[0] = "error_server"
            print("зашло")
            # якщо вже було це вікно , то робимо його видимим 
            if fail_connect.visible == False:
                fail_connect.visible = True
                print("error_server")
            # return False - означає що сталася помилка ,та код не буде далі рухатися
            return False
        # якщо айпі не підходить у рамки нормальних значеннь виводимо помулку
        if not 0 <= int(number) <= 255:
            list_check_connection[0] = "error_connection"
            print("зашло")
            if fail_connect.visible == False:
                fail_connect.visible = True
                print("error_connection")
            # return False - означає що сталася помилка ,та код не буде далі рухатися
            return False
    try:
        #  тепер первіряємо порт на правильність написання
        port = int(input_port.user_text)
        # якщо користувач взагалі не увів цифр або тільки одну то виводимо помилку за допомогою передавання про помилку у список
        if len(ip_address) <= 1:
                list_check_connection[0] = "error_connection"
                print("зашло")
                if fail_connect.visible == False:
                    fail_connect.visible = True
                    print("error_connection")
                # return False - означає що сталася помилка ,та код не буде далі рухатися
                return False
        # якщо користувач увів порт який не підходить у рамки портів то виводимо помилку за допомогою передавання про помилку у список
        elif not 1240 < port < 65553:
            list_check_connection[0] = "error_connection"
            print("зашло")
            if fail_connect.visible == False:
                fail_connect.visible = True
                print("error_connection")
            # return False - означає що сталася помилка ,та код не буде далі рухатися
            return False
    except ValueError:
        # якщо порт взагалі не цифра , то  виводимо помилку за допомогою передавання про помилку у список
        list_check_connection[0] = "error_connection"
        print("зашло")
        if fail_connect.visible == False:
            fail_connect.visible = True
            print("error_server")
        # return False - означає що сталася помилка ,та код не буде далі рухатися
        return False
    # якщо усі перевірки пройдені і користувач вперше натиснув на цю кнопку то запускаємо підключення до серверу
    # if event_connect_to_server.is_set():
    thread_connect.start()
    # якщо усі перевікри пройдені але це не перший запуск, наприклад перший раз увів айди сервера якого ще немає, а тепер такий сервер є 
    # то передаємо у  event_connect_to_server значення True за допомогою .set()
    # else:
    #     event_connect_to_server.set()