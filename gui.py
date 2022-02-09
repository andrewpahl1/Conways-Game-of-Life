import pygame
import life

# Globals.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (75, 75, 75)

class GUI:

    def __init__(self, game_of_life):
        self.game = game_of_life
        self.cell_size = 10
        self.running = False
        self.window_height = self.game.height * (self.cell_size + 1) + 1
        self.window_width = self.game.width * (self.cell_size + 1) + 1
        pygame.init()
        self.screen = pygame.display.set_mode((self.window_height, self.window_width))
        self.draw_field(True)
    
    def draw_field(self, resize=False):
        if resize:
            self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        for y in range(self.game.height):
            for x in range(self.game.width):
                rect = pygame.Rect(x * (self.cell_size + 1) + 1, y * (self.cell_size + 1) + 1, self.cell_size, self.cell_size)
                cell_color = BLACK if self.game.grid[y][x] else WHITE
                pygame.draw.rect(self.screen, cell_color, rect, 0)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
        if event.type == pygame.MOUSEBUTTONUP:
            pass
        if event.type == pygame.KEYDOWN:
            if event.unicode == " ":
                self.game.update_all()
        elif event.type == pygame.QUIT:
            self.running = False
    
    def run_game(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            self.screen.fill(GREY)
            self.draw_field()
            pygame.display.flip()

if __name__ == "__main__":
    game = GUI(life.GameOfLife(50, 50))
    game.run_game()