# https://www.pygame.org/docs/genindex.html
import os
import pygame
import Library

pygame.init()

Library.startSimulation()
#os.environ['SDL_VIDEO_WINDOW_POS'] = "center"
resWidth, resHeight = pygame.display.get_desktop_sizes()[0]
#screen = pygame.display.set_mode((resWidth // 1.25, resHeight // 1.25), pygame.RESIZABLE)

isFullscreen = False
running = Library.running
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    windowRect = Library.screen.get_rect()
    windowCenter = ((windowRect.left + windowRect.right) // 2, (windowRect.top + windowRect.bottom) // 2)

    pygame.draw.circle(screen, (255, 255, 255), (windowCenter), 5)
    if event.type == pygame.KEYDOWN:
        Library.checkKey(event.key)
        
    #def checkKey(keyPressed):
        '''
        if event.key == pygame.K_ESCAPE:
            running = False

        if event.key == pygame.K_F11:
            isFullscreen = not isFullscreen
            if isFullscreen == True:
                os.environ['SDL_VIDEO_WINDOW_POS'] = "0, 0"
                pygame.display.quit(); pygame.display.init()
                screen = pygame.display.set_mode((0, 0))
            else:
                os.environ['SDL_VIDEO_WINDOW_POS'] = "centered"
                pygame.display.quit(); pygame.display.init()
                screen = pygame.display.set_mode((resWidth // 1.25, resHeight // 1.25), pygame.RESIZABLE)
        '''
    pygame.display.flip()

pygame.quit()