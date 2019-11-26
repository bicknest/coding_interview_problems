def trading_stocks(prices):
    if len(prices) < 2:
        return "Cant make a trade without two days of stocks"

    minPrice = min(prices[0], prices[1])
    maxDiff = prices[1] - prices[0]
    for i in range(2, len(prices)):
        minPrice = min(prices[i], minPrice)
        maxDiff = max(prices[i] - minPrice, maxDiff)
    return maxDiff
