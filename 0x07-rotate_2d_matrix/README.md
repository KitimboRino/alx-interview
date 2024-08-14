# rotate_2d_matrix

## Description

`rotate_2d_matrix` is a function designed to rotate an `n x n` 2D matrix 90 degrees clockwise. The function modifies the matrix in place, meaning the original matrix is updated without creating a new matrix.

## Problem Statement

Given an `n x n` 2D matrix, rotate the matrix 90 degrees clockwise. The function must perform the rotation in place, without using any additional data structures for storing the rotated matrix. You can assume that the matrix will have 2 dimensions and will not be empty.

## Approach

The rotation of the matrix is achieved through a two-step process:

1. **Transpose the Matrix:** This step involves swapping the elements at `matrix[i][j]` with `matrix[j][i]`. The transposition effectively converts the rows of the original matrix into the columns of the transposed matrix.

2. **Reverse Each Row:** After the transposition, each row of the matrix is reversed. This step rearranges the elements in each row to achieve the desired 90-degree clockwise rotation.

### Time Complexity

The algorithm operates in `O(n^2)` time, where `n` is the number of rows or columns in the matrix. This is due to the two nested loops required for the transposition and the reversal of each row.

### Space Complexity

The algorithm uses `O(1)` additional space because the matrix is modified in place, and no extra data structures are used.

The final matrix is the result of rotating the original matrix 90 degrees clockwise.
