function bestLine(points) {
  lineCounts = new Map();
  for (let i = 0; i < points.length; i++) {
    for (let j = 0; j < points.length; j++) {
      if (i !== j) {
        let { x: x1, y: y1 } = points[i];
        let { x: x2, y: y2 } = points[j];
        if (x2 > x1) {
          let m = (y2 - y1) / (x2 - x1);
          let b = y1 - m * x1;
          let line = `m: ${m}, b: ${b}`;
          if (lineCounts.has(line)) {
            const count = lineCounts.get(line) + 1;
            lineCounts.set(line, count);
          } else {
            lineCounts.set(line, 1);
          }
        }
      }
    }
  }
  let maxCount = 0;
  let bestLine = "";
  lineCounts.forEach((count, line) => {
    if (count > maxCount) {
      bestLine = line;
      maxCount = count;
    }
  });
  return bestLine;
}

module.exports = bestLine;
