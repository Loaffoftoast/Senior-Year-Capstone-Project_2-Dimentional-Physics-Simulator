import pygame
import sys

pygame.init()
font = pygame.font.Font(None, 28)

screen = pygame.display.set_mode((0, 0), pygame.NOFRAME | pygame.DOUBLEBUF)
pygame.display.set_caption("Physics")

clock = pygame.time.Clock()

windowRect = screen.get_rect()
centerPos = ((windowRect.left + windowRect.right) // 2, (windowRect.top + windowRect.bottom) // 2)
centerPosX, centerPosY = centerPos

mass = 10

v = [25.0, 25.0]
a = [-25.0, -9.81]
timeScale = 0.0
elapsedTime = 0.0

dt = 0

class label:
    def objectValues(vx, vy, ax, ay, elapsedTime):
        values = [
            f"Velocity: {vx:.2f}, {vy:.2f} m/s",
            f"Acceleration: {ax:.2f}, {ay:.2f} m/s²",
            f"Time: {elapsedTime:.3f} s",
        ]
        for index, value in enumerate(values):
            screen.blit(font.render(value, True, (255, 255, 255)), (15, 15 + index * 30))
                    
class Body:
    def __init__(self, mass, v, a, r):
        self.dx = centerPosX
        self.dy = centerPosY
        
        self.vx = v[0]
        self.vy = v[1]
        
        self.ax = a[0]
        self.ay = a[1]

        self.r = r
        self.path = [(int(self.dx), int(self.dy))]
        
    def update(self, dt):
        self.vx += self.ax * dt
        self.vy += self.ay * dt
        
        self.dx += self.vx * dt
        self.dy -= self.vy * dt

        self.path.append((int(self.dx), int(self.dy)))
        if len(self.path) > 1:
            pygame.draw.lines(screen, (100, 200, 255), False, self.path, 2)
        
        pygame.draw.circle(screen, (255, 255, 255), (self.dx, self.dy), self.r)
        
objects = []
objects.append(Body(mass, v, a, 10))

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
            elif event.key == pygame.K_r:
                elapsedTime = 0.0
                objects = [Body(mass, v, a, 10)]
                timeScale = 0.0
        elif event.type == pygame.KEYUP and event.key in (pygame.K_RIGHT, pygame.K_LEFT):
            timeScale = 0.0

    screen.fill((10, 10, 10))
    
    dt = (clock.get_time() / 1000.0) * timeScale
    elapsedTime += dt

    label.objectValues(objects[0].vx, objects[0].vy, objects[0].ax, objects[0].ay, elapsedTime)

    for obj in objects:
        obj.update(dt)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()