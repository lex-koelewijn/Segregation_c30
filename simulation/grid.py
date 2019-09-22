import random


class Grid():
    def __init__(self, height, width):
        self.height = height
        self.width = width

        self.grid = []
        self.empty_spots = set()

        # Fill 2D grid with empty grid spaces
        for x in range(self.width):
            col = []
            for y in range(self.height):
                col.append(None)
                self.empty_spots.add((x, y))
            self.grid.append(col)

    def __getitem__(self, index):
        return self.grid[index]

    def place_agent(self, pos, agent):
        x, y = pos
        self.grid[x][y] = agent
        self.empty_spots.discard(pos)

    def remove_agent(self, pos, agent):
        x, y = pos
        self.grid[x][y] = None
        self.empty_spots.add(pos)

    def move_to_empty(self, agent):
        pos = agent.pos
        new_pos = random.choice(sorted(self.empty_spots))
        self.place_agent(new_pos, agent)
        agent.pos = new_pos
        self.remove_agent(pos, agent)

    def get_neighbors(self, pos):
        x, y = pos
        coordinates = set()
        for neighbors_x in range(3):
            for neighbors_y in range(3):
                if neighbors_x != 1 and neighbors_y != 1:
                    if x < 0 or x >= self.width or y < 0 or y >= self.height:
                        pass
                    else:
                        coordinates.add((neighbors_x, neighbors_y))

        return coordinates