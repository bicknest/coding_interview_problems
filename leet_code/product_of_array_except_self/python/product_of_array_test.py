from product_of_array import product_of_array

def test_simple_case():
    array = [1, 2, 3, 4]
    output = [24, 12, 8, 6]
    assert product_of_array(array) == output

def test_tricky_case():
    array = [1, 0]
    output = [0, 1]
    assert product_of_array(array) == output
