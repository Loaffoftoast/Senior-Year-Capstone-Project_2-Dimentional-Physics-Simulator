import pygame
import sys

class Forces:
    class findForce:
        def gravity(mass, g):
            gravity = mass / g
            return gravity
        
    NORMAL_FORCE = None
    FRICTION = None
    TENSION = None
    APPLIED_FORCE = None
    SPRING_FORCE = None
    GRAVITY = None

pygame.init()
font = pygame.font.Font(None, 28)

screen = pygame.display.set_mode((0, 0), pygame.NOFRAME | pygame.DOUBLEBUF)
pygame.display.set_caption("Physics")

clock = pygame.time.Clock()

windowRect = screen.get_rect()
centerPos = ((windowRect.left + windowRect.right) // 2, (windowRect.top + windowRect.bottom) // 2)
centerPosX, centerPosY = centerPos

mass = 10 #Kg
#μs = 0
#μk = 0 

v = 0.0
a = 0.0
g = -9.81
gravity = None
positionY = float(centerPosY)
timeScale = 1.0
elapsedTime = 0.0

class label:
    def objectValues(v, a, elapsedTime):
        values = [
            f"Velocity: {v:.2f} m/s",
            f"Acceleration: {a:.2f} m/s²",
            f"Time: {elapsedTime:.2f} s",
        ]
        for index, value in enumerate(values):
            screen.blit(font.render(value, True, (255, 255, 255)), (15, 15 + index * 30))
            
    def forces(netForce):
            values = [
                f"Gravity: {gravity:.2f} N",
                f"Net force: {netForce:.2f} N",
            ]
            for index, value in enumerate(values):
                rendered = font.render(value, True, (255, 255, 255))
                screen.blit(rendered, (windowRect.right - rendered.get_width() - 15, 15 + index * 30))
        




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                timeScale = 0.0 if timeScale != 0.0 else 1.0
            elif event.key == pygame.K_RIGHT:
                timeScale = 1.0
            elif event.key == pygame.K_LEFT:
                timeScale = -1.0
        elif event.type == pygame.KEYUP and event.key in (pygame.K_RIGHT, pygame.K_LEFT):
            timeScale = 0.0
        

    screen.fill((30, 30, 30))
    
    dt = (clock.get_time() / 1000.0) * timeScale
    elapsedTime += dt

    # Net force determines acceleration, which updates velocity and position.
    gravity = mass * g
    netForce = gravity
    a = netForce / mass
    v += a * dt
    # Keep the position unconstrained so the circle can move offscreen.
    positionY -= v * dt  # Screen Y increases downward.

    
    pygame.draw.circle(screen, (255, 255, 255), (centerPosX, round(positionY)), 25)
    label.objectValues(v, a, elapsedTime)
    label.forces(netForce)
    
    
    
    
    
    
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()