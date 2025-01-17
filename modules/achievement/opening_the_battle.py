from ..classes import opening_the_battle_achievement, opening_battle_medal
from .four_decker_sniper import list_save_coords_achiv
import modules.client as client_module

player_ships = [0]
enemy_ships = [0]
def opening_the_battle(grid: list , enemy_grid: list):
    if player_ships[0] != 100:
        player_ships[0] = 0
        enemy_ships[0] = 0
        count_enemy_zero = 0
        for row in range(len(grid)):
            for cell in range(len(grid[row])):
                if grid[row][cell] in [1, 2, 3, 4]:
                    player_ships[0] += 1
                if enemy_grid[row][cell] in [1, 2, 3, 4]:
                    enemy_ships[0] += 1
                elif  enemy_grid[row][cell] == 0:
                    count_enemy_zero += 1

        if player_ships[0] == 20 and enemy_ships[0] <= 19 and count_enemy_zero != 100:
            player_ships[0] = 100
            opening_the_battle_achievement.ACTIVE = True
            opening_battle_medal.ACTIVE = True
            list_save_coords_achiv.append(10)
            list_save_coords_achiv[0] = True

