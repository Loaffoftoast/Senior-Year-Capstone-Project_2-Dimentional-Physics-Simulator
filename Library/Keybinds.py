import pygame

from Library.Sim import sim

from Library.Display import display

from Library.Graph import graph

from Library.Physics import objectsClass



class keybind:
    upPressed = False
    downPressed = False
    spacePressed = False

    def getPressed(keyPressed):
        if keyPressed[pygame.K_ESCAPE]: 
            sim.stop()

        if keyPressed[pygame.K_F11]: 
            display.isFullscreen = not display.isFullscreen # flips the fullscreen bool value
            sim.fullscreen(display.isFullscreen)
            
        if keyPressed[pygame.K_RETURN] and (keyPressed[pygame.K_LALT] or keyPressed[pygame.K_RALT]):
            display.isFullscreen = not display.isFullscreen # flips the fullscreen bool value
            sim.fullscreen(display.isFullscreen)

        if keyPressed[pygame.K_UP]: 
            if keybind.upPressed == False:
                graph.zoomIn(0.1)
                keybind.upPressed = True

        elif not keyPressed[pygame.K_UP]: 
            keybind.upPressed = False

        if keyPressed[pygame.K_DOWN]: 
            if keybind.downPressed == False:
                graph.zoomOut(0.1)
                keybind.downPressed = True

        elif not keyPressed[pygame.K_DOWN]: 
            keybind.downPressed = False

        if keyPressed[pygame.K_SPACE]:
            if not keybind.spacePressed:
                objectsClass.newObject()
                objectsClass.nextObjectTime = sim.currentTime + 200
            elif sim.currentTime >= objectsClass.nextObjectTime:
                objectsClass.newObject()
                objectsClass.nextObjectTime = sim.currentTime + 200
            keybind.spacePressed = keyPressed[pygame.K_SPACE]
        else:
            keybind.spacePressed = False
