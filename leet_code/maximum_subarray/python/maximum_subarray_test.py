from maximum_subarray import maximum_subarray

def test_difficult_array():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert maximum_subarray(nums) == 6
