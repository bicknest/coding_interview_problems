from fib_memoized import fib

def tests_zeroth_number():
    assert fib(0) == 0

def tests_first_number():
    assert fib(1) == 1

def tests_eighth_number():
    assert fib(8) == 21
