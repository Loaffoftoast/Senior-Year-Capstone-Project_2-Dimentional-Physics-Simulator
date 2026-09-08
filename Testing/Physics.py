import pygame
import sys
import math

pygame.init()
BACKGROUND = (0, 0, 0)
POSITION_FONT = pygame.font.Font(None, 20)

class physics:

    distance = 0
    time = 0.0 # Time in seconds
    time_running = False
    clock = pygame.time.Clock()

    # Set the velocity magnitude and direction. The component velocities are
    # calculated from these values and then used to find the position.
    velocity = -105
    angle_degrees = 180
    angle_radians = math.radians(angle_degrees)
    vX = velocity * math.cos(angle_radians)
    vY = velocity * math.sin(angle_radians)
    
    posX = 0
    posY = -1200
    
    screen = pygame.display.set_mode((0, 0), pygame.NOFRAME | pygame.DOUBLEBUF)
    windowRect = screen.get_rect()
    centerPos = ((windowRect.left + windowRect.right) // 2, (windowRect.top + windowRect.bottom) // 2)
    centerPosX, centerPosY = centerPos

    def getDistance(velocity, time):
        return velocity * time

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                time_running = not time_running
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                sys.exit()

        delta_time = clock.tick(60) / 1000.0
        keys = pygame.key.get_pressed()
        if time_running:
            time += delta_time
        if keys[pygame.K_RIGHT]:
            time += delta_time
        if keys[pygame.K_LEFT]:
            time -= delta_time
            
        screen.fill(BACKGROUND)
            
            
            
            
            
        posX = (vX * time) + centerPosX
        posY = centerPosY - (vY * time) 
        
        pygame.draw.circle(screen, (150, 150, 150), (posX, posY), 7)

        time_label = POSITION_FONT.render(f"Time: {time:.2f}s", True, (255, 255, 255))
        screen.blit(time_label, (10, 10))

        position_label = POSITION_FONT.render(
            f"({(posX - centerPosX):.1f}, {-(posY - centerPosY):.1f})", True, (255, 255, 255)
        )
        screen.blit(
            position_label,
            (
                int(posX) - 10 - position_label.get_width(),
                int(posY) - 10 - position_label.get_height(),
            ),
        )

        line_length = 100
        pygame.draw.line(
            screen,
            (150, 150, 150),
            (posX, posY),
            (
                posX + line_length * math.cos(angle_radians),
                posY - line_length * math.sin(angle_radians),
            ),
            2,
        )
        
        angle_label = POSITION_FONT.render(
            f"{angle_degrees:.1f}°", True, (255, 255, 255)
        )
        screen.blit(
            angle_label, 
            (
                int(posX) - 10 + angle_label.get_width(),
                int(posY) + 10 - position_label.get_height(),
            ),
        )




        print(posX, posY)



        # Update the full display Surface to the screen
        pygame.display.flip()
