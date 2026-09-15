import pygame


from Library.Graph import graph
from Library.Mouse import mouse
from Library.Display import display
from Library.Sim import sim
            

class objectsClass:
    objects = []
    nextObjectTime = 0

    def newObject(radius = 1, color = (255, 255, 255)):
        mousePosX, mousePosY = mouse.getPos()
        posOffsetX, posOffsetY = mousePosX - sim.centerX, mousePosY - sim.centerY
        obj = {
            "position": 
                (posOffsetX + sim.centerX, posOffsetY + sim.centerY),

            "offset":
                (posOffsetX, posOffsetY),
                
            "radius": 
                radius * 80,

            "startingRadius":
                radius * 80,
                
            "color": 
                color,
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
            
    def updatePos():
        for obj in objectsClass.objects:
            posOffsetX, posOffsetY = obj["offset"]
            obj["position"] = (
                sim.centerX + posOffsetX,
                sim.centerY + posOffsetY,
            )
            obj["radius"] = (obj["startingRadius"] / graph.currentInterval) * graph.zoomLevel
    
    #def updatePositions():
    #    for obj in objectsClass.objects:
    #        obj["position"] = (pos)
        
