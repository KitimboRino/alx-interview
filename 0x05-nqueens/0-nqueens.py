#!/usr/bin/python3
'''Solving nqueens problem'''
import sys


def is_valid(board, row, col):
    """
    Checks if a position of the queen is valid
    Args:
        board: 2D array representing the board
        row: row of the queen
        col: column of the queen
    Returns:
        Boolean: True if the position is valid, False otherwise
    """
    # Check this row on the left side
    if 1 in board[row]:
        return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def nqueens_helper(board, col):
    """
    Helper function for nqueens
    Args:
        board: 2D array representing the board
        col: column to start from
    Returns:
        Boolean: True if a solution is found, False otherwise
    """
    if col >= len(board):
        print_board(board, len(board))
        return True

    res = False
    for i in range(len(board)):
        if is_valid(board, i, col):
            board[i][col] = 1
            res = nqueens_helper(board, col + 1) or res
            board[i][col] = 0

    return res


def print_board(board, n):
    """
    Prints positions of the queens
    Args:
        board: 2D array representing the board
        n: size of the board
    Returns:
        None
    """
    solution = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


def nqueens(n):
    """
    Finds all possible solutions to the n-queens problem
    Args:
        n: size of the board
    Returns:
        None
    """
    board = [[0] * n for _ in range(n)]
    if not nqueens_helper(board, 0):
        print("No solution exists")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    queens = sys.argv[1]
    if not queens.isnumeric():
        print("N must be a number")
        sys.exit(1)

    n = int(queens)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(n)
