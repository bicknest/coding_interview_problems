from collections import deque


def minimum_knights_moves(x, y):
    distances = dict()
    visited = set()
    frontier = deque()

    frontier.append((0, 0))
    visited.add((0, 0))
    distances[(0, 0)] = 0

    while frontier:
        node = frontier.popleft()
        node_neighbors = generate_knights_neighbors(node, visited)
        for neighbor in node_neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                distances[neighbor] = distances[node] + 1
                frontier.append(neighbor)
                if neighbor == (x, y):
                    return distances[neighbor]

    


def generate_knights_neighbors(coords, visited):
    dirs = [[2, 1], [-2, 1], [2, -1], [-2, -1], [1, 2], [1, -2], [-1, -2], [-1, 2]]
    neighbors = []
    x, y = coords
    for x_add, y_add in dirs:
        new_x_coord = x + x_add
        new_y_coord = y + y_add
        neighbors.append((new_x_coord, new_y_coord))

    return neighbors
