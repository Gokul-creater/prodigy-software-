#TASK 4
To implement a Sudoku solver in Python using a backtracking algorithm, we need to create a program that can efficiently solve Sudoku puzzles given an input grid. Here’s a step-by-step guide on how to achieve this:

### Step-by-Step Implementation:

1. **Input Representation**:
   - Represent the Sudoku puzzle using a 2D list (9x9 grid) where empty cells are denoted by 0.

2. **Check Validity Function**:
   - Create a function to check if a number can be placed in a given cell according to Sudoku rules (no repeated numbers in the same row, column, or 3x3 sub-grid).

3. **Backtracking Algorithm**:
   - Implement a recursive function using backtracking to explore possible solutions:
     - Find an empty cell in the grid.
     - Try placing each number (1 to 9) in the cell.
     - Check if placing the number is valid using the validity function.
     - If valid, recursively attempt to solve the rest of the puzzle.
     - Backtrack if no number fits or the solution fails downstream.

4. **Main Solver Function**:
   - Use the backtracking algorithm to solve the puzzle.
   - Once solved, print or display the completed Sudoku grid.

Here's the Python code that implements the Sudoku solver using backtracking:

```python
def print_grid(grid):
    """ Helper function to print the Sudoku grid """
    for row in grid:
        print(" ".join(map(str, row)))

def find_empty_location(grid):
    """ Find an empty location (cell with 0) in the Sudoku grid """
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return (row, col)
    return None

def is_valid_move(grid, row, col, num):
    """ Check if placing 'num' in (row, col) is valid according to Sudoku rules """
    # Check row
    if num in grid[row]:
        return False
    
    # Check column
    for r in range(9):
        if grid[r][col] == num:
            return False
    
    # Check 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == num:
                return False
    
    return True

def solve_sudoku(grid):
    """ Solve Sudoku using backtracking """
    find = find_empty_location(grid)
    if not find:
        return True  # Puzzle solved
    
    row, col = find
    
    for num in range(1, 10):  # numbers 1 to 9
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            
            if solve_sudoku(grid):
                return True
            
            grid[row][col] = 0  # Backtrack
    
    return False  # Trigger backtracking

# Example Sudoku puzzle (0 represents empty cells)
example_grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Sudoku Puzzle to Solve:")
print_grid(example_grid)
print("\nSolving...\n")

if solve_sudoku(example_grid):
    print("Sudoku Solved:")
    print_grid(example_grid)
else:
    print("No solution exists for the given Sudoku puzzle.")
```

### Explanation:

- **Functions**:
  - `print_grid(grid)`: Prints the Sudoku grid in a readable format.
  - `find_empty_location(grid)`: Finds the next empty cell (0) in the grid.
  - `is_valid_move(grid, row, col, num)`: Checks if placing `num` in the cell `(row, col)` is valid according to Sudoku rules.
  - `solve_sudoku(grid)`: Implements the backtracking algorithm to solve the Sudoku puzzle recursively.

- **Example Grid**:
  - `example_grid`: Example Sudoku puzzle provided in a 2D list format. Modify this grid to solve different Sudoku puzzles.

- **Usage**:
  - Run the script to solve the Sudoku puzzle defined in `example_grid`.
  - The program will print the initial puzzle, solve it using backtracking, and print the completed Sudoku grid.

This implementation efficiently solves Sudoku puzzles using backtracking, ensuring all Sudoku rules are adhered to throughout the solving process. You can use this as a basis to solve more complex Sudoku puzzles or integrate it into larger applications requiring puzzle-solving capabilities.
