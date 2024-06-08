def solve_n_queens(n):
    # Create an empty chessboard of size n x n
    board = [[0 for _ in range(n)] for _ in range(n)]
    # List to store all the solutions
    solutions = []
    # Call the recursive function to place queens on the board
    place_queens(board, 0, n, solutions)
    # Print all the solutions
    print_solutions(solutions, n)
    # Return the total number of solutions
    return len(solutions)

def place_queens(board, row, n, solutions):
    # Base case: If all queens are placed, add the solution to the list
    if row >= n:
        solutions.append([row[:] for row in board])
        return
    
    # Try placing a queen in each column of the current row
    for col in range(n):
        # Check if it is safe to place a queen at the current position
        if is_safe(board, row, col, n):
            # Place the queen at the current position
            board[row][col] = 1
            # Recursively call the function to place queens in the next row
            place_queens(board, row + 1, n, solutions)
            # Backtrack by removing the queen from the current position
            board[row][col] = 0

def is_safe(board, row, col, n):
    # Check if there is any queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    # Check if there is any queen in the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check if there is any queen in the upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    # If no conflicts found, it is safe to place a queen at the current position
    return True

def print_solutions(solutions, n):
    # Print each solution
    for solution in solutions:
        # Print each row of the solution
        for row in solution:
            # Print "Q" for queen and "." for empty cell
            print(" ".join("Q" if col == 1 else "." for col in row))
        # Print a new line after each solution
        print("\n")

# Example usage:
n = 5  # You can change the value of n for different board sizes
total_solutions = solve_n_queens(n)
print(f"Total number of solutions: {total_solutions}")
