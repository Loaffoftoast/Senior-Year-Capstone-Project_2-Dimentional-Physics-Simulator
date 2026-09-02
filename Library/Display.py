import pygame

class display:
    screen = pygame.display.set_mode((0, 0), pygame.NOFRAME | pygame.DOUBLEBUF) # sets the display value to be a variable in order to define itself correctly
    
    clock = pygame.time.Clock()
    
    isFullscreen = True # inits isFullscreen variable

    resWidth, resHeight = pygame.display.get_desktop_sizes()[0] #
    
    windowRect = screen.get_rect()
    
    centerPos = ((windowRect.left + windowRect.right) // 2, (windowRect.top + windowRect.bottom) // 2)
    centerPosX, centerPosY = centerPos

    def getScreenValues():
        display.resWidth, display.resHeight = pygame.display.get_desktop_sizes()[0] # sets a variable to the length and width of your moniter
        
        display.windowRect = display.screen.get_rect() # finds positions of different points on the display
        
        display.centerPos = ((display.windowRect.left + display.windowRect.right) // 2, 
                                (display.windowRect.top + display.windowRect.bottom) // 2)
        
        display.centerPosX, display.centerPosY = display.centerPos
        
    def update(w, h):
        if (display.isFullscreen == False):
            pygame.display.set_mode((w, h), pygame.RESIZABLE)

    def getFPS():
        fps = int(display.clock.get_fps())
        return fps
    
    def drawFPS():
        fps = display.getFPS()
        fpsFont = pygame.font.SysFont("Arial", 15)
        display.screen.blit(fpsFont.render(f"FPS: {fps}", True, (255, 255, 255)), (10, 10))
