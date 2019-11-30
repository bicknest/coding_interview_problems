from product_of_three import product_of_three

def test_function_throws_error_if_not_three_items():
    assert product_of_three([]) == 'Cant create product of three with less than three numbers'

def test_function_correctly_returns_only_positive():
    numbers = [1, 2, 3, 4, 5, 6]
    assert product_of_three(numbers) == 120

def test_function_returns_correctly_only_negative():
    numbers = [-1, -3, -4, -6]
    assert product_of_three(numbers) == -12

def test_function_returns_correctly_pos_and_neg():
    numbers = [-100, -3, 8, 9, 10]
    assert product_of_three(numbers) == 3000
