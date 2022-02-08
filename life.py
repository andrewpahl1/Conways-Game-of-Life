class Cell:

    def __init__(self, coords):
        self.coords = coords
        self.alive = False
        self.neighbors = tuple()
    
    def __repr__(self):
        return f"Cell(coords={self.coords})"
        
    def __eq__(self, other):
        return self.coords == other.coords
        
    def __lt__(self, other):
        return self.coords < other.coords
        
    def __gt__(self, other):
        return self.coords > other.coords

class GameOfLife:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = self.get_grid()
        self.cache_neighbors()
        self.living_cells = set()
    
    def __repr__(self):
        return  f"Life(height={self.height}, width={self.width})"
    
    def __str__(self):
        to_str = {False:"░",True:"█"}
        return "\n".join("".join(to_str[cell.alive] for cell in row) for row in self.grid)
        
    def get_grid(self):
        res = list()
        for y in range(self.height):
            res.append(list())
            for x in range(self.width):
                res[-1].append(Cell((y, x)))
        return res

    def get_neighbors(self, cell):
        y, x = cell.coords
        res = list()
        for i in range(-1, 2):
            for j in range(-1, 2):
                if any((i == j == 0, min(y+i, x+j) < 0, y + i >= self.height, x + j >= self.width)):
                    continue
                else:
                    res.append(self.grid[y+i][x+j])
        return tuple(res)

    def cache_neighbors(self): 
        for row in self.grid:
            for cell in row:
                cell.neighbors = self.get_neighbors(cell)
    
    def get_living_neighbor_count(self, cell):
        return sum(cell.alive for cell in cell.neighbors)
    
    def update(self):
        checked_dead_cells = set()
        newly_dead_cells = set()
        newly_living_cells = set()
        for cell in self.living_cells:
            living_neighbors_count = self.get_living_neighbor_count(cell)
            if not 1 < living_neighbors_count < 4:
                newly_dead_cells.add(cell)






































