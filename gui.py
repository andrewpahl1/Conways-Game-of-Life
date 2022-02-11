import pygame
import life
import time
import random

# Globals.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (75, 75, 75)

class GUI:

    def __init__(self, game_of_life):
        self.game = game_of_life
        self.cell_size = 10
        self.update_delay = 0
        self.last_update = time.perf_counter()
        self.running = False
        self.updating = False
        self.cell_painting = False
        self.cell_painting_state = True
        self.random_colors = False
        self.window_height = self.game.height * (self.cell_size + 1) + 1
        self.window_width = self.game.width * (self.cell_size + 1) + 1
        pygame.init()
        pygame.display.set_caption("Conway's Game of Life")
        self.screen = pygame.display.set_mode((self.window_width, self.window_height), pygame.RESIZABLE)
    
    def draw_field(self):
        for y in range(self.game.height):
            for x in range(self.game.width):
                rect = pygame.Rect(x * (self.cell_size + 1) + 1, y * (self.cell_size + 1) + 1, self.cell_size, self.cell_size)
                if not self.random_colors:
                    cell_color = BLACK if self.game.grid[y][x] else WHITE
                elif self.game.grid[y][x]:
                    cell_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                else:
                    cell_color = WHITE
                pygame.draw.rect(self.screen, cell_color, rect, 0)
    
    def resize(self, window_type):
        self.updating = False
        new_vert_cell_count = round((self.screen.get_height() - 1) / (self.cell_size + 1))
        new_horz_cell_count = round((self.screen.get_width() - 1) / (self.cell_size + 1))
        if new_vert_cell_count == self.game.height and new_horz_cell_count == self.game.width:
            return
        self.game = life.GameOfLife(new_vert_cell_count, new_horz_cell_count)
        self.window_height = self.game.height * (self.cell_size + 1) + 1
        self.window_width = self.game.width * (self.cell_size + 1) + 1
        self.screen = pygame.display.set_mode((self.window_width, self.window_height), window_type)
    
    def handle_event(self, event):
        if event.type in (pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN):
            cell_pos = self.get_mouse_cell_pos()
        if event.type == pygame.MOUSEBUTTONUP and cell_pos:
            self.cell_painting = False
        elif event.type == pygame.WINDOWMAXIMIZED:
            self.resize(pygame.FULLSCREEN)
        elif event.type == pygame.VIDEORESIZE:
            self.resize(pygame.RESIZABLE)
        elif event.type == pygame.MOUSEBUTTONDOWN and cell_pos:
            self.cell_painting_state = not self.game.grid[cell_pos[0]][cell_pos[1]]
            self.cell_painting = True
        elif event.type == pygame.KEYDOWN:
            if event.unicode == " ":
                self.updating = not self.updating
            elif event.unicode == "c":
                self.game.reset()
                self.updating = False
            elif event.unicode in "12345":
                self.change_update_delay(event.unicode)
            elif event.unicode == "?":
                self.random_colors = not self.random_colors
        elif event.type == pygame.QUIT:
            self.running = False
    
    def change_update_delay(self, new_speed):
        if new_speed == "5":
            self.update_delay = 0
        elif new_speed == "4":
            self.update_delay = 0.1
        elif new_speed == "3":
            self.update_delay = 0.2
        elif new_speed == "2":
            self.update_delay = 0.5
        elif new_speed == "1":
            self.update_delay = 1
    
    def get_mouse_cell_pos(self):
        x, y = pygame.mouse.get_pos()
        within_cell_bounds_x = x < self.game.width * (self.cell_size + 1) + 1
        within_cell_bounds_y = y < self.game.height * (self.cell_size + 1) + 1
        if not within_cell_bounds_x or not within_cell_bounds_y:
            return None
        cell_y = int(y // ((self.game.height * (self.cell_size + 1) + 1) / self.game.height))
        cell_x = int(x // ((self.game.width * (self.cell_size + 1) + 1) / self.game.width))
        return (cell_y, cell_x)
    
    def paint_cells(self):
        cell_pos = self.get_mouse_cell_pos()
        if cell_pos:
            self.game.update_state(cell_pos, self.cell_painting_state)
    
    def run_game(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            if self.cell_painting:
                self.paint_cells()
            if self.updating and time.perf_counter() - self.last_update > self.update_delay:
                self.game.update_all()
                self.last_update = time.perf_counter()
            self.screen.fill(GREY)
            self.draw_field()
            pygame.display.flip()

if __name__ == "__main__":
    game = GUI(life.GameOfLife(75, 75))
    game.run_game()
