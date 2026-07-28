# https://www.pygame.org/docs/genindex.html
import os
import pygame

pygame.init()

screen = pygame.display.set_mode((0, 0))

class sim:
    running = False
    def start():
        sim.running = True
        pygame.display.set_caption("Test")

    def stop():
        sim.running = False

    def fullscreen(bool):
        global screen
        if bool == True:
            os.environ['SDL_VIDEO_WINDOW_POS'] = "0, 0"
            pygame.display.quit(); pygame.display.init()
            screen = pygame.display.set_mode((0, 0))
        else:
            os.environ['SDL_VIDEO_WINDOW_POS'] = "centered"
            pygame.display.quit(); pygame.display.init()
            screen = pygame.display.set_mode((display.resWidth // 1.25, display.resHeight // 1.25), pygame.RESIZABLE)

class keybind:
    def esc():
        sim.stop()

    def F11():
        display.isFullscreen = not display.isFullscreen
        sim.fullscreen(display.isFullscreen)

class display:
    isFullscreen = False
    resWidth, resHeight = pygame.display.get_desktop_sizes()[0]
    windowRect = screen.get_rect()
    windowCenter = ((windowRect.left + windowRect.right) // 2, (windowRect.top + windowRect.bottom) // 2)
    def findScreenValues():
        global resWidth, resHeight, windowRect, windowCenter
        resWidth, resHeight = pygame.display.get_desktop_sizes()[0]
        windowRect = screen.get_rect()
        windowCenter = ((windowRect.left + windowRect.right) // 2, (windowRect.top + windowRect.bottom) // 2)



sim.fullscreen(False)
sim.start()
while sim.running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sim.stop()

    display.findScreenValues()

    pygame.draw.circle(screen, (255, 255, 255), (windowCenter), 5)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            keybind.esc()

        if event.key == pygame.K_F11:
            keybind.F11()


    pygame.display.flip()

pygame.quit()