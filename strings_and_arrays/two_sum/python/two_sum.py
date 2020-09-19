def two_sum(nums, target):
    if len(nums) < 2:
        raise Exception
    index_dict = dict()
    for idx, num in enumerate(nums):
        if index_dict.get(num) is not None:
            return index_dict.get(num), idx
        index_dict[target - num] = idx
    raise Exception
