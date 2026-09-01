# https://www.pygame.org/docs/genindex.html
import os
import sys

# Ensure both the project root and Library are available for the package imports.
projectRoot = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, projectRoot)
sys.path.insert(0, os.path.join(projectRoot, "Library"))

import pygame

from Library.Display import display

from Library.Sim import sim

from Library.Graph import graph
            
from Library.Keybinds import keybind

from Library.Mouse import mouse

from Library.Events import events
        

        
pygame.init() #Runs all the code below

sim.fullscreen(True)
sim.start()

while sim.running:
    for event in pygame.event.get(): # when any event happens
        events.runEvent(event)

    display.getScreenValues()
    display.screen.fill((20, 20, 20))

    keybind.getPressed(pygame.key.get_pressed())
    mouse.getInput(pygame.mouse.get_pressed())
    mouse.getPos()
                
    fps = int(display.clock.get_fps())
    fpsFont = pygame.font.SysFont("Arial", 15)
    display.screen.blit(fpsFont.render(f"FPS: {fps}", True, (255, 255, 255)), (10, 10))
    
    
    graph.drawGraph()
    pygame.display.flip() # updates the entire contents of the display with whatever drawn in code
    display.clock.tick(240)

pygame.quit()