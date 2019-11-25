function isBinarySearchTree(treeRoot) {
  if (!treeRoot || !treeRoot.value) {
    return "Tree root needs a value";
  }
  const nodeStack = [];
  nodeStack.push({
    node: treeRoot,
    upperBound: Number.POSITIVE_INFIINTY,
    lowerBound: Number.NEGATIVE_INFINITY
  });

  while (nodeStack.length) {
    const { node, upperBound, lowerBound } = nodeStack.pop();
    if (node.value >= upperBound || node.value <= lowerBound) {
      return false;
    }

    if (node.right) {
      nodeStack.push({
        node: node.right,
        upperBound,
        lowerBound: node.value
      });
    }
    if (node.left) {
      nodeStack.push({
        node: node.left,
        upperBound: node.value,
        lowerBound
      });
    }
  }
  return true;
}

module.exports = isBinarySearchTree;
