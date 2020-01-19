const getPermutations = require("../solution");

test("tests a string that is only two letters long", () => {
  const smallString = "ab";
  const expectedSet = new Set(["ba"]);
  expect(getPermutations(smallString)).toEqual(expectedSet);
});

test("tests a string that is three letters long", () => {
  const threeString = "abc";
  const expectedSet = new Set(["bac", "cab", "cba", "bca"]);
  expect(getPermutations(threeString)).toEqual(expectedSet);
});
