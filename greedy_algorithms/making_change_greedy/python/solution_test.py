from solution import makeChange

def test_denominations():
    assert makeChange(25) == 1
    assert makeChange(10) == 1
    assert makeChange(5) == 1
    assert makeChange(1) == 1
    
def test_four_pennies():
    assert makeChange(4) == 4

def test_higher_number():
    assert makeChange(31) == 3
