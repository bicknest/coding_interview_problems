from rotting_oranges import rotting_oranges

def test_first_example():
    oranges = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    assert rotting_oranges(oranges) == 4

def test_second_example():
    oranges = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    assert rotting_oranges(oranges) == -1
