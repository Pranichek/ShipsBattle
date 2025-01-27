import pygame
from ..classes import Button
from ..classes.class_click import all_sounds
from .turn_off_volume import save_data_volume

pygame.init()

def volume_down_func():
    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.05)
    if pygame.mixer.music.get_volume() < 0.1:
        save_data_volume[0] = 0
        pygame.mixer.music.set_volume(0)
    for sound_effects in all_sounds:
        sound_effects.set_volume(pygame.mixer.music.get_volume())
        save_data_volume[0] = pygame.mixer.music.get_volume()
    

volume_down_button = Button(
    x = 113, 
    y = 14, 
    width = 74, 
    height = 71, 
    image_hover_path = "button_music_lower_hover.png", 
    image_path = "button_music_lower.png", 
    action = volume_down_func
    )