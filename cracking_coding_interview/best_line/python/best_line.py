from collections import Counter

def best_line(points):
    line_counter = Counter()
    for i in range(0, len(points)):
        for j in range(0, len(points)):
            if i != j:
                x1, y1 = points[i]
                x2, y2 = points[j]
                if x2 > x1:
                    m = (y2 - y1) / (x2 - x1)
                    b = y1 - m * x1
                    line_tuple = (m, b)
                    line_counter.update([line_tuple])
    return line_counter.most_common(1)[0][0]
