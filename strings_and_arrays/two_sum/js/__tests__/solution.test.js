const twoSum = require("../solution");

test("finds the correct indices of a simple target and sum", () => {
  const nums = [1, 2, 3, 5, 8];
  const target = 11;
  const [indexOne, indexTwo] = twoSum(nums, target);
  expect(indexOne).toEqual(4);
  expect(indexTwo).toEqual(2);
});

test("returns an error if the nums array does not have enough elements", () => {
  const nums = [11];
  const target = 11;
  expect(() => twoSum(nums, target)).toThrow(
    "Not enough elements in array for solution"
  );
});

test("no sums in the whole array", () => {
  const nums = [1, 2, 3, 4, 5];
  const target = 200;
  expect(() => twoSum(nums, target)).toThrow(
    "No elements found that add to the target"
  );
});
