const fibFactory = require("../solution");

test("tests throw error if a negative number is passed in", () => {
  const fib = fibFactory();
  expect(fib(-1)).toEqual("No negative numbers in series");
});

test("tests if the 0th number is 0", () => {
  const fib = fibFactory();
  expect(fib(0)).toEqual(0);
});

test("tests if the 1th number is 1", () => {
  const fib = fibFactory();
  expect(fib(1)).toEqual(1);
});

test("tests if the 8th number is 21", () => {
  const fib = fibFactory();
  expect(fib(8)).toEqual(21);
});
