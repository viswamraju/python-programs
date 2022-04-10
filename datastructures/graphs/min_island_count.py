import sys

def get_island_count(grid):
    visited = set()
    min_size = sys.maxsize
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            size = explore(grid, row, col, visited)
            if 0 < size < min_size:
                min_size = size
    return min_size


def explore(grid, row, col, visited):
    row_in_bounds = 0 <= row < len(grid)
    col_in_bounds = 0 <= col < len(grid[0])

    if not row_in_bounds or not col_in_bounds:
        return 0

    if grid[row][col] == 'W':
        return 0

    pos = (row, col)
    if pos in visited:
        return 0
    visited.add(pos)
    size = 1
    size += explore(grid, row - 1, col, visited)
    size += explore(grid, row + 1, col, visited)
    size += explore(grid, row, col - 1, visited)
    size += explore(grid, row, col + 1, visited)
    return size


if __name__ == '__main__':
    grid = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W']
    ]

    print(get_island_count(grid))
