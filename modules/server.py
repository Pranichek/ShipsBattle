import socket
import threading

# Створюємо об'єкт Event для управління завершенням потоку
event_thread = threading.Event()

# Функція для запуску сервера
def start_server():
    # Цикл, який працює, поки подія не буде встановлена
    while not event_thread.is_set():
        # Створюємо сокет з використанням протоколу IPv4 (AF_INET) та TCP (SOCK_STREAM)
        with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as server_socket:
            # Прив'язуємо сокет до порту 7322
            server_socket.bind(("0.0.0.0", 7322))
            # Ставимо сервер у режим очікування підключень
            server_socket.listen()
            print("Сервер запущено, чекаємо підключень...")
            # Приймаємо підключення від клієнта
            client_socket, address = server_socket.accept()
            print("Підключено: ", address)
            # Отримуємо дані від клієнта (максимум 1240 байт) і декодуємо їх у текст
            response_data = client_socket.recv(1240).decode()
            print("Отримані дані: ", response_data)

# Створюємо потік для запуску сервера
server_thread = threading.Thread(target=start_server)
server_thread.start()

# Для завершення роботи сервера, можна викликати:
# event_thread.set()  # Це встановить подію, і сервер завершить роботу
