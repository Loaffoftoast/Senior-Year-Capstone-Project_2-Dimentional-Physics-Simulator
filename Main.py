# https://www.pygame.org/docs/genindex.html

import pygame

from Library.Display import display

from Library.Sim import sim

from Library.Graph import graph
            
from Library.Keybinds import keybind

from Library.Mouse import mouse

from Library.Events import events

from Library.Physics import objectsClass
        
def draw():
    graph.drawGraph()
    objectsClass.drawObjects()
    objectsClass.update()
        
pygame.init() #Runs all the code below

sim.fullscreen(True)
sim.start()

while sim.running:
    for event in pygame.event.get(): # when any event happens
        events.runEvent(event)

    display.getScreenValues()

    keybind.getPressed(pygame.key.get_pressed())
    mouse.getInput(pygame.mouse.get_pressed())
    mouse.getPos()
    
    sim.getTime()

    draw()

    # Present the completed frame only after the graph and objects are drawn.
    pygame.display.flip()
    display.clock.tick(60)
    
    

pygame.quit()