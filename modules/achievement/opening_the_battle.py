from ..classes import DrawImage , opening_the_battle_achievement
from .four_decker_sniper import list_save_coords_achiv

player_ships = [0]
enemy_ships = [0]
def opening_the_battle(grid: list , enemy_grid: list):
    if player_ships[0] != "True":
        player_ships[0] = 0
    enemy_ships[0] = 0
    for row in range(len(grid)):
        for cell in range(len(grid[row])):
            if grid[row][cell] != 5 and grid[row][cell] != 7 and grid[row][cell] != 0:
                player_ships[0] += 1
            if enemy_grid[0][row][cell] != 5 and enemy_grid[0][row][cell] != 7 and enemy_grid[0][row][cell] != 0:
                enemy_ships[0]+= 1

    if player_ships[0] == 20 and enemy_ships[0] <= 19:
        player_ships[0] = "True"
        opening_the_battle_achievement.ACTIVE = True
        medal_opening_battle.y_cor = 64
        list_save_coords_achiv.append((10 , medal_opening_battle.x_cor , medal_opening_battle.y_cor))

medal_opening_battle = DrawImage(
    x_cor = 931,
    y_cor = -50 ,
    width = 50 ,
    height = 50,
    folder_name = "achievement",
    image_name = "medal_opening_the_battle.png"

)