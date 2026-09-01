import pygame

from Library.Sim import sim
from Library.Display import display

# PLEASE GOD FIGURE OUT HOW ANY OF THIS WORKS IM SO SCARED

class graph:
    zoomLevel = 1
    currentInterval = 2
    intervalCount = 1

    def zoomAroundMouse(zoomAction):
        mouseX, mouseY = pygame.mouse.get_pos()
        oldSpacing = 80 * graph.zoomLevel
        oldInterval = graph.currentInterval

        # Convert the mouse position into graph coordinates before the zoom changes.
        # This keeps the same value (for example, 1, 1) under the cursor after
        # the zoom level and interval are adjusted.
        worldX = ((mouseX - sim.centerX) / oldSpacing) * oldInterval
        worldY = ((mouseY - sim.centerY) / oldSpacing) * oldInterval

        zoomAction()

        newSpacing = 80 * graph.zoomLevel
        if newSpacing == 0:
            return

        sim.centerX = mouseX - (worldX / graph.currentInterval) * newSpacing
        sim.centerY = mouseY - (worldY / graph.currentInterval) * newSpacing

    def zoomIn(zoomInterval):
        def applyZoom():
            graph.zoomLevel += zoomInterval

            if graph.intervalCount % 3 == 0:
                if graph.zoomLevel >= 2.5:
                    graph.currentInterval /= 2.5
                    graph.zoomLevel = 1
                    graph.intervalCount += 1
            elif graph.zoomLevel >= 2:
                graph.currentInterval /= 2
                graph.zoomLevel = 1
                graph.intervalCount += 1

        graph.zoomAroundMouse(applyZoom)

    def zoomOut(zoomInterval):
        def applyZoom():
            graph.zoomLevel -= zoomInterval

            if graph.zoomLevel < 1:
                graph.intervalCount -= 1
                if graph.intervalCount % 3 == 0:
                    if graph.zoomLevel < 1:
                        graph.currentInterval *= 2.5
                        graph.zoomLevel = 2.4
                else:
                    graph.zoomLevel = 1.9
                    graph.currentInterval *= 2

        graph.zoomAroundMouse(applyZoom)

    def drawGraph():
        zoomLevel = graph.zoomLevel
        currentInterval = graph.currentInterval
        screen = display.screen
        resWidth, resHeight = screen.get_size()
        gridInterval = int(str(abs(currentInterval)).replace('.', '').lstrip('0')[0])

        def drawGrid(spacing, color):
            xLines = range(-int(sim.centerX / spacing),
                           int((resWidth - sim.centerX) / spacing) + 2)
            yLines = range(-int(sim.centerY / spacing),
                           int((resHeight - sim.centerY) / spacing) + 2)
            for step in xLines:
                x = sim.centerX + step * spacing
                pygame.draw.line(screen, color, (x, 0), (x, resHeight), 1)
            for step in yLines:
                y = sim.centerY + step * spacing
                pygame.draw.line(screen, color, (0, y), (resWidth, y), 1)

        if gridInterval == 5:
            drawGrid(16 * zoomLevel, (50, 50, 50))
        elif gridInterval in (1, 2):
            drawGrid(20 * zoomLevel, (50, 50, 50))

        spacing = 80 * zoomLevel
        xLines = range(-int(sim.centerX / spacing),
                       int((resWidth - sim.centerX) / spacing) + 2)
        yLines = range(-int(sim.centerY / spacing),
                       int((resHeight - sim.centerY) / spacing) + 2)

        for step in xLines:
            i = step * spacing
            pygame.draw.line(screen, (100, 100, 100), (sim.centerX + i, 0),
                           (sim.centerX + i, resHeight), 1)
        for step in yLines:
            i = step * spacing
            pygame.draw.line(screen, (100, 100, 100), (0, sim.centerY + i),
                           (resWidth, sim.centerY + i), 1)

        font = pygame.font.SysFont("Arial", 15)
        backgroundColor = (20, 20, 20)
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
                labelY = max(2, min(resHeight - font.size(f"{coord:g}")[1] - 2,
                                    sim.centerY + 2))
                drawLabel(f"{coord:g}", (x + 2, labelY), xLabelColor)

        for step in yLines:
            if step != 0:
                y = sim.centerY + step * spacing
                coord = -currentInterval * step
                labelX = max(2, min(resWidth - font.size(f"{coord:g}")[0] - 2,
                                    sim.centerX + 4))
                drawLabel(f"{coord:g}", (labelX, y + 2), yLabelColor)

        pygame.draw.line(screen, (200, 200, 200), (sim.centerX, 0),
                        (sim.centerX, resHeight), 2)
        pygame.draw.line(screen, (200, 200, 200), (0, sim.centerY),
                        (resWidth, sim.centerY), 2)