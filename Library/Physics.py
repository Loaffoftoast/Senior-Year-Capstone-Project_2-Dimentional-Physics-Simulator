import pygame


from Library.Graph import graph
from Library.Mouse import mouse
from Library.Display import display
            

class objectsClass:
    objects = []
    nextObjectTime = 0

    def newObject(radius=10, color=(255, 255, 255)):
        mouseX, mouseY = mouse.getPos()
        obj = {
            "position": (mouseX, mouseY),
            "radius": radius,
            "color": color,
        }
        objectsClass.objects.append(obj)
        return obj

    def drawObjects():
        for obj in objectsClass.objects:
            pygame.draw.circle(
                display.screen,
                obj["color"],
                obj["position"],
                obj["radius"],
            )
    
    #def getRadius(radius=10):
        
