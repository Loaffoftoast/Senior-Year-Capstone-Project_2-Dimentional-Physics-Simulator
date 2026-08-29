import os

import pygame

import itertools

from Library.Sim import sim

from Library.Display import display

from Library.Graph import graph



class keybind:
    upPressed = False
    downPressed = False

    def getPressed(keyPressed):
        if keyPressed[pygame.K_ESCAPE]: 
            sim.stop()

        if keyPressed[pygame.K_F11]: 
            display.isFullscreen = not display.isFullscreen # flips the fullscreen bool value
            sim.fullscreen(display.isFullscreen)

        if keyPressed[pygame.K_UP]: 
            if keybind.upPressed == False:
                graph.zoomIn()
                keybind.upPressed = True

        elif not keyPressed[pygame.K_UP]: 
            keybind.upPressed = False

        if keyPressed[pygame.K_DOWN]: 
            if keybind.downPressed == False:
                graph.zoomOut()
                keybind.downPressed = True

        elif not keyPressed[pygame.K_DOWN]: 
            keybind.downPressed = False
        
        
    #scrollWheelY = 0
    #scrollWheelMoving = False
