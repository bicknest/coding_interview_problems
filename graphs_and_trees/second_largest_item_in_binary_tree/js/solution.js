function findLargest(treeRoot) {
  if (treeRoot.right) {
    return findLargest(treeRoot.right);
  }
  return treeRoot.value;
}

function findSecondLargest(rootNode) {
  if (!rootNode || (!rootNode.left && !rootNode.right)) {
    return "Tree must have two nodes";
  }

  let current = rootNode;

  while (current) {
    if (current.left && !current.right) {
      return findLargest(current.left);
    }

    if (current.right && !current.left && !current.right.right) {
      return current.value;
    }
    current = current.right;
  }
}

module.exports = findSecondLargest;
