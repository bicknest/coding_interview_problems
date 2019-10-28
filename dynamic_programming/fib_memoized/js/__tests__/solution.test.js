const Fib = require("../solution");

test("tests throw error if a negative number is passed in", () => {
  const FibCalculator = new Fib();
  expect(FibCalculator.fibonacci(-1)).toEqual("No negative numbers in series");
});

test("tests if the 0th number is 0", () => {
  const FibCalculator = new Fib();
  expect(FibCalculator.fibonacci(0)).toEqual(0);
});

test("tests if the 1th number is 1", () => {
  const FibCalculator = new Fib();
  expect(FibCalculator.fibonacci(1)).toEqual(1);
});

test("tests if the 8th number is 21", () => {
  const FibCalculator = new Fib();
  expect(FibCalculator.fibonacci(8)).toEqual(21);
});
