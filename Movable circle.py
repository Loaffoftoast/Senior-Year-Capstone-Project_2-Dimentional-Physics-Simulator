import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moveable Circle")

circleX, circleY = 400, 300
dragging = False

mouseXPos, mouseYPos = pygame.mouse.get_pos()
lastMouseX, lastMouseY = mouseXPos, mouseYPos

mouseXOffset, mouseYOffset = (mouseXPos - lastMouseX), (mouseYPos - lastMouseY)

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:  # Left click
                mouseXPos, mouseYPos = pygame.mouse.get_pos()
                lastCircleX, lastCircleY = circleX, circleY
                lastMouseX, lastMouseY = mouseXPos, mouseYPos
                dragging = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                mouseXPos, mouseYPos = pygame.mouse.get_pos()
                mouseXOffset, mouseYOffset = (mouseXPos - lastMouseX), (mouseYPos - lastMouseY)
                circleX, circleY = (lastCircleX + mouseXOffset), (lastCircleY + mouseYOffset)

    print(circleX, circleY)
    pygame.draw.circle(screen, (100, 100, 100), (circleX, circleY), 40)

    pygame.display.flip()

pygame.quit()
