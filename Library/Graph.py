import pygame

from Library.Sim import sim

from Library.Display import display

# PLEASE GOD FIGURE OUT HOW ANY OF THIS WORKS IM SO SCARED

class graph:
    zoomLevel = 1
    currentInterval = 2
    intervalCount = 1

    lines = {
        "origin": [],
        "interval": [],
        "grid": [],
    }
    
        
    theme = 'dark'
    #theme = 'light'
    
    background = (0, 0, 0)
    
    if theme == 'dark':
        background = (20, 20, 20)
        #lines[] color = da color
        

    def zoom(zoomAmount):
        mouseX, mouseY = pygame.mouse.get_pos()
        oldSpacing = 80 * graph.zoomLevel
        oldInterval = graph.currentInterval

        # Convert the mouse position into graph coordinates before the zoom changes.
        # This keeps the same value (for example, 1, 1) under the cursor after
        # the zoom level and interval are adjusted.
        worldX = ((mouseX - sim.centerX) / oldSpacing) * oldInterval
        worldY = ((mouseY - sim.centerY) / oldSpacing) * oldInterval

        zoomAmount()

        newSpacing = 80 * graph.zoomLevel
        if newSpacing == 0:
            return

        sim.centerX = mouseX - (worldX / graph.currentInterval) * newSpacing
        sim.centerY = mouseY - (worldY / graph.currentInterval) * newSpacing

        graph.drawGraph()

    def zoomIn(interval):
        def getZoomAmount():
            graph.zoomLevel += interval

            if graph.intervalCount % 3 == 0:
                if graph.zoomLevel >= 2.5:
                    graph.currentInterval /= 2.5
                    graph.zoomLevel = 1
                    graph.intervalCount += 1
            elif graph.zoomLevel >= 2:
                graph.currentInterval /= 2
                graph.zoomLevel = 1
                graph.intervalCount += 1

        graph.zoom(getZoomAmount)
        graph.drawGraph()

    def zoomOut(interval):
        def getZoomAmount():
            graph.zoomLevel -= interval

            if graph.zoomLevel < 1:
                graph.intervalCount -= 1
                if graph.intervalCount % 3 == 0:
                    if graph.zoomLevel < 1:
                        graph.currentInterval *= 2.5
                        graph.zoomLevel = 2.4
                else:
                    graph.zoomLevel = 1.9
                    graph.currentInterval *= 2

        graph.zoom(getZoomAmount)
        graph.drawGraph()

    def drawGraph():

        def addLine(lineType, start, end, color, width=1):
            graph.lines[lineType].append(
                (display.screen, color, start, end, width)
            )

        def drawLineSet(lineType):
            for lineData in graph.lines[lineType]:
                pygame.draw.line(*lineData)

        graph.lines = {"origin": [], "interval": [], "grid": []}

        gridSpacing = (16 if graph.currentInterval == 5 else 20) * graph.zoomLevel
        xLines = range(-int(sim.centerX / gridSpacing),
                       int((display.resWidth - sim.centerX) / gridSpacing) + 2)
        yLines = range(-int(sim.centerY / gridSpacing),
                       int((display.resHeight - sim.centerY) / gridSpacing) + 2)
        for step in xLines:
            x = sim.centerX + step * gridSpacing
            addLine("grid", (x, 0), (x, display.resHeight), (50, 50, 50))
        for step in yLines:
            y = sim.centerY + step * gridSpacing
            addLine("grid", (0, y), (display.resWidth, y), (50, 50, 50))

        intervalSpacing = 80 * graph.zoomLevel
        xLines = range(-int(sim.centerX / intervalSpacing),
                       int((display.resWidth - sim.centerX) / intervalSpacing) + 2)
        yLines = range(-int(sim.centerY / intervalSpacing),
                       int((display.resHeight - sim.centerY) / intervalSpacing) + 2)
        for step in xLines:
            x = sim.centerX + step * intervalSpacing
            addLine("interval", (x, 0), (x, display.resHeight), (100, 100, 100))
        for step in yLines:
            y = sim.centerY + step * intervalSpacing
            addLine("interval", (0, y), (display.resWidth, y), (100, 100, 100))

        addLine("origin", (sim.centerX, 0),
                (sim.centerX, display.resHeight), (200, 200, 200), 2)
        addLine("origin", (0, sim.centerY),
                (display.resWidth, sim.centerY), (200, 200, 200), 2)

        def drawLabels():
            def renderLabel(text, position, color):
                label = font.render(text, True, color)
                outline = font.render(text, True, (20, 20, 20))
                x, y = position
                for offsetX, offsetY in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    display.screen.blit(outline, (x + offsetX, y + offsetY))
                display.screen.blit(label, position)

            spacing = 80 * graph.zoomLevel
            xLines = range(-int(sim.centerX / spacing),
                        int((display.resWidth - sim.centerX) / spacing) + 2)
            yLines = range(-int(sim.centerY / spacing),
                        int((display.resHeight - sim.centerY) / spacing) + 2)

            font = pygame.font.SysFont("Arial", 15)

            xLabelColor = (200, 200, 200) if 0 <= sim.centerX <= display.resWidth else (140, 140, 140)
            yLabelColor = (200, 200, 200) if 0 <= sim.centerY <= display.resHeight else (140, 140, 140)

            for step in xLines:
                if step != 0:
                    x = sim.centerX + step * spacing
                    coord = graph.currentInterval * step
                    labelY = max(2, min(display.resHeight - font.size(f"{coord:g}")[1] - 2,
                                        sim.centerY + 2))
                    renderLabel(f"{coord:g}", (x + 2, labelY), xLabelColor)

            for step in yLines:
                if step != 0:
                    y = sim.centerY + step * spacing
                    coord = -graph.currentInterval * step
                    labelX = max(2, min(display.resWidth - font.size(f"{coord:g}")[0] - 2,
                                        sim.centerX + 4))
                    renderLabel(f"{coord:g}", (labelX, y + 2), yLabelColor)

        def drawZoomInfo():
            font = pygame.font.SysFont("Arial", 15)
            spacing = 80 * graph.zoomLevel
            text = (f"Zoom: {graph.zoomLevel:g}x  Spacing: {spacing:g}px  "
                    f"Interval: {graph.currentInterval:g}")
            label = font.render(text, True, (200, 200, 200))
            outline = font.render(text, True, (20, 20, 20))
            x = display.resWidth - label.get_width() - 8
            y = 8
            for offsetX, offsetY in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                display.screen.blit(outline, (x + offsetX, y + offsetY))
            display.screen.blit(label, (x, y))

        display.screen.fill((20, 20, 20))
        drawLineSet("grid")
        drawLineSet("interval")
        drawLineSet("origin")
        drawLabels()
        drawZoomInfo()
        
        



            