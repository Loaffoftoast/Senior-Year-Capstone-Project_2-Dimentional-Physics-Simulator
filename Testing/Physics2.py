import pygame
import sys
from pygame._sdl2 import Window

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

class Window_Border:
    def draw_border():
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, windowRect.width, 36))
    
    def draw_X():
        rect = pygame.Rect(windowRect.width - 36, 0, 36, 36)
        if rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (255, 0, 0), (windowRect.width - 46, 0, windowRect.width, 36))
            pygame.draw.line(screen, (255, 255, 255), (windowRect.width - 18, 12), (windowRect.width - 28, 22), 2)
            pygame.draw.line(screen, (255, 255, 255), (windowRect.width - 28, 12), (windowRect.width - 18, 22), 2)
            
        else:
            pygame.draw.line(screen, (0, 0, 0), (windowRect.width - 18, 12), (windowRect.width - 28, 22), 1)
            pygame.draw.line(screen, (0, 0, 0), (windowRect.width - 28, 12), (windowRect.width - 18, 22), 1)
    
    def draw_fullscreen():
        rect = pygame.Rect(windowRect.width - 92, 0, 46, 36)
        if rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (200, 200, 200), (windowRect.width - 92, 0, 46, 36))
        
        
        

class label:
    def objectValues(vx, vy, ax, ay, elapsedTime):
        values = [
            f"Velocity: {vx:.2f}, {vy:.2f} m/s",
            f"Acceleration: {ax:.2f}, {ay:.2f} m/s²",
            f"Time: {elapsedTime:.3f} s",
        ]
        for index, value in enumerate(values):
            screen.blit(font.render(value, True, (255, 255, 255)), (15, 15 + index * 30))
                    
class Dynamic_Body:
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
        
        
class Static_Body:
    def __init__(self, r):
        self.dx = centerPosX
        self.dy = centerPosY
        
        self.vx = 0
        self.vy = 0
        
        self.ax = 0
        self.ay = 0

        self.r = r
        
    def update(self, dt):
        pygame.draw.circle(screen, (255, 255, 255), (self.dx, self.dy), self.r)
        
objects = []
objects.append(Static_Body(10))

dragging = False
dragOffset = (0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if pygame.Rect(windowRect.width - 36, 0, 36, 36).collidepoint(event.pos):
                running = False
            elif pygame.Rect(0, 0, windowRect.width - 92, 36).collidepoint(event.pos):
                dragging = True
                dragOffset = event.pos
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            dragging = False
        elif event.type == pygame.MOUSEMOTION and dragging:
            window = Window.from_display_module()
            windowX, windowY = window.position
            mouseX, mouseY = pygame.mouse.get_pos()
            window.position = (
                windowX + mouseX - dragOffset[0],
                windowY + mouseY - dragOffset[1],
            )
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
                objects = [Static_Body(10)]
                timeScale = 0.0
        elif event.type == pygame.KEYUP and event.key in (pygame.K_RIGHT, pygame.K_LEFT):
            timeScale = 0.0

    screen.fill((10, 10, 10))
    
    dt = (clock.get_time() / 1000.0) * timeScale
    elapsedTime += dt

    label.objectValues(objects[0].vx, objects[0].vy, objects[0].ax, objects[0].ay, elapsedTime)

    for obj in objects:
        obj.update(dt)

    Window_Border.draw_border()
    Window_Border.draw_X()
    Window_Border.draw_fullscreen()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()