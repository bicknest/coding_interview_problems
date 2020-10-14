def generate_neighbors(node, word_dict, visited):
    neighbors = []
    for word in word_dict:
        try:
            if node.index(word) == 0 and node[len(word):] not in visited:
                neighbors.append(node[len(word):])
        except:
            pass

    return neighbors


def word_break(s, word_dict):
    visited = set([s])
    frontier = [s]

    while frontier:
        node = frontier.pop()
        if node == "":
            return True
        neighbors = generate_neighbors(node, word_dict, visited)
        for neighbor in neighbors:
            frontier.append(neighbor)
            visited.add(neighbor)

    return False
