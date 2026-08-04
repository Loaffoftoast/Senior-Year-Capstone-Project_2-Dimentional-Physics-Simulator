from itertools import count

import pygame
import sys

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((800, 500), pygame.RESIZABLE)
pygame.display.set_caption("Vertical Lines Every 40 Pixels")

font = pygame.font.SysFont("Arial", 12)

resWidth, resHeight = pygame.display.get_desktop_sizes()[0] # sets a variable to the length and width of your moniter
windowRect = screen.get_rect() # finds positions of different points on the display
windowXCenter = ((windowRect.left + windowRect.right) // 2)
windowYCenter = ((windowRect.top + windowRect.bottom) // 2)

zoomLevel = 1
zoomFactor = 0.1

pressed = False

xMax = 0

def drawGrid():
 
    for i in count(0, 40):
        pygame.draw.line(screen, (50, 50, 50), ((windowXCenter - (i * zoomLevel)), 0), ((windowXCenter - (i * zoomLevel)), resHeight), 1)
        pygame.draw.line(screen, (50, 50, 50), ((windowXCenter + (i * zoomLevel)), 0), ((windowXCenter + (i * zoomLevel)), resHeight), 1)
        pygame.draw.line(screen, (50, 50, 50), (0, (windowYCenter + (i * zoomLevel))), (resWidth, (windowYCenter + (i * zoomLevel))), 1)
        pygame.draw.line(screen, (50, 50, 50), (0, (windowYCenter - (i * zoomLevel))), (resWidth, (windowYCenter - (i * zoomLevel))), 1)
        pygame.draw.circle(screen, (250, 250, 250), (windowXCenter, windowYCenter + i), 5, 1)
        
        if i > 250*40: break

    pygame.draw.line(screen, (255, 255, 255), (windowXCenter, 0), (windowXCenter, resHeight), 2)
    pygame.draw.line(screen, (255, 255, 255), (0, windowYCenter), (resWidth, windowYCenter), 2)
    
    

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True  # Setting up loop exit
            pygame.quit()
            sys.exit()
        
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and pressed == False:  # Scroll Up
            zoomLevel = zoomLevel * 1.1
            pressed = True
        elif event.key == pygame.K_DOWN and pressed == False:  # Scroll Down
            zoomLevel = zoomLevel * 0.9
            pressed = True
    if not event.type == pygame.KEYDOWN:
        pressed = False

    windowRect = screen.get_rect() # finds positions of different points on the display
    windowXCenter = ((windowRect.left + windowRect.right) // 2)
    windowYCenter = ((windowRect.top + windowRect.bottom) // 2)

    windowScale = (resHeight / screen.get_height())
    scalemult = (windowScale + zoomLevel)

    screen.fill((20, 20, 20))

    drawGrid()

    scale = (f"Scale: {(windowScale + zoomLevel)}")
    text_scale = font.render(scale, True, (255, 255, 255))
    screen.blit(text_scale, (10, 100))

    pressedText = (f"Pressed: {pressed}")
    text_pressed = font.render(pressedText, True, (255, 255, 255))
    screen.blit(text_pressed, (10, 130))

   
       

    # Update display
    pygame.display.flip()
