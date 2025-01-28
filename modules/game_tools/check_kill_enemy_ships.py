from ..screens import list_object_map_enemy, enemy_matrix
from ..classes import Animation
from ..server import enemy_died_ships , enemy_ships
import modules.server as server_module

# список в котором храним флаг выполнил ли игрок ачивку с названием target_attack
check_target_attack = ["None"]
# чтобы у на ототбражались зачеркнутые клеточки вокргу корабля(список в котором храним анимации зачеркнутых клеточек на поле игрока , то есть с права)
our_miss_anim = []
# список где хранятся крестики которые отрисовываются в том случаи если игрок попал ко кораблю
list_cross = []

# номер рядка и клеточки в этом рядке где отрисовываются зачеркиванные клеточки
miss_row_enemy = [0]
miss_col_enemy = [0]
# направление поворота корабля
list_direction_enemy = [""]
# список клеток которые уже проверялись
check_number_cell_enemy = []
# длина корабля\
# флаг убитого корабля
check_kill_enemy = [False]
enemy_data_kill = ['']
# длина убитого корабля
count_len_enemy = [1]
# считать сколько пятерок вокруг убитого корабля
count_five_around = [0]
def kill_enemy_ships():
    for rowee in range(len(enemy_matrix)):
        for cellee in range(len(enemy_matrix[rowee])):
            if enemy_matrix[rowee][cellee] == 7:
                if check_target_attack[0] == "None" and  check_kill_enemy[0] == True:
                    check_target_attack[0] = True

                if check_target_attack[0] != True:
                    check_target_attack[0] = "None"

                str_cel = str(cellee)
                miss_col_enemy[0] = cellee
                miss_row_enemy[0] = rowee
                check_kill_enemy[0] = False
                list_direction_enemy[0] = ""
                count_len_enemy[0] = 1
                
                num_cell = (rowee * 10) + int(str_cel[-1])

                x = list_object_map_enemy[num_cell].x
                y = list_object_map_enemy[num_cell].y

                for ship in enemy_ships:
                    if ship[0] - 638 == x and ship[1] == y:
                        count_len_enemy[0] = ship[2]
                        list_direction_enemy[0] = ship[3]
                        break

                if num_cell not in check_number_cell_enemy:
                    if count_len_enemy[0] == 1 and list_direction_enemy[0] != "":
                        print("убили корабль" , count_len_enemy[0])
                        check_kill_enemy[0] = True
                        check_number_cell_enemy.append(num_cell)
                        enemy_died_ships.append(count_len_enemy[0])
                    elif list_direction_enemy[0] == "horizontal" and check_kill_enemy[0] != True:
                        for len_ship in range(1 , count_len_enemy[0]):
                            if enemy_matrix[rowee][cellee + len_ship] == 7:
                                pass
                            elif enemy_matrix[rowee][cellee + len_ship]!= 7:
                                break
                            if len_ship == count_len_enemy[0] - 1:
                                print("убили корабль" , count_len_enemy[0])
                                check_kill_enemy[0] = True
                                for i in range(0, count_len_enemy[0]):
                                    check_number_cell_enemy.append(num_cell + i)
                                enemy_died_ships.append(count_len_enemy[0])           
                    elif list_direction_enemy[0] == "vertical" and check_kill_enemy[0] != True:
                        for len_ship in range(1 , count_len_enemy[0]):
                            if enemy_matrix[rowee + len_ship][cellee] == 7:
                                pass
                            elif enemy_matrix[rowee + len_ship][cellee]!= 7:
                                break
                            if len_ship == count_len_enemy[0] - 1:
                                print("убили корабль" , count_len_enemy[0])
                                check_kill_enemy[0] = True
                                for i in range(0, count_len_enemy[0]):
                                    check_number_cell_enemy.append(num_cell + i)
                                enemy_died_ships.append(count_len_enemy[0])

                if list_direction_enemy[0] == "vertical" and check_kill_enemy[0] == True:      
                    for anim_miss in range(0, count_len_enemy[0] + 2):
                        rowka = miss_row_enemy[0] - 1 + anim_miss
                        cellka = miss_col_enemy[0] - 1 
                        if rowka == -1 or cellka == -1:
                            continue
                        else:
                            if rowka <= 9 and cellka <= 9:
                                if check_target_attack[0] != True:
                                    if enemy_matrix[rowka][cellka] == 5:
                                        check_target_attack[0] = False
                                        count_five_around[0] += 1
                                if enemy_matrix[rowka][cellka] == 0:
                                    enemy_matrix[rowka][cellka] = 5
                    for anim_miss in range(0, count_len_enemy[0] + 2):
                        rowka = miss_row_enemy[0] - 1 + anim_miss
                        cellka = miss_col_enemy[0] 
                        if rowka == -1 or cellka == -1:
                            continue
                        else:
                            if rowka <= 9 and cellka <= 9:
                                if check_target_attack[0] != True:
                                    if enemy_matrix[rowka][cellka] == 5:
                                        check_target_attack[0] = False
                                        count_five_around[0] += 1

                                if enemy_matrix[rowka][cellka] == 0:
                                    enemy_matrix[rowka][cellka] = 5

                    for anim_miss in range(0, count_len_enemy[0] + 2):
                        rowka = miss_row_enemy[0] - 1 + anim_miss
                        cellka = miss_col_enemy[0] + 1 
                        if rowka == -1 or cellka == -1:
                            continue
                        else:
                            if rowka <= 9 and cellka <= 9:
                                if check_target_attack[0] != True:
                                    if enemy_matrix[rowka][cellka] == 5:
                                        check_target_attack[0] = False
                                        count_five_around[0] += 1
                                
                                if enemy_matrix[rowka][cellka] == 0:
                                    enemy_matrix[rowka][cellka] = 5
            
                            
                if list_direction_enemy[0] == "horizontal" and check_kill_enemy[0] == True:
                    for anim_miss in range(0, count_len_enemy[0] + 2):
                        rowka = miss_row_enemy[0] - 1
                        cellka = miss_col_enemy[0] - 1 + anim_miss
                        if rowka == -1 or cellka == -1:
                            continue
                        else:
                            if rowka <= 9 and cellka <= 9:
                                if check_target_attack[0] != True:
                                    if enemy_matrix[rowka][cellka] == 5:
                                        check_target_attack[0] = False
                                        count_five_around[0] += 1

                                if enemy_matrix[rowka][cellka] == 0:
                                    enemy_matrix[rowka][cellka] = 5
                    for anim_miss in range(0 , count_len_enemy[0] + 2):
                        rowka = miss_row_enemy[0] 
                        cellka = miss_col_enemy[0] - 1 + anim_miss
                        if rowka == -1 or cellka == - 1:
                            continue
                        else:
                            if rowka <= 9 and cellka <= 9:
                                if check_target_attack[0] != True:
                                    if enemy_matrix[rowka][cellka] == 5:
                                        check_target_attack[0] = False
                                        count_five_around[0] += 1

                                if enemy_matrix[rowka][cellka] == 0:
                                    enemy_matrix[rowka][cellka] = 5           
                    for anim_miss in range(0 , count_len_enemy[0] + 2):
                        rowka = miss_row_enemy[0] + 1
                        cellka = miss_col_enemy[0] - 1 + anim_miss
                        if rowka == -1 or cellka == - 1:
                            continue
                        else:
                            if rowka <= 9 and cellka <= 9:
                                if check_target_attack[0] != True:
                                    if enemy_matrix[rowka][cellka] == 5:
                                        check_target_attack[0] = False
                                        count_five_around[0] += 1
                                
                                if enemy_matrix[rowka][cellka] == 0:
                                    enemy_matrix[rowka][cellka] = 5
                                
                            
                            
                                            

                                