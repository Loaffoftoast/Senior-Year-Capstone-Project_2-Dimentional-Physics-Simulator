import os

import pygame

import itertools

import Library

from Library.Sim import sim

from Library.Display import display

from Library.Graph import graph

from Library.Mouse import mouse



class events:
    def runEvent(event):
        if event.type == pygame.QUIT: # pygame.QUIT = simply closing the application
            sim.stop()

        if event.type == pygame.VIDEORESIZE:
            display.update(event.w, event.h)

        if event.type == pygame.MOUSEWHEEL:
            mouse.scrollWheel(event.y)