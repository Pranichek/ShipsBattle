import pygame
import os
from ..screens import grid_player , list_grid

 

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
        self.number_ship = { # Словарь для хранения длины(координат) корабля 
            self.LENGHT : [0]
        }
    
    # Метод загрузки картинок кораблей
    def load_image(self):
        # Переменная с абсолютным путём, до папки картинок кораблей ( абсолютный путь строится через модуль os.path.abspath()
        ship = os.path.abspath(__file__ + f"/../../../images/ships/{self.IMAGE_SHIP}")
        # Переменная с абсолютным путём, до папки перевёрнутых кораблей 
        rotate_ship = os.path.abspath(__file__ + f"/../../../images/ships/{self.ROTATE_SHIP}")
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
        # Рассчитываем индекс столбца и строки, в которые попадает корабль.
        # grid_player.X_SCREEN - координаты сетки по иксу
        # grid_player.Y_SCREEN - координаты сетки по игреку
        # x - координаты кораблы по иску
        # y - координаты корабля по игреку
        col = (x - grid_player.X_SCREEN) // 62  # Индекс столбца 
        row = (y - grid_player.Y_SCREEN) // 62  # Индекс строки 

        # Учитываем, что клетки нумеруются с 1, поэтому:
        # Номер клетки = (строка * количество столбцов) + (столбец) + 1.
        cell_number = row * 9 + col + 1

        # Возвращаем номер клетки.
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
        # Создаём переменную мышки, и получаем координаты мышки игрока
        mouse = pygame.mouse.get_pos()
        # Если координаты мышки равняются координатам корабля
        if self.RECT.collidepoint(mouse):
            # И если клавиша отпущена 
            if event.type == pygame.KEYDOWN:
                # И если клавиша R нажата
                if event.key == pygame.K_r: 
                    # Если ориентация корабля horizontal
                    if self.CHEK_ROTATION == "horizontal":
                        # Присваиваем значение vertical
                        self.ORIENTATION_SHIP = "vertical"
                        # Записываем в переменную для проверки 
                        self.CHEK_ROTATION = self.ORIENTATION_SHIP
                        # Отрисовываем изображение при помощи метода
                        self.load_image()
                        # Записываем в переменную изменённую позицию
                        self.RECT = self.IMAGE_ROTATE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
                        # Если ориентация корабля vertical
                    elif self.CHEK_ROTATION == "vertical":
                        # Присваиваем значение horizontal
                        self.ORIENTATION_SHIP = "horizontal"
                        # Записываем в переменную для проверки
                        self.CHEK_ROTATION = self.ORIENTATION_SHIP
                        # Отрисовываем изображение при помощи метода
                        self.load_image()
                        # Записываем в переменную изменённую позицию
                        self.RECT = self.READY_IMAGE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
                        
    def matrix_move(self, event: pygame.event, matrix_width: int, matrix_height: int, cell: int):
        mouse = pygame.mouse.get_pos()  # Получаем текущие координаты мыши

        if event.type == pygame.MOUSEBUTTONDOWN and self.RECT.collidepoint(event.pos):
            # Начало перемещения
            self.CHECK_MOVE = True
            self.STATIC_MOUSE_OFFSET = (
                mouse[0] - self.X_COR,
                mouse[1] - self.Y_COR,
            )  # Смещение мышки относительно корабля

        elif event.type == pygame.MOUSEMOTION and self.CHECK_MOVE:
            # Обновляем координаты с учётом смещения
            self.X_COR = mouse[0] - self.STATIC_MOUSE_OFFSET[0]
            self.Y_COR = mouse[1] - self.STATIC_MOUSE_OFFSET[1]

            # Ограничиваем движение корабля границами матрицы
            self.X_COR = max(0, min(self.X_COR, matrix_width * cell - self.RECT.width))
            self.Y_COR = max(0, min(self.Y_COR, matrix_height * cell - self.RECT.height))
            # Обновляем прямоугольник только при движении
            self.RECT.topleft = (self.X_COR, self.Y_COR)

        elif event.type == pygame.MOUSEBUTTONUP and self.CHECK_MOVE:
            # Завершаем перемещение
            right_x = self.X_COR + self.WIDTH
            print(right_x)
            if grid_player.X_SCREEN <= self.X_COR and self.X_COR + self.RECT.width <= grid_player.X_SCREEN + 558:
                if grid_player.Y_SCREEN <= self.Y_COR and self.Y_COR + self.RECT.height <= grid_player.Y_SCREEN + 558:
                    self.snap_to_grid()
                    number_ship_cell = self.center_to_cell_number(x = self.X_COR,y = self.Y_COR)

                    if self.LENGHT == 4:
                        self.number_ship[self.LENGHT] = [number_ship_cell]
                        if self.ORIENTATION_SHIP == "horizontal":
                            for coord_ship in range(1, self.LENGHT):
                                self.number_ship[self.LENGHT].append(number_ship_cell + coord_ship)
                        elif self.ORIENTATION_SHIP == "vertical":
                            for coord_ship in range(1, self.LENGHT):
                                self.number_ship[self.LENGHT].append(self.number_ship[self.LENGHT][-1] + 9)
                    if self.LENGHT == 3:
                        self.number_ship[self.LENGHT] = [number_ship_cell]
                        if self.ORIENTATION_SHIP == "horizontal":
                            for coord_ship in range(1, self.LENGHT):
                                self.number_ship[self.LENGHT].append(number_ship_cell + coord_ship)
                        elif self.ORIENTATION_SHIP == "vertical":
                            for coord_ship in range(1, self.LENGHT):
                                self.number_ship[self.LENGHT].append(self.number_ship[self.LENGHT][-1] + 9)
                    if self.LENGHT == 2:
                        self.number_ship[self.LENGHT] = [number_ship_cell]
                        if self.ORIENTATION_SHIP == "horizontal":
                            for coord_ship in range(1, self.LENGHT):
                                self.number_ship[self.LENGHT].append(number_ship_cell + coord_ship)
                        elif self.ORIENTATION_SHIP == "vertical":
                            for coord_ship in range(1, self.LENGHT):
                                self.number_ship[self.LENGHT].append(self.number_ship[self.LENGHT][-1] + 9)
                    if self.LENGHT == 1:
                        self.number_ship[self.LENGHT] = [number_ship_cell]
                        if self.ORIENTATION_SHIP == "horizontal":
                            for coord_ship in range(1, self.LENGHT):
                                self.number_ship[self.LENGHT].append(number_ship_cell + coord_ship)
                        elif self.ORIENTATION_SHIP == "vertical":
                            for coord_ship in range(1, self.LENGHT):
                                self.number_ship[self.LENGHT].append(self.number_ship[self.LENGHT][-1] + 9)
                        
                    print(self.number_ship[self.LENGHT])
                else:
                    self.X_COR, self.Y_COR = self.STASIC_X, self.STASIC_Y
                    self.RECT = self.IMAGE_ROTATE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
                    self.ORIENTATION_SHIP = "horizontal"
                    # Записываем в переменную для проверки
                    self.CHEK_ROTATION = self.ORIENTATION_SHIP
                    # Отрисовываем изображение при помощи метода
                    self.load_image()
                    # Записываем в переменную изменённую позицию
                    self.RECT = self.READY_IMAGE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
               
            else:
                self.X_COR, self.Y_COR = self.STASIC_X, self.STASIC_Y
                self.RECT = self.IMAGE_ROTATE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
                self.ORIENTATION_SHIP = "horizontal"
                # Записываем в переменную для проверки
                self.CHEK_ROTATION = self.ORIENTATION_SHIP
                # Отрисовываем изображение при помощи метода
                self.load_image()
                # Записываем в переменную изменённую позицию
                self.RECT = self.READY_IMAGE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
               

            # Проверка пересечения с другими кораблями
            # делаем перебор списка с кораблями , чтобы модно было проверять не пытается ли поставить пользователь корабль на корабль
            for ship in list_ships:
                # Проверяем ship != self - это для того чтобы не проверять кораблик сам с собой
                # self.RECT.colliderect(ship.RECT) - проверям каждый корабль из списка с текущим кораблем, если ихние прямоугольники(колизии) пересекаются то ставим кораблик на начальные координаты
                if ship != self and self.RECT.colliderect(ship.RECT):
                    # Если столкнулись, то ставим кораблик на начальные координаты
                    self.X_COR, self.Y_COR = self.STASIC_X, self.STASIC_Y
                    # поворачиваем его по горизонтале если он был вертикальным
                    self.ORIENTATION_SHIP = "horizontal"
                    # Записываем в переменную для проверки
                    self.CHEK_ROTATION = self.ORIENTATION_SHIP
                    # Отрисовываем изображение при помощи метода
                    self.load_image()
                    # Записываем в переменную изменённую позицию
                    self.RECT = self.READY_IMAGE_SHIP.get_rect(topleft=(self.X_COR, self.Y_COR))
                    break

            # Обновляем прямоугольник в конце
            self.RECT.topleft = (self.X_COR, self.Y_COR)
            self.CHECK_MOVE = False


# Тут мы создаём сами корабли, цифры в словах, типа: three, two, one , это деления корабля, на сколько клеточек он задуман
ship_four = Ship(
    x_cor = 900 , 
    y_cor = 100 , 
    width = 62 , 
    height =62 , 
    image_ship = "ship_four.png", 
    image_rotate_ship = "rotate_ship_four.png", 
    length = 4 , 
    position_ship = "horizontal"
)

ship_two = Ship(
    x_cor = 900,
    y_cor =  300,
    width = 62,
    height = 62,
    image_ship = "ship_two.png",
    image_rotate_ship = "rotate_ship_two.png",
    length = 2,
    position_ship = "horizontal"
)

ship_one = Ship(
    x_cor = 900 , 
    y_cor = 400 , 
    width = 62 , 
    height = 62 , 
    image_ship = "ship_one.png", 
    image_rotate_ship = "rotate_ship_one.png", 
    length = 1 , 
    position_ship = "horizontal"
)

ship_three = Ship(
    x_cor = 900 , 
    y_cor = 500 , 
    width = 62 , 
    height =62 , 
    image_ship = "ship_three.png", 
    image_rotate_ship = "rotate_ship_three.png", 
    length = 3 , 
    position_ship = "horizontal"
)

# Создаём всех список кораблей
list_ships = []

# Добавляем В КОНЕЦ СПИСКА все корабли
list_ships.append(ship_four)
list_ships.append(ship_two)
list_ships.append(ship_one)
list_ships.append(ship_three)