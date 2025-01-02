our_ships2 = [0]
enemy_ships2 = [0]
achiv_img = [0]

def first_kill_four_decker_achivment(grid , enemy_grid):
    our_ships2[0] = 0
    if enemy_ships2[0] != "kill four-decker ship":
        enemy_ships2[0] = 0
    for row in range(len(grid)):
        for cell in range(len(grid[row])):
            if grid[row][cell] == 4:
                our_ships2[0] += 1
            if enemy_grid[0][row][cell] == 4:
                enemy_ships2[0] += 1

    if our_ships2[0] >= 1 and enemy_ships2[0] == 0 and enemy_ships2[0] != "kill four-decker ship":
        enemy_ships2[0] = "kill four-decker ship"
        achiv_img[0] = True
        print("Ты убил четыреx палубный кораблик")
        
 # first  
first_kill = [0]   
count_shot2 = [0]
def first_shot_is_kill_achivment(cell):
    print("voshlo")
    count_shot2[0] += 1
    if cell == 1 and count_shot2[0] == 1:
        print("vpsh")
        count_shot2.append("You are kill ship in one shot")
        first_kill[0] = True
        print("You are first shot is kill")
     
     
# 111111111111
single_ships2 = []
achiv_img_single = [0]
def kill_four_single_ships_in_a_row_achivment(cell):
    count_ship = [0]
    single_ships2.append(cell)
    for single_ship2 in single_ships2:
        if single_ship2 == 1:
            count_ship[0] += 1
        else:
            count_ship[0] = 0
            single_ships2.clear()
            return False
        
    if count_ship[0] == 4 and "Kill four single ships in a row" not in single_ships2:
        single_ships2.append("Kill four single ships in a row")
        achiv_img_single[0] = True
        print("You are kill four single ships in a row")
        return True


#2  выжить 5 раз чтобы твои корабли не подбили ниразу
secrecy_img = [0]
count_turns = [0]
save_sevens = []
def kept_all_ships_alive_for_five_turns_achivment(grid: object):
    print("errrrrrrrrrrrrr")
    count_turns[0] += 1
    for row in range(len(grid)):
        for cell in range(len(grid[row])):
            if grid[row][cell] == 7 and (row * 10) + cell not in save_sevens:
                print("lllllllllll")
                count_turns[0] = 0
                save_sevens.append((row * 10) + cell)
    

    if count_turns[0] >= 5 and True not in count_turns:
        print("kkkkkkkk")
        print("У тебя целы корабли 10 раундов")
        secrecy_img[0] = True
        save_sevens.append(True)
        
        