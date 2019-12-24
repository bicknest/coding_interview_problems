from largest_contiguous_sequence import largest_contiguous_sequence

def test_simple_range():
    sequence = [2, -8, 3, -2, 4, -10]
    assert largest_contiguous_sequence(sequence) == 5

def test_different_sequence():
    sequence = [2, -8, 3, -2, 4, -10, 100]
    assert largest_contiguous_sequence(sequence) == 100
