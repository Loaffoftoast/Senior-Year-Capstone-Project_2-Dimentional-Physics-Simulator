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
    windowCenterX = ((windowRect.left + windowRect.right) // 2)
    windowCenterY = ((windowRect.top + windowRect.bottom) // 2)

    def findScreenValues():
        display.resWidth, display.resHeight = pygame.display.get_desktop_sizes()[0] # sets a variable to the length and width of your moniter
        display.windowRect = display.screen.get_rect() # finds positions of different points on the display
        display.windowCenter = ((display.windowRect.left + display.windowRect.right) // 2, (display.windowRect.top + display.windowRect.bottom) // 2)
        display.windowCenterX = ((display.windowRect.left + display.windowRect.right) // 2)
        display.windowCenterY = ((display.windowRect.top + display.windowRect.bottom) // 2)
        
    def update():
        if (display.isFullscreen == False):
            pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

class sim:
    running = False #running is the variable used to see if the loop is active
    centerX, centerY = display.windowCenter
    mousePosX, mousePosY = pygame.mouse.get_pos()
    lastCenterX, lastCenterY = centerX, centerY
    lastMouseX, lastMouseY = mousePosX, mousePosY
    mouseOffsetX, mouseOffsetY = (mousePosX - lastMouseX), (mousePosY - lastMouseY)

    
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
            sim.graph.zoomLevel = sim.graph.zoomLevel + 0.1
            
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
            sim.graph.zoomLevel = sim.graph.zoomLevel - 0.1

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
            # Use the actual window dimensions so axis labels stay inside the window.
            resWidth, resHeight = screen.get_size()
            gridInterval = int(str(abs(currentInterval)).replace('.', '').lstrip('0')[0])
                
# TURN THIS INTO A RANGE FOR YOUR SCREEN
            def drawGrid(spacing, color):
                xLines = range(-int(sim.centerX / spacing) - 1,
                               int((resWidth - sim.centerX) / spacing) + 2)
                yLines = range(-int(sim.centerY / spacing) - 1,
                               int((resHeight - sim.centerY) / spacing) + 2)
                for step in xLines:
                    x = sim.centerX + step * spacing
                    pygame.draw.line(screen, color, (x, 0), (x, resHeight), 1)
                for step in yLines:
                    y = sim.centerY + step * spacing
                    pygame.draw.line(screen, color, (0, y), (resWidth, y), 1)

            if gridInterval == 5:
                drawGrid(16 * zoomLevel, (50, 50, 50))
            elif gridInterval == 1 or gridInterval == 2:
                drawGrid(20 * zoomLevel, (50, 50, 50))

            spacing = 80 * zoomLevel
            xLines = range(-int(sim.centerX / spacing) - 1,
                           int((resWidth - sim.centerX) / spacing) + 2)
            yLines = range(-int(sim.centerY / spacing) - 1,
                           int((resHeight - sim.centerY) / spacing) + 2)
            for step in xLines:
                i = step * spacing
                pygame.draw.line(screen, (100, 100, 100), (sim.centerX + i, 0), (sim.centerX + i, resHeight), 1)
            for step in yLines:
                i = step * spacing
                pygame.draw.line(screen, (100, 100, 100), (0, sim.centerY + i), (resWidth, sim.centerY + i), 1)

            font = pygame.font.SysFont("Arial", 15)
            backgroundColor = (20, 20, 20)
            # Fade labels for an axis whose origin is outside the window, while
            # keeping a small background-colored outline around each number.
            xLabelColor = (140, 140, 140) if not 0 <= sim.centerY <= resHeight else (200, 200, 200)
            yLabelColor = (140, 140, 140) if not 0 <= sim.centerX <= resWidth else (200, 200, 200)

            def drawLabel(text, position, color):
                label = font.render(text, True, color)
                outline = font.render(text, True, backgroundColor)
                x, y = position
                for offsetX, offsetY in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    screen.blit(outline, (x + offsetX, y + offsetY))
                screen.blit(label, position)

            for step in xLines:
                if step != 0:
                    x = sim.centerX + step * spacing
                    coord = currentInterval * step
                    label = font.render(f"{coord:g}", True, xLabelColor)
                    # Keep x-axis numbers visible when the x-axis is offscreen.
                    labelY = max(2, min(resHeight - label.get_height() - 2,
                                        sim.centerY + 2))
                    drawLabel(f"{coord:g}", (x + 2, labelY), xLabelColor)
            for step in yLines:
                if step != 0:
                    y = sim.centerY + step * spacing
                    coord = -currentInterval * step
                    label = font.render(f"{coord:g}", True, yLabelColor)
                    # Keep y-axis numbers visible when the y-axis is offscreen.
                    labelX = max(2, min(resWidth - label.get_width() - 2,
                                        sim.centerX + 4))
                    drawLabel(f"{coord:g}", (labelX, y + 2), yLabelColor)

            pygame.draw.line(screen, (200, 200, 200), (sim.centerX, 0), (sim.centerX, resHeight), 2)
            pygame.draw.line(screen, (200, 200, 200), (0, sim.centerY), (resWidth, sim.centerY), 2)
            
class keybind:
    # functions below are for specific key interactions
    keyPressed = pygame.key.get_pressed
    mouseButton = pygame.mouse.get_pressed() 

    def getKeyPressed():
        keybind.keyPressed = pygame.key.get_pressed()
        keybind.mouseButton = pygame.mouse.get_pressed() 
        
    def esc():
        sim.stop()

    def F11():
        display.isFullscreen = not display.isFullscreen # flips the fullscreen bool value
        sim.fullscreen(display.isFullscreen)
        
    dragging = False
    
    def mouseUpdate ():
        sim.mousePosX, sim.mousePosY = pygame.mouse.get_pos()
    
    def rightClickDown():
        sim.mousePosX, sim.mousePosY = pygame.mouse.get_pos()
        if keybind.dragging == False:
            sim.lastCenterX, sim.lastCenterY = sim.centerX, sim.centerY
            sim.lastMouseX, sim.lastMouseY = sim.mousePosX, sim.mousePosY

    def rightClickUp(): 
        keybind.dragging = False
        
    def mouseMovement():
        if keybind.dragging:
            sim.mousePosX, sim.mousePosY = pygame.mouse.get_pos()
            sim.mouseOffsetX, sim.mouseOffsetY = (sim.mousePosX - sim.lastMouseX), (sim.mousePosY - sim.lastMouseY)

            sim.centerX, sim.centerY = (sim.lastCenterX + sim.mouseOffsetX), (sim.lastCenterY + sim.mouseOffsetY)
    
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
        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                sim.graph.zoomIn()
            elif event.y < 0:
                sim.graph.zoomOut()

    display.findScreenValues()
    display.screen.fill((20, 20, 20))


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
        
        
    if keybind.mouseButton[2]:
        keybind.rightClickDown()
        keybind.dragging = True
    
    if not keybind.mouseButton[2]:
        keybind.dragging = False
        keybind.rightClickUp()
        
    if keybind.dragging == True:
        keybind.mouseMovement()
            
            
    print(sim.centerX, sim.centerY)
    
    fps = int(display.clock.get_fps())
    fpsFont = pygame.font.SysFont("Arial", 15)
    display.screen.blit(fpsFont.render(f"FPS: {fps}", True, (255, 255, 0)), (10, 10))
    
    
    sim.graph.drawGraph()
    pygame.display.flip() # updates the entire contents of the display with whatever drawn in code
    display.clock.tick(240)

pygame.quit()