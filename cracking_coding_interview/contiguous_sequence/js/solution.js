function largestContiguousSequence(sequence) {
  let maxSoFar = 0;
  let maxEndingHere = 0;

  for (let i = 0; i < sequence.length; i++) {
    maxEndingHere += sequence[i];
    if (maxEndingHere < 0) {
      maxEndingHere = 0;
    }
    if (maxSoFar < maxEndingHere) {
      maxSoFar = maxEndingHere;
    }
  }
  return maxSoFar;
}

module.exports = largestContiguousSequence;
