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



