import socket



def connect_user():
    with socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) as client_socket:
        client_socket.connect(("192.168.0.4", 6060))
        client_socket.send("-_-".encode())
    


    

    
    