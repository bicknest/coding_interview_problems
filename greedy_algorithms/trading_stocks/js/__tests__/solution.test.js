const tradeStocks = require("../solution");

test("tests that that the function throws an error if prices doesnt have two days", () => {
  expect(tradeStocks([1])).toEqual(
    "Cant make a trade without two days of stocks"
  );
});

test("tests that the function returns correct diff as prices increase", () => {
  const prices = [1, 2, 3, 4, 5, 6];
  expect(tradeStocks(prices)).toEqual(5);
});

test("tests that the function returns negative if thats the only option", () => {
  const prices = [5, 3];
  expect(tradeStocks(prices)).toEqual(-2);
});

test("tests that the function returns correctly if prices rise then fall", () => {
  const prices = [2, 3, 5, 7, 4, 1];
  expect(tradeStocks(prices)).toEqual(5);
});

test("tests returns if prices fall then rise", () => {
  const prices = [9, 8, 7, 5, 8, 10];
  expect(tradeStocks(prices)).toEqual(5);
});
