"""
Create minesweeper game given each row of the board
"""
# minesweeper(["XOO", "OOO", "XXO"])
in_board = ["XOO", "OOO", "XXO"]
board = []
for row in in_board:
    new_row = []
    for el in row:
        new_row.append(el)
    board.append(new_row)
for row in board:
    print(" ".join(row))
print()
new_board = []
for i in range(len(board)):
    new_row = []
    for j in range(len(board[i])):
        if board[i][j] == 'X':
            new_row.append(board[i][j])
            # Loop through this section of the board
            min_row = 0
            max_row = len(board)
            min_col = 0
            max_col = len(board[i])
            new_min_row = i - 1
            if new_min_row < 0:
                new_min_row = 0
            new_min_col = j - 1
            if new_min_col < 0:
                new_min_col = 0
            new_max_row = i + 2
            if new_max_row > max_row:
                new_max_row = max_row
            new_max_col = j + 2
            if new_max_col > max_col:
                new_max_col = max_col
            for k in range(new_min_row, new_max_row):
                for l in range(new_min_col, new_max_col):
                    if board[k][l] != 'X':
                        if type(board[k][l]) == int:
                            board[k][l] += 1
                        else:
                            board[k][l] = 1
for row in board:
    print(" ".join(row))

