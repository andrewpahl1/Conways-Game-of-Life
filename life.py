import numpy as np

class GameOfLife:

    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), bool)
        self.cache = dict()
        self.living_cells = set()
    
    def __repr__(self):
        return  f"Life(height={self.height}, width={self.width})"
    
    def __str__(self):
        to_str = {False:"░",True:"█"}
        return "\n".join("".join(to_str[cell] for cell in row) for row in self.grid)

    def get_neighbors(self, coords):
        if coords in self.cache:
            return self.cache[coords]
        y, x = coords
        res = list()
        for i in range(-1, 2):
            for j in range(-1, 2):
                if any((i == j == 0, min(y+i, x+j) < 0, y + i >= self.height, x + j >= self.width)):
                    continue
                else:
                    res.append((y+i,x+j))
        self.cache[coords] = set(res)
        return self.cache[coords]
        
    def update_state(self, coords, state):
        if self.grid[coords[0]][coords[1]] == state:
            return
        self.grid[coords[0]][coords[1]] = state
        if state == True:
            self.living_cells.add(coords)
        else:
            self.living_cells.remove(coords)
    
    def update_all(self):
        all_neighbors = set()
        newly_dead_cells = set()
        newly_alive_cells = set()
        for cell in self.living_cells:
            neighbors = self.get_neighbors(cell)
            living_neighbors_count = sum(self.grid[pos[0]][pos[1]] for pos in neighbors)
            if living_neighbors_count not in (2, 3):
                newly_dead_cells.add(cell)
            all_neighbors |= neighbors
        for cell in all_neighbors:
            living_neighbor_count = sum(self.grid[pos[0]][pos[1]] for pos in self.get_neighbors(cell))
            if living_neighbor_count == 3:
                newly_alive_cells.add(cell)
        for cell in newly_alive_cells:
            self.update_state(cell, True)
        for cell in newly_dead_cells:
            self.update_state(cell, False)
            
    def reset(self):
        self.grid = np.zeros((self.height, self.width), bool)
        self.living_cells = set()
