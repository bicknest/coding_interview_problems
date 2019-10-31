function makeChange(amount) {
    const denominations = [25, 10, 5, 1];
    let totalCoins = 0;
    denominations.forEach((denom) => {
       totalCoins += Math.floor(amount / denom);
       amount = amount % denom;
    });
    return totalCoins;
}

module.exports = makeChange;