import pygame
import os
import Test

global screen
global resWidth
global resHeight

def startSimulation():
    os.environ['SDL_VIDEO_WINDOW_POS'] = "center"
    resWidth, resHeight = pygame.display.get_desktop_sizes()[0]
    screen = pygame.display.set_mode((resWidth // 1.25, resHeight // 1.25), pygame.RESIZABLE)
    pygame.display.set_caption("Test")

def checkKey(keyPressed):

    if keyPressed == pygame.K_ESCAPE:
        running = False

    if keyPressed == pygame.K_F11:
        isFullscreen = not isFullscreen
        if isFullscreen == True:
            os.environ['SDL_VIDEO_WINDOW_POS'] = "0, 0"
            pygame.display.quit(); pygame.display.init()
            screen = pygame.display.set_mode((0, 0))
        else:
            os.environ['SDL_VIDEO_WINDOW_POS'] = "centered"
            pygame.display.quit(); pygame.display.init()
            screen = pygame.display.set_mode((resWidth // 1.25, resHeight // 1.25), pygame.RESIZABLE)