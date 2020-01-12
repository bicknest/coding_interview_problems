const changePossibilitiesBottomUp = require("../solution");

test("tests a simple case of denominations", () => {
  const amount = 10;
  const denominations = [1, 10];
  expect(changePossibilitiesBottomUp(amount, denominations)).toEqual(2);
});

test("tests a more complicated case", () => {
  const amount = 26;
  const denominations = [1, 5, 10, 25];
  expect(changePossibilitiesBottomUp(amount, denominations)).toEqual(13);
});

test("tests a medium case", () => {
  const amount = 25;
  const denominations = [5, 10, 25];
  expect(changePossibilitiesBottomUp(amount, denominations)).toEqual(4);
});
