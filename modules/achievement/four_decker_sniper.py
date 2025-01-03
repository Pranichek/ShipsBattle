from ..classes import DrawImage , first_four_decker_achivment

list_save_coords_achiv = []

achiv_our_ships = [0]
achiv_enemy_ships = [0]
achiv_img = [0]
def first_kill_four_decker_achivment(grid , enemy_grid):
    achiv_our_ships[0] = 0
    if achiv_enemy_ships[0] != "kill four-decker ship":
        achiv_enemy_ships[0] = 0
    for row in range(len(grid)):
        for cell in range(len(grid[row])):
            if grid[row][cell] == 4:
                achiv_our_ships[0] += 1
            if enemy_grid[0][row][cell] == 4:
                achiv_enemy_ships[0] += 1

    if achiv_our_ships[0] >= 1 and achiv_enemy_ships[0] == 0 and achiv_enemy_ships[0] != "kill four-decker ship":
        achiv_enemy_ships[0] = "kill four-decker ship"
        achiv_img[0] = True
        medal_four_decker.y_cor = 24
        first_four_decker_achivment.ACTIVE = True
        # 1 - номе задания
        # 2 - икс
        # 3 - игрек
        list_save_coords_achiv.append((1 , medal_four_decker.x_cor , medal_four_decker.y_cor))
        print("Ты убил четыреx палубный кораблик 777")

medal_four_decker = DrawImage(
    x_cor = 750 ,
    y_cor = -50,
    width = 50 ,
    height = 50 ,
    folder_name = "achievement",
    image_name = "medal_four_decker.png"
)