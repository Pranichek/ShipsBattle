import modules.server as server_module
from ....client import list_check_need_send, data_player_shot
from ....screens import list_grid, list_object_map
from ....classes.animation import animation_health
from ....game_tools import check_number_cell
import modules.shop as shop
from ....screens import enemy_matrix

def restore_part_of_ship(row:int, col: int, str_col: str, health_anim: list):
    '''
    `Функция` которая позволяет восстановить часть повреждённого корабля (не мёртвого)

    `Параметры` 
    - :mod:`row`:номер ряда клетки
    - :mod:`col`: номер столбца клетки
    - :mod:`str_col`: строковое представление номера столбца
    - :mod:`health_anim`: список  для анимации восстановления
    '''
     # сохраняем индекс рядка и клеточки в которой находится наш подсетрленный корабль
    if enemy_matrix != "yes":
        cltx = (row * 10) + int(str_col[-1])

        x_anim = list_object_map[cltx].x
        y_anim = list_object_map[cltx].y

        animation_health.X_COR = x_anim
        animation_health.Y_COR = y_anim
        
        if cltx not in check_number_cell:
            try:
                if list_grid[row + 1][col] == 2:
                    list_grid[row][col] = 2
            except:
                print("index error")
            try:
                if list_grid[row - 1][col] == 2:
                    list_grid[row][col] = 2
            except:
                print("index error")
            try:
                if list_grid[row][col + 1] == 2:
                    list_grid[row][col] = 2
            except:
                print("index error")
            try:
                if list_grid[row][col - 1] == 2:
                    list_grid[row][col] = 2
            except:
                print("index error")
            try:
                if list_grid[row + 1][col] == 3:
                    list_grid[row][col] = 3
            except:
                print("index error")
            try:
                if list_grid[row - 1][col] == 3:
                    list_grid[row][col] = 3
            except:
                print("index error")
            try:
                if list_grid[row][col + 1] == 3:
                    list_grid[row][col] = 3
            except:
                print("index error")
            try:
                if list_grid[row][col - 1] == 3:
                    list_grid[row][col] = 3
            except:
                print("index error")

            try:
                if list_grid[row + 1][col] == 4:
                    list_grid[row][col] = 4
            except:
                print("index error")
            try:
                if list_grid[row - 1][col] == 4:
                    list_grid[row][col] = 4
            except:
                print("index error")
            try:
                if list_grid[row][col + 1] == 4:
                    list_grid[row][col] = 4
            except:
                print("index error")
            try:
                if list_grid[row][col - 1] == 4:
                    list_grid[row][col] = 4
            except:
                print("index error")
            if list_grid[row][col] != 7:
                health_anim[0] = True
                shop.but_flag[0] = False
                data_player_shot.append("restore_cell")
                data_player_shot.append(str(list_grid[row][col]))
                data_player_shot.append(str(row))
                data_player_shot.append(str(col))
                list_check_need_send[0] = True

            server_module.row_list[0] = row
            server_module.col_list[0] = col
            server_module.number_list[0] = list_grid[row][col]