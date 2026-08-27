import os
import sys
import pygame
       
def getKeyPressed(key):
    #key = pygame.key.get_pressed
    global spacePressed, rightPressed, leftPressed
    global objects, selectedCircle
    
    if key[pygame.K_SPACE] and not spacePressed:
        objectsClass.newObject()
    spacePressed = key[pygame.K_SPACE]
        
    if objects:
        if key[pygame.K_LEFT] and not leftPressed:
            selectedCircle = (selectedCircle - 1) % len(objects)
        leftPressed = key[pygame.K_LEFT]

        if key[pygame.K_RIGHT] and not rightPressed:
            selectedCircle = (selectedCircle + 1) % len(objects)
        rightPressed = key[pygame.K_RIGHT]


        if key[pygame.K_w]:
            objects[selectedCircle][1] -= objectSpeed
        if key[pygame.K_a]:
            objects[selectedCircle][0] -= objectSpeed
        if key[pygame.K_s]:
            objects[selectedCircle][1] += objectSpeed
        if key[pygame.K_d]:
            objects[selectedCircle][0] += objectSpeed

    if key[pygame.K_BACKSPACE]:
        objectsClass.removeObjects(selectedCircle)
            
        
class objectsClass:
    def removeObjects(selectedCircle):
        objectsToRemove = []
        for index, obj in enumerate(objects):
            distance = ((obj[0] - mousePosX) ** 2 + (obj[1] - mousePosY) ** 2) ** 0.5
            if distance <= 15:
                objectsToRemove.append(index)

        for index in sorted(objectsToRemove, reverse=True):
            objects.pop(index)

        if objects:
            selectedCircle = min(selectedCircle, len(objects) - 1)
        else:
            selectedCircle = 0
    
    def newObject():
        newObject = [mousePosX, mousePosY]
        objects.append(newObject)
        spacePressed = True
    
    def displaySelectedCircle(selectedCircle):
        if objects:
            selectedText = font.render(
                f"Controlling circle {selectedCircle + 1}",
                True,
                (255, 255, 255),
            )
            screen.blit(selectedText, (10, 10))
            
    def labelCircles(objectNumber, obj):
        pygame.draw.circle(screen, (255, 255, 255), (obj[0], obj[1]), 15)
        coordinateText = font.render(
            f"{objectNumber}: ({obj[0]:.0f}, {obj[1]:.0f})",
            True,
            (255, 255, 255),
        )
        screen.blit(coordinateText, (obj[0] + 20, obj[1] - 12))


pygame.init()
screen = pygame.display.set_mode((1080, 720))
font = pygame.font.Font(None, 18)

objects = []

selectedCircle = 0
objectSpeed = 0.5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))


    mousePosX, mousePosY = pygame.mouse.get_pos()

    getKeyPressed(pygame.key.get_pressed())
    
    objectsClass.displaySelectedCircle(selectedCircle)
    
    for objectNumber, obj in enumerate(objects, 1):
        objectsClass.labelCircles(objectNumber, obj)



    pygame.display.flip()

pygame.quit()
sys.exit()
