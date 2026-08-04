#Grid Zoom Math

import pygame
import sys

count = 1
number = 1
numberLast = 1
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
        elif event.key == pygame.K_DOWN and pressed == False:  # Scroll Down
            zoomLevel = zoomLevel * 0.9
            pressed = True
        if event.key == pygame.K_ESCAPE:
            running = False
    if not event.type == pygame.KEYDOWN:
        pressed = False
    
    if zoomLevel > number:
        numberLast = number
        count += 1
        if count % 3 == 0:
            number = number * 2.5
        else:
            number = number * 2
    elif zoomLevel < numberLast:
        count -= 1
        if count % 3 == 0:
            number = number / 2.5
        else:
            number = number / 2
        
    print(zoomLevel,number)
