import customtkinter as ctk

def user_screen():
    user_screen = ctk.CTk(fg_color = "Red")
    user_screen.title("User")
    WIDTH = 1920
    HEIGHT = 832
    user_screen.geometry(f"{WIDTH}x{HEIGHT}")