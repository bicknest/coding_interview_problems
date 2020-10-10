def spiral_matrix(matrix):
    if len(matrix) < 1:
        return []
    m = len(matrix)
    n = len(matrix[0])
    visited = set()
    start = (0, 0)
    # clockwise chirality
    dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    
    frontier = [start]
    visited.add(start)
    spiraled = []
    current_direction = 0
    
    while frontier:
        node = frontier.pop()
        x, y = node
        spiraled.append(matrix[y][x])
        next_node, current_direction = decide_next_node(node, current_direction, m, n, dirs, visited)
        if next_node is not None:
            frontier.append(next_node)
            visited.add(next_node)
    
    return spiraled
        
        
def decide_next_node(node, current_direction, m, n, dirs, visited):
    # if the next node based on current direction is out of range or has been
    # visited, change direction and get next node
    direction_counter = 0
    x_add, y_add = dirs[current_direction % len(dirs)]
    x, y = node
    while direction_counter < 4:
        if ((0 <= x + x_add < n) and (0 <= y + y_add < m) and ((x + x_add, y + y_add) not in visited)):
            return (x + x_add, y + y_add), current_direction
        else:
            direction_counter += 1
            current_direction += 1
            x_add, y_add = dirs[current_direction % len(dirs)]
        
    return None, current_direction
