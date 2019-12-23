function generateDivingBoardLengths(k, shorter, longer) {
  const lengths = [];
  for (let i = 0; i < k + 1; i++) {
    length_to_add = shorter * i + longer * (k - i);
    lengths.push(length_to_add);
  }
  return lengths;
}

module.exports = generateDivingBoardLengths;
