WEIGHT_INDEX = 0
VALUE_INDEX = 1

def max_knapsack_value(items, capacity):
    max_values = []
    for i in range(capacity + 1):
        max_value = 0
        for item in items:
            if i - item[WEIGHT_INDEX] >= 0:
                max_value = max(max_values[i - item[WEIGHT_INDEX]] + item[VALUE_INDEX], max_value)

        max_values.append(max_value)

    return max_values[capacity]

