def find_path(maze, row, col):
    if row < 0 or col < 0 or row >= len(maze) or col >= len(maze[0]) or maze[row][col] == "X":
        return False
    if maze[row][col] == "E":
        return True

    # Mark the current cell as visited
    maze[row][col] = "X"

    # Check adjacent cells
    if (find_path(maze, row + 1, col) or
        find_path(maze, row - 1, col) or
        find_path(maze, row, col + 1) or
        find_path(maze, row, col - 1)):
        return True

    return False

def solve_maze(maze):
    # Find the start point
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "S":
                start_row, start_col = i, j
                break

    # Try to find a path from the start point
    if find_path(maze, start_row, start_col):
        print("Solution found:")
        for row in maze:
            print(" ".join(row))
    else:
        print("No solution found.")

maze = [
    ["O","O","O","O","E"],
    ["O","X","X","X","X"],
    ["O","X","O","O","O"],
    ["O","X","O","X","O"],
    ["O","S","O","O","O"],
]

solve_maze(maze)
