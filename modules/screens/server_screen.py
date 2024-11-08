import customtkinter as ctk

def server_screen():
    server_screen = ctk.CTk(fg_color = "Blue")
    server_screen.title("Server")
    WIDTH = 1920
    HEIGHT = 832
    server_screen.geometry(f"{WIDTH}x{HEIGHT}")