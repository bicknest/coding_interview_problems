from number_of_islands import NumberOfIslands

def test_single_island_grid():
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    island_solver = NumberOfIslands(grid)

    assert island_solver.number_of_islands == 1

def test_three_island_grid():
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    island_solver = NumberOfIslands(grid)

    assert island_solver.number_of_islands == 3

def test_empty_grid():
    grid = []
    island_solver = NumberOfIslands(grid)
    assert island_solver.number_of_islands == 0
