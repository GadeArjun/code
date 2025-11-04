def is_safe(board, row, col, n):
    # Check column above
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    # Base case: all rows processed
    if row >= n:
        return True

    # Skip this row if it already has a queen
    if 1 in board[row]:
        return solve_n_queens(board, row + 1, n)

    # Try placing queen in each column
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # place queen
            if solve_n_queens(board, row + 1, n):
                return True
            board[row][col] = 0  # backtrack

    return False


def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))


# --- Main Program ---
n = int(input("Enter N: "))
r = int(input("Enter row for first queen (0 to N-1): "))
c = int(input("Enter column for first queen (0 to N-1): "))

# Create empty board
board = [[0] * n for _ in range(n)]

# Check valid position
if not (0 <= r < n and 0 <= c < n):
    print("Invalid first queen position.")
else:
    board[r][c] = 1  # place the first queen

    # Solve starting from row 0
    if solve_n_queens(board, 0, n):
        print("\nFinal N-Queens Board:")
        print_board(board)
    else:
        print("\nNo solution exists for this position.")
