from spiral_matrix import spiral_matrix

def test_simple_spiral():
    matrix = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
    output = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiral_matrix(matrix) == output

def test_different_spiral():
    matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]
    output = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert spiral_matrix(matrix) == output


def test_empty_matrix():
    matrix = []
    output = []
    assert spiral_matrix(matrix) == output
