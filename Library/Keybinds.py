import os

import pygame

import itertools

from Library.Sim import sim

from Library.Display import display

from Library.Graph import graph



class keybind:
    def runKeyPressed(keyPressed):
        if keyPressed[pygame.K_ESCAPE]: keybind.esc()
        if keyPressed[pygame.K_F11]: keybind.F11()
        if keyPressed[pygame.K_UP]: keybind.up()
        

        keybind.mouseButton = pygame.mouse.get_pressed() 


        
        
    def esc():
        sim.stop()

    def F11():
        display.isFullscreen = not display.isFullscreen # flips the fullscreen bool value
        sim.fullscreen(display.isFullscreen)
        
    def up():
        if keybind.upPressed == False:
            graph.zoomIn()
            keybind.upPressed = True
    
    dragging = False
    
    def mouseUpdate():
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
