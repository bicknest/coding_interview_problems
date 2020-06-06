def number_of_possible_food_trucks(city, rows, columns):
    Searcher = CitySearcher(city, rows, columns)
    while Searcher.blocks_to_visit:
        Searcher.search()
    return Searcher.number_of_trucks


class CitySearcher:

    def __init__(self, city, rows, columns):
        self.city = city
        self.rows = rows
        self.columns = columns
        self.number_of_trucks = 0
        self.dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        self.all_blocks, self.blocks_to_visit = self.generate_block_sets()

    def generate_block_sets(self):
        park_blocks = set()
        all_blocks = set()
        for i, row in enumerate(self.city):
            for j, block in enumerate(row):
                if block == 1:
                    park_blocks.add((i, j))
                all_blocks.add((i,j))
        return all_blocks, park_blocks


    def neighbors(self, block):
        neighbor_list = []
        for dir in self.dirs:
            neighbor = (block[0] + dir[0], block[1] + dir[1])
            if neighbor in self.all_blocks:
                neighbor_list.append(neighbor)
        return neighbor_list


    # alternate neighbor (saves space of storing self.all_blocks when we know the N and M)
    """
    def alternate_neighbors(self, block):
        neighbor_list = []
        for dir in self.dirs:
            neighbor = (block[0] + dir[0], block[1] + dir[1])
            if 0 <= neighbor[0] < self.rows and 0 <= neighbor[1] < self.columns:
                neighbor_list.append(neighbor)
        return neighbor_list
    """

    
    def search(self):
        starting_block = self.blocks_to_visit.pop()
        frontier =  [starting_block]
        while frontier:
            current_block = frontier.pop(0)
            neighbor_blocks = self.neighbors(current_block)
            for neighbor_block in neighbor_blocks:
                if neighbor_block in self.blocks_to_visit:
                    frontier.append(neighbor_block)
                    self.blocks_to_visit.remove(neighbor_block)
        self.number_of_trucks += 1
