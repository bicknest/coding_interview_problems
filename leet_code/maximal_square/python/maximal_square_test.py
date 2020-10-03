from maximal_square import maximal_square

def test_maximal_square():
    grid = [[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]]
    assert maximal_square(grid) == 4
