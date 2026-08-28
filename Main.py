# https://www.pygame.org/docs/genindex.html
import os
import sys

# Ensure both the project root and Library are available for the package imports.
projectRoot = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, projectRoot)
sys.path.insert(0, os.path.join(projectRoot, "Library"))

import pygame

import itertools

from Library.Display import display

from Library.Sim import sim

from Library.Graph import graph
            
from Library.Keybinds import keybind
        
        
        
pygame.init() #Runs all the code below

sim.fullscreen(False)
sim.start()

while sim.running:
    for event in pygame.event.get(): # when any event happens
        if event.type == pygame.QUIT: # pygame.QUIT = simply closing the application
            sim.stop()
        if event.type == pygame.VIDEORESIZE:
            display.update(event.w, event.h)
        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                graph.zoomIn()
            elif event.y < 0:
                graph.zoomOut()

    display.findScreenValues()
    display.screen.fill((20, 20, 20))

    keyPressed = pygame.key.get_pressed()
    keybind.runKeyPressed(keyPressed)
        
        
    '''    if keybind.keyPressed[pygame.K_UP] and keybind.upPressed == False:
        graph.zoomIn()
        keybind.upPressed = True'''
        
    if keybind.keyPressed[pygame.K_DOWN] and keybind.downPressed == False: 
        graph.zoomOut()
        keybind.downPressed = True
        
    if not keybind.keyPressed[pygame.K_UP] and not keybind.keyPressed[pygame.K_DOWN]:
        keybind.upPressed = False
        keybind.downPressed = False
        
        
    if keybind.mouseButton[2]:
        keybind.rightClickDown()
        keybind.dragging = True
    
    if not keybind.mouseButton[2]:
        keybind.dragging = False
        keybind.rightClickUp()
        
    if keybind.dragging == True:
        keybind.mouseMovement()
            
            
    print(sim.centerX, sim.centerY)
    
    fps = int(display.clock.get_fps())
    fpsFont = pygame.font.SysFont("Arial", 15)
    display.screen.blit(fpsFont.render(f"FPS: {fps}", True, (255, 255, 0)), (10, 10))
    
    
    graph.drawGraph()
    pygame.display.flip() # updates the entire contents of the display with whatever drawn in code
    display.clock.tick(240)

pygame.quit()