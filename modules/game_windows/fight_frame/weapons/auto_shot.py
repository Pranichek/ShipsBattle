from ....screens import enemy_matrix
from ....client import list_check_need_send

def auto_aim(row: int, column: int):
    '''
    `Функция` которая отвечает за автоматический прицель на ближайший корабль противника
    '''
    row_ship = None
    col_ship = None
    killed_cells = []
    if row -2 >= 0 and row + 2 < 10:
        if column - 2 >= 0 and column + 2 < 10:
            for col in range(0, 5):
                if enemy_matrix[row - 2][(column - 2) + col] in [1, 2, 3, 4]:
                    print("Maybe baby")
                    row_ship = row - 2
                    col_ship = (column - 2) + col
                    str_col = str(col_ship)
                    number_cell = (row_ship * 10) + int(str_col[-1])
                    killed_cells.append(number_cell)
                    break
            if row_ship is None:
                for col in range(0, 5):
                    if enemy_matrix[row - 1][(column - 2) + col] in [1, 2, 3, 4]:
                        row_ship = row - 1
                        col_ship = (column - 2) + col
                        str_col = str(col_ship)
                        number_cell = (row_ship * 10) + int(str_col[-1])
                        killed_cells.append(number_cell)
                        break
            if row_ship is None:
                for col in range(0, 5):
                    if enemy_matrix[row][(column - 2) + col] in [1, 2, 3, 4]:
                        row_ship = row
                        col_ship = (column - 2) + col
                        str_col = str(col_ship)
                        number_cell = (row_ship * 10) + int(str_col[-1])
                        killed_cells.append(number_cell)
                        break
            if row_ship is None:
                for col in range(0, 5):
                    if enemy_matrix[row + 1][(column - 2) + col] in [1, 2, 3, 4]:
                        row_ship = row + 1
                        col_ship = (column - 2) + col
                        str_col = str(col_ship)
                        number_cell = (row_ship * 10) + int(str_col[-1])
                        killed_cells.append(number_cell)
                        break
            if row_ship is None:
                for col in range(0, 5):
                    if enemy_matrix[row + 2][(column - 2) + col] in [1, 2, 3, 4]:
                        row_ship = row + 2
                        col_ship = (column - 2) + col
                        str_col = str(col_ship)
                        number_cell = (row_ship * 10) + int(str_col[-1])
                        killed_cells.append(number_cell)
                        break

            if row_ship != None:
                # вправо
                for cell in range(1, 4):
                    if col_ship + cell < 10 and col_ship + cell >= 0:
                        if row_ship >= 0 and row_ship < 10:
                            if enemy_matrix[row_ship][col_ship + cell] in [0, 5]:
                                break
                            if enemy_matrix[row_ship][col_ship + cell] in [1, 2, 3, 4]:
                                str_col = str(col_ship + cell) 
                                number_cell = (row_ship * 10) + int(str_col[-1])
                                killed_cells.append(number_cell)
                # вниз
                for cell in range(1, 4):
                    if row_ship + cell < 10 and row_ship + cell >= 0:
                        if col_ship >= 0 and col_ship < 10:
                            if enemy_matrix[row_ship + cell][col_ship] in [0, 5]:
                                break
                            if enemy_matrix[row_ship + cell][col_ship] in [1, 2, 3, 4]:
                                str_col = str(col_ship)
                                number_cell = ((row_ship + cell) * 10) + int(str_col[-1])
                                killed_cells.append(number_cell)
                # влево
                for cell in range(1, 4):
                    if col_ship - cell >= 0 and col_ship - cell < 10:
                        if row_ship >= 0 and row_ship < 10:
                            if enemy_matrix[row_ship][col_ship - cell] in [0, 5]:
                                break
                            if enemy_matrix[row_ship][col_ship - cell] in [1, 2, 3, 4]:
                                str_col = str(col_ship - cell) 
                                number_cell = (row_ship * 10) + int(str_col[-1])

                                killed_cells.append(number_cell)
                # вверх
                for cell in range(1, 4):
                    if row_ship - cell >= 0 and row_ship - cell < 10:
                        if col_ship >= 0 and col_ship < 10:
                            if enemy_matrix[row_ship - cell][col_ship] in [0, 5]:
                                break
                            if enemy_matrix[row_ship - cell][col_ship] in [1, 2, 3, 4]:
                                str_col = str(col_ship)
                                number_cell = ((row_ship - cell) * 10) + int(str_col[-1])
                                killed_cells.append(number_cell)
            elif row_ship == None:
                str_col = str(column)
                number_cell = (row * 10) + int(str_col[-1])
                killed_cells.append(number_cell)
    return killed_cells



            
                    
