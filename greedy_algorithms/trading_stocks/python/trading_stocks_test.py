from trading_stocks import trading_stocks

def test_function_throws_error_if_not_two_days():
    prices = [1]
    assert trading_stocks(prices) == 'Cant make a trade without two days of stocks'

def test_function_returns_correctly_prices_increase():
    prices = [1, 2, 3, 4, 5, 6]
    assert trading_stocks(prices) == 5

def test_function_returns_negative_if_prices_only_fall():
    prices = [5, 3]
    assert trading_stocks(prices) == -2

def test_function_returns_correctly_prices_rise_then_fall():
    prices = [2, 3, 5, 7, 4, 1]
    assert trading_stocks(prices) == 5

def test_returns_correctly_if_prices_fall_then_rise():
    prices = [9, 8, 7, 5, 8, 10]
    assert trading_stocks(prices) == 5
