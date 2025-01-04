from ..classes import DrawImage , piooner_achievement
from .four_decker_sniper import list_save_coords_achiv


# kill three ships in a row
count_ships = [0]
count_kill = [0]
def piooner(cell: int , enemy_grid: list):
    if count_kill[0] != "You killes three ships in row":
        count_ships.append(cell)

        for ship in count_ships:
            if ship == 0:
                count_ships.clear()
                count_kill[0] = 0
                once = 0
                twice = 0
                thirde = 0
                four = 0
                return False
        
        enemy_once = 0
        enemy_twice = 0
        enemy_thirde = 0
        enemy_four = 0
        
        for row in range(len(enemy_grid[0])):
            for cell in range(len(enemy_grid[0][row])):
                if enemy_grid[0][row][cell] == 1:
                    enemy_once += 1
                elif enemy_grid[0][row][cell] == 2:
                    enemy_twice += 1
                elif enemy_grid[0][row][cell] == 3:
                    enemy_thirde += 1
                elif enemy_grid[0][row][cell] == 4:
                    enemy_four += 1

        once = count_ships.count(1)
        twice = count_ships.count(2)
        thirde = count_ships.count(3)
        four = count_ships.count(4)

        if once >= 1:
            for on in count_ships:
                if on == 1:
                    count_ships.remove(on)
            count_kill[0] += 1
        elif twice >= 2:
            for tw in count_ships:
                if tw == 2:
                    count_ships.remove(tw)
            count_kill[0] += 1
        elif thirde >= 3:
            for th in count_ships:
                if th == 3:
                    count_ships.remove(th)
            count_kill[0] += 1
        elif four >= 4:
            count_kill[0] += 1
            for fr in count_ships:
                if fr == 4:
                    count_ships.remove(fr)

        if count_kill[0] >= 1 and enemy_once >= 4 and enemy_twice >= 5 and enemy_thirde >= 4 and enemy_four >= 1:
            count_kill[0] = "You killes three ships in row"
            piooner_achievement.ACTIVE = True
            medal_fisr_kill_any_ship.y_cor = 24
            list_save_coords_achiv.append((8 , medal_fisr_kill_any_ship.x_cor , medal_fisr_kill_any_ship.y_cor))
            print("jajaajjajajajajajajjajj")

medal_fisr_kill_any_ship = DrawImage(
    x_cor = 1001 ,
    y_cor = -50,
    width = 100,
    height = 50,
    folder_name = "achievement",
    image_name = "pioneer_medal.png"
)

