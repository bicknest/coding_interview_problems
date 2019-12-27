const bestLine = require("../solution");

test("tests a two line graph", () => {
  const points = [
    { x: 0, y: 0 },
    { x: 1, y: 1 },
    { x: 2, y: 2 },
    { x: 1, y: 2 },
    { x: 2, y: 4 }
  ];
  expect(bestLine(points)).toEqual("m: 1, b: 0");
});
