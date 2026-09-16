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
    objectsClass.drawObjects()
    objectsClass.update()
        
pygame.init() #Runs all the code below

sim.fullscreen(True)
sim.start()
graph.drawGraph()

while sim.running:
    for event in pygame.event.get(): # when any event happens
        events.runEvent(event)

    display.getScreenValues()

    keybind.getPressed(pygame.key.get_pressed())
    mouse.getInput(pygame.mouse.get_pressed())
    mouse.getPos()
    
    pygame.display.flip() # updates the entire contents of the display with whatever drawn in code
    display.clock.tick(240)
    
    sim.getTime()

    draw()
    
    print("Screen size:", pygame.display.get_window_size())
    
    

pygame.quit()