def search(nums, target):

    ### find the rotational index

    def rotate_index(left, right):

        # case where no rotation exists
        if nums[left] < nums[right]:
            return 0


        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] > nums[pivot + 1]:
                return pivot + 1
            else:
                if nums[pivot] < nums[left]:
                    right = pivot - 1
                else:
                    left = pivot + 1



    def binary_search(left, right):

        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                return pivot
            else:
                if nums[pivot] < target:
                    left = pivot + 1
                else:
                    right = pivot - 1

        return -1

    if len(nums) == 0:
        return -1

    if len(nums) == 1:
        return 0 if nums[0] == target else -1


    rotated_index = rotate_index(0, len(nums) - 1)

    # now do two searches on each subset of nums
    result = binary_search(0, rotated_index -1)
    if result is not -1:
        return result

    return binary_search(rotated_index, len(nums) - 1)
