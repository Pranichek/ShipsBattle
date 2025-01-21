import pygame
from ..classes import Button, all_sounds
pygame.init()

def volume_up_func():
    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.05)
    if pygame.mixer.music.get_volume() > 0.99:
        pygame.mixer.music.set_volume(1)
    for sound_effects in all_sounds:
        sound_effects.set_volume(pygame.mixer.music.get_volume())


volume_up_button = Button(
    x = 21, 
    y = 14, 
    width = 74, 
    height = 71, 
    image_hover_path = "button_volue_up_hover.png", 
    image_path = "button_volue_up.png", 
    action = volume_up_func
    )