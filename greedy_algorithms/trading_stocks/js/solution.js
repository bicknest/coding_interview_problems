function tradeStocks(prices) {
  if (prices.length < 2) {
    return "Cant make a trade without two days of stocks";
  }
  let minPrice = Math.min(prices[0], prices[1]);
  let maxDiff = prices[1] - prices[0];
  for (let i = 2; i < prices.length; i++) {
    minPrice = Math.min(prices[i], minPrice);
    maxDiff = Math.max(maxDiff, prices[i] - minPrice);
  }
  return maxDiff;
}

module.exports = tradeStocks;
