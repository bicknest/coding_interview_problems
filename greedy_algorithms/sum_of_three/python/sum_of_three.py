def sum_of_three(nums):

    if len(nums) < 3:
        return []

    positive_nums = []
    negative_nums = []
    count_of_zeros = 0
    for num in nums:
        if num == 0:
            count_of_zeros += 1
        elif num < 0:
            negative_nums.append(num)
        elif num > 0:
            positive_nums.append(num)


    zero_sums = set()
    
    negative_sums = generate_sums(negative_nums)
    positive_sums = generate_sums(positive_nums)

    for negative_num in negative_nums:
        for positive_item in positive_sums.items():
            if negative_num + positive_item[1] == 0:
                a1, a2 = positive_item[0]
                zero_sum_tuple = (a1, a2, negative_num)
                zero_sums.add(zero_sum_tuple)

    for positive_num in positive_nums:
        for negative_item in negative_sums.items():
            if positive_num + negative_item[1] == 0:
                a1, a2 = negative_item[0]
                zero_sum_tuple = (a1, a2, positive_num)
                zero_sums.add(zero_sum_tuple)

    if count_of_zeros > 0:
        for negative_num in negative_nums:
            for positive_num in positive_nums:
                if negative_num + positive_num == 0:
                    zero_sums.add((negative_num, positive_num, 0))

    if count_of_zeros > 2:
        zero_sums.add((0, 0, 0))

    sum_list = []
    for zero_sum in zero_sums:
        sum_list.append([x for x in zero_sum])

    return sum_list




def generate_sums(nums):
    sums = dict()
    for i in range(len(nums)):
        for j in range(len(nums)):
            a = nums[i]
            b = nums[j]
            if sums.get((b, a)) is None:
                sums[(a, b)] = a + b
    return sums
