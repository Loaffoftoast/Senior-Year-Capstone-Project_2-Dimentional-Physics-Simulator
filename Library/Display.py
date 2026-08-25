import os

import pygame

import itertools



class display:
    screen = pygame.display.set_mode((0, 0), pygame.NOFRAME | pygame.DOUBLEBUF) # sets the display value to be a variable in order to define itself correctly
    
    clock = pygame.time.Clock()
    
    isFullscreen = False # inits isFullscreen variable

    resWidth, resHeight = pygame.display.get_desktop_sizes()[0] #
    
    windowRect = screen.get_rect()
    
    windowCenter = ((windowRect.left + windowRect.right) // 2, (windowRect.top + windowRect.bottom) // 2)
    
    windowCenterX = ((windowRect.left + windowRect.right) // 2)
    
    windowCenterY = ((windowRect.top + windowRect.bottom) // 2)



    def findScreenValues():
        display.resWidth, display.resHeight = pygame.display.get_desktop_sizes()[0] # sets a variable to the length and width of your moniter
        
        display.windowRect = display.screen.get_rect() # finds positions of different points on the display
        
        display.windowCenter = ((display.windowRect.left + display.windowRect.right) // 2, 
                                (display.windowRect.top + display.windowRect.bottom) // 2)
        
        display.windowCenterX = ((display.windowRect.left + display.windowRect.right) // 2)
        
        display.windowCenterY = ((display.windowRect.top + display.windowRect.bottom) // 2)
        
    def update(w, h):
        if (display.isFullscreen == False):
            pygame.display.set_mode((w, h), pygame.RESIZABLE)