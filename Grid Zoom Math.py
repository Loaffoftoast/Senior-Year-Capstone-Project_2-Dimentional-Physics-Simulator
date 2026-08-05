#Grid Zoom Math

import pygame
import sys

count = 2
currInterval = 2
prevInterval = 1
zoomLevel = 1

screen = pygame.display.set_mode((800, 500), pygame.RESIZABLE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True  # Setting up loop exit
            pygame.quit()
            sys.exit()
        
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and pressed == False:  # Scroll Up
            zoomLevel = zoomLevel * 1.1
            pressed = True
            if (zoomLevel > currInterval):
                prevInterval = currInterval
                count = count + 1
                if count % 3 == 0: currInterval = currInterval * 2.5
                else: currInterval = currInterval * 2
                
        elif event.key == pygame.K_DOWN and pressed == False:  # Scroll Down
            zoomLevel = zoomLevel * 0.9
            pressed = True
            if (zoomLevel < prevInterval):
                count = count - 1
                if ((count + 1) % 3) == 0: currInterval = currInterval / 2.5
                else: currInterval = currInterval / 2
                
                if count % 3 == 0: prevInterval = prevInterval / 2.5
                else: prevInterval = prevInterval / 2
                

        if event.key == pygame.K_ESCAPE:
            running = False
    if not event.type == pygame.KEYDOWN:
        pressed = False
    


        
    print(count, zoomLevel, currInterval, prevInterval)