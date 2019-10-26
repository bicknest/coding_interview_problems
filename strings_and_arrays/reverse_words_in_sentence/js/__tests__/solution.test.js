const reverseInPlace = require("../solution");
const reverseWordsAndSentence = require("../solution");

test("reverses an array of chars correctly", () => {
  const word = ["a", "r", "r", "a", "y"];
  reverseInPlace(word);
  expect(word).toEqual(word.reverse());
});

test("reverses an array of 1 char correctly", () => {
  const word = ["a"];
  reverseInPlace(word);
  expect(word).toEqual(word.reverse());
});

test("reverses a sentence correctly", () => {
  const sentence = "We had a fun time at the park";
  const answer = "park the at time fun a had We";
  const sentenceArray = sentence.split("");
  reverseWordsAndSentence(sentenceArray);
  expect(sentenceArray.join("")).toEqual(answer);
});
