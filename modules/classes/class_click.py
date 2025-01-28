import pygame
from os.path import abspath, join

class Sound:
      '''
      ### Класс `звука` который будет `паралельно` `работать` `вместе` с `основной` `музыкой` ###
      '''
      def __init__(self, name_sound):
        '''
         #### Метод конструктор, который позволит нам создавать `звуки` ####
         Атрибуты:

         - :mod:`NAME_SOUND`: имя файла звука, который будет загружен
         - :mod:`SOUND`: объект звука, загруженный через pygame.mixer.Sound

         Пример использования : 
         ```python
         radar_sound = Sound(name_sound = "radar_sound.mp3")
         ```

        '''
        pygame.mixer.init()
        self.NAME_SOUND = name_sound  
        #os.path.abspath(__file__ + f"/../../../static/sounds/{self.NAME_SOUND}")
        sound_path = abspath(join(__file__, "..", "..", "..", "static", "sounds", f"{self.NAME_SOUND}"))
        self.SOUND = pygame.mixer.Sound(sound_path)
        self.SOUND.set_volume(0.2)
              
      def play2(self, loops):
         '''
         `Метод` который будет проигрывать `звук` `паралельно` `от` `основной` `музыки`
         '''
         self.SOUND.play(loops=0, maxtime=0, fade_ms=0)

      def set_volume(self, volume):
         self.SOUND.set_volume(volume)

music_click = Sound(name_sound = "button_pressed.mp3")
music_achieve = Sound(name_sound = "get_achievement.mp3")
death_ship_sound = Sound(name_sound = "death_ship.mp3")
miss_water_sound = Sound(name_sound = "miss_attack.mp3")
del_letter_sound = Sound(name_sound = "deliting_letter.mp3")
typing_sound = Sound(name_sound = "typing_sound.mp3")
shot_sound = Sound(name_sound = "attack.mp3")
buy_product_sound = Sound(name_sound = "buy_product.mp3")
random_first_choice_sound = Sound(name_sound = "random_choice.mp3")
get_coin_sound = Sound(name_sound = "coin.mp3")
player_turn_sound = Sound(name_sound = "player_turn.mp3")
enemy_turn_sound = Sound(name_sound = "enemy_turn.mp3")
radar_sound = Sound(name_sound = "radar_sound.mp3")

all_sounds = [
   music_click, music_achieve, death_ship_sound, miss_water_sound,
   del_letter_sound, typing_sound, shot_sound, buy_product_sound,
   random_first_choice_sound, get_coin_sound, player_turn_sound, enemy_turn_sound,
   radar_sound
]