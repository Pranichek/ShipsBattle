import socket 
import colorama
import random
# Импортируем классы
from threading import Thread


# функция для болной загрузки данных
def recv_all(sock):
    data = b""
    while True:
        part = sock.recv(1024)  # Получаем данные порциями
        if not part:
            break
        data += part
    return data




enemy_data = [""]
#где стоят корабли соперника
enemy_ships = []
# для восстановления клеточки
number_list = [100]
row_list = [100]
col_list = [100]
check_send_data_health = [0]
# список для того чтобы мы получили матрицу соперника только один раз
check_repeat = [0]
# список для проверки перехода на фрейм боя
list_check_ready_to_fight = [None]
# лист очереди
turn = ["server_turn", False]
# лист таймер времени
check_time = [0]
# Лист для проверки за кого мы играем(сервер или клиент)
list_player_role = [""]
# список куда сохраняем кто выиграл
list_check_win = [None]
# сохраняем где отрисовываем анимацию зачеркания когда мы убили корабль
enemy_animation_miss_coord = []
# список где сохраняем баланс врага
enemy_balance = [0]
# сохраняем координаты вражеских медалей
save_medals_coordinates = []
# список в котором храним какие корабли убили у игрока
player_died_ships = []
# список в коотором храним какие корабли убил игрок у врага
enemy_died_ships = []
#------------------------------------------------------------------------------------------------
flag_bomb_animation = [False]
#------------------------------------------------------------------------------------------------
# флаг в котором храним все ли впорядке с связью между игроками
check_connection = [True]


def listen_client(client, second_client):
    while SERVER.run == True:
        try:
            # if SERVER.clients > 1:
            #     client.settimeout(5)
            data = client.recv(1024)
            if data:
                second_client.sendall(data)
        except ConnectionResetError:
            SERVER.RESTART = True
            SERVER.clients = 0
            break
        except Exception as error:
            SERVER.RESTART = True
            SERVER.clients = 0
            break


players = ["server_player", "client_player"]
class Server():
    def __init__(self):
        self.RESTART = False
        self.START_CONNECT = False
        self.clients = 0
        self.PORT = 0
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.run = True

    def start_server(self, ip_adress: str, port: int):
        self.PORT = int(port) 
        while self.run == True:
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
                    self.clients = 0
                    self.clients += 1

                    thread2 = Thread(target = listen_client, args = (client_socket_second, client_socket))
                    thread2.start()
                    self.clients += 1

                    thread1.join()
                    thread2.join()
                    print("Congratulations")
                    self.PORT += 1
                if self.RESTART:
                    self.RESTART = False
                    continue
            except Exception as error:
                pass
        # self.server_socket.close()
        # self.PORT = 0
        # self.RESTART = False
        # self.START_CONNECT = False
        # self.clients = 0
        # print("Server cloesed")
        # print(f"{colorama.Fore.RED} SERVER CLOSED {colorama.Style.RESET_ALL}")

SERVER = Server()



def run_server(input_ip_address, input_port):
    SERVER.start_server(input_ip_address, input_port)

