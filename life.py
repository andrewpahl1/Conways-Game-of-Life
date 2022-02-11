class GameOfLife:
    """Represents a non-infinite version of Conway's Game of Life. Contains the gamespace as a two-dimensional list of boolean values and several methods that implement the Game of Life's rules."""

    def __init__(self, height, width):
        self.width = width
        self.height = height
        self.grid = [[False for y in range(self.width)] for x in range(self.height)]
        self.cache = dict() # Store previously computed values from the get_neighbors method.
        self.living_cells = set() # Store the coordinates of all "living" (True) cells in self.grid.
    
    def __repr__(self):
        return  f"Life(height={self.height}, width={self.width})"
    
    def __str__(self):
        to_str = {False:"░",True:"█"}
        return "\n".join("".join(to_str[cell] for cell in row) for row in self.grid)

    def get_neighbors(self, coords):
        """Return the (up to) eight cells that border the cell at a given tuple of (y, z) coordinates."""
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
        """Updates a boolean value in self.grid, keeps a record of living cells in self.living_cells."""
        if self.grid[coords[0]][coords[1]] == state:
            return
        self.grid[coords[0]][coords[1]] = state
        if state == True:
            self.living_cells.add(coords)
        else:
            self.living_cells.remove(coords)
    
    def update_all(self):
        """Updates all cells in self.grid according to the rules of Conway's Game of Life:
        1. Any living cell with two or three living neighbors survives.
        2. Any dead cell with exactly three living neighbors is brought to life.
        3. All other cells either remain dead or are killed."""
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
        """Kill all cells."""
        self.grid = [[False for y in range(self.width)] for x in range(self.height)]
        self.living_cells = set()
