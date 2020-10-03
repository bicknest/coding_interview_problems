import pdb

def maximal_square(grid):
    # use dynamic programming to calculate the larest sums of areas at each point
    m = len(grid)
    n = len(grid[0])

    grid_sum = [[0 for _ in range(n)] for _ in range(m)]


    for i in range(n):
        grid_sum[0][i] = grid[0][i]


    for j in range(1, m):
        for i in range(n):
            if grid[j][i] == 1:
                grid_sum[j][i] = min(grid_sum[j][i -1], grid_sum[j - 1][i], grid_sum[j -1][i -1]) + 1
            else:
                grid_sum[j][i] = 0


    max_area = 0
    for row in grid_sum:
        for area in row:
            max_area = max(area, max_area)

    return max_area * max_area


