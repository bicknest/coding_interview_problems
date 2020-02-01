const MaxStack = require("../solution");

it("should keep track easily of ascending stack pushing", () => {
  const myMaxStack = new MaxStack();
  myMaxStack.push(1);
  myMaxStack.push(2);
  myMaxStack.push(3);
  expect(myMaxStack.getMax()).toEqual(3);
});

it("should keep track of descending stack pushing", () => {
  const myMaxStack = new MaxStack();
  myMaxStack.push(3);
  myMaxStack.push(2);
  myMaxStack.push(1);
  expect(myMaxStack.getMax()).toEqual(3);
});

it("should keep track of some pushing and popping", () => {
  const myMaxStack = new MaxStack();
  const shouldBeNull = myMaxStack.pop();
  myMaxStack.push(3);
  myMaxStack.push(19);
  myMaxStack.pop();
  myMaxStack.push(4);
  myMaxStack.push(2);
  myMaxStack.pop();
  expect(myMaxStack.getMax()).toEqual(4);
  expect(shouldBeNull).toBeNull();
});
