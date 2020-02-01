const isCodeValid = require("../solution");

it("should return true with a simple code input", () => {
  const code = "functionCall()";
  expect(isCodeValid(code)).toEqual(true);
});

it("should return false with a simple false input", () => {
  const code = "functionCall(";
  expect(isCodeValid(code)).toEqual(false);
});

it("should return true with some nested brackets and parenths", () => {
  const code = "functionCall({payload: {object}}[{[data and cool code]}])";
  expect(isCodeValid(code)).toEqual(true);
});

it("should return false when the nested brackets dont line up right", () => {
  const code = "functionCall({payload: }})[]";
  expect(isCodeValid(code)).toEqual(false);
});

it("should return false when not enough openers for closers", () => {
  const code = "functionCall()))))";
  expect(isCodeValid(code)).toEqual(false);
});
