def solve_sudoku(board):
    """
    Solve the given Sudoku board using backtracking.
    
    :param board: 2D list representing the Sudoku board, where empty cells are represented by 0
    :return: True if a solution is found, False otherwise
    """
    # Helper function to check if a number can be placed in a given position
    def is_valid(board, row, col, num):
        # Check row
        for i in range(9):
            if board[row][i] == num:
                return False
        # Check column
        for j in range(9):
            if board[j][col] == num:
                return False
        # Check 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True
    
    # Helper function for backtracking
    def backtrack(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for num in range(1, 10):
                        if is_valid(board, i, j, num):
                            board[i][j] = num
                            if backtrack(board):
                                return True
                            board[i][j] = 0
                    return False
        return True
    
    # Start backtracking from the top-left corner
    return backtrack(board)

def print_board(board):
    """
    Print the Sudoku board.
    
    :param board: 2D list representing the Sudoku board
    """
    for row in board:
        print(" ".join(map(str, row)))

# Example usage:
if __name__ == "__main__":
    # Input Sudoku board (0 represents empty cells)
    sudoku_board = [
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
    
    print("Input Sudoku Puzzle:")
    print_board(sudoku_board)
    print("\nSolving...\n")
    
    if solve_sudoku(sudoku_board):
        print("Sudoku Solved:")
        print_board(sudoku_board)
    else:
        print("No solution exists.")
