const fibBottomUp = require("../solution");

test("tests throw error if a negative number is passed in", () => {
    expect(fibBottomUp(-1)).toEqual("No negative numbers in series");
});

test("tests if the 0th number is 0", () => {
    expect(fibBottomUp(0)).toEqual(0);
});

test("tests if the 1th number is 1", () => {
    expect(fibBottomUp(1)).toEqual(1);
});

test("tests if the 8th number is 21", () => {
    expect(fibBottomUp(8)).toEqual(21);
});