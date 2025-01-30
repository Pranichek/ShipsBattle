import pygame
from ..classes import Button
from..classes.class_click import all_sounds
pygame.init()

save_data_loud = [1]
def turn_off_volume_func():
    pygame.mixer.music.set_volume(0)
    for sound_effects in all_sounds:
        sound_effects.set_volume(pygame.mixer.music.get_volume())
        save_data_loud[0] = pygame.mixer.music.get_volume()

off_sound_button = Button(
    x = 205, 
    y = 14, 
    width = 74, 
    height = 71, 
    image_hover_path = "off_music.png", 
    image_path = "off_music_hover.png", 
    action = turn_off_volume_func
    )