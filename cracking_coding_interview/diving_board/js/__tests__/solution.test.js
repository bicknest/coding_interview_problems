const generateDivingBoardLengths = require("../solution");

function compare(a, b) {
  return a - b;
}

test("test simple case", () => {
  const shorter = 2;
  const longer = 4;
  const lengths = [shorter, longer];
  expect(generateDivingBoardLengths(1, shorter, longer).sort(compare)).toEqual(
    lengths.sort(compare)
  );
});

test("test k at two", () => {
  const shorter = 2;
  const longer = 4;
  const lengths = [shorter + shorter, shorter + longer, longer + longer];
  expect(generateDivingBoardLengths(2, shorter, longer).sort(compare)).toEqual(
    lengths.sort(compare)
  );
});

test("test k at three", () => {
  const shorter = 2;
  const longer = 4;
  const lengths = [
    shorter + shorter + shorter,
    shorter + shorter + longer,
    shorter + longer + longer,
    longer + longer + longer
  ];
  expect(generateDivingBoardLengths(3, shorter, longer).sort(compare)).toEqual(
    lengths.sort(compare)
  );
});
