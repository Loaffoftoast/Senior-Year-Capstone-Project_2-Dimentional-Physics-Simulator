from itertools import count

import pygame
import sys

# Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((1600, 1000), pygame.RESIZABLE)
pygame.display.set_caption("Coordinate Grid")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 12)

resWidth, resHeight = pygame.display.get_desktop_sizes()[0] # sets a variable to the length and width of your moniter
windowRect = screen.get_rect() # finds positions of different points on the display
windowXCenter = ((windowRect.left + windowRect.right) // 2)
windowYCenter = ((windowRect.top + windowRect.bottom) // 2)

gridZoomCount = 1
currInterval = 2
prevInterval = 1

zoomLevel = 1
zoomFactor = 0.1
zoomInterval = 1

pressed = False

xMax = 0

def zoomIn():
    global zoomLevel, currInterval, gridZoomCount
    zoomLevel = zoomLevel + 0.1
    
    if (gridZoomCount) % 3 == 0:
        if zoomLevel >= 2.5:
            currInterval = currInterval / 2.5
            zoomLevel = 1
            gridZoomCount = gridZoomCount + 1
    elif zoomLevel >= 2:
        currInterval = currInterval / 2
        zoomLevel = 1
        gridZoomCount = gridZoomCount + 1

def zoomOut():
    global zoomLevel, currInterval, gridZoomCount
    zoomLevel = zoomLevel - 0.1

    if zoomLevel < 1:
        gridZoomCount = gridZoomCount - 1
        if gridZoomCount % 3 == 0:
            if zoomLevel < 1:
                currInterval = currInterval * 2.5
                zoomLevel = 2.4
        else:
            zoomLevel = 1.9
            currInterval = currInterval * 2

def drawGrid():
    gridInterval = int(str(abs(currInterval)).replace('.', '').lstrip('0')[0])

    if gridInterval == 5:
        for i in count(0, 16 * zoomLevel):
            pygame.draw.line(screen, (50, 50, 50), ((windowXCenter - i), 0), ((windowXCenter - i), resHeight), 1)
            pygame.draw.line(screen, (50, 50, 50), ((windowXCenter + i), 0), ((windowXCenter + i), resHeight), 1)
            pygame.draw.line(screen, (50, 50, 50), (0, (windowYCenter + i)), (resWidth, (windowYCenter + i)), 1)
            pygame.draw.line(screen, (50, 50, 50), (0, (windowYCenter - i)), (resWidth, (windowYCenter - i)), 1)
            if i > 2500: break
        
    elif gridInterval == 1 or gridInterval == 2:
        for i in count(0, 20 * zoomLevel):
            pygame.draw.line(screen, (50, 50, 50), ((windowXCenter - i), 0), ((windowXCenter - i), resHeight), 1)
            pygame.draw.line(screen, (50, 50, 50), ((windowXCenter + i), 0), ((windowXCenter + i), resHeight), 1)
            pygame.draw.line(screen, (50, 50, 50), (0, (windowYCenter + i)), (resWidth, (windowYCenter + i)), 1)
            pygame.draw.line(screen, (50, 50, 50), (0, (windowYCenter - i)), (resWidth, (windowYCenter - i)), 1)
            if i > 2500: break

    for i in count(0, 80 * zoomLevel):
        pygame.draw.line(screen, (100, 100, 100), ((windowXCenter - i), 0), ((windowXCenter - i), resHeight), 1)
        pygame.draw.line(screen, (100, 100, 100), ((windowXCenter + i), 0), ((windowXCenter + i), resHeight), 1)
        pygame.draw.line(screen, (100, 100, 100), (0, (windowYCenter + i)), (resWidth, (windowYCenter + i)), 1)
        pygame.draw.line(screen, (100, 100, 100), (0, (windowYCenter - i)), (resWidth, (windowYCenter - i)), 1)

        if i > 0:
            coord = currInterval * i / (80 * zoomLevel)
            posCoords, negCoords = f"{coord:g}", f"{-coord:g}"
            screen.blit(font.render(negCoords, True, (200, 200, 200)), (windowXCenter - i + 2, windowYCenter + 2))
            screen.blit(font.render(posCoords, True, (200, 200, 200)), (windowXCenter + i + 2, windowYCenter + 2))
            screen.blit(font.render(negCoords, True, (200, 200, 200)), (windowXCenter + 4, windowYCenter - i + 2))
            screen.blit(font.render(posCoords, True, (200, 200, 200)), (windowXCenter + 4, windowYCenter + i + 2))

        if i > 2500: break

    pygame.draw.line(screen, (200, 200, 200), (windowXCenter, 0), (windowXCenter, resHeight), 2)
    pygame.draw.line(screen, (200, 200, 200), (0, windowYCenter), (resWidth, windowYCenter), 2)
    

running = True
while running:
    scrollWheelY = 0 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True  # Setting up loop exit
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and pressed == False:  # Scroll Up
                zoomIn()
                pressed = True
                    
            elif event.key == pygame.K_DOWN and pressed == False:  # Scroll Down
                zoomOut()
                pressed = True

            if event.key == pygame.K_ESCAPE:
                running = False
                
        if event.type == pygame.KEYUP: pressed = False
        
        scrollWheelY = 0
        if event.type == pygame.MOUSEWHEEL and pressed == False:
            scrollWheelY = event.y
            pressed = True
        
    if scrollWheelY == 1: zoomIn()
    if scrollWheelY == -1: zoomOut()
    if scrollWheelY == 0: pressed = False

    windowRect = screen.get_rect() # finds positions of different points on the display
    windowXCenter = ((windowRect.left + windowRect.right) // 2)
    windowYCenter = ((windowRect.top + windowRect.bottom) // 2)

    screen.fill((20, 20, 20))

    drawGrid()

    print(gridZoomCount, zoomLevel, currInterval, prevInterval, pressed, (int(str(abs(currInterval)).replace('.', '').lstrip('0')[0])))

    pygame.display.flip()
