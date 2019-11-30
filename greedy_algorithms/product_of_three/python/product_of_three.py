def product_of_three(numbers):
    if len(numbers) < 3:
        return "Cant create product of three with less than three numbers"

    # store max product of three, min/max product of two, and min and max
    max_product_three = numbers[0] * numbers[1] * numbers[2]
    max_product_two = max(numbers[0] * numbers[1], numbers[0] * numbers[2], numbers[1] * numbers[2])
    min_product_two = min(numbers[0] * numbers[1], numbers[0] * numbers[2], numbers[1] * numbers[2])
    minimum = min(numbers[0], numbers[1], numbers[2])
    maximum = min(numbers[0], numbers[1], numbers[2])

    # iterate over the list of numbers and update, (make sure to update in the correct order)
    for i in range(3, len(numbers)):
        max_product_three = max(max_product_two * numbers[i], min_product_two * numbers[i], max_product_three)
        max_product_two = max(max_product_two, minimum * numbers[i], maximum * numbers[i])
        min_product_two = min(min_product_two, minimum * numbers[i], maximum * numbers[i])
        minimum = min(numbers[i], minimum)
        maximum = max(numbers[i], maximum)

    return max_product_three
