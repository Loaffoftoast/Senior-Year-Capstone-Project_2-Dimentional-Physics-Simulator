import pygame

from Library.Sim import sim

from Library.Display import display

# PLEASE GOD FIGURE OUT HOW ANY OF THIS WORKS IM SO SCARED

class graph:
    zoomLevel = 1
    currentInterval = 2
    intervalCount = 1

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

    def drawGraph():

        def drawGridLines():
            def getLinePos():
                if graph.currentInterval == 5:
                    spacing = 16 * graph.zoomLevel
                else: 
                    spacing = 20 * graph.zoomLevel
                
                xLines = range(-int(sim.centerX / spacing),
                                int((display.resWidth - sim.centerX) / spacing) + 2)
                yLines = range(-int(sim.centerY / spacing),
                                int((display.resHeight - sim.centerY) / spacing) + 2)

                return xLines, yLines, spacing

            def drawLines(xLines, yLines, spacing):
                for step in xLines:
                    x = sim.centerX + step * spacing
                    pygame.draw.line(display.screen, (50, 50, 50), (x, 0), (x, display.resHeight), 1)
                for step in yLines:
                    y = sim.centerY + step * spacing
                    pygame.draw.line(display.screen, (50, 50, 50), (0, y), (display.resWidth, y), 1)

            xLines, yLines, spacing = getLinePos()
            drawLines(xLines, yLines, spacing)

        def drawIntervalLines():
            def getLinePos():
                spacing = 80 * graph.zoomLevel

                xLines = range(-int(sim.centerX / spacing),
                                int((display.resWidth - sim.centerX) / spacing) + 2)
                yLines = range(-int(sim.centerY / spacing),
                                int((display.resHeight - sim.centerY) / spacing) + 2)

                return xLines, yLines, spacing

            def drawLines(xLines, yLines, spacing):
                for step in xLines:
                    i = step * spacing
                    pygame.draw.line(display.screen, (100, 100, 100), (sim.centerX + i, 0),
                                (sim.centerX + i, display.resHeight), 1)
                for step in yLines:
                    i = step * spacing
                    pygame.draw.line(display.screen, (100, 100, 100), (0, sim.centerY + i),
                                (display.resWidth, sim.centerY + i), 1)

            xLines, yLines, spacing = getLinePos()
            drawLines(xLines, yLines, spacing)

        def drawCenterLines():
            def drawLines():
                pygame.draw.line(display.screen, (200, 200, 200), (sim.centerX, 0),
                            (sim.centerX, display.resHeight), 2)
                pygame.draw.line(display.screen, (200, 200, 200), (0, sim.centerY),
                            (display.resWidth, sim.centerY), 2)

            drawLines()

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

        drawGridLines()
        drawIntervalLines()
        drawCenterLines()
        drawLabels()



            