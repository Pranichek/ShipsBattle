from ..classes import DrawImage , piooner_achievement
from .four_decker_sniper import list_save_coords_achiv

count_ships_achiv = []
count_kill_achiv = [0]
def piooner(cell: int , grid: list):
    if count_kill_achiv[0] != "You killes three ships in row":
        count_ships_achiv.append(cell)

        for ship in count_ships_achiv:
            if ship == 0:
                count_ships_achiv.clear()
                count_kill_achiv[0] = 0
                once = 0
                twice = 0
                thirde = 0
                four = 0
                return False
        
        player_once = 0
        player_twice = 0
        player_thirde = 0
        player_four = 0
        
        for row in range(len(grid)):
            for cell in range(len(grid[row])):
                if grid[row][cell] == 1:
                    player_once += 1
                elif grid[row][cell] == 2:
                    player_twice += 1
                elif grid[row][cell] == 3:
                    player_thirde += 1
                elif grid[row][cell] == 4:
                    player_four += 1

        once = count_ships_achiv.count(1)
        twice = count_ships_achiv.count(2)
        thirde = count_ships_achiv.count(3)
        four = count_ships_achiv.count(4)

        if once >= 1:
            for on in count_ships_achiv:
                if on == 1:
                    count_ships_achiv.remove(on)
            count_kill_achiv[0] += 1
        if twice >= 2:
            for tw in count_ships_achiv:
                if tw == 2:
                    count_ships_achiv.remove(tw)
            count_kill_achiv[0] += 1
        if thirde >= 3:
            for th in count_ships_achiv:
                if th == 3:
                    count_ships_achiv.remove(th)
            count_kill_achiv[0] += 1
        if four >= 4:
            count_kill_achiv[0] += 1
            for fr in count_ships_achiv:
                if fr == 4:
                    count_ships_achiv.remove(fr)

        if count_kill_achiv[0] >= 1:
            print("jajaajjajajajajajajjajj")
            count_kill_achiv[0] = "You killes three ships in row"
            piooner_achievement.ACTIVE = True
            medal_fisr_kill_any_ship.y_cor = 24
            list_save_coords_achiv.append((8 , medal_fisr_kill_any_ship.x_cor , medal_fisr_kill_any_ship.y_cor))
            

medal_fisr_kill_any_ship = DrawImage(
    x_cor = 950 ,
    y_cor = -50,
    width = 100,
    height = 50,
    folder_name = "achievement",
    image_name = "pioneer_medal.png"
)

