def makeChange(amount):
    denominations = [25, 10, 5, 1]
    totalCoins = 0
    for denomination in denominations:
        totalCoins += amount / denomination
        amount = amount % denomination
    return totalCoins