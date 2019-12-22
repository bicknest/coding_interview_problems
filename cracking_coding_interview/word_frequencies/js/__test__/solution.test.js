const countWordFrequency = require("../solution");

test("tests counts a three word book", () => {
  const book = "bingo bingo bingo";
  const wordMap = countWordFrequency(book);
  expect(wordMap.get("bingo")).toEqual(3);
});

test("tests book with punctuation", () => {
  const book = "bingo, bingo: bingo.";
  const wordMap = countWordFrequency(book);
  expect(wordMap.get("bingo")).toEqual(3);
});

test("tests book with capitalization", () => {
  const book = "Bingo, bingo: album.";
  const wordMap = countWordFrequency(book);
  expect(wordMap.get("bingo")).toEqual(2);
  expect(wordMap.get("album")).toEqual(1);
});
