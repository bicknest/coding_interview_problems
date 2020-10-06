from rotated_array import search


def test_a_rotated_array():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    assert search(nums, target) == 4

def test_a_non_rotated_array():
    nums = [0, 1, 2, 3, 4, 5, 6]
    target = 0
    assert search(nums, target) == 0

def test_rotated_at_early_index():
    nums = [1, 2, 3, 4, 5, 0]
    target = 0
    assert search(nums, target) == 5

def test_rotated_late_index():
    nums = [6, 0, 1, 2, 3, 4, 5]
    target = 0
    assert search(nums, target) == 1

def test_large_target():
    nums = [6, 0, 1, 2, 3, 4, 5]
    target = 6
    assert search(nums, target) == 0

def test_a_single_item_array():
    nums = [1]
    target = 0
    assert search(nums, target) == -1

def test_a_single_item_array_found():
    nums = [0]
    target = 0
    assert search(nums, target) == 0

def test_an_empty_array():
    nums = []
    target = 0
    assert search(nums, target) == -1


def test_full_array_no_target():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 8
    assert search(nums, target) == -1
