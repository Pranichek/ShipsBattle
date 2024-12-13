import pygame
import os
from ..screens import grid_player , list_grid , list_object_map 

# Лист для проверки когда накладываем корабль на корабль
check_for_shipsmoving = [0]

class Ship:
    def __init__(self, x_cor: int, y_cor: int, width: int, height: int, image_ship: str, image_rotate_ship: str , length: int, position_ship: str):
        self.X_COR = x_cor#место где будет стоять корабыль по иксу
        self.Y_COR = y_cor#место где будет стоять корабль по игреку
        self.WIDTH = width#ширина корабля
        self.HEIGHT = height#высота корабля
        self.IMAGE_SHIP = image_ship#картинка обычного корабля
        self.ROTATE_SHIP = image_rotate_ship#картинка повернутого корабля
        self.LENGHT = length#длина корабля в клеточках
        self.ORIENTATION_SHIP = position_ship#горизонтально или вертикально сейчас стоит корабль
        self.CHEK_ROTATION = self.ORIENTATION_SHIP#для проверки оризонтально или вертикально сейчас стоит корабль
        self.READY_IMAGE_SHIP = None#отмаштобированная и готовая кратинка норамльного корабля
        self.IMAGE_ROTATE_SHIP = None#отмаштобированная и готовая кратинка повернутого корабля
        self.load_image()#вызываем метод загрузки картинки
        self.CHECK_MOVE = None # Флаг для проверки движений мыши
        self.RECT = self.READY_IMAGE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))#прямоугольник для того чтобы могли отслеживать курсор ли на кораблике или нет
        self.STASIC_X = self.X_COR # Static_x = это начальные координаты
        self.STASIC_Y = self.Y_COR # Static_y = это начальные координаты
        # это свйоство где хранится новая клетка где стоит корабль 
        self.number_cell = 0
        # это свойство где хранится стараяя клетка где стоял корабль
        self.number_ship_cell = 0
        # номер рядка в матрице где он стоит
        self.row = 0
        # номер клетки где он стоит
        self.col = 0
        # флаг для проверки столкновения с кораблями(коллизиями)
        self.check_collision = None

        self.check_after_random = None
    
    # Метод загрузки картинок кораблей
    def load_image(self):
        # Переменная с абсолютным путём, до папки картинок кораблей ( абсолютный путь строится через модуль os.path.abspath()
        ship = os.path.abspath(__file__ + f"/../../../media/ships/{self.IMAGE_SHIP}")
        # Переменная с абсолютным путём, до папки перевёрнутых кораблей 
        rotate_ship = os.path.abspath(__file__ + f"/../../../media/ships/{self.ROTATE_SHIP}")
        # Загружаем картинку при помощи метода load
        image_ship = pygame.image.load(ship)
        # Загружаем картинку повернутого корабля при
        image_rotate_ship = pygame.image.load(rotate_ship)
        
        # Размер корабля зависит от ориентации
        if self.ORIENTATION_SHIP == "horizontal":
            size_ship = (self.WIDTH * self.LENGHT, self.HEIGHT)
            # self.RECT = self.READY_IMAGE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
        elif self.ORIENTATION_SHIP == "vertical":
            size_ship = (self.WIDTH, self.HEIGHT * self.LENGHT)
            # self.RECT = self.IMAGE_ROTATE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
        self.READY_IMAGE_SHIP = pygame.transform.scale(image_ship, size_ship)
        self.IMAGE_ROTATE_SHIP = pygame.transform.scale(image_rotate_ship, size_ship)
      
    # Создаём метод "прилепания" корабля к сетке 
    def snap_to_grid(self): 
        # Привязываем координаты к сетке, это что бы корабль не уходил на саму сетку
        self.X_COR, self.Y_COR = grid_player.snap_to_grid(self.X_COR, self.Y_COR) 
    def center_to_cell_number(self, x, y):
        #Рассчитываем индекс столбца и строки, в которые попадает корабль.
        # grid_player.X_SCREEN - координаты сетки по иксу
        # grid_player.Y_SCREEN - координаты сетки по игреку
        # x - координаты кораблы по иску
        # y - координаты корабля по игреку
        col = (x - grid_player.X_SCREEN) // 62  # Индекс столбца 
        row = (y - grid_player.Y_SCREEN) // 62  # Индекс строки 

        # Учитываем, что клетки нумеруются с 1, поэтому:
        # Номер клетки = (строка * количество столбцов) + (столбец) + 1.
        cell_number = row * 10 + col + 1

        # Возвращаем номер клетки
        return cell_number


    # Cоздаём метод отрисовки корабля, параметр screen - там где он у нас будет отрисовываться 
    def draw_sheep(self, screen: pygame.Surface):
        # Отрисовываем корабль на экране, зависит от ориентации
        if self.ORIENTATION_SHIP == "horizontal":
            screen.blit(self.READY_IMAGE_SHIP, (self.X_COR, self.Y_COR))
        # Отрисовываем корабль на экране, зависит от ориентации
        elif self.ORIENTATION_SHIP == "vertical":
            screen.blit(self.IMAGE_ROTATE_SHIP, (self.X_COR, self.Y_COR))
    # Создаём метод разворота корабля 
    def rotate_ship(self, event: pygame.event):
        self.RECT.topleft = (self.X_COR, self.Y_COR)
        # Создаём переменную мышки, и получаем координаты мышки игрока
        mouse = pygame.mouse.get_pos()
        # Если координаты мышки равняются координатам корабля
        if self.RECT.collidepoint(mouse):
            # И если клавиша отпущена 
            if event.type == pygame.KEYDOWN:
                # И если клавиша R нажата
                if event.key == pygame.K_r and self.CHECK_MOVE == True: 
                    # Если ориентация корабля horizontal
                    if self.CHEK_ROTATION == "horizontal":
                        self.ORIENTATION_SHIP = "vertical"
                        self.CHEK_ROTATION = self.ORIENTATION_SHIP
                        self.load_image()
                        self.RECT = self.IMAGE_ROTATE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
    
                        # Обновляем прямоугольник только при движении
                       

                    elif self.CHEK_ROTATION == "vertical":
                        self.ORIENTATION_SHIP = "horizontal"
                        self.CHEK_ROTATION = self.ORIENTATION_SHIP
                        self.load_image()
                        self.RECT = self.READY_IMAGE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
                        
                        
                    self.X_COR = mouse[0] - self.RECT.width // 2
                    self.Y_COR = mouse[1] - self.RECT.height // 2

                    
                    

    # метод який чистить положення корабля на матриці якщо його передвинули
    def clear_matrix(self):
        if check_for_shipsmoving[0] == 0:
            check_prev_pos = 0

            for index_col in range(0 , 2):
                # Добалвяем к ячейке 
                try:
                    # print(list_grid[self.row][self.col + index_col])
                    if list_grid[self.row][self.col + index_col] == 0:
                        check_prev_pos += 1
                except Exception as e:
                    check_prev_pos = 1


            if self.check_collision != True:
                if check_prev_pos == 0:
                    print("clear col")
                    if list_grid[self.row][self.col] == 0:
                        print("already clear")
                    else:
                        for index_col in range(0 , self.LENGHT):
                            list_grid[self.row][self.col + index_col] = 0
                            # return False
                elif check_prev_pos > 0:
                    print("cler row")
                    if list_grid[self.row][self.col] == 0:
                        print("already clear")
                    else:
                        print(self.row , self.col)
                        print(list_grid[self.row][self.col])
                        for index_row in range(0 , self.LENGHT):
                            print(self.LENGHT , "length")
                            print(list_grid[self.row + index_row][self.col])
                            list_grid[self.row + index_row][self.col] = 0
                            # return False
            elif self.check_collision == True:
                print("banana")
                if self.ORIENTATION_SHIP == "vertical":
                    print("clean row")
                    if list_grid[self.row][self.col] == 0:
                        print("already clear")
                    else:
                        for index_row in range(0 , self.LENGHT):
                            list_grid[self.row + index_row][self.col] = 0
                            # return False
                elif self.ORIENTATION_SHIP == "horizontal":
                    print("clean col")
                    if list_grid[self.row][self.col] == 0:
                        print("already clear")
                    else:
                        for index_col in range(0 , self.LENGHT):
                            list_grid[self.row][self.col + index_col] = 0
                            # return False
        check_for_shipsmoving[0] = 0
       

    # метод который телепортирует коарбль на начальную точку  и поворачивает в положение по горизонатали
    def return_start_code(self):
        self.X_COR, self.Y_COR = self.STASIC_X, self.STASIC_Y
        self.RECT = self.IMAGE_ROTATE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
        self.ORIENTATION_SHIP = "horizontal"
        # Записываем в переменную для проверки
        self.CHEK_ROTATION = self.ORIENTATION_SHIP
        # Отрисовываем изображение при помощи метода
        self.load_image()
        # Записываем в переменную изменённую позицию
        self.RECT = self.READY_IMAGE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
            
       

    def matrix_move(self, event: pygame.event, matrix_width: int, matrix_height: int, cell: int):
        # Получаем текущие координаты мыши
        mouse = pygame.mouse.get_pos() 

        if event.type == pygame.MOUSEBUTTONDOWN and self.RECT.collidepoint(event.pos):
            # Начало перемещения
            self.CHECK_MOVE = True

        # Если мы двигаем курсором по экрану , и уже нажимали на корабль
        elif event.type == pygame.MOUSEMOTION and self.CHECK_MOVE:

            self.X_COR = mouse[0] - self.RECT.width // 2
            self.Y_COR = mouse[1] - self.RECT.height // 2


            # Ограничиваем движение корабля границами матрицы
            self.X_COR = max(0, min(self.X_COR, matrix_width * cell - self.RECT.width))
            self.Y_COR = max(0, min(self.Y_COR, matrix_height * cell - self.RECT.height))
            # Обновляем прямоугольник только при движении
            self.RECT.topleft = (self.X_COR, self.Y_COR)

        elif event.type == pygame.MOUSEBUTTONUP and self.CHECK_MOVE:
            self.CHECK_MOVE = False
            print(self.WIDTH , "self_width")
            print(self.RECT.width , "self_rect")

            if self.check_after_random == True:
                print("Зашло")
                self.clear_matrix()
                self.check_after_random = None
                print(list_grid)

            # Проверка пересечения с другими кораблями
            # делаем перебор списка с кораблями , чтобы модно было проверять не пытается ли поставить пользователь корабль на корабль
            for ship in list_ships:
                # Проверяем ship != self - это для того чтобы не проверять кораблик сам с собой
                # self.RECT.colliderect(ship.RECT) - проверям каждый корабль из списка с текущим кораблем, если ихние прямоугольники(колизии) пересекаются то ставим кораблик на начальные координаты
                if ship != self and self.RECT.colliderect(ship.RECT):
                    print("пересекается")
                    self.return_start_code()
                    # self.number_cell = self.number_ship_cell
                    # # Переделываем значение клетки в строку чтобы можно было лекго узнать в калоночке он стоит
                    # str_col = str(self.number_cell) 
                    # # Вычисляем номер рядка где стоит корабль(например 23 , делим на 10 без остатка и получаем 2 , вот нашь столбец)
                    # self.row = self.number_cell // 10  
                    if ship.col == self.col and ship.row == self.row:
                        check_for_shipsmoving[0] += 1
                    else:
                        check_for_shipsmoving[0] = 0
                    self.clear_matrix()
                    print(list_grid)
                    return False
 
            if grid_player.X_SCREEN - 30 <= self.X_COR and self.X_COR + self.RECT.width <= grid_player.X_SCREEN + 650:
                if grid_player.Y_SCREEN - 30 <= self.Y_COR and self.Y_COR + self.RECT.height <= grid_player.Y_SCREEN + 650:
                    self.snap_to_grid()

       
                    if self.number_ship_cell != self.number_cell and self.check_collision != True:
                        self.clear_matrix()

                    self.check_collision = None

                    # Пересчитываем номер клетки где стоит корабль для старых координат
                    self.number_ship_cell = self.center_to_cell_number(x = self.X_COR,y = self.Y_COR)

                    print(list_grid)
                    print("------------------------------------------------------------------------------------------------")
                    for cell in list_object_map: 
                            if cell.x <= self.X_COR and self.X_COR < cell.x + 62:
                                if cell.y <= self.Y_COR and self.Y_COR < cell.y + 62:
                                    # Узнаем номер клетки где стоит кораблик
                                    self.number_cell = list_object_map.index(cell)
                                    # Переделываем значение клетки в строку чтобы можно было лекго узнать в калоночке он стоит
                                    str_col = str(self.number_cell) 
                                    # Вычисляем номер рядка где стоит корабль(например 23 , делим на 10 без остатка и получаем 2 , вот нашь столбец)
                                    self.row = self.number_cell // 10  
                                    #Колонку кораблика вычисляем по такому принципу
                                    # Например опять 23 число номер колонки где стоит корабль , тогда с помощью -1 мы берем последнее число тоесть тройку, и вот так получаем номер колонки
                                    self.col = int(str_col[-1])

                                    # Устанавливаем значение где стоит корабль в матрице
                                    if self.ORIENTATION_SHIP == "horizontal":
                                        for index_column in range(0 , self.LENGHT):
                                            list_grid[self.row][self.col + index_column] = self.LENGHT
                                    elif self.ORIENTATION_SHIP == "vertical":
                                        for index_row in range(0 , self.LENGHT):
                                            list_grid[self.row + index_row][self.col] = self.LENGHT
                    
                     
                    for shiper in list_ships:
                        # проверка чтобы корабль который двигаем не сравнивали с самим собой
                        if list_ships.index(shiper) != list_ships.index(self):
                            if shiper.ORIENTATION_SHIP == "horizontal":
                                if self.X_COR >= shiper.X_COR - 62:
                                    if self.X_COR < shiper.X_COR + shiper.RECT.width + 62:
                                        if self.Y_COR >= shiper.Y_COR - 62:
                                            if self.Y_COR < shiper.Y_COR + 124:
                                                self.X_COR = self.STASIC_X
                                                self.Y_COR = self.STASIC_Y
                                                print(self.row , self.col)
                                                self.check_collision = True
                                                self.clear_matrix()
                                                self.return_start_code()
                                                break
                                        
                                
                                if self.X_COR + self.RECT.width > shiper.X_COR - 62:
                                    if self.X_COR + self.RECT.width <= shiper.X_COR + shiper.RECT.width + 62:
                                            if self.ORIENTATION_SHIP == "horizontal":
                                                if self.Y_COR >= shiper.Y_COR - 62:
                                                    if self.Y_COR < shiper.Y_COR + 124:
                                                            
                                                            self.X_COR = self.STASIC_X
                                                            self.Y_COR = self.STASIC_Y
                                                            print(self.row , self.col)
                                                            self.check_collision = True
                                                            self.clear_matrix()
                                                            self.return_start_code()
                                                            break
                                                
                                            elif self.ORIENTATION_SHIP == "vertical":
                                                if self.Y_COR + self.RECT.height > shiper.Y_COR - 62:
                                                    if self.Y_COR + self.RECT.height <= shiper.Y_COR + 124:
                                                            print("HAAHAHAHAHHAHA")
                                                            self.X_COR = self.STASIC_X
                                                            self.Y_COR = self.STASIC_Y
                                                            print(self.row , self.col)
                                                            self.check_collision = True
                                                            self.clear_matrix()
                                                            self.return_start_code()
                                                            break
                                                    

                            elif shiper.ORIENTATION_SHIP == "vertical":
                                if self.X_COR >= shiper.X_COR - 62:
                                    if self.X_COR < shiper.X_COR + shiper.RECT.width + 62:
                                        if self.Y_COR >= shiper.Y_COR - 62:
                                            if self.Y_COR < shiper.Y_COR + shiper.RECT.height + 62:
                                                    self.X_COR = self.STASIC_X
                                                    self.Y_COR = self.STASIC_Y
                                                    print(self.row , self.col)
                                                    self.check_collision = True
                                                    self.clear_matrix()
                                                    self.return_start_code()
                                                    break
                                            

                                if self.X_COR + self.RECT.width > shiper.X_COR - 62:
                                    if self.X_COR + self.RECT.width <= shiper.X_COR + shiper.RECT.width + 62:
                                            if self.Y_COR + self.RECT.height > shiper.Y_COR - 62:
                                                if self.Y_COR + self.RECT.height <= shiper.Y_COR + shiper.RECT.height + 62:
                                                        self.X_COR = self.STASIC_X
                                                        self.Y_COR = self.STASIC_Y
                                                        print(self.row , self.col)
                                                        self.check_collision = True
                                                        self.clear_matrix()
                                                        self.return_start_code()
                                                        break
                        
            
                    print("------------------------------------------------------------------------------------------------")
                    print(list_grid)
                else:
                    print("Колбаsa")
                    self.clear_matrix()
                    self.return_start_code()
                    print(list_grid)
       
            else:
                print("Колбаса")
                self.clear_matrix()
                self.return_start_code()
                print(list_grid)
                
 
            

            # Обновляем прямоугольник в конце
            self.RECT.topleft = (self.X_COR, self.Y_COR)
       


# Тут мы создаём сами корабли, цифры в словах, типа: three, two, one , это деления корабля, на сколько клеточек он задуман
# Чотирипалубний корабель
ship_four = Ship(
    x_cor = 882,  # x кордината для чотирипалубного корабля
    y_cor = 475,   # y кордината для першого ряду
    width = 62,
    height = 62,
    image_ship = "ship_four.png", 
    image_rotate_ship = "rotate_ship_four.png", 
    length = 4, 
    position_ship = "horizontal"
)

# Тріпалубні кораблі (перший ряд)
ship_three = Ship(
    x_cor = 773, 
    y_cor = 350,  # y кордината для другого ряду
    width = 62,
    height = 62,
    image_ship = "ship_three.png", 
    image_rotate_ship = "rotate_ship_three.png", 
    length = 3, 
    position_ship = "horizontal"
)

# Тріпалубні кораблі (другий ряд)
ship_three2 = Ship(
    x_cor = 1038,  # зміщення по x
    y_cor = 350,
    width = 62,
    height = 62,
    image_ship = "ship_three.png", 
    image_rotate_ship = "rotate_ship_three.png", 
    length = 3, 
    position_ship = "horizontal"
)

# Двопалубні кораблі (перший ряд)
ship_two = Ship(
    x_cor = 783, 
    y_cor = 215,  # y кордината для третього ряду
    width = 62,
    height = 62,
    image_ship = "ship_two.png", 
    image_rotate_ship = "rotate_ship_two.png", 
    length = 2, 
    position_ship = "horizontal"
)

# Двопалубні кораблі (другий ряд)
ship_two2 = Ship(
    x_cor = 933,  # зміщення по x
    y_cor = 215,
    width = 62,
    height = 62,
    image_ship = "ship_two.png", 
    image_rotate_ship = "rotate_ship_two.png", 
    length = 2, 
    position_ship = "horizontal"
)

# Двопалубні кораблі (третій ряд)
ship_two3 = Ship(
    x_cor = 1082,  # зміщення по x
    y_cor = 215,
    width = 62,
    height = 62,
    image_ship = "ship_two.png", 
    image_rotate_ship = "rotate_ship_two.png", 
    length = 2, 
    position_ship = "horizontal"
)

# Однопалубні кораблі (перший ряд)
ship_one = Ship(
    x_cor = 814, 
    y_cor = 80,  # y кордината для четвертого ряду
    width = 62,
    height = 62,
    image_ship = "ship_one.png", 
    image_rotate_ship = "rotate_ship_one.png", 
    length = 1, 
    position_ship = "horizontal"
)

# Однопалубні кораблі (другий ряд)
ship_one2 = Ship(
    x_cor = 918,  # зміщення по x
    y_cor = 80,
    width = 62,
    height = 62,
    image_ship = "ship_one.png", 
    image_rotate_ship = "rotate_ship_one.png", 
    length = 1, 
    position_ship = "horizontal"
)

# Однопалубні кораблі (третій ряд)
ship_one3 = Ship(
    x_cor = 1022,  # зміщення по x
    y_cor = 80,
    width = 62,
    height = 62,
    image_ship = "ship_one.png", 
    image_rotate_ship = "rotate_ship_one.png", 
    length = 1, 
    position_ship = "horizontal"
)

# Однопалубні кораблі (четвертий ряд)
ship_one4 = Ship(
    x_cor = 1126,  # зміщення по x
    y_cor = 80,
    width = 62,
    height = 62,
    image_ship = "ship_one.png", 
    image_rotate_ship = "rotate_ship_one.png", 
    length = 1, 
    position_ship = "horizontal"
)







# Создаём всех список кораблей
list_ships = []

# Добавляем В КОНЕЦ СПИСКА все корабли
list_ships.append(ship_four)
list_ships.extend([ship_three , ship_three2])
list_ships.extend([ship_two , ship_two2 , ship_two3])
list_ships.extend([ship_one , ship_one2 , ship_one3, ship_one4])



