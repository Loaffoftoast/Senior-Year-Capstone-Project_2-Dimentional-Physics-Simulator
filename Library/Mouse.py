import os

import pygame

import itertools

import Library

from Library.Sim import sim

from Library.Display import display

from Library.Graph import graph

class mouse:
    def getInput(input):
        if input[0]:
            mouse.isDragging()
            mouse.dragging = True

        elif not input[0]:
            mouse.dragging = False

    dragging = False
    def isDragging():
        mouse.getPos()
        if mouse.dragging == False:
            sim.lastCenterX, sim.lastCenterY = sim.centerX, sim.centerY
            mouse.getLastPos()

        if mouse.dragging == True:
            mouse.getOffset()
            sim.centerX, sim.centerY = (sim.lastCenterX + mouse.offsetX), (sim.lastCenterY + mouse.offsetY)
            
    
    pos = pygame.mouse.get_pos()
    posX, posY = pos
    def getPos():
        mouse.pos = pygame.mouse.get_pos()
        mouse.posX, mouse.posY = mouse.pos

    lastPos = posX, posY
    lastPosX, lastPosY = lastPos
    def getLastPos():
        mouse.lastPos = mouse.pos
        mouse.lastPosX, mouse.lastPosY = mouse.lastPos

    offsetX, offsetY = (posX - lastPosX), (posX - lastPosY)
    def getOffset():
        mouse.offsetX, mouse.offsetY = (mouse.posX - mouse.lastPosX), (mouse.posY - mouse.lastPosY)

    def scrollWheel(scrollY):
        if scrollY > 0:
            graph.zoomIn(0.05)
        elif scrollY < 0:
            graph.zoomOut(0.05)
