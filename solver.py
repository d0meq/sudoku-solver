import generator
import csv

N = 9

def printing(arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()

def isSafe(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
    
    for x in range(9):
        if grid[x][col] == num:
            return False
    
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def solveSudoku(grid, row, col):
    if (row == N - 1 and col == N):
        return True
    
    if col == N:
        row += 1
        col = 0
        
    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1)
    
    for num in range(1, N + 1, 1):
        if isSafe(grid, row, col, num):
            grid[row][col] = num
            
            if solveSudoku(grid, row, col + 1):
                return True
    
        grid[row][col] = 0
    return False

def save_to_csv(grid, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in grid:
            writer.writerow(row)

# Generate the Sudoku puzzle
puzzle = generator.generate_sudoku_puzzle(num_to_remove=30)

# Print the generated puzzle
print('Generated Puzzle: \n')
printing(puzzle)
print('-------------------------')

# Make a copy of the puzzle to solve
grid_to_solve = [row[:] for row in puzzle]

# Solve the puzzle
if solveSudoku(grid_to_solve, 0, 0):
    print('Solved Puzzle: \n')
    printing(grid_to_solve)
    
    # Save the solved puzzle to a CSV file
    save_to_csv(grid_to_solve, 'solved_sudoku.csv')
    print('Solved Sudoku has been saved to solved_sudoku.csv')
else:
    print("No solution exists")