import Library
import pygame
import os

pygame.init()
y = Library.x

running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    Library.add(5)
    print(y)

pygame.quit()