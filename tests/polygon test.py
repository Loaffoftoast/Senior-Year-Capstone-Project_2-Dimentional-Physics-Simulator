import pygame
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
center = (200, 125)
radius = 100
point_count = 5
rotation = 0
left_pressed = False
right_pressed = False
dragging = False
resizing = False
drag_offset = (0, 0)

while running:
    dt = clock.tick(60) / 1000.0

    if left_pressed:
        rotation -= math.radians(180) * dt
    if right_pressed:
        rotation += math.radians(180) * dt

    points = []
    for i in range(point_count):
        angle = -math.pi / 2 + rotation + i * (2 * math.pi / point_count)
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        points.append((x, y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left_pressed = True
            elif event.key == pygame.K_RIGHT:
                right_pressed = True
            elif event.key == pygame.K_SPACE:
                point_count += 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_pressed = False
            elif event.key == pygame.K_RIGHT:
                right_pressed = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if math.hypot(event.pos[0] - center[0], event.pos[1] - center[1]) <= 10:
                    dragging = True
                    drag_offset = (center[0] - event.pos[0], center[1] - event.pos[1])
                elif any(math.hypot(event.pos[0] - x, event.pos[1] - y) <= 12 for x, y in points):
                    resizing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
                resizing = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                center = (event.pos[0] + drag_offset[0], event.pos[1] + drag_offset[1])
            elif resizing:
                radius = max(10, math.hypot(event.pos[0] - center[0], event.pos[1] - center[1]))

    screen.fill((0, 0, 0))
    
    points = []
    for i in range(point_count):
        angle = -math.pi / 2 + rotation + i * (2 * math.pi / point_count)
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        points.append((x, y))

    pygame.draw.polygon(screen, (255, 0, 0), points)
    pygame.draw.circle(screen, (255, 255, 255), center, 5)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

