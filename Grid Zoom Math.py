#Grid Zoom Math

import pygame
import sys

pygame.init()

count = 1
currInterval = 1
zoomCount = 1
pressed = False

screen = pygame.display.set_mode((800, 500), pygame.RESIZABLE)
clock = pygame.time.Clock()

def zoomIn():
    global zoomCount, currInterval, count
    zoomCount = zoomCount + 0.1
    
    if zoomCount >= 2:
        if (count + 1) % 3 == 0:
            if zoomCount >= 2.5:
                currInterval = currInterval * 2.5
                zoomCount = 1
                count = count + 1
        else: 
            currInterval = currInterval * 2
            zoomCount = 1
            count = count + 1

def zoomOut():
    global zoomCount, currInterval, count
    zoomCount = zoomCount - 0.1
    if zoomCount < 1:
        if count % 3 == 0:
            currInterval = currInterval / 2.5
            zoomCount = 2.4
        else: 
            zoomCount = 1.9
            currInterval = currInterval / 2
    count = count - 1

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
    
    print(count, zoomCount, currInterval, pressed, scrollWheelY)
    clock.tick(60)