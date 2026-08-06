#Grid Zoom Math

import pygame
import sys

pygame.init()

count = 2
currInterval = 2
prevInterval = 1
zoomLevel = 1
pressed = False

screen = pygame.display.set_mode((800, 500), pygame.RESIZABLE)
clock = pygame.time.Clock()

def zoomIn():
    global zoomLevel, prevInterval, currInterval, count
    zoomLevel = zoomLevel * 1.1
    if (zoomLevel > currInterval):
        prevInterval = currInterval
        count = count + 1
        if count % 3 == 0: currInterval = currInterval * 2.5
        else: currInterval = currInterval * 2

def zoomOut():
    global zoomLevel, prevInterval, currInterval, count
    zoomLevel = zoomLevel * 0.9
    if (zoomLevel < prevInterval):
        count = count - 1
        if ((count + 1) % 3) == 0: currInterval = currInterval / 2.5
        else: currInterval = currInterval / 2

        if count % 3 == 0: prevInterval = prevInterval / 2.5
        else: prevInterval = prevInterval / 2

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
    
    print(count, zoomLevel, currInterval, prevInterval, pressed, scrollWheelY)
    clock.tick(60)