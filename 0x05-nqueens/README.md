Here is a README file for the N-Queens problem solution:

---

# N-Queens Problem Solution

This repository contains a Python script to solve the N-Queens problem, which involves placing N non-attacking queens on an N×N chessboard.

## Usage

```sh
./0-nqueens.py N
```

- `N` must be an integer greater than or equal to 4.

### Example

```sh
./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

## Thought Process

### Problem Understanding

The N-Queens problem is a classic combinatorial problem where the goal is to place N queens on an N×N chessboard so that no two queens threaten each other. This means:
- No two queens can be in the same row, column, or diagonal.

### Approach

1. **Backtracking**: The solution uses backtracking, a recursive algorithm to solve the problem. The idea is to place queens one by one in different columns, starting from the leftmost column. When placing a queen, check if the current position is safe. If it is, place the queen and proceed to place the next queen. If placing the queen leads to no solution, backtrack and remove the queen from the current position.

2. **Safety Check**: A helper function `is_valid` checks if placing a queen at a particular position is safe by ensuring no other queens are in the same row, upper diagonal, or lower diagonal.

3. **Solution Representation**: The board is represented as a 2D list, and solutions are printed in the format of lists of [row, col] pairs.

### Functions

- `is_valid(board, row, col)`: Checks if a position is safe for placing a queen.
- `nqueens_helper(board, col)`: Recursively tries to place queens in columns and prints solutions.
- `print_board(board, n)`: Formats and prints the board.
- `nqueens(n)`: Initializes the board and starts the solving process.

### Error Handling

- If the number of arguments is incorrect, the program prints `Usage: nqueens N` and exits with status 1.
- If `N` is not a number, the program prints `N must be a number` and exits with status 1.
- If `N` is less than 4, the program prints `N must be at least 4` and exits with status 1.

### Example Execution

- For `N = 4`:

```sh
./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

- For `N = 6`:

```sh
./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

### Script

The following script implements the solution:


This README file provides an overview of the problem, the thought process, and detailed instructions on how to use and test the script.