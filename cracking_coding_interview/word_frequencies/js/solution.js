function countWordFrequency(book) {
  const stripped = book.replace(/[.,\/#!;:-]/g, "");
  const wordList = stripped.split(" ");
  wordList.forEach((word, idx) => {
    wordList[idx] = word.toLowerCase();
  });
  const wordMap = new Map();
  wordList.forEach(word => {
    if (wordMap.has(word)) {
      const count = wordMap.get(word) + 1;
      wordMap.set(word, count);
    } else {
      wordMap.set(word, 1);
    }
  });
  return wordMap;
}

module.exports = countWordFrequency;
