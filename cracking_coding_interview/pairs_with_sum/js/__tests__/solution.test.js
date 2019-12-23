const pairOfSums = require("../solution");

test("test small array", () => {
  const pairs = [1, 3, 6, 8, 10, 15];
  const target_sum = 9;
  expect(pairOfSums(pairs, target_sum).sort()).toEqual([1, 8, 3, 6].sort());
});

test("test array with negatives", () => {
  const pairs = [-1, 3, 9, 0];
  const target_sum = 2;
  expect(pairOfSums(pairs, target_sum).sort()).toEqual([-1, 3].sort());
});
