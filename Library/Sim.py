import os

import pygame

import itertools

import pywinstyles

from Library.Display import display



class sim:
    running = False #running is the variable used to see if the loop is active
    centerX, centerY = display.centerPos
    lastCenterX, lastCenterY = centerX, centerY
    
    def start():    #start function begins the loop
        sim.running = True
        pygame.display.set_caption("Physics Simulation Senior Project - Alex LD")

        window_handle = pygame.display.get_wm_info()["window"]
        pywinstyles.change_header_color(window_handle, color="#000000FF") # Hex color code
        pywinstyles.change_title_color(window_handle, color="#FFFFFF")  # Text color


    def stop(): #stop ends the loop
        sim.running = False

    def fullscreen(fullscreen):
        if fullscreen == True: # if the function sets fullscreen (bool) to 'True', it fullscreens the display
            os.environ['SDL_VIDEO_WINDOW_POS'] = "0, 0"  # sets the window to top left (default) in order to position the display correctly
            pygame.display.quit(); pygame.display.init() # stops the display and starts it again in order to save the screen position
            display.screen = pygame.display.set_mode((0, 0), pygame.NOFRAME | pygame.DOUBLEBUF)     # sets the screen size to (0, 0), which defaults it to the whole screen
                                                                                                    # doublebuf stops flickering when display is updated with pygame.display.flip()
        if fullscreen == False:
            os.environ['SDL_VIDEO_WINDOW_POS'] = "centered" # centers the window so that the non-fullscreen display starts in the middle
            pygame.display.quit(); pygame.display.init()    # stops and starts display to save
            display.screen = pygame.display.set_mode((display.resWidth // 1.25, display.resHeight // 1.25), pygame.RESIZABLE | pygame.DOUBLEBUF)   
                # above sets display size to smaller than fullscreen so that it can be Windowed + Resized
