from knapsack import max_knapsack_value

def tests_an_easy_set_of_items():
    items = [(1, 1), (1, 2)]
    capacity = 10
    assert max_knapsack_value(items, capacity) == 20

def tests_more_complicated_case():
    items = [(1, 1), (2, 4)]
    capacity = 11
    assert max_knapsack_value(items, capacity) == 21

def tests_a_bigger_set():
    items = [(7, 160), (3, 90), (2, 15)]
    capacity = 20
    assert max_knapsack_value(items, capacity) == 555
