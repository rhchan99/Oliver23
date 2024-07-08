def is_valid(grid, row, col, num):
    """Checks if a number is valid in a given cell."""
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    box_row = row // 3
    box_col = col // 3
    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if grid[i][j] == num:
                return False
    return True


def solve_sudoku(grid, row, col):
    """Solves the Sudoku puzzle recursively."""
    if row == 9:
        return True
    if col == 9:
        return solve_sudoku(grid, row + 1, 0)
    if grid[row][col] != 0:
        return solve_sudoku(grid, row, col + 1)
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid, row, col + 1):
                return True
            grid[row][col] = 0
    return False


def print_sudoku(grid):
    """Prints the Sudoku puzzle."""
    for row in grid:
        for num in row:
            print(num, end=' ')
        print()


if __name__ == '__main__':
    sudoku = [
        [0, 0, 8, 6, 2, 5, 1, 0, 0],
        [2, 0, 6, 0, 7, 1, 3, 0, 4],
        [5, 7, 1, 0, 4, 3, 0, 0, 0],
        [0, 0, 0, 0, 9, 0, 0, 2, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 3],
        [1, 4, 0, 0, 0, 0, 8, 6, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 9],
        [0, 5, 2, 1, 8, 0, 0, 0, 6],
        [9, 0, 0, 0, 5, 7, 0, 0, 8],
    ]

solved = solve_sudoku(sudoku, 0, 0)

if solved:
    print('Solved Sudoku:')
    print_sudoku(sudoku)
else:
    print('No solution found.')
