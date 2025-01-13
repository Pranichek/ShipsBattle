from ..screens import list_object_map 
from ..classes import Animation
from ..server import enemy_died_ships , enemy_ships, enemy_matrix

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
list_direction = [""]
# список клеток которые уже проверялись
check_number_cell_enemy = []
# длина корабля\
# флаг убитого корабля
check_kill = [False]
enemy_data_kill = ['']
# длина убитого корабля
count_len = [1]
# считать сколько пятерок вокруг убитого корабля
count_five_around = [0]
def kill_enemy_ships():
    if len(enemy_ships[0]) > 0:
        for rowee in range(len(enemy_matrix[0])):
            for cellee in range(len(enemy_matrix[0][rowee])):
                if enemy_matrix[0][rowee][cellee] == 7:
                    if check_target_attack[0] != False and check_kill[0] == True:
                        check_target_attack[0] = True
        
                    if check_target_attack[0] != True:
                        check_target_attack[0] = "None"
                    str_cel = str(cellee)

                    miss_col_enemy[0] = cellee
                    miss_row_enemy[0] = rowee
                    check_kill[0] = False
                    list_direction[0] = ""
                    count_len[0] = 1
                    
                    num_cell = (rowee * 10) + int(str_cel[-1])

                    x = list_object_map[num_cell].x
                    y = list_object_map[num_cell].y

                    for ship in enemy_ships[0]:
                        if ship[0] == x and ship[1] == y:
                            count_len[0] = ship[2]
                            list_direction[0] = ship[3]
                            break
                    
                    if num_cell not in check_number_cell_enemy:
                        if count_len[0] == 1 and list_direction[0] != "":
                            print("убили корабль" , count_len[0])
                            check_kill[0] = True
                            check_number_cell_enemy.append(num_cell)
                            enemy_died_ships.append(count_len[0])


                        elif list_direction[0] == "horizontal" and check_kill[0] != True:
                            for len_ship in range(1 , count_len[0]):
                                if enemy_matrix[0][rowee][cellee + len_ship] == 7:
                                    pass
                                elif enemy_matrix[0][rowee][cellee + len_ship]!= 7:
                                    break
                                if len_ship == count_len[0] - 1:
                                    print("убили корабль" , count_len[0])
                                    check_kill[0] = True
                                    for i in range(0, count_len[0]):
                                        check_number_cell_enemy.append(num_cell + i)
                                    enemy_died_ships.append(count_len[0])
                                    
                        elif list_direction[0] == "vertical" and check_kill[0] != True:
                            for len_ship in range(1 , count_len[0]):
                                if enemy_matrix[0][rowee + len_ship][cellee] == 7:
                                    pass
                                elif enemy_matrix[0][rowee + len_ship][cellee]!= 7:
                                    break
                                if len_ship == count_len[0] - 1:
                                    print("убили корабль" , count_len[0])
                                    check_kill[0] = True
                                    for i in range(0, count_len[0]):
                                        check_number_cell_enemy.append(num_cell + i)
                                    enemy_died_ships.append(count_len[0])

                    if list_direction[0] == "vertical" and check_kill[0] == True:
                        for anim_miss in range(0, count_len[0] + 2):
                            rowka = miss_row_enemy[0] - 1 + anim_miss
                            cellka = miss_col_enemy[0] - 1 
                            if rowka == -1 or cellka == -1:
                                continue
                            else:
                                if rowka <= 9 and cellka <= 9:
                                    cltka = (rowka * 10) + cellka
                                    x_anim_miss = list_object_map[cltka].x
                                    y_anim_miss = list_object_map[cltka].y
                                    if check_target_attack[0] != True:
                                        if enemy_matrix[0][rowka][cellka] == 5:
                                            check_target_attack[0] = False
                                            count_five_around[0] += 1
                                    if enemy_matrix[0][rowka][cellka] == 5:
                                        animation_miss = Animation(
                                            x_cor = x_anim_miss,
                                            y_cor = y_anim_miss,
                                            image_name="0.png",
                                            width = 55,
                                            height = 55,
                                            need_clear = False,
                                            name_folder = "animation_miss",
                                            animation_speed = 3
                                        )
                                        existss = False
                                        for anim_miss in our_miss_anim:
                                            if anim_miss.X_COR == animation_miss.X_COR and anim_miss.Y_COR == animation_miss.Y_COR:
                                                existss = True
                                        if not existss:
                                            our_miss_anim.append(animation_miss)
                                    if enemy_matrix[0][rowka][cellka] == 7:
                                        cross_animation = Animation(
                                            x_cor = x_anim_miss,
                                            y_cor = y_anim_miss,
                                            image_name="0.png",
                                            width = 55,
                                            height = 55,
                                            need_clear = False,
                                            name_folder = "animation_cross",
                                            animation_speed = 3
                                        )
                                        exists = False
                                        for cross in list_cross:
                                            if cross.X_COR == cross_animation.X_COR and cross.Y_COR == cross_animation.Y_COR:
                                                exists = True
                                        if not exists:
                                            list_cross.append(cross_animation)

                        for anim_miss in range(0, count_len[0] + 2):
                            rowka = miss_row_enemy[0] - 1 + anim_miss
                            cellka = miss_col_enemy[0] 
                            if rowka == -1 or cellka == -1:
                                continue
                            else:
                                if rowka <= 9 and cellka <= 9:
                                    cltka = (rowka * 10) + cellka
                                    x_anim_miss = list_object_map[cltka].x
                                    y_anim_miss = list_object_map[cltka].y

                                    if check_target_attack[0] != True:
                                        if enemy_matrix[0][rowka][cellka] == 5:
                                            check_target_attack[0] = False
                                            count_five_around[0] += 1
                                    if enemy_matrix[0][rowka][cellka] == 5:
                                        animation_miss = Animation(
                                            x_cor = x_anim_miss,
                                            y_cor = y_anim_miss,
                                            image_name="0.png",
                                            width = 55,
                                            height = 55,
                                            need_clear = False,
                                            name_folder = "animation_miss",
                                            animation_speed = 3
                                        )
                                        existss = False
                                        for anim_miss in our_miss_anim:
                                            if anim_miss.X_COR == animation_miss.X_COR and anim_miss.Y_COR == animation_miss.Y_COR:
                                                existss = True
                                        if not existss:
                                            our_miss_anim.append(animation_miss)
                                    if enemy_matrix[0][rowka][cellka] == 7:
                                        cross_animation = Animation(
                                            x_cor = x_anim_miss,
                                            y_cor = y_anim_miss,
                                            image_name="0.png",
                                            width = 55,
                                            height = 55,
                                            need_clear = False,
                                            name_folder = "animation_cross",
                                            animation_speed = 3
                                        )
                                        exists = False
                                        for cross in list_cross:
                                            if cross.X_COR == cross_animation.X_COR and cross.Y_COR == cross_animation.Y_COR:
                                                exists = True
                                        if not exists:
                                            list_cross.append(cross_animation)
                        for anim_miss in range(0, count_len[0] + 2):
                            rowka = miss_row_enemy[0] - 1 + anim_miss
                            cellka = miss_col_enemy[0] + 1 
                            if rowka == -1 or cellka == -1:
                                continue
                            else:
                                if rowka <= 9 and cellka <= 9:
                                    cltka = (rowka * 10) + cellka
                                    x_anim_miss = list_object_map[cltka].x
                                    y_anim_miss = list_object_map[cltka].y

                                    if check_target_attack[0] != True:
                                        if enemy_matrix[0][rowka][cellka] == 5:
                                            check_target_attack[0] = False
                                            count_five_around[0] += 1
                                    if enemy_matrix[0][rowka][cellka] == 5:
                                        animation_miss = Animation(
                                            x_cor = x_anim_miss,
                                            y_cor = y_anim_miss,
                                            image_name="0.png",
                                            width = 55,
                                            height = 55,
                                            need_clear = False,
                                            name_folder = "animation_miss",
                                            animation_speed = 3
                                        )
                                        existss = False
                                        for anim_miss in our_miss_anim:
                                            if anim_miss.X_COR == animation_miss.X_COR and anim_miss.Y_COR == animation_miss.Y_COR:
                                                existss = True
                                        if not existss:
                                            our_miss_anim.append(animation_miss)
                                    if enemy_matrix[0][rowka][cellka] == 7:
                                        cross_animation = Animation(
                                            x_cor = x_anim_miss,
                                            y_cor = y_anim_miss,
                                            image_name="0.png",
                                            width = 55,
                                            height = 55,
                                            need_clear = False,
                                            name_folder = "animation_cross",
                                            animation_speed = 3
                                        )
                                        exists = False
                                        for cross in list_cross:
                                            if cross.X_COR == cross_animation.X_COR and cross.Y_COR == cross_animation.Y_COR:
                                                exists = True
                                        if not exists:
                                            list_cross.append(cross_animation)



                if list_direction[0] == "horizontal" and check_kill[0] == True:
                    for anim_miss in range(0, count_len[0] + 2):
                        rowka = miss_row_enemy[0] - 1
                        cellka = miss_col_enemy[0] - 1 + anim_miss
                        if rowka == -1 or cellka == -1:
                            continue
                        else:
                            if rowka <= 9 and cellka <= 9:
                                cltka = (rowka * 10) + cellka
                                x_anim_miss = list_object_map[cltka].x
                                y_anim_miss = list_object_map[cltka].y

                                if check_target_attack[0] != True:
                                    if enemy_matrix[0][rowka][cellka] == 5:
                                        check_target_attack[0] = False
                                        count_five_around[0] += 1
                                if enemy_matrix[0][rowka][cellka] == 5:
                                    animation_miss = Animation(
                                        x_cor = x_anim_miss,
                                        y_cor = y_anim_miss,
                                        image_name="0.png",
                                        width = 55,
                                        height = 55,
                                        need_clear = False,
                                        name_folder = "animation_miss",
                                        animation_speed = 3
                                    )
                                    existss = False
                                    for anim_miss in our_miss_anim:
                                        if anim_miss.X_COR == animation_miss.X_COR and anim_miss.Y_COR == animation_miss.Y_COR:
                                            existss = True
                                    if not existss:
                                        our_miss_anim.append(animation_miss)
                                if enemy_matrix[0][rowka][cellka] == 7:
                                        cross_animation = Animation(
                                            x_cor = x_anim_miss,
                                            y_cor = y_anim_miss,
                                            image_name="0.png",
                                            width = 55,
                                            height = 55,
                                            need_clear = False,
                                            name_folder = "animation_cross",
                                            animation_speed = 3
                                        )
                                        exists = False
                                        for cross in list_cross:
                                            if cross.X_COR == cross_animation.X_COR and cross.Y_COR == cross_animation.Y_COR:
                                                exists = True
                                        if not exists:
                                            list_cross.append(cross_animation)

                    for anim_miss in range(0 , count_len[0] + 2):
                        rowka = miss_row_enemy[0] 
                        cellka = miss_col_enemy[0] - 1 + anim_miss
                        if rowka == -1 or cellka == - 1:
                            continue
                        else:
                            if rowka <= 9 and cellka <= 9:
                                cltka = (rowka * 10) + cellka
                                
                                x_anim_miss = list_object_map[cltka].x
                                y_anim_miss = list_object_map[cltka].y

                                if check_target_attack[0] != True:
                                    if enemy_matrix[0][rowka][cellka] == 5:
                                        check_target_attack[0] = False
                                        count_five_around[0] += 1
                                if enemy_matrix[0][rowka][cellka] == 5:
                                    animation_miss = Animation(
                                        x_cor = x_anim_miss,
                                        y_cor = y_anim_miss,
                                        image_name="0.png",
                                        width = 55,
                                        height = 55,
                                        need_clear = False,
                                        name_folder = "animation_miss",
                                        animation_speed = 3
                                    )
                                    existss = False
                                    for anim_miss in our_miss_anim:
                                        if anim_miss.X_COR == animation_miss.X_COR and anim_miss.Y_COR == animation_miss.Y_COR:
                                            existss = True
                                    if not existss:
                                        our_miss_anim.append(animation_miss)
                                if enemy_matrix[0][rowka][cellka] == 7:
                                        cross_animation = Animation(
                                            x_cor = x_anim_miss,
                                            y_cor = y_anim_miss,
                                            image_name="0.png",
                                            width = 55,
                                            height = 55,
                                            need_clear = False,
                                            name_folder = "animation_cross",
                                            animation_speed = 3
                                        )
                                        exists = False
                                        for cross in list_cross:
                                            if cross.X_COR == cross_animation.X_COR and cross.Y_COR == cross_animation.Y_COR:
                                                exists = True
                                        if not exists:
                                            list_cross.append(cross_animation)

                    for anim_miss in range(0 , count_len[0] + 2):
                        rowka = miss_row_enemy[0] + 1
                        cellka = miss_col_enemy[0] - 1 + anim_miss
                        if rowka == -1 or cellka == - 1:
                            continue
                        else:
                            if rowka <= 9 and cellka <= 9:
                                cltka = (rowka * 10) + cellka
                                
                                x_anim_miss = list_object_map[cltka].x
                                y_anim_miss = list_object_map[cltka].y

                                if check_target_attack[0] != True:
                                    if enemy_matrix[0][rowka][cellka] == 5:
                                        check_target_attack[0] = False
                                        count_five_around[0] += 1
                                if enemy_matrix[0][rowka][cellka] == 5:
                                    animation_miss = Animation(
                                        x_cor = x_anim_miss,
                                        y_cor = y_anim_miss,
                                        image_name="0.png",
                                        width = 55,
                                        height = 55,
                                        need_clear = False,
                                        name_folder = "animation_miss",
                                        animation_speed = 3
                                    )
                                    existss = False
                                    for anim_miss in our_miss_anim:
                                        if anim_miss.X_COR == animation_miss.X_COR and anim_miss.Y_COR == animation_miss.Y_COR:
                                            existss = True
                                    if not existss:
                                        our_miss_anim.append(animation_miss)
                                if enemy_matrix[0][rowka][cellka] == 7:
                                        cross_animation = Animation(
                                            x_cor = x_anim_miss,
                                            y_cor = y_anim_miss,
                                            image_name="0.png",
                                            width = 55,
                                            height = 55,
                                            need_clear = False,
                                            name_folder = "animation_cross",
                                            animation_speed = 3
                                        )
                                        exists = False
                                        for cross in list_cross:
                                            if cross.X_COR == cross_animation.X_COR and cross.Y_COR == cross_animation.Y_COR:
                                                exists = True
                                        if not exists:
                                            list_cross.append(cross_animation)
