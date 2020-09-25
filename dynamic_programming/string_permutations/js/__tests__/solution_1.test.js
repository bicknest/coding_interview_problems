const permute = require("../solution_1");

test("tests a string that is only two letters long", () => {
  const smallString = "ab";
  const expectedSet = new Set(["ba", "ab"]);
  expect(permute(smallString)).toEqual(expectedSet);
});

test("tests a string that is three letters long", () => {
  const threeString = "abc";
  const expectedSet = new Set(["abc", "bac", "cab", "cba", "bca", "acb"]);
  expect(permute(threeString)).toEqual(expectedSet);
});

test("tests a string that has dupes", () => {
  const dupeString = "aab";
  const expectedSet = new Set(["aab", "aba", "baa"]);
  expect(permute(dupeString)).toEqual(expectedSet);
});
