def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    place_queens(board, 0, n, solutions)
    print_solutions(solutions, n)
    return len(solutions)

def place_queens(board, row, n, solutions):
    # Base case: If all queens are placed, add the solution
    if row >= n:
        solutions.append([row[:] for row in board])
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            place_queens(board, row + 1, n, solutions)
            board[row][col] = 0

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True

def print_solutions(solutions, n):
    for solution in solutions:
        for row in solution:
            print(" ".join("Q" if col == 1 else "." for col in row))
        print("\n")

# Example usage:
n = 5  # You can change the value of n for different board sizes
total_solutions = solve_n_queens(n)
print(f"Total number of solutions: {total_solutions}")
