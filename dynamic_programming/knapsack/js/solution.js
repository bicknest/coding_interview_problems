function maxKnapsackValue(items, capacity) {
  const maxVals = [];
  for (let i = 0; i <= capacity; i++) {
    let maxVal = 0;
    items.forEach(item => {
      if (i - item.weight >= 0) {
        maxVal = Math.max(maxVals[i - item.weight] + item.value, maxVal);
      }
    });
    maxVals[i] = maxVal;
  }
  return maxVals[capacity];
}

module.exports = maxKnapsackValue;
