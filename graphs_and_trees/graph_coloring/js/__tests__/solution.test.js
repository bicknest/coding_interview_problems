const colorGraph = require("../solution");

test("tests to see if we can color a simple graph", () => {
  let node1 = { neighbors: new Set(), color: null };
  let node2 = { neighbors: new Set(), color: null };
  let node3 = { neighbors: new Set(), color: null };
  node1.neighbors.add(node2);
  node1.neighbors.add(node3);
  node2.neighbors.add(node1);
  node3.neighbors.add(node1);
  const graph = [node1, node2, node3];
  const colors = ["orange", "blue", "red"];
  colorGraph(graph, colors);
  expect(node1.color).not.toEqual(node2.color);
  expect(node1.color).not.toEqual(node3.color);
});

test("tests a cyclical graph", () => {
  let node1 = { neighbors: new Set(), color: null };
  let node2 = { neighbors: new Set(), color: null };
  let node3 = { neighbors: new Set(), color: null };
  node1.neighbors.add(node1);
  node1.neighbors.add(node3);
  node2.neighbors.add(node1);
  node2.neighbors.add(node3);
  node3.neighbors.add(node2);
  const graph = [node1, node2, node3];
  const colors = ["orange", "blue", "red"];
  expect(colorGraph(graph, colors)).toEqual(
    "Legal coloring impossible for node with loop"
  );
});

test("tests to see if we can color a full graph", () => {
  let node1 = { neighbors: new Set(), color: null };
  let node2 = { neighbors: new Set(), color: null };
  let node3 = { neighbors: new Set(), color: null };
  let node4 = { neighbors: new Set(), color: null };
  let node5 = { neighbors: new Set(), color: null };
  let node6 = { neighbors: new Set(), color: null };
  // Node 1
  node1.neighbors.add(node2);
  node1.neighbors.add(node3);
  node1.neighbors.add(node4);
  node1.neighbors.add(node5);
  // Node 2
  node2.neighbors.add(node1);
  node2.neighbors.add(node6);
  node2.neighbors.add(node4);
  node2.neighbors.add(node3);
  node2.neighbors.add(node5);

  // Node 3
  node3.neighbors.add(node1);
  node3.neighbors.add(node5);
  node3.neighbors.add(node4);
  node3.neighbors.add(node2);
  node3.neighbors.add(node6);
  // Node 4
  node4.neighbors.add(node1);
  node4.neighbors.add(node2);
  node4.neighbors.add(node3);
  node4.neighbors.add(node5);
  node4.neighbors.add(node6);
  // Node 5
  node5.neighbors.add(node1);
  node5.neighbors.add(node2);
  node5.neighbors.add(node3);
  node5.neighbors.add(node4);
  node5.neighbors.add(node6);
  // Node 6
  node6.neighbors.add(node1);
  node6.neighbors.add(node2);
  node6.neighbors.add(node3);
  node6.neighbors.add(node4);
  node6.neighbors.add(node5);

  const graph = [node1, node2, node3, node4, node5, node6];
  const colors = ["orange", "blue", "red", "black", "brown", "green", "teal"];
  colorGraph(graph, colors);
  expect(node1.color).not.toEqual(null);
  expect(node2.color).not.toEqual(null);
  expect(node3.color).not.toEqual(null);
  expect(node4.color).not.toEqual(null);
  expect(node5.color).not.toEqual(null);
  expect(node6.color).not.toEqual(null);
  expect(node1.color).not.toEqual(node2.color);
  expect(node1.color).not.toEqual(node3.color);
  expect(node1.color).not.toEqual(node4.color);
  expect(node1.color).not.toEqual(node5.color);
  expect(node1.color).not.toEqual(node6.color);
  expect(node2.color).not.toEqual(node6.color);
  expect(node2.color).not.toEqual(node4.color);
  expect(node3.color).not.toEqual(node5.color);
  expect(node3.color).not.toEqual(node4.color);
});
