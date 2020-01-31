const diceFunctions = require("../solution");

test("tests that rand7 always returns a number between 1 and 7", () => {
  const roll1 = diceFunctions.rand7();
  const roll2 = diceFunctions.rand7();
  const roll3 = diceFunctions.rand7();
  expect(roll1).toBeGreaterThanOrEqual(1);
  expect(roll1).toBeLessThan(8);
  expect(roll2).toBeGreaterThanOrEqual(1);
  expect(roll2).toBeLessThan(8);
  expect(roll3).toBeGreaterThanOrEqual(1);
  expect(roll3).toBeLessThan(8);
});
