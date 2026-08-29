import os

import pygame

import itertools

from Library.Sim import sim

from Library.Display import display



class graph:
        
        zoomLevel = 1
        currentInterval = 2
        intervalCount = 1
        
        def zoomIn(zoomInterval):
            graph.zoomLevel = graph.zoomLevel + zoomInterval
            
            if (graph.intervalCount) % 3 == 0:
                if graph.zoomLevel >= 2.5:
                    graph.currentInterval = graph.currentInterval / 2.5
                    graph.zoomLevel = 1
                    graph.intervalCount = graph.intervalCount + 1
            elif graph.zoomLevel >= 2:
                graph.currentInterval = graph.currentInterval / 2
                graph.zoomLevel = 1
                graph.intervalCount = graph.intervalCount + 1

        def zoomOut(zoomInterval):
            graph.zoomLevel = graph.zoomLevel - zoomInterval

            if graph.zoomLevel < 1:
                graph.intervalCount = graph.intervalCount - 1
                if graph.intervalCount % 3 == 0:
                    if graph.zoomLevel < 1:
                        graph.currentInterval = graph.currentInterval * 2.5
                        graph.zoomLevel = 2.4
                else:
                    graph.zoomLevel = 1.9
                    graph.currentInterval = graph.currentInterval * 2
        
        def drawGraph():
            zoomLevel = graph.zoomLevel
            currentInterval = graph.currentInterval
            screen = display.screen
            # Use the actual window dimensions so axis labels stay inside the window.
            resWidth, resHeight = screen.get_size()
            gridInterval = int(str(abs(currentInterval)).replace('.', '').lstrip('0')[0])
                
# TURN THIS INTO A RANGE FOR YOUR SCREEN
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
            elif gridInterval == 1 or gridInterval == 2:
                drawGrid(20 * zoomLevel, (50, 50, 50))

            spacing = 80 * zoomLevel
            xLines = range(-int(sim.centerX / spacing),
                           int((resWidth - sim.centerX) / spacing) + 2)
            yLines = range(-int(sim.centerY / spacing),
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