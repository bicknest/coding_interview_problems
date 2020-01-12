function reconstructPath(howWeReachedNodes, startNode, endNode) {
  const reversedPath = [];

  // start from the end of the path and work backwards
  let currentNode = endNode;

  while (currentNode !== null) {
    reversedPath.push(currentNode);
    currentNode = howWeReachedNodes[currentNode];
  }

  // Reverse path to get the right order
  return reversedPath.reverse();
}

function bfsGetPath(graph, startNode, endNode) {
  // first deal with the cases of nodes not being in graph
  if (!graph.hasOwnProperty(startNode)) {
    return "Start node not in graph";
  }
  if (!graph.hasOwnProperty(endNode)) {
    return "End node not in graph";
  }

  // this is a queue, will use shift (inefficient)
  const nodesToVisit = [];
  nodesToVisit.push(startNode);

  // keep track of how we got to each node
  // we'll use this to reconstruct the shortest path at the end
  // we'll also use this to keep track of which nodes we've already visited
  const howWeReachedNodes = {};
  howWeReachedNodes[startNode] = null;

  while (nodesToVisit.length) {
    const currentNode = nodesToVisit.shift();

    // stop when we reach the end node
    if (currentNode === endNode) {
      return reconstructPath(howWeReachedNodes, startNode, endNode);
    }

    // for each of the current nodes neighbors check if that neighbor
    // has been visited
    // if it hasn't add it to the nodesToVisit queue
    graph[currentNode].forEach(neighbor => {
      if (!howWeReachedNodes.hasOwnProperty(neighbor)) {
        nodesToVisit.push(neighbor);
        howWeReachedNodes[neighbor] = currentNode;
      }
    });
  }
  // if we get here we never got to the currentNode from endNode
  return "No path from start node to end node";
}

module.exports = bfsGetPath;
