const largestContiguousSequence = require("../solution");

test("Tests simple sequence", () => {
  const sequence = [2, -8, 3, -2, 4, -10];
  expect(largestContiguousSequence(sequence)).toBe(5);
});

test("test a different sequence", () => {
  const sequence = [2, -8, 3, -2, 4, -10, 100];
  expect(largestContiguousSequence(sequence)).toBe(100);
});
