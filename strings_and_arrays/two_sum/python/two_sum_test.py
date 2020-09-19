import pytest
from two_sum import two_sum

def test_finds_the_right_indices():
    nums = [1, 2, 3, 5, 8]
    target = 11
    index_one, index_two = two_sum(nums, target)
    assert index_one == 2
    assert index_two == 4

def test_not_enough_elements():
    with pytest.raises(Exception):
        nums = [1]
        target = 11
        index_one, index_two = two_sum(nums, target)

def test_no_sums_in_elements():
    with pytest.raises(Exception):
        nums = [1, 2, 3]
        target = 200
        index_one, index_two = two_sum(nums, target)
