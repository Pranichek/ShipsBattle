from .class_image import DrawImage
from ..screens import list_object_map_enemy

class Radar:
    def __init__(self):
        self.list_cells = []
    def check_target_grid(self, enemy_matrix: list, row: int, column: int):
        for cell in range(0, 3):
            col = (row * 10) + ((column - 1) + cell)
            x_cell = list_object_map_enemy[col].x
            y_cell = list_object_map_enemy[col].y
            if enemy_matrix[row][(column - 1) + cell] in [1, 2, 3, 4]:
                target_cell = DrawImage(
                        width = 55,
                        height = 55,
                        x_cor = x_cell,
                        y_cor = y_cell,
                        folder_name = "radar",
                        image_name = "ship_radar.png"
                    )
                target_cell.visible = 0
                self.list_cells.append(target_cell)
            else:
                empty_cell = DrawImage(
                    width = 55,
                    height = 55,
                    x_cor = x_cell,
                    y_cor = y_cell,
                    folder_name = "radar",
                    image_name = "empty_cell.png"
                )
                empty_cell.visible = 0
                self.list_cells.append(empty_cell)
        for cell in range(0, 3):
            col = ((row - 1) * 10) + ((column - 1) + cell)
            x_cell = list_object_map_enemy[col].x
            y_cell = list_object_map_enemy[col].y
            if enemy_matrix[row - 1][(column - 1)+ cell] in [1, 2, 3, 4]:
                target_cell = DrawImage(
                        width = 55,
                        height = 55,
                        x_cor = x_cell,
                        y_cor = y_cell,
                        folder_name = "radar",
                        image_name = "ship_radar.png"
                    )
                target_cell.visible = 0
                self.list_cells.append(target_cell)
            else:
                empty_cell = DrawImage(
                    width = 55,
                    height = 55,
                    x_cor = x_cell,
                    y_cor = y_cell,
                    folder_name = "radar",
                    image_name = "empty_cell.png"
                )
                empty_cell.visible = 0
                self.list_cells.append(empty_cell)
        for cell in range(0, 3):
            col = ((row + 1) * 10) + ((column - 1) + cell)
            x_cell = list_object_map_enemy[col].x
            y_cell = list_object_map_enemy[col].y
            if enemy_matrix[row + 1][(column - 1) + cell] in [1, 2, 3, 4]:
                target_cell = DrawImage(
                        width = 55,
                        height = 55,
                        x_cor = x_cell,
                        y_cor = y_cell,
                        folder_name = "radar",
                        image_name = "ship_radar.png"
                    )
                target_cell.visible = 0
                self.list_cells.append(target_cell)
            else:
                empty_cell = DrawImage(
                    width = 55,
                    height = 55,
                    x_cor = x_cell,
                    y_cor = y_cell,
                    folder_name = "radar",
                    image_name = "empty_cell.png"
                )
                empty_cell.visible = 0
                self.list_cells.append(empty_cell)

radar = Radar()