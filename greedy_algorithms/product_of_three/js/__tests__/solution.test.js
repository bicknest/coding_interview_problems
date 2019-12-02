const productOfThree = require("../solution");

test("The function returns error if not three items", () => {
  expect(productOfThree([])).toEqual(
    "Cant create a product of three with less than three numbers"
  );
});

test("Function returns correctly with only positive numbers", () => {
  numbers = [1, 2, 3, 4, 5, 6];
  expect(productOfThree(numbers)).toEqual(120);
});

test("function returns correctly only negative nubmers", () => {
  numbers = [-1, -3, -4, -6];
  expect(productOfThree(numbers)).toEqual(-12);
});

test("function returns correctly positve and negative", () => {
  numbers = [-100, -3, 8, 9, 10];
  expect(productOfThree(numbers)).toEqual(3000);
});
