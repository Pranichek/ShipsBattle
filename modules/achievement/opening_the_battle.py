from ..classes import opening_the_battle_achievement, opening_battle_medal
from .four_decker_sniper import list_save_coords_achiv

player_ships = [0]
enemy_ships = [0]
def opening_the_battle(grid: list , enemy_grid: list):
    if player_ships[0] != 100:
        player_ships[0] = 0
        enemy_ships[0] = 0
        for row in range(len(grid)):
            for cell in range(len(grid[row])):
                if grid[row][cell] != 5 and grid[row][cell] != 7 and grid[row][cell] != 0:
                    player_ships[0] += 1
                if enemy_grid[0][row][cell] != 5 and enemy_grid[0][row][cell] != 7 and enemy_grid[0][row][cell] != 0:
                    enemy_ships[0] += 1

        if player_ships[0] == 20 and enemy_ships[0] <= 19:
            player_ships[0] = 100
            opening_the_battle_achievement.ACTIVE = True
            opening_battle_medal.ACTIVE = True
            list_save_coords_achiv.append((10))

