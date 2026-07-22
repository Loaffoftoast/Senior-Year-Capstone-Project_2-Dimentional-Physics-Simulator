import pygame
import sys

# 1. Initialize all Pygame modules
pygame.init()

# 2. Define window dimensions (Width, Height)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 3. Set the window title (optional)
pygame.display.set_caption("My First Pygame Window")

# 4. Set up a clock to control the frame rate
clock = pygame.time.Clock()

# Main Game Loop
running = True
while running:
    # 5. Event Handling Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 6. Fill the background with a color (RGB tuple)
    screen.fill((40, 44, 52))

    # 7. Update the actual display
    pygame.display.flip()

    # 8. Limit the loop to 60 frames per second
    clock.tick(60)

# Neatly close everything down
pygame.quit()
sys.exit()
