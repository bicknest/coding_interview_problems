class NumberOfIslands:

    def __init__(self, grid):
        self.grid = grid
        self.dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        self.m = len(grid)
        if self.m:
            self.n = len(grid[0])
        else:
            self.n = None
        self.visited = set()
        self.island_count = 0

    def land_neighbors(self, current_node):
        neighbors = []
        x, y = current_node
        for x_add, y_add in self.dirs:
            if 0 <= x + x_add < self.n and 0 <= y + y_add < self.m and self.grid[y + y_add][x + x_add] == "1":
                neighbors.append((x + x_add, y + y_add))
        
        return neighbors

    @property
    def number_of_islands(self):

        if self.n is None or self.n is 0:
            return 0

        for j, row in enumerate(self.grid):
            for i, space in enumerate(row):
                if space == "0" or (i, j) in self.visited:
                    continue
                frontier = []
                frontier.append((i, j))
                self.visited.add((i, j))
                while frontier:
                    current_node = frontier.pop()
                    land_neighbors = self.land_neighbors(current_node)
                    for land_neighbor in land_neighbors:
                        if land_neighbor not in self.visited:
                            self.visited.add(land_neighbor)
                            frontier.append(land_neighbor)

                self.island_count += 1

        return self.island_count
