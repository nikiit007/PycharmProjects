#!/usr/bin/env python3


def main(args):
    board = [[0 for i in range(8)] for i in range(8)]
    eight_queens(0, board)


def eight_queens(r, board):
    if r > 7:
        print(board)
        return
    for c in range(8):
        if board[r][c] == 0:
            board[r][c] = 'q'
            board = set_board(board, r, c)
            eight_queens(r + 1, board)
    for i in range(8):
        print(board[i])
    print(" ")


def set_board(board, row, col):
    # setting row
    for r in range(8):
        if board[r][col] == 0:
            board[r][col] = 1
    # setting column
    for c in range(8):
        if board[row][c] == 0:
            board[row][c] = 1
    # setting diaognals
    r = row
    c = col
    while r >= 0 and c >= 0:
        if board[r][c] == 0:
            board[r][c] = 1
        r -= 1
        c -= 1
    r = row
    c = col
    while r < 8 and c >= 0:
        if board[r][c] == 0:
            board[r][c] = 1
        r += 1
        c -= 1
    r = row
    c = col
    while r >= 0 and c < 8:
        if board[r][c] == 0:
            board[r][c] = 1
        r -= 1
        c += 1

    r = row
    c = col
    while r < 8 and c < 8:
        if board[r][c] == 0:
            board[r][c] = 1
        r += 1
        c += 1
    return board


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
