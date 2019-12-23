from pair_of_sums import pair_of_sums

def test_small_array():
    pairs = [1, 3, 6, 8, 10, 15]
    target_sum = 9
    assert pair_of_sums(pairs, target_sum) == set([1, 8, 3, 6])

def test_array_with_negatives():
    pairs = [-1, 3, 9, 0]
    target_sum = 2
    assert pair_of_sums(pairs, target_sum) == set([-1, 3])
