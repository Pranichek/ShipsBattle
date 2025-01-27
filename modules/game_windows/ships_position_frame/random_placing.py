from ...screens import list_grid , list_object_map
from ...classes import list_ships
import random


list_random_position = ["horizontal", "vertical"]
is_collision = [False]
def random_places_ships():
    for rowe in range(len(list_grid)):
        for celle in range(len(list_grid[rowe])):
            list_grid[rowe][celle] = 0

    for shipka in range(10):
        if shipka == 0:
            while True: 
                random_number_cell = random.randint(0 , 99)
                number_cell = list_object_map.index(list_object_map[random_number_cell])
                # Переделываем значение клетки в строку чтобы можно было лекго узнать в калоночке он стоит
                str_col = str(number_cell) 
                # Вычисляем номер рядка где стоит корабль(например 23 , делим на 10 без остатка и получаем 2 , вот нашь столбец)
                row = number_cell // 10  
                #Колонку кораблика вычисляем по такому принципу
                # Например опять 23 число номер колонки где стоит корабль , тогда с помощью -1 мы берем последнее число тоесть тройку, и вот так получаем номер колонки
                col = int(str_col[-1])
                
                orientation = random.choice(list_random_position)
                if orientation == 'horizontal':
                    if col + list_ships[shipka].LENGHT < 9:
                        for index_column in range(0 , list_ships[shipka].LENGHT):
                            list_grid[row][col + index_column] = list_ships[shipka].LENGHT
                        list_ships[shipka].WIDTH = 62
                        list_ships[shipka].HEIGHT = 62 
                        list_ships[shipka].ORIENTATION_SHIP = orientation
                        list_ships[shipka].CHEK_ROTATION = orientation
                        list_ships[shipka].load_image()
                        list_ships[shipka].RECT = list_ships[shipka].READY_IMAGE_SHIP.get_rect(topleft=(list_ships[shipka].X_COR, list_ships[shipka].Y_COR))
                        x_cor = list_object_map[number_cell].x
                        y_cor = list_object_map[number_cell].y
                        list_ships[shipka].X_COR = x_cor
                        list_ships[shipka].Y_COR = y_cor
                        list_ships[shipka].row = row
                        list_ships[shipka].col = col
                        list_ships[shipka].check_after_random = True
                        break
                if orientation == 'vertical':
                    if row + list_ships[shipka].LENGHT < 10:
                        for index_row in range(0 , list_ships[shipka].LENGHT):
                                list_grid[row + index_row][col] = list_ships[shipka].LENGHT
                        list_ships[shipka].ORIENTATION_SHIP = orientation
                        list_ships[shipka].CHEK_ROTATION = orientation
                        list_ships[shipka].load_image()
                        list_ships[shipka].RECT = list_ships[shipka].IMAGE_ROTATE_SHIP.get_rect(topleft=(list_ships[shipka].X_COR, list_ships[shipka].Y_COR))
                        x_cor = list_object_map[number_cell].x
                        y_cor = list_object_map[number_cell].y
                        list_ships[shipka].X_COR = x_cor
                        list_ships[shipka].Y_COR = y_cor
                        list_ships[shipka].row = row
                        list_ships[shipka].col = col
                        list_ships[shipka].check_after_random = True
                        print(list_grid)
                        break
                else:
                    continue
        else:
            while True:
                is_collision[0] = False
                random_number_cell = random.randint(0 , 99)
                number_cell = list_object_map.index(list_object_map[random_number_cell])
                # Переделываем значение клетки в строку чтобы можно было лекго узнать в калоночке он стоит
                str_col = str(number_cell) 
                # Вычисляем номер рядка где стоит корабль(например 23 , делим на 10 без остатка и получаем 2 , вот нашь столбец)
                row = number_cell // 10  
                #Колонку кораблика вычисляем по такому принципу
                # Например опять 23 число номер колонки где стоит корабль , тогда с помощью -1 мы берем последнее число тоесть тройку, и вот так получаем номер колонки
                col = int(str_col[-1])
                orientation = random.choice(list_random_position)

                list_ships[shipka].ORIENTATION_SHIP = orientation
                list_ships[shipka].CHEK_ROTATION = orientation
                list_ships[shipka].load_image()
                list_ships[shipka].RECT = list_ships[shipka].IMAGE_ROTATE_SHIP.get_rect(topleft=(list_ships[shipka].X_COR, list_ships[shipka].Y_COR))
                x_cor = list_object_map[number_cell].x
                y_cor = list_object_map[number_cell].y
                list_ships[shipka].X_COR = x_cor
                list_ships[shipka].Y_COR = y_cor
                list_ships[shipka].row = row
                list_ships[shipka].col = col

    
                for shiper in list_ships:
                    # проверка чтобы корабль который двигаем не сравнивали с самим собой
                    if list_ships.index(shiper) != shipka:
                        if shiper.ORIENTATION_SHIP == "horizontal":
                            if list_ships[shipka].X_COR >= shiper.X_COR - 62:
                                if list_ships[shipka].X_COR < shiper.X_COR + shiper.RECT.width + 62:
                                    if list_ships[shipka].Y_COR >= shiper.Y_COR - 62:
                                        if list_ships[shipka].Y_COR < shiper.Y_COR + 124:
                                            is_collision[0] = True
                                            break
                                        
                            if list_ships[shipka].X_COR + list_ships[shipka].RECT.width > shiper.X_COR - 62:
                                if list_ships[shipka].X_COR + list_ships[shipka].RECT.width <= shiper.X_COR + shiper.RECT.width + 62:
                                        if list_ships[shipka].ORIENTATION_SHIP == "horizontal":
                                            if list_ships[shipka].Y_COR >= shiper.Y_COR - 62:
                                                if list_ships[shipka].Y_COR < shiper.Y_COR + 124:
                                                        is_collision[0] = True
                                                        break
                                                
                                        elif list_ships[shipka].ORIENTATION_SHIP == "vertical":
                                            if list_ships[shipka].Y_COR + list_ships[shipka].RECT.height > shiper.Y_COR - 62:
                                                if list_ships[shipka].Y_COR + list_ships[shipka].RECT.height <= shiper.Y_COR + 124:
                                                        is_collision[0] = True
                                                        break
                                                
                                                    
                        elif shiper.ORIENTATION_SHIP == "vertical":
                            if list_ships[shipka].X_COR >= shiper.X_COR - 62:
                                if list_ships[shipka].X_COR < shiper.X_COR + shiper.RECT.width + 62:
                                    if list_ships[shipka].Y_COR >= shiper.Y_COR - 62:
                                        if list_ships[shipka].Y_COR < shiper.Y_COR + shiper.RECT.height + 62:
                                                is_collision[0] = True
                                                break
                                            
                            if list_ships[shipka].X_COR + list_ships[shipka].RECT.width > shiper.X_COR - 62:
                                if list_ships[shipka].X_COR + list_ships[shipka].RECT.width <= shiper.X_COR + shiper.RECT.width + 62:
                                        if list_ships[shipka].Y_COR + list_ships[shipka].RECT.height > shiper.Y_COR - 62:
                                            if list_ships[shipka].Y_COR + list_ships[shipka].RECT.height <= shiper.Y_COR + shiper.RECT.height + 62:
                                                    is_collision[0] = True
                                                    break             
    
                if is_collision[0] == True:
                    continue
                else:
                    if orientation == 'horizontal':
                        if col + list_ships[shipka].LENGHT < 11:
                            for index_column in range(0 , list_ships[shipka].LENGHT):
                                list_grid[row][col + index_column] = list_ships[shipka].LENGHT
                            list_ships[shipka].WIDTH = 62
                            list_ships[shipka].HEIGHT = 62 
                            list_ships[shipka].ORIENTATION_SHIP = orientation
                            list_ships[shipka].CHEK_ROTATION = orientation
                            list_ships[shipka].load_image()
                            list_ships[shipka].RECT = list_ships[shipka].READY_IMAGE_SHIP.get_rect(topleft=(list_ships[shipka].X_COR, list_ships[shipka].Y_COR))
                            x_cor = list_object_map[number_cell].x
                            y_cor = list_object_map[number_cell].y
                            list_ships[shipka].X_COR = x_cor
                            list_ships[shipka].Y_COR = y_cor
                            list_ships[shipka].row = row
                            list_ships[shipka].col = col
                            list_ships[shipka].check_after_random = True
                            print(list_grid)
                            break
                    if orientation == 'vertical':
                        if row + list_ships[shipka].LENGHT < 11:
                            for index_row in range(0 , list_ships[shipka].LENGHT):
                                    list_grid[row + index_row][col] = list_ships[shipka].LENGHT
                            list_ships[shipka].ORIENTATION_SHIP = orientation
                            list_ships[shipka].CHEK_ROTATION = orientation
                            list_ships[shipka].load_image()
                            list_ships[shipka].RECT = list_ships[shipka].IMAGE_ROTATE_SHIP.get_rect(topleft=(list_ships[shipka].X_COR, list_ships[shipka].Y_COR))
                            x_cor = list_object_map[number_cell].x
                            y_cor = list_object_map[number_cell].y
                            list_ships[shipka].X_COR = x_cor
                            list_ships[shipka].Y_COR = y_cor
                            list_ships[shipka].row = row
                            list_ships[shipka].col = col
                            list_ships[shipka].check_after_random = True
                            print(list_grid)
                            is_collision[0] = True
                            break
                    else:
                        continue