const bfsGetPath = require("../solution");

test("tests a very straightforward graph", () => {
  const network = {
    Mike: ["Ally"],
    Ally: ["Mike", "Ben"],
    Ben: ["Emilia", "Ally"],
    Emilia: ["Ben"]
  };
  const startNode = "Mike";
  const endNode = "Emilia";
  expect(bfsGetPath(network, startNode, endNode)).toEqual([
    "Mike",
    "Ally",
    "Ben",
    "Emilia"
  ]);
});

test("tests no start node in graph", () => {
  const network = {
    Mike: ["Bobby"],
    Bobby: ["Mike"]
  };
  const startNode = "Biggy Smalls";
  const endNode = "Mike";
  expect(bfsGetPath(network, startNode, endNode)).toEqual(
    "Start node not in graph"
  );
});

test("tests no end node in graph", () => {
  const network = {
    Mike: ["Bobby"],
    Bobby: ["Mike"]
  };
  const startNode = "Mike";
  const endNode = "Biggy Smalls";
  expect(bfsGetPath(network, startNode, endNode)).toEqual(
    "End node not in graph"
  );
});

test("tests no path from start node to end node", () => {
  const network = {
    Mike: ["Bobby"],
    Bobby: ["Mike"],
    Billy: []
  };
  const startNode = "Mike";
  const endNode = "Billy";
  expect(bfsGetPath(network, startNode, endNode)).toEqual(
    "No path from start node to end node"
  );
});
