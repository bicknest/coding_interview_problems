function pairOfSums(pairs, targetSum) {
  const potentialAdditives = new Set();
  pairs.forEach(num => {
    potentialAdditives.add(targetSum - num);
  });
  const intersection = pairs.filter(num => potentialAdditives.has(num));
  return intersection;
}

module.exports = pairOfSums;
