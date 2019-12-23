function pairOfSums(pairs, targetSum) {
  const potentialAddends = new Set();
  pairs.forEach(num => {
    potentialAddends.add(targetSum - num);
  });
  const intersection = pairs.filter(num => potentialAddends.has(num));
  return intersection;
}

module.exports = pairOfSums;
