import pygame
import random
import time

# Define constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
ROWS = SCREEN_HEIGHT // BLOCK_SIZE
COLS = SCREEN_WIDTH // BLOCK_SIZE
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
SHAPES = [
    [[1, 1, 1, 1]],               # I
    [[1, 1, 1], [0, 1, 0]],      # T
    [[1, 1, 1], [1, 0, 0]],      # L
    [[1, 1, 1], [0, 0, 1]],      # J
    [[0, 1, 1], [1, 1, 0]],      # S
    [[1, 1], [1, 1]],            # O
    [[1, 1, 0], [0, 1, 1]]       # Z
]

# Class for the Tetris game
class Tetris:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.board = [[0] * COLS for _ in range(ROWS)]
        self.current_shape = None
        self.current_shape_row = 0
        self.current_shape_col = COLS // 2
        self.score = 0
        self.game_over = False
        self.generate_shape()

    # Function to generate a random shape
    def generate_shape(self):
        self.current_shape = random.choice(SHAPES)
        self.current_shape_row = 0
        self.current_shape_col = COLS // 2 - len(self.current_shape[0]) // 2

    # Function to rotate the current shape
    def rotate_shape(self):
        self.current_shape = [list(row) for row in zip(*self.current_shape[::-1])]

    # Function to move the current shape down
    def move_down(self):
        self.current_shape_row += 1
        if self.check_collision():
            self.current_shape_row -= 1
            self.merge_shape()

    # Function to move the current shape left
    def move_left(self):
        self.current_shape_col -= 1
        if self.check_collision():
            self.current_shape_col += 1

    # Function to move the current shape right
    def move_right(self):
        self.current_shape_col += 1
        if self.check_collision():
            self.current_shape_col -= 1

    # Function to check if the current shape collides with the board or bottom
    def check_collision(self):
        for row in range(len(self.current_shape)):
            for col in range(len(self.current_shape[0])):
                if (
                    self.current_shape[row][col]
                    and (self.current_shape_col + col < 0
                    or self.current_shape_col + col >= COLS
                    or self.current_shape_row + row >= ROWS
                    or self.board[self.current_shape_row + row][self.current_shape_col + col])
                ):
                    return True
        return False

    # Function to merge the current shape with the board
    def merge_shape(self):
        for row in range(len(self.current_shape)):
            for col in range(len(self.current_shape[0])):
                if self.current_shape[row][col]:
                    self.board[self.current_shape_row + row][self.current_shape_col + col] = 1
        lines_cleared = self.check_lines()
        self.score += lines_cleared * 100
        self.generate_shape()
        if self.check_collision():
            self.game_over = True

    # Function to check and clear completed lines
    def check_lines(self):
        completed_lines = [row for row in range(ROWS) if all(self.board[row])]
        for row in completed_lines:
            del self.board[row]
            self.board.insert(0, [0] * COLS)
        return len(completed_lines)

    # Function to draw the game
    def draw(self):
        self.screen.fill(BLACK)
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col]:
                    pygame.draw.rect(self.screen, WHITE, (col * BLOCK_SIZE, row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        for row in range(len(self.current_shape)):
            for col in range(len(self.current_shape[0])):
                if self.current_shape[row][col]:
                    pygame.draw.rect(self.screen, GRAY, ((self.current_shape_col + col) * BLOCK_SIZE, (self.current_shape_row + row) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)
        font = pygame.font.SysFont(None, 30)
        text = font.render("Score: " + str(self.score), True, WHITE)
        self.screen.blit(text, (10, 10))
        pygame.display.update()

    # Function to run the game loop
    def run(self):
        self.countdown()
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move_left()
                    elif event.key == pygame.K_RIGHT:
                        self.move_right()
                    elif event.key == pygame.K_DOWN:
                        self.move_down()
                    elif event.key == pygame.K_UP:
                        self.rotate_shape()

            self.move_down()
            self.draw()
            self.clock.tick(5)

        pygame.quit()

    # Function for countdown before the game starts
    def countdown(self):
        for i in range(3, 0, -1):
            self.screen.fill(BLACK)
            font = pygame.font.SysFont(None, 100)
            text = font.render(str(i), True, WHITE)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.wait(1000)
            self.screen.fill(BLACK)
            pygame.display.flip()

# Main function to start the game
def main():
    tetris_game = Tetris()
    tetris_game.run()

if __name__ == "__main__":
    main()
