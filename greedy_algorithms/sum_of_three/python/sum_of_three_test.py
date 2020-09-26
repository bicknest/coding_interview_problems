from sum_of_three import sum_of_three

def test_easy_case():
    nums = [1, 2]
    assert sum_of_three(nums) == []

def test_actual_case():
    nums = [-1, 0, 1, 2, -1, -4]

    sums = [[-1, 1, 0], [-1, -1, 2], [2, 2, -4]]
    assert sum_of_three(nums) == sums


def test_large_case():
    nums = [0, 0, 0, 4, -4, 1, -4, 3, -3, 2, 1, 3, 2, 1, 2, -1, -2, 1, -1]
    sums = [
        [-1, 1, 0], [-1, -1, 2], [1, 1, -2], [2, 2, -4], [-2, -2, 4],
        [-2, 2, 0], [-3, -1, 4], [-3, 3, 0], [-4, 4, 0], [0, 0, 0], [1, 2, -3],
        [-1, -2, 3], [1, 3, -4]
    ]
    assert sum_of_three(nums) == sums
