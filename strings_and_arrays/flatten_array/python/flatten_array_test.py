from flatten_array import flatten_array

def test_flat_simple_array():
    array = [1, 2, [3, 4], 5]
    assert flatten_array(array) == [1, 2, 3, 4, 5]


def test_nested_array():
    array = [[1, [2, 3], 4], 5, [6, 7, [8]]]
    assert flatten_array(array) == [1, 2, 3, 4, 5, 6, 7, 8]
