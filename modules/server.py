import socket


def start_server():
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as server_socket:
        
        server_socket.bind(("0.0.0.0", 6060))
        server_socket.listen()
        print("connecting")
        client_soket, adress = server_socket.accept()
        
        print("connected: ", adress)
        response_data = client_soket.recv(1240).decode()
        print(response_data)

 
