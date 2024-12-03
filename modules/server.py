import pygame
import socket
import threading
import json
from .classes.class_input_text import input_port, input_ip_adress, input_nick
from .json_functions.write_json import write_json, list_server_status, list_users
from .json_functions.read_json import read_json

# Ліст для перевірки чи зайшов користувач на сервер
list_server_status = {"status": None}
write_json(filename="utility.json", object_dict=list_server_status)

# Подія для зупинки сервера
stop_event = threading.Event()

# Функція для запуску сервера
def start_server():
    if input_nick.user_text not in list_users:
        list_users[input_nick.user_text] = {"points": 0}
        write_json(filename="data_base.json", object_dict=list_users)

    ip_address = input_ip_adress.user_text
    port = int(input_port.user_text)

    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as server_socket:
        server_socket.bind((ip_address, port))
        server_socket.listen()
        print("Server is waiting for a connection...")
        list_server_status["status"] = "wait"
        write_json(filename="utility.json", object_dict=list_server_status)

        while not stop_event.is_set():
            server_socket.settimeout(1.0)
            try:
                client_socket, address = server_socket.accept()
                break
            except socket.timeout:
                continue

        if stop_event.is_set():
            print("Server was canceled.")
            list_server_status["status"] = "canceled"
            write_json(filename="utility.json", object_dict=list_server_status)
            return

        print(f"Connection established with {address}.")
        list_server_status["status"] = "connect"
        write_json(filename="utility.json", object_dict=list_server_status)

        with client_socket:
            response_data = client_socket.recv(1024).decode()
            data_in_list = json.loads(response_data)
            if data_in_list["nick"] not in list_users:
                list_users[data_in_list["nick"]] = {"points": data_in_list["points"]}
            else:
                list_users[data_in_list["nick"]]["points"] = data_in_list["points"]
            write_json(filename="data_base.json", object_dict=list_users)

            points_for_client = list_users[input_nick.user_text]["points"]
            data_for_client = {
                "nick": input_nick.user_text,
                "points": points_for_client,
                "status": list_server_status,
            }
            client_socket.send(json.dumps(data_for_client).encode())

# Функція для скасування сервера
def cancel_server():
    stop_event.set()
    print("Canceling the server...")

# Функція для запуску потоку сервера
def start_server_thread():
    global server_thread
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

# Інтерфейс з використанням Pygame
def pygame_interface():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Server Control")
    font = pygame.font.Font(None, 36)

    # Кнопка отмены
    button_color = (200, 0, 0)
    button_rect = pygame.Rect(100, 100, 200, 50)
    button_text = font.render("Cancel Server", True, (255, 255, 255))

    running = True
    while running:
        screen.fill((30, 30, 30))
        pygame.draw.rect(screen, button_color, button_rect)
        screen.blit(button_text, (button_rect.x + 20, button_rect.y + 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                cancel_server()  # Отмена сервера при выходе
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    cancel_server()  # Отмена сервера по нажатию кнопки

        pygame.display.flip()

    pygame.quit()

# Запуск сервера и интерфейса
start_server_thread()  # Запускаем сервер в отдельном потоке
pygame_interface()  # Запускаем интерфейс
