from ....screens import list_grid, list_object_map
from ....classes import Animation

def check_and_add_hit_markers(x_enemy_cross: list, y_enemy_cross: list, list_cross_player: list, enemy_fire: list):
    for index_row ,row in enumerate(list_grid):
        for index_cell , cell in enumerate(row):
            # то есть если в нашей матрице находится 7 , то это значит что соперник выстрелил успешно
            # 7 - значит что соперник выстрелил успешно по нашей сетке
            if cell == 7:
                exist = False
                for row_col in enemy_fire:
                    if row_col[0] == row and row_col[1] == cell:
                        exist = True
                if not exist:
                    # сохраняем индекс рядка и клеточки в которой находится наш подсетрленный корабль
                    row = index_row
                    cell = str(index_cell)
                    # из двух чисел(индекс рядка и клеточки) мы находим номер клеточки куда выстрелил соперник
                    # То есть например 2й рядок и первая клеточка , то будет клеточка под номером 11
                    cltx = (row * 10) + int(cell[-1])
                    # получаем через список где хранятся клеточки , координати , в якій буде відображатися анимація попадання по нашему кораблю
                    x_enemy_cross[0] = list_object_map[cltx].x
                    y_enemy_cross[0] = list_object_map[cltx].y
                    # создаем екземпляр крестика , чтобы мы могли их отрисовывать столько раз , сколько попали по нашему кораблю
                    cross_animation = Animation(
                        image_name = "0.png" , 
                        width = 55 , 
                        height = 55 , 
                        x_cor =  list_object_map[cltx].x, 
                        y_cor = list_object_map[cltx].y, 
                        need_clear = False , 
                        name_folder = "animation_cross",
                        animation_speed = 3
                    )
                    # Проверка на то чтобы если в определенной клеточке уже стоит крестик, то мы не создавали еще один(для того чтобы не нагружать устройство)
                    exists = False
                    for cross in list_cross_player:
                        # проверяем по координатам каждый крестик с тем который хотим создать 
                        # если такой уже есть, то выходим из цикла и не добавляем с список
                        if cross.X_COR == cross_animation.X_COR and cross.Y_COR == cross_animation.Y_COR:
                            exists = True
                            break
                    if not exists:
                        list_cross_player.append(cross_animation)
            # elif cell == 5:
            #     row = index_row
            #     cell = str(index_cell)
            #     # из двух чисел(индекс рядка и клеточки) мы находим номер клеточки куда выстрелил соперник
            #     # То есть например 2й рядок и первая клеточка , то будет клеточка под номером 11
            #     cltx = (row * 10) + int(cell[-1])
            #     # получаем через список где хранятся клеточки , координати , в якій буде відображатися анимація попадання по нашему кораблю
            #     x_enemy_cross[0] = list_object_map[cltx].x
            #     y_enemy_cross[0] = list_object_map[cltx].y
            #     # создаем екземпляр крестика , чтобы мы могли их отрисовывать столько раз , сколько попали по нашему кораблю
            #     miss_animation = Animation(
            #         image_name = "0.png" , 
            #         width = 55 , 
            #         height = 55 , 
            #         x_cor =  list_object_map[cltx].x, 
            #         y_cor = list_object_map[cltx].y, 
            #         need_clear = False , 
            #         name_folder = "animation_miss",
            #         animation_speed = 3
            #     )

            #     exist = False
            #     for anim_miss in list_animation_miss:
            #         # проверяем по координатам каждый крестик с тем который хотим создать 
            #         # если такой уже есть, то выходим из цикла и не добавляем с список
            #         if anim_miss.X_COR == miss_animation.X_COR and anim_miss.Y_COR == miss_animation.Y_COR:
            #             exist = True
            #             break
            #     if not exist:
            #         list_animation_miss.append(miss_animation)