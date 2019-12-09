function colorGraph(graph, colors) {
  let BreakException = {};
  try {
    graph.forEach(node => {
      if (node.neighbors.has(node)) {
        throw BreakException;
      }

      const illegalColors = new Set();

      node.neighbors.forEach(neighbor => {
        if (neighbor.color !== null) {
          illegalColors.add(neighbor.color);
        }
      });

      for (let i = 0; i < colors.length; i++) {
        const color = colors[i];

        if (!illegalColors.has(color)) {
          node.color = color;
          break;
        }
      }
    });
  } catch (e) {
    return "Legal coloring impossible for node with loop";
  }
}

module.exports = colorGraph;
