import pygame
import random
from pygame.locals import *

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILE_SIZE = 40

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Font for text
font = pygame.font.Font(None, 50)
small_font = pygame.font.Font(None, 36)

# Pac-Man and ghost dimensions
PACMAN_RADIUS = TILE_SIZE // 2 - 2
GHOST_RADIUS = TILE_SIZE // 2 - 2

# Create a maze
maze = [
    "########################",
    "#...........#..........#",
    "#.####.#####.####.#####.#",
    "#........#.............#",
    "#.####.#.#.####.#####.##",
    "#......#.#.............#",
    "########################",
]

ROWS = len(maze)
COLS = len(maze[0])

# Game variables
pacman_start_x, pacman_start_y = TILE_SIZE, TILE_SIZE
ghosts_start_positions = [
    {"x": 5 * TILE_SIZE, "y": 5 * TILE_SIZE, "dx": 1, "dy": 0},
    {"x": 15 * TILE_SIZE, "y": 1 * TILE_SIZE, "dx": 0, "dy": 1},
]

# Directions
directions = {"LEFT": (-1, 0), "RIGHT": (1, 0), "UP": (0, -1), "DOWN": (0, 1)}


def draw_button(text, x, y, width, height, color, text_color):
    """Draw a button and return the rectangle for click detection."""
    pygame.draw.rect(screen, color, (x, y, width, height))
    label = small_font.render(text, True, text_color)
    screen.blit(label, (x + (width - label.get_width()) // 2, y + (height - label.get_height()) // 2))
    return pygame.Rect(x, y, width, height)


def main_game():
    """Main game function."""
    pacman_x, pacman_y = pacman_start_x, pacman_start_y
    pacman_dx, pacman_dy = 0, 0

    # Initialize pellets and power-ups
    pellets = []
    power_ups = []

    for row in range(ROWS):
        for col in range(COLS):
            if maze[row][col] == ".":
                pellets.append((col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2))
            elif maze[row][col] == "P":
                power_ups.append((col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2))

    ghosts = [
        {"x": ghost["x"], "y": ghost["y"], "dx": ghost["dx"], "dy": ghost["dy"]}
        for ghost in ghosts_start_positions
    ]

    running = True
    game_over = False

    while running:
        screen.fill(BLACK)

        if game_over:
            # Display Game Over screen
            game_over_label = font.render("GAME OVER", True, WHITE)
            screen.blit(game_over_label, (SCREEN_WIDTH // 2 - game_over_label.get_width() // 2, 200))

            restart_button = draw_button("Restart", SCREEN_WIDTH // 2 - 75, 300, 150, 50, GRAY, WHITE)

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if restart_button.collidepoint(event.pos):
                        return main_game()  # Restart the game

            pygame.display.flip()
            clock.tick(30)
            continue

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    pacman_dx, pacman_dy = directions["LEFT"]
                elif event.key == K_RIGHT:
                    pacman_dx, pacman_dy = directions["RIGHT"]
                elif event.key == K_UP:
                    pacman_dx, pacman_dy = directions["UP"]
                elif event.key == K_DOWN:
                    pacman_dx, pacman_dy = directions["DOWN"]

        # Move Pac-Man with boundary check
        new_x = pacman_x + pacman_dx * TILE_SIZE // 8
        new_y = pacman_y + pacman_dy * TILE_SIZE // 8
        col = max(0, min(COLS - 1, new_x // TILE_SIZE))
        row = max(0, min(ROWS - 1, new_y // TILE_SIZE))

        if maze[row][col] != "#":
            pacman_x, pacman_y = new_x, new_y

        # Move ghosts
        for ghost in ghosts:
            ghost["x"] += ghost["dx"] * TILE_SIZE // 8
            ghost["y"] += ghost["dy"] * TILE_SIZE // 8
            col = max(0, min(COLS - 1, ghost["x"] // TILE_SIZE))
            row = max(0, min(ROWS - 1, ghost["y"] // TILE_SIZE))
            if maze[row][col] == "#":
                ghost["dx"], ghost["dy"] = random.choice(list(directions.values()))

        # Check collisions with ghosts
        for ghost in ghosts:
            if (pacman_x - ghost["x"]) ** 2 + (pacman_y - ghost["y"]) ** 2 < (PACMAN_RADIUS + GHOST_RADIUS) ** 2:
                game_over = True

        # Eat pellets
        pellets = [p for p in pellets if (p[0] - pacman_x) ** 2 + (p[1] - pacman_y) ** 2 > (PACMAN_RADIUS + 5) ** 2]

        # Eat power-ups
        power_ups = [p for p in power_ups if (p[0] - pacman_x) ** 2 + (p[1] - pacman_y) ** 2 > (PACMAN_RADIUS + 10) ** 2]

        # Draw maze, pellets, and power-ups
        for row in range(ROWS):
            for col in range(COLS):
                if maze[row][col] == "#":
                    pygame.draw.rect(screen, BLUE, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))

        for pellet in pellets:
            pygame.draw.circle(screen, WHITE, pellet, 5)

        for power_up in power_ups:
            pygame.draw.circle(screen, YELLOW, power_up, 10)

        # Draw Pac-Man
        pygame.draw.circle(screen, YELLOW, (pacman_x, pacman_y), PACMAN_RADIUS)

        # Draw ghosts
        for ghost in ghosts:
            pygame.draw.circle(screen, RED, (ghost["x"], ghost["y"]), GHOST_RADIUS)

        # Check win condition
        if not pellets:
            print("You Win!")
            running = False

        pygame.display.flip()
        clock.tick(30)


# Start the game
main_game()
pygame.quit()
