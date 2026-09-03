import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((500, 500))
BACKGROUND = (0, 0, 0)

class physics:

    distance = 0
    time = 0.0 # Time in seconds
    time_running = False
    clock = pygame.time.Clock()


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

        delta_time = clock.tick(60) / 1000.0
        keys = pygame.key.get_pressed()
        if time_running:
            time += delta_time
        if keys[pygame.K_RIGHT]:
            time += delta_time
        if keys[pygame.K_LEFT]:
            time -= delta_time
            
        distance = getDistance(60, time)

        # Clear screen with background color
        screen.fill(BACKGROUND)


        print(time, distance)



        # Update the full display Surface to the screen
        pygame.display.flip()
