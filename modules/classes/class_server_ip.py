import pygame
import socket
from os.path import abspath, join
from .class_text import Font
from .class_input_text import input_ip_adress

def get_local_ip():
    try:
        # Попробовать получить IPv4
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        ip = sock.getsockname()[0]
        sock.close()
    except OSError:
        # Если IPv4 недоступен пробуем IPv6
        sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
        sock.connect(("2001:4860:4860::8888", 80)) 
        ip = sock.getsockname()[0]
        sock.close()
    return ip
    
    
class ServerIp:
    def __init__(self):
        pass
    def change_to_wan_ip(self):
        input_ip_adress.user_text = "0.0.0.0"
    def change_to_local_ip(self):
        user_local_ip = get_local_ip()
        input_ip_adress.user_text = user_local_ip

sdckn = ServerIp()