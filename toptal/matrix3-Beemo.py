def main():
    in_board = ["XOO", "OOO", "XXO"]
    in_board = list(map(lambda x: list(map(lambda y: True if y == 'X' else False, x)), in_board))
    print(eval_board(in_board))


# Correct solution implemented by my friend Dave
"""
Create end result of a game of minesweeper given each row of the board
Was supposed to solve this in 30 minutes
"""


def eval_board(board):
    lim_y = len(board)
    lim_x = len(board[0])
    ret_board = []
    for y in range(lim_y):
        line = []
        for x in range(lim_x):
            if board[y][x]:
                hit = 'X'
                line.append(hit)
                continue
            hit = 0

            def f(a):
                if a[0] < 0:
                    return False
                if a[0] >= lim_y:
                    return False
                if a[1] < 0:
                    return False
                if a[1] >= lim_x:
                    return False
                return True

            possible_points = list(filter(f, [(y - 1, x - 1), (y - 1, x), (y - 1, x + 1), (y, x - 1), (y, x + 1),
                                              (y + 1, x - 1), (y + 1, x), (y + 1, x + 1)]))
            for p in possible_points:
                hit += board[p[0]][p[1]]
            line.append(hit)
        ret_board.append(line)
    return ret_board


if __name__ == "__main__":
    main()
