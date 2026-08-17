# https://www.pygame.org/docs/genindex.html
import os
import pygame
import itertools

pygame.init() #Runs all the code below

class display:
    screen = pygame.display.set_mode((0, 0), pygame.NOFRAME | pygame.DOUBLEBUF) # sets the display value to be a variable in order to define itself correctly
    clock = pygame.time.Clock()
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

class sim:
    running = False #running is the variable used to see if the loop is active
    centerX, centerY = display.windowCenter
    lastCenterX, lastCenterY = centerX, centerY
    mouseXPos, mouseYPos = pygame.mouse.get_pos()
    lastMouseX, lastMouseY = mouseXPos, mouseYPos
    
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

    class graph:
        
        zoomLevel = 1
        currentInterval = 2
        intervalCount = 1
        
        def zoomIn():
            sim.graph.zoomLevel = sim.graph.zoomLevel + 0.25
            
            if (sim.graph.intervalCount) % 3 == 0:
                if sim.graph.zoomLevel >= 2.5:
                    sim.graph.currentInterval = sim.graph.currentInterval / 2.5
                    sim.graph.zoomLevel = 1
                    sim.graph.intervalCount = sim.graph.intervalCount + 1
            elif sim.graph.zoomLevel >= 2:
                sim.graph.currentInterval = sim.graph.currentInterval / 2
                sim.graph.zoomLevel = 1
                sim.graph.intervalCount = sim.graph.intervalCount + 1

        def zoomOut():
            sim.graph.zoomLevel = sim.graph.zoomLevel - 0.25

            if sim.graph.zoomLevel < 1:
                sim.graph.intervalCount = sim.graph.intervalCount - 1
                if sim.graph.intervalCount % 3 == 0:
                    if sim.graph.zoomLevel < 1:
                        sim.graph.currentInterval = sim.graph.currentInterval * 2.5
                        sim.graph.zoomLevel = 2.4
                else:
                    sim.graph.zoomLevel = 1.9
                    sim.graph.currentInterval = sim.graph.currentInterval * 2
        
        def drawGraph():
            zoomLevel = sim.graph.zoomLevel
            currentInterval = sim.graph.currentInterval
            screen = display.screen
            windowXCenter, windowYCenter = display.windowXCenter, display.windowYCenter
            resWidth, resHeight = display.resWidth, display.resHeight
            gridInterval = int(str(abs(currentInterval)).replace('.', '').lstrip('0')[0])
                
            if gridInterval == 5:
                for i in itertools.count(0, 16 * zoomLevel):
                    pygame.draw.line(screen, (50, 50, 50), ((sim.centerX - i), 0), ((sim.centerX - i), resHeight), 1)
                    pygame.draw.line(screen, (50, 50, 50), ((sim.centerX + i), 0), ((sim.centerX + i), resHeight), 1)
                    pygame.draw.line(screen, (50, 50, 50), (0, (sim.centerY + i)), (resWidth, (sim.centerY + i)), 1)
                    pygame.draw.line(screen, (50, 50, 50), (0, (sim.centerY - i)), (resWidth, (sim.centerY - i)), 1)
                    if i > 2500: break
                
            elif gridInterval == 1 or gridInterval == 2:
                for i in itertools.count(0, 20 * zoomLevel):
                    pygame.draw.line(screen, (50, 50, 50), ((sim.centerX - i), 0), ((sim.centerX - i), resHeight), 1)
                    pygame.draw.line(screen, (50, 50, 50), ((sim.centerX + i), 0), ((sim.centerX + i), resHeight), 1)
                    pygame.draw.line(screen, (50, 50, 50), (0, (sim.centerY + i)), (resWidth, (sim.centerY + i)), 1)
                    pygame.draw.line(screen, (50, 50, 50), (0, (sim.centerY - i)), (resWidth, (sim.centerY - i)), 1)
                    if i > 2500: break

            for i in itertools.count(0, 80 * zoomLevel):
                pygame.draw.line(screen, (100, 100, 100), ((sim.centerX - i), 0), ((sim.centerX - i), resHeight), 1)
                pygame.draw.line(screen, (100, 100, 100), ((sim.centerX + i), 0), ((sim.centerX + i), resHeight), 1)
                pygame.draw.line(screen, (100, 100, 100), (0, (sim.centerY + i)), (resWidth, (sim.centerY + i)), 1)
                pygame.draw.line(screen, (100, 100, 100), (0, (sim.centerY - i)), (resWidth, (sim.centerY - i)), 1)

                font = pygame.font.SysFont("Arial", 15)
                if i > 0:
                    coord = currentInterval * i / (80 * zoomLevel)
                    posCoords, negCoords = f"{coord:g}", f"{-coord:g}"
                    screen.blit(font.render(negCoords, True, (200, 200, 200)), (sim.centerX - i + 2, sim.centerY + 2))
                    screen.blit(font.render(posCoords, True, (200, 200, 200)), (sim.centerX + i + 2, sim.centerY + 2))
                    screen.blit(font.render(posCoords, True, (200, 200, 200)), (sim.centerX + 4, sim.centerY - i + 2))
                    screen.blit(font.render(negCoords, True, (200, 200, 200)), (sim.centerX + 4, sim.centerY + i + 2))

                if i > 2500: break

            pygame.draw.line(screen, (200, 200, 200), (sim.centerX, 0), (sim.centerX, resHeight), 2)
            pygame.draw.line(screen, (200, 200, 200), (0, sim.centerY), (resWidth, sim.centerY), 2)
            
class keybind:
    # functions below are for specific key interactions
    keyPressed = pygame.key.get_pressed

    def getKeyPressed():
        keybind.keyPressed = pygame.key.get_pressed()
        keybind.mousePressed = pygame.mouse.get_pressed()
        
    def esc():
        sim.stop()

    def F11():
        display.isFullscreen = not display.isFullscreen # flips the fullscreen bool value
        sim.fullscreen(display.isFullscreen)
        
    dragging = False
    
    def rightClickDown():
        mouseXPos, mouseYPos = pygame.mouse.get_pos()
        sim.lastCenterX, sim.lastCenterY = sim.centerX, sim.centerY
        sim.lastMouseX, sim.lastMouseY = mouseXPos, mouseYPos
        keybind.dragging = True

    def rightClickUp(): 
        keybind.dragging = False
        
    def mouseMovement():
        if keybind.dragging == True:
            mouseXPos, mouseYPos = pygame.mouse.get_pos()
            mouseXOffset, mouseYOffset = (mouseXPos - sim.lastMouseX), (mouseYPos - sim.lastMouseY)
            sim.centerX, sim.centerY = (sim.lastCenterX + mouseXOffset), (sim.lastCenterY + mouseYOffset)
    
    upPressed = False            
    downPressed = False
        
    scrollWheelY = 0
    scrollWheelMoving = False

        

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
    display.screen.fill((0, 0, 0))

    keybind.getKeyPressed()

    if keybind.keyPressed[pygame.K_ESCAPE]: keybind.esc()

    if keybind.keyPressed[pygame.K_F11]: keybind.F11()
        
    if keybind.keyPressed[pygame.K_UP] and keybind.upPressed == False:
        sim.graph.zoomIn()
        keybind.upPressed = True
        
    if keybind.keyPressed[pygame.K_DOWN] and keybind.downPressed == False: 
        sim.graph.zoomOut()
        keybind.downPressed = True
        
    if not keybind.keyPressed[pygame.K_UP] and not keybind.keyPressed[pygame.K_DOWN]:
        keybind.upPressed = False
        keybind.downPressed = False
        
    #this wont work it always says zoombindpressed is false :(
    #'''
    keybind.scrollWheelY = 0
    if event.type == pygame.MOUSEWHEEL:
        keybind.scrollWheelY = event.y
        
    if keybind.scrollWheelY == 1 and keybind.scrollWheelMoving == False:
        sim.graph.zoomIn()
        keybind.scrollWheelMoving = True
        
    if keybind.scrollWheelY == -1 and keybind.scrollWheelMoving == False:
        sim.graph.zoomOut()
        keybind.scrollWheelMoving = True
            
    if keybind.scrollWheelY == 0:
        keybind.scrollWheelMoving = False
    #'''
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 3: keybind.rightClickDown() 
        
    if event.type == pygame.MOUSEBUTTONUP:
        if event.button == 3: keybind.rightClickUp() 
        
        #this no longer working pls fix
    if event.type == pygame.MOUSEMOTION: keybind.mouseMovement()
    
        
            
    print(sim.graph.intervalCount, sim.graph.zoomLevel, sim.graph.currentInterval, keybind.upPressed, keybind.downPressed, keybind.scrollWheelMoving, (int(str(abs(sim.graph.currentInterval)).replace('.', '').lstrip('0')[0])))
            
    sim.graph.drawGraph()
    pygame.display.flip() # updates the entire contents of the display with whatever drawn in code
    display.clock.tick(60)

pygame.quit()