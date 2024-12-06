class Grid:
    def __init__(self, x_screen: int, y_screen: int):
        self.X_SCREEN = x_screen
        self.Y_SCREEN = y_screen

    def generate_grid(self):
        x_screen, y_screen = self.X_SCREEN, self.Y_SCREEN
        for row in list_grid:
            for cell in row:
                if cell == 0:
                    empty_cell = Cell(x=x_screen, y=y_screen, width=62, height=62, image_name="empty_cell.png")
                    list_object_map.append(empty_cell)
                x_screen += 62
            y_screen += 62
            x_screen = 81

    def snap_to_grid(self, x, y):
        # Рассчитываем индекс столбца сетки (grid_x), в который попадает точка (x)-координата корабля.
        grid_x = round((x - self.X_SCREEN) / 62)
        grid_y = round((y - self.Y_SCREEN) / 62)
        grid_x = max(0, min(10 - 1, grid_x))
        grid_y = max(0, min(10 - 1, grid_y))
        return self.X_SCREEN + grid_x * 62, self.Y_SCREEN + grid_y * 62

    def cell_number_to_coordinates(self, cell_number):
        # Преобразуем номер клетки в экранные координаты
        # cell_number - это номер клетки, который начинается с 1 (например, 1, 2, 3,...)
        grid_x = (cell_number - 1) % 10  # Преобразуем в столбец
        grid_y = (cell_number - 1) // 10  # Преобразуем в строку
        x_coord = self.X_SCREEN + grid_x * 62
        y_coord = self.Y_SCREEN + grid_y * 62
        return x_coord, y_coord


# Функция для нахождения кораблей и преобразования координат в экране
def find_ships(matrix, grid: Grid):
    ship_positions = []  # Список для хранения информации о кораблях
    
    rows = len(matrix)
    cols = len(matrix[0])

    visited = set()  # Чтобы избежать повторного учета клеток кораблей

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited and matrix[i][j] > 0:
                # Это начало нового корабля
                ship_type = matrix[i][j]
                start_cell = i * cols + j + 1  # Номер клетки
                visited.add((i, j))

                # Проверим направление (горизонтально или вертикально)
                if j + 1 < cols and matrix[i][j + 1] == ship_type:
                    direction = "horizontal"
                    # Пройти по горизонтали
                    k = j
                    while k < cols and matrix[i][k] == ship_type:
                        visited.add((i, k))
                        k += 1
                    start_coordinates = grid.cell_number_to_coordinates(start_cell)  # Координаты начала корабля
                elif i + 1 < rows and matrix[i + 1][j] == ship_type:
                    direction = "vertical"
                    # Пройти по вертикали
                    k = i
                    while k < rows and matrix[k][j] == ship_type:
                        visited.add((k, j))
                        k += 1
                    start_coordinates = grid.cell_number_to_coordinates(start_cell)  # Координаты начала корабля
                else:
                    direction = "single-cell"  # Одноклеточный корабль
                    start_coordinates = grid.cell_number_to_coordinates(start_cell)  # Координаты начала одноклеточного корабля

                # Добавить информацию о корабле
                ship_positions.append({
                    "ship_type": ship_type,
                    "start_cell": start_cell,
                    "start_coordinates": start_coordinates,
                    "direction": direction
                })

    return ship_positions


# Пример матрицы
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 3, 3, 3, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 4, 0, 0],
    [1, 0, 0, 0, 2, 0, 0, 4, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 4, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 4, 0, 0],
    [1, 0, 0, 0, 2, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 2, 0, 3, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 0, 0, 0]
]

# Создаем экземпляр класса Grid
grid_player = Grid(x_screen=81, y_screen=128)

# Найти корабли
ships = find_ships(matrix, grid_player)

# Вывести результат
for ship in ships:
    print(f"Корабль {ship['ship_type']}-палубный начинается с клетки {ship['start_cell']} ({ship['start_coordinates']}) и ориентирован {ship['direction']}.")
