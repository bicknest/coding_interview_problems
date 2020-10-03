def product_of_array(nums):
    # create lists L and R that are the length of nums
    # each list stores the product of all numbers to the L of i, and so on

    # trick/insight here is that you can use dp to create left_product and right_product
    # arrays with just O(n)

    output = [0 for _ in range(len(nums))]
    left_products = [0 for _ in range(len(nums))]
    right_products = [0 for _ in range(len(nums))]

    left_products[0] = 1
    for i in range(1, len(nums)):
        left_products[i] = nums[i - 1] * left_products[i - 1]

    right_products[-1] = 1
    for i in reversed(range((len(nums) - 1))):
        right_products[i] = nums[i + 1] * right_products[i + 1]

    for i in range(len(nums)):
        output[i] = left_products[i] * right_products[i]

    return output
