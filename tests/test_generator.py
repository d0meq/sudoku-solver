import random

def is_valid(board, row, col, num):
    # Check if 'num' is not in the current row, column, and 3x3 subgrid
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in random.sample(range(1, 10), 9):  # Try numbers in random order
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_complete_sudoku():
    board = [[0 for _ in range(9)] for _ in range(9)]
    solve_sudoku(board)
    return board

def remove_numbers(board, num_to_remove):
    for _ in range(num_to_remove):
        while True:
            row, col = random.randint(0, 8), random.randint(0, 8)
            if board[row][col] != 0:
                backup = board[row][col]
                board[row][col] = 0
                # Check if the puzzle still has a unique solution
                temp_board = [row[:] for row in board]
                if solve_sudoku(temp_board):
                    break
                else:
                    board[row][col] = backup
    return board

def generate_sudoku_puzzle(num_to_remove=30):
    complete_board = generate_complete_sudoku()
    puzzle_board = remove_numbers(complete_board, num_to_remove)
    return puzzle_board