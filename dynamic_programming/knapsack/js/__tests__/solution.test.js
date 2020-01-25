const maxKnapsackValue = require("../solution");

test("tests an easy set of items", () => {
  const items = [{ weight: 1, value: 1 }, { weight: 1, value: 2 }];
  const capacity = 10;
  expect(maxKnapsackValue(items, capacity)).toEqual(20);
});

test("tests a bit more complicated set of items", () => {
  const items = [{ weight: 1, value: 1 }, { weight: 2, value: 4 }];
  const capacity = 11;
  expect(maxKnapsackValue(items, capacity)).toEqual(21);
});

test("tests a bigger set of items", () => {
  const items = [
    { weight: 7, value: 160 },
    { weight: 3, value: 90 },
    { weight: 2, value: 15 }
  ];
  const capacity = 20;
  expect(maxKnapsackValue(items, capacity)).toEqual(555);
});
