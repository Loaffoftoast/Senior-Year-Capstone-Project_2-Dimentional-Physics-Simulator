import pygame
import sys

# Initialize Pygame
pygame.init()

# Layout Dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 40  # Size of each grid square

# Color Definitions
COLOR_BG = (20, 20, 20)          # Dark background
COLOR_GRID = (50, 50, 50)        # Subtle grid lines
COLOR_AXIS = (100, 100, 100)     # Main axis lines
COLOR_TEXT = (200, 200, 200)     # Coordinate text color

# Setup display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Pygame Coordinate Grid")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 12)

def draw_grid():
    # Draw vertical grid lines
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, COLOR_GRID, (x, 0), (x, WINDOW_HEIGHT))
        # Optional: Label X-coordinates along the top margin
        if x % 100 == 0 and x > 0:
            text = font.render(f"X:{x}", True, COLOR_TEXT)
            screen.blit(text, (x + 4, 4))

    # Draw horizontal grid lines
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, COLOR_GRID, (0, y), (WINDOW_WIDTH, y))
        # Optional: Label Y-coordinates along the left margin
        if y % 100 == 0 and y > 0:
            text = font.render(f"Y:{y}", True, COLOR_TEXT)
            screen.blit(text, (4, y + 4))
            
    # Highlight the primary origin margins (Top and Left borders)
    pygame.draw.line(screen, COLOR_AXIS, (0, 0), (WINDOW_WIDTH, 0), 2)
    pygame.draw.line(screen, COLOR_AXIS, (0, 0), (0, WINDOW_HEIGHT), 2)

def draw_mouse_position():
    # Get current pixel coordinates of the mouse
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    # Convert pixel positions into grid-cell coordinates
    grid_x = mouse_x // CELL_SIZE
    grid_y = mouse_y // CELL_SIZE
    
    # Display coordinate telemetry on screen
    coord_string = f"Pixels: ({mouse_x}, {mouse_y}) | Grid Cell: [{grid_x}, {grid_y}]"
    text_surface = font.render(coord_string, True, (0, 255, 0))
    screen.blit(text_surface, (10, WINDOW_HEIGHT - 25))

# Main game loop
while True:
    screen.fill(COLOR_BG)
    
    # Process inputs / events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    # Render elements
    draw_grid()
    draw_mouse_position()
    
    # Refresh screen and lock frame rate to 60 FPS
    pygame.display.flip()
    clock.tick(60)
