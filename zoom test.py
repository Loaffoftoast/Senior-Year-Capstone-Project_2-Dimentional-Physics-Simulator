import pygame
import sys

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame Zoom Example")
clock = pygame.time.Clock()

internal_surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))

zoom_level = 1

rect_color = (0, 255, 128)
rect_pos = (WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 - 50, 100, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True
            pygame.quit()
            sys.exit()

        zoom_factor = zoom_level / 10
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll Up
                zoom_level = zoom_level + zoom_factor
            elif event.button == 5:  # Scroll Down
                zoom_level = zoom_level - zoom_factor

    internal_surf.fill((30, 30, 30))
    pygame.draw.rect(internal_surf, rect_color, rect_pos)
    pygame.draw.circle(internal_surf, (255, 100, 100), (200, 150), 40)

    new_width = int(WINDOW_WIDTH * zoom_level)
    new_height = int(WINDOW_HEIGHT * zoom_level)
    
    scaled_surf = pygame.transform.scale(internal_surf, (new_width, new_height))
    
    scaled_rect = scaled_surf.get_rect()
    scaled_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

    screen.fill((0, 0, 0)) # Clear outer boundary artifacts
    screen.blit(scaled_surf, scaled_rect)
    
    pygame.display.flip()
    clock.tick(60)
