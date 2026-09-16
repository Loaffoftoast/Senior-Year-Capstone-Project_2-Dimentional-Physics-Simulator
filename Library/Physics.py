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
        # Store the position in graph coordinates so the first update produces
        # the same screen position as the mouse position.
        posOffsetX = (mousePosX - sim.centerX) * graph.currentInterval / graph.zoomLevel
        posOffsetY = (mousePosY - sim.centerY) * graph.currentInterval / graph.zoomLevel
        obj = {
            "position": 
                (mousePosX, mousePosY),

            "offset":
                (posOffsetX, posOffsetY),
                
            "radius": 
                radius,

            "startingRadius":
                radius,
                
            "color": 
                color,
        }
        objectsClass.objects.append(obj)
        return obj
        

    def drawObjects():
        objectsClass.update()
        for obj in objectsClass.objects:
            pygame.draw.circle(
                display.screen,
                obj["color"],
                obj["position"],
                obj["radius"],
            )
            
    def update():
        for obj in objectsClass.objects:
            posOffsetX, posOffsetY = obj["offset"]
            obj["position"] = (
                (sim.centerX + (posOffsetX * graph.zoomLevel / graph.currentInterval)),
                (sim.centerY + (posOffsetY * graph.zoomLevel / graph.currentInterval)),
            )
            obj["radius"] = (obj["startingRadius"] / graph.currentInterval) * graph.zoomLevel * 80
        
