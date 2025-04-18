from ..screens import list_grid , list_object_map , main_screen
from ..classes  import list_ships , Animation
from ..server import player_died_ships 

# номер рядка и клеточки в этом рядке где отрисовываются зачеркиванные клеточки
miss_row = [0]
miss_col = [0]

# направление поворота корабля
list_direction = [""]
# список клеток которые уже проверялись
check_number_cell = []
# длина корабля\
# флаг убитого корабля
check_kill = [False]

count_len = [1]
# список в котором сохраняем все обьекты зачерканных клеточек
list_animation_miss = []

count_fives = [0]
def ship_border():
    for rowee in range(len(list_grid)):
        for cellee in range(len(list_grid[rowee])):
            if list_grid[rowee][cellee] == 7:
                miss_row[0] = rowee
                miss_col[0] = cellee
                str_cel = str(cellee)

                count_fives[0] = 0

                check_kill[0] = False
                list_direction[0] = ""
                count_len[0] = 1
                
                num_cell = (rowee * 10) + int(str_cel[-1])

                x = list_object_map[num_cell].x
                y = list_object_map[num_cell].y

                for ship in list_ships:
                    if ship.row == rowee and ship.col == cellee:
                        count_len[0] = ship.LENGHT
                        list_direction[0] = ship.ORIENTATION_SHIP
                        break
                
                if list_direction[0] != "":
                    if count_len[0] == 1 and list_direction[0] != "":
                        check_kill[0] = True
                        if num_cell not in check_number_cell:
                            check_number_cell.append(num_cell)
                            player_died_ships.append(count_len[0])

                    elif list_direction[0] == "horizontal" and check_kill[0] != True:
                        for len_ship in range(1 , count_len[0]):
                            if list_grid[rowee][cellee + len_ship] == 7:
                                pass
                            elif list_grid[rowee][cellee + len_ship]!= 7:
                                break
                            if len_ship + 1 == count_len[0]:
                                check_kill[0] = True
                                for i in range(1, count_len[0]):
                                    if num_cell + i not in check_number_cell:
                                        check_number_cell.append(num_cell + i)
                                if num_cell not in check_number_cell:
                                    check_number_cell.append(num_cell)
                                    player_died_ships.append(count_len[0])
             
                    elif list_direction[0] == "vertical" and check_kill[0] != True:
                        for len_ship in range(1 , count_len[0]):
                            if list_grid[rowee + len_ship][cellee] == 7:
                                pass
                            elif list_grid[rowee + len_ship][cellee]!= 7:
                                break
                            if len_ship + 1 == count_len[0]:
                                check_kill[0] = True
                                for i in range(1, count_len[0]):
                                    if num_cell + i not in check_number_cell:
                                        check_number_cell.append(num_cell + i)
                                if num_cell not in check_number_cell:
                                    check_number_cell.append(num_cell)
                                    player_died_ships.append(count_len[0])

                    if list_direction[0] == "vertical" and check_kill[0] == True:
                        for anim_miss in range(0, count_len[0] + 2):
                            rowka = miss_row[0] - 1 + anim_miss
                            cellka = miss_col[0] - 1 
                            if rowka == -1 or cellka == -1:
                                continue
                            else:
                                if rowka <= 9 and cellka <= 9:
                                    cltka = (rowka * 10) + cellka
                                    x_anim_miss = list_object_map[cltka].x
                                    y_anim_miss = list_object_map[cltka].y

                                    animation_miss = Animation(
                                        x_cor = x_anim_miss,
                                        y_cor = y_anim_miss,
                                        image_name="0.png",
                                        width = 55,
                                        height = 55,
                                        need_clear = False,
                                        name_folder = "animation_miss",
                                        animation_speed = 1.5
                                    )
                                    existss = False
                                    for anim_miss in list_animation_miss:
                                        if anim_miss.X_COR == animation_miss.X_COR and anim_miss.Y_COR == animation_miss.Y_COR:
                                            existss = True
                                    if not existss:
                                        list_animation_miss.append(animation_miss)

                        for anim_miss in range(0, count_len[0] + 2):
                            rowka = miss_row[0] - 1 + anim_miss
                            cellka = miss_col[0] 
                            if rowka == -1 or cellka == -1:
                                continue
                            else:
                                if rowka <= 9 and cellka <= 9:
                                    cltka = (rowka * 10) + cellka
                                    x_anim_miss = list_object_map[cltka].x
                                    y_anim_miss = list_object_map[cltka].y

                                    animation_miss = Animation(
                                        x_cor = x_anim_miss,
                                        y_cor = y_anim_miss,
                                        image_name="0.png",
                                        width = 55,
                                        height = 55,
                                        need_clear = False,
                                        name_folder = "animation_miss",
                                        animation_speed = 1.5
                                    )
                                    existss = False
                                    if list_grid[rowka][cellka] == 7:
                                        existss = True
                                    for anim_miss in list_animation_miss:
                                        if anim_miss.X_COR == animation_miss.X_COR and anim_miss.Y_COR == animation_miss.Y_COR:
                                            existss = True
                                    if not existss:
                                        list_animation_miss.append(animation_miss)
                        for anim_miss in range(0, count_len[0] + 2):
                            rowka = miss_row[0] - 1 + anim_miss
                            cellka = miss_col[0] + 1 
                            if rowka == -1 or cellka == -1:
                                continue
                            else:
                                if rowka <= 9 and cellka <= 9:
                                    cltka = (rowka * 10) + cellka
                                    x_anim_miss = list_object_map[cltka].x
                                    y_anim_miss = list_object_map[cltka].y

                                    animation_miss = Animation(
                                        x_cor = x_anim_miss,
                                        y_cor = y_anim_miss,
                                        image_name="0.png",
                                        width = 55,
                                        height = 55,
                                        need_clear = False,
                                        name_folder = "animation_miss",
                                        animation_speed = 1.5
                                    )
                                    existss = False
                                    for anim_miss in list_animation_miss:
                                        if anim_miss.X_COR == animation_miss.X_COR and anim_miss.Y_COR == animation_miss.Y_COR:
                                            existss = True
                                    if not existss:
                                        list_animation_miss.append(animation_miss)

                    if list_direction[0] == "horizontal" and check_kill[0] == True:
                        for anim_miss in range(0, count_len[0] + 2):
                            rowka = miss_row[0] - 1
                            cellka = miss_col[0] - 1 + anim_miss
                            if rowka == -1 or cellka == -1:
                                continue
                            else:
                                if rowka <= 9 and cellka <= 9:
                                    cltka = (rowka * 10) + cellka
                                    x_anim_miss = list_object_map[cltka].x
                                    y_anim_miss = list_object_map[cltka].y

                                    animation_miss = Animation(
                                        x_cor = x_anim_miss,
                                        y_cor = y_anim_miss,
                                        image_name="0.png",
                                        width = 55,
                                        height = 55,
                                        need_clear = False,
                                        name_folder = "animation_miss",
                                        animation_speed = 1.5
                                    )
                                    existss = False
                                    for anim_miss in list_animation_miss:
                                        if anim_miss.X_COR == animation_miss.X_COR and anim_miss.Y_COR == animation_miss.Y_COR:
                                            existss = True
                                    if not existss:
                                        list_animation_miss.append(animation_miss)

                        for anim_miss in range(0 , count_len[0] + 2):
                            rowka = miss_row[0] 
                            cellka = miss_col[0] - 1 + anim_miss
                            if rowka == -1 or cellka == - 1:
                                continue
                            else:
                                if rowka <= 9 and cellka <= 9:
                                    cltka = (rowka * 10) + cellka
                                    
                                    x_anim_miss = list_object_map[cltka].x
                                    y_anim_miss = list_object_map[cltka].y

                                    animation_miss = Animation(
                                        x_cor = x_anim_miss,
                                        y_cor = y_anim_miss,
                                        image_name="0.png",
                                        width = 55,
                                        height = 55,
                                        need_clear = False,
                                        name_folder = "animation_miss",
                                        animation_speed = 1.5
                                    )
                                    existss = False

                                    if list_grid[rowka][cellka] == 7:
                                        existss = True
                                    for anim_miss in list_animation_miss:
                                        if anim_miss.X_COR == animation_miss.X_COR and anim_miss.Y_COR == animation_miss.Y_COR:
                                            existss = True
                                    if not existss:
                                        list_animation_miss.append(animation_miss)

                        for anim_miss in range(0 , count_len[0] + 2):
                            rowka = miss_row[0] + 1
                            cellka = miss_col[0] - 1 + anim_miss
                            if rowka == -1 or cellka == - 1:
                                continue
                            else:
                                if rowka <= 9 and cellka <= 9:
                                    cltka = (rowka * 10) + cellka
                                    
                                    x_anim_miss = list_object_map[cltka].x
                                    y_anim_miss = list_object_map[cltka].y

                                    animation_miss = Animation(
                                        x_cor = x_anim_miss,
                                        y_cor = y_anim_miss,
                                        image_name="0.png",
                                        width = 55,
                                        height = 55,
                                        need_clear = False,
                                        name_folder = "animation_miss",
                                        animation_speed = 1.5
                                    )
                                    existss = False

                                    if list_grid[rowka][cellka] == 7:
                                        existss = True

                                    for anim_miss in list_animation_miss:
                                        if anim_miss.X_COR == animation_miss.X_COR and anim_miss.Y_COR == animation_miss.Y_COR:
                                            existss = True
                                    if not existss:
                                        list_animation_miss.append(animation_miss)


    # Отображение анимации
    for anim_miss in list_animation_miss:
        anim_miss.animation(main_screen = main_screen, count_image=29)