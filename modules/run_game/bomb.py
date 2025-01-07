from ..server import enemy_matrix
from ..screens.create_grid import list_object_map_enemy
from ..classes.animation import Animation

def upgrade_attack(index : str, col: int, row: int, count_7 : int):
    """
ВНИМАНИЕ ЖООООООООСКИЕ КАСТЫЛИ, ВСЕМ БАЯТЬСЯ ! ! !
entry_cell для внутренних клеток, если надо ударить 3 на 3 во внутренних клеточках
top_left_corner для верхнего левого угла 3 на 3 
bot_left_corner для нижнего левого угла 3 на 3
left_wall для левой стенки 3 на 3 
top_right_corner для правого верхнего угла 3 на 3
bot_right_corner для правого нижнего угла 3 на 3 
bot_wall для нижней стенки 3 на 3
top_wall для верхней стенки 3 на 3 
right_wall для правой стенки 3 на 3 
    """
    if index == "entry_cell":
        for row_offset in range(-1, 2):
            for index_col in range(0, 3):
                current_row = row + row_offset
                current_col = col - 1 + index_col
                if enemy_matrix[0][current_row][current_col] in [1, 2, 3, 4]:
                    enemy_matrix[0][current_row][current_col] = 7
                    count_7[0] += 1
                elif enemy_matrix[0][current_row][current_col] == 0:
                    enemy_matrix[0][current_row][current_col] = 5
                    
    if index == "top_left_corner":
        for row_offset in range(0, 3):
            for index_col in range(0, 3):
                current_row = row + row_offset
                if enemy_matrix[0][current_row][col + index_col] in [1, 2, 3, 4]:
                    enemy_matrix[0][current_row][col  + index_col] = 7
                    count_7[0] += 1
                elif enemy_matrix[0][current_row][col + index_col] == 0:
                    enemy_matrix[0][current_row][col + index_col] = 5

    if index == "bot_left_corner":
        for row_offset in range(0, 3):
            for index_col in range(0, 3):
                current_row = row - row_offset
                current_col = col + index_col
                if enemy_matrix[0][current_row][current_col] in [1, 2, 3, 4]:
                    enemy_matrix[0][current_row][current_col] = 7
                    count_7[0] += 1
                elif enemy_matrix[0][current_row][current_col] == 0:
                    enemy_matrix[0][current_row][current_col] = 5
    
    if index == "left_wall":
        for row_offset in range(-1, 2):
            for index_col in range(0, 3):
                current_row = row + row_offset
                current_col = col + index_col
                if enemy_matrix[0][current_row][current_col] in [1, 2, 3, 4]:
                    enemy_matrix[0][current_row][current_col] = 7
                    count_7[0] += 1
                elif enemy_matrix[0][current_row][current_col] == 0:
                    enemy_matrix[0][current_row][current_col] = 5
    
    if index == "top_right_corner":
        for row_offset in range(0, 3):
            for index_col in range(0, 3):
                current_row = row + row_offset

                if enemy_matrix[0][current_row][col - index_col] in [1, 2, 3, 4]:
                    enemy_matrix[0][current_row][col  - index_col] = 7
                    count_7[0] += 1
                elif enemy_matrix[0][current_row][col - index_col] == 0:
                    enemy_matrix[0][current_row][col - index_col] = 5

    if index == "bot_right_corner":
        for row_offset in range(0, 3):
            for index_col in range(0, 3):
                current_row = row - row_offset

                if enemy_matrix[0][current_row][col - index_col] in [1, 2, 3, 4]:
                    enemy_matrix[0][current_row][col  - index_col] = 7
                    count_7[0] += 1
                elif enemy_matrix[0][current_row][col - index_col] == 0:
                    enemy_matrix[0][current_row][col - index_col] = 5                

    if index == "bot_wall":
        for row_offset in range(0, 3):
            for index_col in range(0, 3):
                current_row = row - row_offset
                if enemy_matrix[0][current_row][col + index_col - 1] in [1, 2, 3, 4]:
                    enemy_matrix[0][current_row][col + index_col - 1] = 7
                    count_7[0] += 1
                elif enemy_matrix[0][current_row][col + index_col - 1] == 0:
                    enemy_matrix[0][current_row][col + index_col - 1] = 5

    if index == "top_wall":
        for row_offset in range(0, 3):
            for index_col in range(0, 3):
                current_row = row + row_offset
                if enemy_matrix[0][current_row][col + index_col - 1] in [1, 2, 3, 4]:
                    enemy_matrix[0][current_row][col + index_col - 1] = 7
                    count_7[0] += 1
                elif enemy_matrix[0][current_row][col + index_col - 1] == 0:
                    enemy_matrix[0][current_row][col + index_col - 1] = 5
    
    if index == "right_wall":
        for row_offset in range(-1, 2):
            for index_col in range(0, 3):
                current_row = row + row_offset

                if enemy_matrix[0][current_row][col - index_col] in [1, 2, 3, 4]:
                    enemy_matrix[0][current_row][col - index_col] = 7
                    count_7[0] += 1
                elif enemy_matrix[0][current_row][col - index_col] == 0:
                    enemy_matrix[0][current_row][col - index_col] = 5