from coin_change import coin_change

def test_coin_change():
    coins = [1, 2, 5]
    amount = 11
    assert coin_change(coins, amount) == 3

def test_no_change():
    coins = [2]
    amount = 3
    assert coin_change(coins, amount) == -1

def test_no_ways_to_make_change():
    coins = [1]
    amount = 0
    assert coin_change(coins, amount) == 0

def test_one_way():
    coins = [1]
    amount = 1
    assert coin_change(coins, amount) == 1

def test_two_ways():
    coins = [1]
    amount = 2
    assert coin_change(coins, amount) == 2
