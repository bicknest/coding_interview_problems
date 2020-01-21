const getPermutations = require("../solution");

test("tests a string that is only two letters long", () => {
  const smallString = "ab";
  const expectedSet = new Set(["ba", "ab"]);
  expect(getPermutations(smallString)).toEqual(expectedSet);
});

test("tests a string that is three letters long", () => {
  const threeString = "abc";
  const expectedSet = new Set(["abc", "bac", "cab", "cba", "bca", "acb"]);
  expect(getPermutations(threeString)).toEqual(expectedSet);
});

test("tests a string that has dupes", () => {
  const dupeString = "aab";
  const expectedSet = new Set(["aab", "aba", "baa"]);
  expect(getPermutations(dupeString)).toEqual(expectedSet);
});
