# def find_all_neighbors(matrix, row, col, target_value):
#     # Список для хранения всех соседей
#     neighbors = []

#     # Если клетка за пределами матрицы или ее значение не совпадает с target_value, выходим
#     if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
#         return neighbors
#     if matrix[row][col] != target_value:
#         return neighbors

#     # Помечаем текущую клетку как посещенную (ставим значение, которое невозможно найти в дальнейшем, например, None)
#     matrix[row][col] = None  # Мы изменяем значение, чтобы избежать зацикливания

#     # Соседние позиции (вверх, вниз, влево, вправо)
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#     # Добавляем текущую клетку в список соседей
#     neighbors.append([row, col])

#     # Рекурсивно проверяем соседей
#     for dr, dc in directions:
#         new_row, new_col = row + dr, col + dc
#         neighbors.extend(find_all_neighbors(matrix, new_row, new_col, target_value))

# #     return neighbors
# def find_all_auto_rocket(matrix, row, col, target_value):
#     # Список для хранения всех соседей
#     neighbors = []

#     # Если клетка за пределами матрицы или уже была посещена, выходим
#     if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] is None:
#         return neighbors

#     # Если клетка имеет значение `7`, пропускаем её, но продолжаем поиск
#     if matrix[row][col] == 7:
#         # Соседние позиции (вверх, вниз, влево, вправо)
#         directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#         for dr, dc in directions:
#             new_row, new_col = row + dr, col + dc
#             # Рекурсивно проверяем соседей после клетки `7`
#             neighbors.extend(find_all_neighbors(matrix, new_row, new_col, target_value))
#         return neighbors

#     # Если клетка не совпадает с target_value, выходим
#     if matrix[row][col] != target_value:
#         return neighbors

#     # Помечаем текущую клетку как посещенную
#     matrix[row][col] = None  # Изменяем значение, чтобы избежать зацикливания

#     # Добавляем текущую клетку в список соседей
#     neighbors.append([row, col])

#     # Соседние позиции (вверх, вниз, влево, вправо)
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     for dr, dc in directions:
#         new_row, new_col = row + dr, col + dc
#         neighbors.extend(find_all_neighbors(matrix, new_row, new_col, target_value))
        
#     return neighbors

def find_all_neighbors(matrix, row, col, target_value, visited=None):
    if visited is None:
        visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    # List for storing neighbors
    neighbors = []

    if (
        row < 0 or col < 0 or
        row >= len(matrix) or col >= len(matrix[0]) or
        visited[row][col]
    ):
        return neighbors

    visited[row][col] = True

    # If the cell contains `7`, skip it but continue searching
    if matrix[row][col] == 7:
        # Directions for adjacent cells (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            neighbors.extend(find_all_neighbors(matrix, new_row, new_col, target_value, visited))
        return neighbors

    # If the cell value doesn't match the target, stop recursion
    if matrix[row][col] != target_value:
        return neighbors

    # Add the cell to the neighbors list
    neighbors.append([row, col])

    # Directions for adjacent cells (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        neighbors.extend(find_all_neighbors(matrix, new_row, new_col, target_value, visited))

    return neighbors

def find_all_auto_rocket(matrix, row, col, target_value , row_save = None ,col_save = None , count = None):
    # Список для хранения всех соседей
    neighbors = []
    if row_save ==  None:
        row_sav= row
        col_sav= col
    else :
        row_sav = row_save
        col_sav = col_save

    if count == None:
        a= 1 
        save_count = a 
    if count != None: 
        save_count = count
        save_count +=1
    
    if save_count > 900 :
        

        print (row_sav , col_sav , save_count)
        return [[row_sav, col_sav]]
        
    if save_count > 900 or save_count != None:
        # Если клетка за пределами матрицы или уже была посещена, выходим
        if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or matrix[row][col] is None:
            return neighbors

        # Если клетка имеет значение `7`, пропускаем её, но продолжаем поиск
        if matrix[row][col] == 7:
            # Соседние позиции (вверх, вниз, влево, вправо)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for directions_row, directions_col in directions:
                new_row, new_col = row + directions_row, col + directions_col
                # Рекурсивно проверяем соседей после клетки `7`
                neighbors.extend(find_all_auto_rocket(matrix, new_row, new_col, target_value , row_sav, col_sav, save_count))
            return neighbors

        # Если клетка не совпадает с target_value, выходим
        if matrix[row][col] != target_value:
            return neighbors

        # Помечаем текущую клетку как посещенную
        matrix[row][col] = None  # Изменяем значение, чтобы избежать зацикливания

        # Добавляем текущую клетку в список соседей
        neighbors.append([row, col])

        # Соседние позиции (вверх, вниз, влево, вправо)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for directions_row, directions_col in directions:
            new_row, new_col = row + directions_row, col + directions_col
            neighbors.extend(find_all_auto_rocket(matrix, new_row, new_col, target_value , row_sav, col_sav, save_count))
            
        return neighbors
    else :
        print (row_sav , col_sav , save_count, "error")
        return [[row_sav, col_sav]]
    
def Missile_200 (col:int  ,row:int,enemy_matrix):
    access_rights = None
    # Запрещенные клетки
    list_of_banned_cells =[0,1,8,9]
    ban="True"
    nema = [[ban ,col,row]]
    #проверяем не нажали на бан клетку -_-
    if col in list_of_banned_cells and col in list_of_banned_cells:
        print("BAN")
        access_rights = "false"
        return access_rights
    else :
        access_rights = "true"
    #корди col and row  левого верхнего  угла сетки 5x5
    cell_shot = [col-2,row-2]
    
    # корди ограничители  col and row для обрезании матрици до 5на5
    cell_shot5row=cell_shot[0]+5
    cell_shot5col=cell_shot[1]+5
    # кастрированная матрица  до 5 на 5 клеток из enemy_matrix Центром является та клетка, в которую кликнул игрок. 
   
    
    trimmed_matrix = []
    
    for rowf in enemy_matrix[cell_shot[0]:cell_shot5row]:  # Проходим по строкам в нужном диапазоне а именно col-2 до (col - 2 )+5
        trimmed_row = rowf[cell_shot[1]:cell_shot5col]  # Обрезаем строку по заданным столбцам а именно row-2 до (row - 2 )+5
        trimmed_matrix.append(trimmed_row)  # Добавляем обрезанную строку в итоговую матрицу

    found_row = -1
    found_column = -1
    #Просматривает цикл до того момента, пока не наткнется на число, отличное от 0, 5 или 7, и возвращает столбец и ряд.
    for row, matrix in enumerate(trimmed_matrix):
       for  column, num in enumerate(matrix):
           if num not in (0, 5, 7):  
               found_row = row
               found_column = column
               ship_deck_number = num
               break
        # если нашли то BAN
       if found_row != -1:  
           break
    if found_row == -1:
        print("No target found")
        
        return nema
    #Находим ряд и столбец нашего кораблика для основной матрицы, а не для 5 на 5.
    real_column_enemy = found_column + cell_shot[1]
    real_row_enemy=found_row + cell_shot[0]
    
    rocket_coordinate = [real_row_enemy ,real_column_enemy]
    
    #Если одиночный кораблик, то нет необходимости искать его другую часть. 
    if ship_deck_number != 1:
        print(rocket_coordinate)
        rowneig = rocket_coordinate[0]
        colneig =rocket_coordinate[1]
        # Находим все соседние клетки корабля
        neighbors = find_all_auto_rocket([rowneig [:] for rowneig  in enemy_matrix], rowneig , colneig , ship_deck_number)
        if len (neighbors) == 10 :
            unique_data = []
            for item in neighbors:
                if item not in unique_data:
                    unique_data.append(item)
            neighbors =  unique_data



        print ("neighbors: ",neighbors)
        return neighbors
    else:
        rocket_coordinatex=[rocket_coordinate]
        return rocket_coordinatex

# def Missile_200 (col:int  ,row:int,enemy_matrix):
#     access_rights = None
#     # Запрещенные клетки
#     list_of_banned_cells =[0,1,8,9]
#     ban="True"
#     nema = [[ban ,col,row]]
#     #проверяем не нажали на бан клетку -_-
#     if col in list_of_banned_cells and col in list_of_banned_cells:
#         print("BAN")
#         access_rights = "false"
#         return access_rights
#     else :
#         access_rights = "true"
#     #корди col and row  левого верхнего  угла сетки 5x5
#     cell_shot = [col-2,row-2]
    
#     # корди ограничители  col and row для обрезании матрици до 5на5
#     cell_shot5row=cell_shot[0]+5
#     cell_shot5col=cell_shot[1]+5
#     # кастрированная матрица  до 5 на 5 клеток из enemy_matrix Центром является та клетка, в которую кликнул игрок. 
#     trimmed_matrix = [
#         rowf[cell_shot[1]:cell_shot5col]
#         for rowf in enemy_matrix[cell_shot[0]:cell_shot5row]
#     ]

#     print ("#########################################################")
#     print (trimmed_matrix)
#     print ("#########################################################")
#     print (enemy_matrix)
    
#     found_row = -1
#     found_column = -1
#     #Просматривает цикл до того момента, пока не наткнется на число, отличное от 0, 5 или 7, и возвращает столбец и ряд.
#     for i, roww in enumerate(trimmed_matrix):
#        for  column, num in enumerate(roww):
#            if num not in (0, 5, 7):  
#                found_row = i
#                found_column = column
#                ship_deck_number = num
#                break
#         # если нашли то BAN
#        if found_row != -1:  
#            break
#     if found_row == -1:
#         print("No target found")
        
#         return nema
#     #Находим ряд и столбец нашего кораблика для основной матрицы, а не для 5 на 5.
#     real_column_enemy = found_column + cell_shot[1]
#     real_row_enemy=found_row + cell_shot[0]
    
#     rocket_coordinate = [real_row_enemy ,real_column_enemy]
    
#     #Если одиночный кораблик, то нет необходимости искать его другую часть. 
#     if ship_deck_number != 1:
#         print(rocket_coordinate)
#         rowneig = rocket_coordinate[0]
#         colneig =rocket_coordinate[1]
#         # Находим все соседние клетки корабля
#         neighbors = find_all_auto_rocket([rowneig [:] for rowneig  in enemy_matrix], rowneig , colneig , ship_deck_number)
#         print ("neighbors: ",neighbors)
#         return neighbors
#     else:
#         rocket_coordinatex=[rocket_coordinate]
#         return rocket_coordinatex

# def Missile_200 (col:int  ,row:int,enemy_matrix):
#     access_rights = None
#     # Запрещенные клетки
#     list_of_banned_cells =[0,1,8,9]
#     ban="True"
#     nema = [[ban ,col,row]]
#     #проверяем не нажали на бан клетку -_-
#     if col in list_of_banned_cells and col in list_of_banned_cells:
#         print("BAN")
#         access_rights = "false"
#         return access_rights
#     else :
#         access_rights = "true"
#     #корди col and row  левого верхнего  угла сетки 5x5
#     cell_shot = [col-2,row-2]
    
#     # корди ограничители  col and row для обрезании матрици до 5на5
#     cell_shot5row=cell_shot[0]+5
#     cell_shot5col=cell_shot[1]+5
#     # кастрированная матрица  до 5 на 5 клеток из enemy_matrix Центром является та клетка, в которую кликнул игрок. 
#     trimmed_matrix = [
#         rowf[cell_shot[1]:cell_shot5col]
#         for rowf in enemy_matrix[cell_shot[0]:cell_shot5row]
#     ]

#     print ("#########################################################")
#     print (trimmed_matrix)
#     print ("#########################################################")
#     print (enemy_matrix)
    
#     found_row = -1
#     found_column = -1
#     #Просматривает цикл до того момента, пока не наткнется на число, отличное от 0, 5 или 7, и возвращает столбец и ряд.
#     for i, roww in enumerate(trimmed_matrix):
#        for  column, num in enumerate(roww):
#            if num not in (0, 5, 7):  
#                found_row = i
#                found_column = column
#                ship_deck_number = num
#                break
#         # если нашли то BAN
#        if found_row != -1:  
#            break
#     if found_row == -1:
#         print("No target found")
        
#         return nema
#     #Находим ряд и столбец нашего кораблика для основной матрицы, а не для 5 на 5.
#     real_column_enemy = found_column + cell_shot[1]
#     real_row_enemy=found_row + cell_shot[0]
    
#     rocket_coordinate = [real_row_enemy ,real_column_enemy]
    
#     #Если одиночный кораблик, то нет необходимости искать его другую часть. 
#     if ship_deck_number != 1:
#         print(rocket_coordinate)
#         rowneig = rocket_coordinate[0]
#         colneig =rocket_coordinate[1]
#         # Находим все соседние клетки корабля
#         neighbors = find_all_neighbors([rowneig [:] for rowneig  in enemy_matrix], rowneig , colneig , ship_deck_number)
#         print ("neighbors: ",neighbors)
#         return neighbors
#     else:
#         rocket_coordinatex=[rocket_coordinate]
#         return rocket_coordinatex

    




