#!/usr/bin/env python3

solutions = 0


def main(args):
    board = [[0 for i in range(8)] for i in range(8)]
    # board[0][0]='q'
    eight_queens(0, board)
    print(solutions)


def eight_queens(r, board):
    if r > 7:
        global solutions
        solutions += 1
        # printing(board)
        for i in range(8):
            print(board[i])
        print('')
        return

    for c in range(8):
        if not check_conflict(r, c, board):
            board[r][c] = 'q'
            eight_queens(r + 1, board)
            board[r][c] = 0



            # return true if conflict else return false


def check_conflict(row, col, board):
    for c in range(8):
        if board[row][c] == 'q':
            return True
    for r in range(8):
        if board[r][col] == 'q':
            return True
    r, c = row, col

    while r >= 0 and c >= 0:
        if board[r][c] == 'q':
            return True
        r -= 1
        c -= 1
    r, c = row, col

    while r >= 0 and c < 8:
        if board[r][c] == 'q':
            return True
        r -= 1
        c += 1


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
