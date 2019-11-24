const findSecondLargest = require("../solution");

function Node(value, left, right) {
  this.value = value;
  this.left = left;
  this.right = right;
}

test("tests to see if a null tree root was passed in", () => {
  const node = null;
  expect(findSecondLargest(node)).toEqual("Tree must have two nodes");
});

test("tests to see if it returns the second largest with just two items", () => {
  const rootNode = new Node(10);
  rootNode.right = new Node(15);
  expect(findSecondLargest(rootNode)).toEqual(10);
});

test("tests to see if it returns the second largest, with one left node", () => {
  const rootNode = new Node(10);
  rootNode.left = new Node(3);
  expect(findSecondLargest(rootNode)).toEqual(3);
});

test("tests to see if it returns the second largest, with a big right tree", () => {
  const rootNode = new Node(10);
  rootNode.right = new Node(12);
  rootNode.right.right = new Node(15);
  rootNode.right.right.right = new Node(17);
  expect(findSecondLargest(rootNode)).toEqual(15);
});

test("tests to see if it returns the second largest, with a left then a big right tree", () => {
  const rootNode = new Node(100);
  rootNode.left = new Node(10);
  rootNode.left.right = new Node(15);
  rootNode.left.right.right = new Node(19);
  expect(findSecondLargest(rootNode)).toEqual(19);
});
