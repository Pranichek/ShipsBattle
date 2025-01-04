from ..classes import DrawImage , strategist_achievement
from .four_decker_sniper import list_save_coords_achiv

count_player_ships = [0]

def strategist(grid: list, enemy_grid: list):
    # счетчик кораблей сервера
    if count_player_ships[0] != 21:
        count_player_ships[0] = 0
    # счетчик кораблей клиента
    count_enemy_ships = 0
    # делаем перебор матриц сервера и клиента, чтобы проверять ввыиграл уже кто то или нет
    for row_server in range(len(grid)):
        for cell_server in range(len(grid[row_server])):
            # 5 - по клетке уже стреляли
            # 0 - кораблей просто нет
            # 7 - уже потопленный корабль
            if grid[row_server][cell_server] != 0 and grid[row_server][cell_server] != 5 and grid[row_server][cell_server] != 7:
                count_player_ships[0] += 1

    for row_client in range(len(enemy_grid[0])):
        for cell_client in range(len(enemy_grid[0][row_client])):
            # 5 - по клетке уже стреляли
            # 0 - кораблей просто нет
            # 7 - уже потопленный корабль
            if enemy_grid[0][row_client][cell_client] != 0 and enemy_grid[0][row_client][cell_client] != 5 and enemy_grid[0][row_client][cell_client] != 7:
                count_enemy_ships += 1

    if count_player_ships[0] >= 20 and count_enemy_ships <= 0:
        print("you won without losing a ship!")
        strategist_achievement.ACTIVE = True
        strategist_medal.y_cor = 64
        list_save_coords_achiv.append((3 , strategist_medal.x_cor , strategist_medal.y_cor))
        count_player_ships[0] = 21


strategist_medal = DrawImage(
    x_cor = 796 ,
    y_cor = -50,
    width = 50,
    height = 50,
    folder_name = "achievement",
    image_name = "strategist_medal.png"
)