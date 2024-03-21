def find_path(maze, row, col):
    print(f"Checking cell ({row}, {col})")
    if row < 0 or col < 0 or row >= len(maze) or col >= len(maze[0]) or maze[row][col] != "O":
        print(f"Out of bounds or wall at ({row}, {col})")
        return False
    if maze[row][col] == "E":
        print(f"Reached the end at ({row}, {col})")
        return True

    maze[row][col] = "X"  # Mark visited

    if (find_path(maze, row + 1, col) or
            find_path(maze, row - 1, col) or
            find_path(maze, row, col + 1) or
            find_path(maze, row, col - 1)):
        return True

    return False


def solve_maze(maze):
    start_row, start_col = None, None
    
    for i in range(len(maze)):  # Iterate over rows
        for j in range(len(maze[0])):  # Iterate over columns
            if maze[i][j] == "S":
                start_row, start_col = i, j
                break
        if start_row is not None:
            break

    if start_row is None:
        print("Starting position 'S' not found in the maze.")
        return

    if find_path(maze, start_row, start_col):
        print("Path is found")
        for row in maze:
            print(" ".join(row))
    else:
        print("Path is not found")


maze = [
    ["O", "O", "O", "O", "E"],
    ["O", "X", "X", "X", "X"],
    ["O", "X", "O", "O", "O"],
    ["O", "X", "O", "X", "O"],
    ["O", "S", "O", "O", "O"],
]

solve_maze(maze)


