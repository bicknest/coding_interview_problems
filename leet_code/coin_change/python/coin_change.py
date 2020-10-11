import math

def coin_change(coins, amount):
    number_of_coins = [0] * (amount + 1)
    for i in range(1, amount + 1):
        min_coins = math.inf
        for coin in coins:
            if i - coin >= 0:
                if (number_of_coins[i - coin] != -1):
                    min_coins = min(number_of_coins[i - coin] + 1, min_coins)
        if min_coins == math.inf:
            number_of_coins[i] = -1
        else:
            number_of_coins[i] = min_coins

    return number_of_coins.pop()
