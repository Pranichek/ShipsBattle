import modules.server as server_module
from ....classes import Animation
from ....screens import list_object_map_enemy

def update_enemy_matrix_animations(check_animation_rocket: list, flag_miss_rocket_animation: list, list_cross: list):
    """
     Функция которая отрисовывает крестики и зачеркнутые клеточки на вражеском поле(то есть поле которое слева)
    """
    if server_module.flag_bomb_animation[0] == False and check_animation_rocket[0] == "" and flag_miss_rocket_animation[0] == "":
        for row in range(len(server_module.enemy_matrix[0])):
            for cell in range(len(server_module.enemy_matrix[0][row])):
                if server_module.enemy_matrix[0][row][cell] in [1, 2, 3, 4]:
                    cltka = (row * 10) + cell
                    x_anim_miss = list_object_map_enemy[cltka].x
                    y_anim_miss = list_object_map_enemy[cltka].y

                    for cross in list_cross:
                        if cross.X_COR == x_anim_miss and cross.Y_COR == y_anim_miss:
                            list_cross.remove(cross)
                if server_module.enemy_matrix[0][row][cell] == 7:
                    cltka = (row * 10) + cell
                    x_anim_miss = list_object_map_enemy[cltka].x
                    y_anim_miss = list_object_map_enemy[cltka].y

                    cross_animation = Animation(
                    image_name = "0.png", 
                    width = 55, 
                    height = 55, 
                    x_cor = x_anim_miss, 
                    y_cor = y_anim_miss, 
                    need_clear = False , 
                    name_folder = "animation_cross",
                    animation_speed = 3
                    )
                    exists = False
                    for cross in list_cross:
                        if cross.X_COR == cross_animation.X_COR and cross.Y_COR == cross_animation.Y_COR:
                            exists = True
                            break
                    if not exists:
                        list_cross.append(cross_animation)
                elif server_module.enemy_matrix[0][row][cell] == 5:
                    cltka = (row * 10) + cell
                    x_anim_miss = list_object_map_enemy[cltka].x
                    y_anim_miss = list_object_map_enemy[cltka].y

                    miss_cell_animation = Animation(
                    image_name = "0.png", 
                    width = 55, 
                    height = 55, 
                    x_cor = x_anim_miss + 1, 
                    y_cor = y_anim_miss, 
                    need_clear = False , 
                    name_folder = "animation_miss",
                    animation_speed = 3
                    )
                    exists = False
                    for miss_cell in server_module.our_miss_anim:
                        if miss_cell.X_COR == miss_cell_animation.X_COR and miss_cell.Y_COR == miss_cell_animation.Y_COR:
                            exists = True
                            break
                    if not exists:
                        server_module.our_miss_anim.append(miss_cell_animation)