0x09. Island Perimeter

# Island Perimeter Calculator

## Overview

The `island_perimeter` function calculates the perimeter of an island in a grid representation. The grid is a rectangular 2D list where:
- `0` represents water
- `1` represents land

Each cell in the grid is a square with a side length of 1 unit. The function assumes there is only one island in the grid, and the island is completely surrounded by water.

## Function Signature

```python
def island_perimeter(grid):
```

## Parameters

- `grid`: A 2D list of integers representing the map, where `0` indicates water and `1` indicates land.

## Return Value

- Returns an integer representing the perimeter of the island.

## How It Works

The function iterates through each cell in the grid. For each land cell (`1`), the function initially adds 4 to the perimeter, assuming the cell is isolated. It then checks adjacent cells to the left and above:
- If there is a land cell to the left or above, it subtracts 2 from the perimeter for each shared boundary.

### Example

Given the following grid:

```python
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
```

The function call:

```python
print(island_perimeter(grid))  # Output: 16
```

The function calculates a perimeter of `16` for this island.

## Edge Cases

- The function handles grids with no land cells by returning `0`.
- The function assumes the grid is completely surrounded by water.

## Implementation

Here is the implementation of the `island_perimeter` function:


## Conclusion

This function provides an efficient and straightforward method to calculate the perimeter of an island within a given grid. It avoids unnecessary complexity by directly computing the perimeter during a single pass through the grid.

