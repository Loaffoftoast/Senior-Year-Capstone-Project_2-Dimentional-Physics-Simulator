# https://www.pygame.org/docs/genindex.html
import os
import pygame

pygame.init() #Runs all the code below

class sim:
    running = False #running is the variable used to see if the loop is active
    def start():    #start function begins the loop
        sim.running = True
        pygame.display.set_caption("Physics Simulation Senior Project - Alex LD")

    def stop(): #stop ends the loop
        sim.running = False

    def fullscreen(bool):
        if bool == True: # if the function sets fullscreen (bool) to 'True', it fullscreens the display

            os.environ['SDL_VIDEO_WINDOW_POS'] = "0, 0"  # sets the window to top left (default) in order to position the display correctly
            pygame.display.quit(); pygame.display.init() # stops the display and starts it again in order to save the screen position
            display.screen = pygame.display.set_mode((0, 0), pygame.NOFRAME | pygame.DOUBLEBUF)     # sets the screen size to (0, 0), which defaults it to the whole screen
                                                                                                    # doublebuf stops flickering when display is updated with pygame.display.flip()
        else: # if fullscreen is 'False'

            os.environ['SDL_VIDEO_WINDOW_POS'] = "centered" # centers the window so that the non-fullscreen display starts in the middle
            pygame.display.quit(); pygame.display.init()    # stops and starts display to save
            display.screen = pygame.display.set_mode((display.resWidth // 1.25, display.resHeight // 1.25), pygame.RESIZABLE | pygame.DOUBLEBUF)   
                # above sets display size to smaller than fullscreen so that it can be Windowed + Resized

    def drawGrid():

        for x in range(display.windowXCenter, display.windowRect.right, 40):
            pygame.draw.line(display.screen, (50, 50, 50), (x, 0), (x, display.resHeight), 1)

        for x in range(display.windowXCenter, display.windowRect.left, -40): 
            pygame.draw.line(display.screen, (50, 50, 50), (x, 0), (x, display.resHeight), 1)

        for y in range(display.windowYCenter, display.windowRect.top, -40):
            pygame.draw.line(display.screen, (50, 50, 50), (0, y), (display.resWidth, y), 1)

        for y in range(display.windowYCenter, display.windowRect.bottom, 40):
            pygame.draw.line(display.screen, (50, 50, 50), (0, y), (display.resWidth, y), 1)
                
        pygame.draw.line(display.screen, (255, 255, 255), (display.windowXCenter, 0), (display.windowXCenter, display.resHeight), 2)
        pygame.draw.line(display.screen, (255, 255, 255), (0, display.windowYCenter), (display.resWidth, display.windowYCenter), 2)

class keybind:
    # functions below are for specific key interactions
    def esc():
        sim.stop()

    def F11():
        display.isFullscreen = not display.isFullscreen # flips the fullscreen bool value
        sim.fullscreen(display.isFullscreen)

class display:
    screen = pygame.display.set_mode((0, 0), pygame.NOFRAME | pygame.DOUBLEBUF) # sets the display value to be a variable in order to define itself correctly
    isFullscreen = False # inits isFullscreen variable

    resWidth, resHeight = pygame.display.get_desktop_sizes()[0] #
    windowRect = screen.get_rect()
    windowCenter = ((windowRect.left + windowRect.right) // 2, (windowRect.top + windowRect.bottom) // 2)
    windowXCenter = ((windowRect.left + windowRect.right) // 2)
    windowYCenter = ((windowRect.top + windowRect.bottom) // 2)

    def findScreenValues():
        display.resWidth, display.resHeight = pygame.display.get_desktop_sizes()[0] # sets a variable to the length and width of your moniter
        display.windowRect = display.screen.get_rect() # finds positions of different points on the display
        display.windowCenter = ((display.windowRect.left + display.windowRect.right) // 2, (display.windowRect.top + display.windowRect.bottom) // 2)
        display.windowXCenter = ((display.windowRect.left + display.windowRect.right) // 2)
        display.windowYCenter = ((display.windowRect.top + display.windowRect.bottom) // 2)
        
    def update():
        if (display.isFullscreen == False):
            pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)


# due to the previous comments on functions, I hope below code can be inferred only by looking back at functions (with a few exceptions)

sim.fullscreen(False)
sim.start()

while sim.running: 
    for event in pygame.event.get(): # when any event happens
        if event.type == pygame.QUIT: # pygame.QUIT = simply closing the application
            sim.stop()
        if event.type == pygame.VIDEORESIZE:
            display.update()

    display.findScreenValues()
    sim.drawGrid()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            keybind.esc()

        if event.key == pygame.K_F11:
            keybind.F11()

    pygame.display.flip() # updates the entire contents of the display with whatever drawn in code

pygame.quit()