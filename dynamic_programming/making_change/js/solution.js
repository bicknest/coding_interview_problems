function changePossibilitiesBottomUp(amount, denominations) {
  // Initialize an array of zeroes with indices up to amount
  const waysOfDoingNCents = new Array(amount + 1).fill(0);
  waysOfDoingNCents[0] = 1;

  denominations.forEach(coin => {
    for (let higherAmount = coin; higherAmount <= amount; higherAmount++) {
      const higherAmountRemainder = higherAmount - coin;
      waysOfDoingNCents[higherAmount] +=
        waysOfDoingNCents[higherAmountRemainder];
    }
  });
  return waysOfDoingNCents[amount];
}

module.exports = changePossibilitiesBottomUp;
