from fib_bottom_up import fib_bottom_up

def test_negative_number():
    assert fib_bottom_up(-1) == 'No negative numbers in series'

def test_zeroth_number():
    assert fib_bottom_up(0) == 0

def test_first_number():
    assert fib_bottom_up(1) == 1

def test_eighth_number():
    assert fib_bottom_up(8) == 21
