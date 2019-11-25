const isBinarySearchTree = require("../iterative_solution");

function Node(value, left, right) {
  this.value = value;
  this.left = left;
  this.right = right;
}

test("tests to see if a null tree root was passed in", () => {
  const node = null;
  expect(isBinarySearchTree(node)).toEqual("Tree root needs a value");
});

test("tests to see if it returns true with just two items defined correctly", () => {
  const rootNode = new Node(10);
  rootNode.right = new Node(15);
  expect(isBinarySearchTree(rootNode)).toEqual(true);
});

test("tests to see if it returns true, with one left node", () => {
  const rootNode = new Node(10);
  rootNode.left = new Node(3);
  expect(isBinarySearchTree(rootNode)).toEqual(true);
});

test("tests to see if it returns true with with a big right tree", () => {
  const rootNode = new Node(10);
  rootNode.right = new Node(12);
  rootNode.right.right = new Node(15);
  rootNode.right.right.right = new Node(17);
  expect(isBinarySearchTree(rootNode)).toEqual(true);
});

test("tests to see if it returns true with this structure of BST", () => {
  const rootNode = new Node(100);
  rootNode.left = new Node(10);
  rootNode.left.right = new Node(15);
  rootNode.left.right.right = new Node(19);
  expect(isBinarySearchTree(rootNode)).toEqual(true);
});

test("tests to see if it returns false with a clearly wrong BST", () => {
  const rootNode = new Node(100);
  rootNode.left = new Node(150);
  rootNode.right = new Node(80);
  expect(isBinarySearchTree(rootNode)).toEqual(false);
});
