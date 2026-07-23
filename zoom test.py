import pygame
import sys

# Initialize Pygame
pygame.init()

# Define window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame Zoom Example")
clock = pygame.time.Clock()

# 1. Create the internal surface (virtual canvas)
internal_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))

# Base zoom levels
zoom_factor = 1.0
MIN_ZOOM = 0.5
MAX_ZOOM = 4.0

# Create a sample object to display
rect_color = (0, 255, 128)
rect_pos = (WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 - 50, 100, 100)

running = True
while running:
    # 2. Handle Inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
            pygame.quit()
            sys.exit()
            
        # Zoom using mouse scroll wheel
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll Up
                zoom_factor = min(MAX_ZOOM, zoom_factor + 0.1)
            elif event.button == 5:  # Scroll Down
                zoom_factor = max(MIN_ZOOM, zoom_factor - 0.1)

    # 3. Clear and draw everything onto the internal surface at normal size
    internal_surf.fill((30, 30, 30))
    pygame.draw.rect(internal_surf, rect_color, rect_pos)
    pygame.draw.circle(internal_surf, (255, 100, 100), (200, 150), 40)

    # 4. Calculate the target size of the zoomed view
    new_width = int(WINDOW_WIDTH * zoom_factor)
    new_height = int(WINDOW_HEIGHT * zoom_factor)
    
    # 5. Scale the entire virtual canvas
    # Use transform.smoothscale() for pixel blending or transform.scale() for crisp pixel-art
    scaled_surf = pygame.transform.scale(internal_surf, (new_width, new_height))
    
    # 6. Center the zoomed surface onto the main display
    # This prevents the perspective from shifting to the top-left corner
    scaled_rect = scaled_surf.get_rect()
    scaled_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

    # 7. Render to the visible window display
    screen.fill((0, 0, 0)) # Clear outer boundary artifacts
    screen.blit(scaled_surf, scaled_rect)
    
    pygame.display.flip()
    clock.tick(60)
