import os

import pygame

import itertools

from Library.Sim import sim

from Library.Display import display



class keybind:
    # functions below are for specific key interactions
    keyPressed = pygame.key.get_pressed
    mouseButton = pygame.mouse.get_pressed() 

    def getKeyPressed():
        keybind.keyPressed = pygame.key.get_pressed()
        keybind.mouseButton = pygame.mouse.get_pressed() 
        
    def esc():
        sim.stop()

    def F11():
        display.isFullscreen = not display.isFullscreen # flips the fullscreen bool value
        sim.fullscreen(display.isFullscreen)
        
    dragging = False
    
    def mouseUpdate ():
        sim.mousePosX, sim.mousePosY = pygame.mouse.get_pos()
    
    def rightClickDown():
        sim.mousePosX, sim.mousePosY = pygame.mouse.get_pos()
        if keybind.dragging == False:
            sim.lastCenterX, sim.lastCenterY = sim.centerX, sim.centerY
            sim.lastMouseX, sim.lastMouseY = sim.mousePosX, sim.mousePosY

    def rightClickUp(): 
        keybind.dragging = False
        
    def mouseMovement():
        if keybind.dragging:
            sim.mousePosX, sim.mousePosY = pygame.mouse.get_pos()
            sim.mouseOffsetX, sim.mouseOffsetY = (sim.mousePosX - sim.lastMouseX), (sim.mousePosY - sim.lastMouseY)

            sim.centerX, sim.centerY = (sim.lastCenterX + sim.mouseOffsetX), (sim.lastCenterY + sim.mouseOffsetY)
    
    upPressed = False            
    downPressed = False
        
    scrollWheelY = 0
    scrollWheelMoving = False
