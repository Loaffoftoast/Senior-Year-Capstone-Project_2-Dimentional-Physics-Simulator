import os
import sys
import pygame

class keybinds:
    def keyPressed(keybind):
        if objects:
            if keybind[pygame.K_LEFT] and not left_arrow_pressed:
                selected_circle = (selected_circle - 1) % len(objects)
            if keybind[pygame.K_RIGHT] and not right_arrow_pressed:
                selected_circle = (selected_circle + 1) % len(objects)

            # Move the selected object with WASD.
            if keybind[pygame.K_w]:
                objects[selected_circle][1] -= movement_speed
            if keybind[pygame.K_a]:
                objects[selected_circle][0] -= movement_speed
            if keybind[pygame.K_s]:
                objects[selected_circle][1] += movement_speed
            if keybind[pygame.K_d]:
                objects[selected_circle][0] += movement_speed
        
        if keybind[pygame.K_SPACE] and not space_pressed:
            new_object = [mouse_pos_x, mouse_pos_y]
            objects.append(new_object)
            space_pressed = True
        elif not keybind[pygame.K_SPACE]:
            space_pressed = False

        # Remove any object under the mouse when Backspace is pressed.
        if keybind[pygame.K_BACKSPACE]:
            objects_to_remove = []
            for index, obj in enumerate(objects):
                distance = ((obj[0] - mouse_pos_x) ** 2 + (obj[1] - mouse_pos_y) ** 2) ** 0.5
                if distance <= 15:
                    objects_to_remove.append(index)

            for index in sorted(objects_to_remove, reverse=True):
                objects.pop(index)

            if objects:
                selected_circle = min(selected_circle, len(objects) - 1)
            else:
                selected_circle = 0
                

# Initialize the game window and font.
pygame.init()
screen = pygame.display.set_mode((1080, 720))
font = pygame.font.Font(None, 18)

# Store all visible objects as [x, y] coordinate pairs.
objects = []

# Track whether keys were pressed in the previous frame so we can detect edge presses.

space_pressed = False
left_arrow_pressed = False
right_arrow_pressed = False

# Which object is currently selected for movement.
selected_circle = 0
movement_speed = 0.5

# Main game loop.
running = True
while running:
    # Handle all events that Pygame detects this frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen each frame.
    screen.fill((0, 0, 0))

    # Retrieve the current keyboard and mouse state.
    keybinds.keyPressed(pygame.key.get_pressed())
    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()

    left_arrow_pressed = [pygame.K_LEFT]
    right_arrow_pressed = [pygame.K_RIGHT]
    space_pressed = [pygame.K_SPACE]

    # Display which object is currently selected.
    if objects:
        selected_text = font.render(
            f"Controlling circle {selected_circle + 1}",
            True,
            (255, 255, 255),
        )
        screen.blit(selected_text, (10, 10))

    # Draw every object and label it with its index.
    for object_number, obj in enumerate(objects, 1):
        pygame.draw.circle(screen, (255, 255, 255), (obj[0], obj[1]), 15)
        coordinate_text = font.render(
            f"{object_number}: ({obj[0]:.0f}, {obj[1]:.0f})",
            True,
            (255, 255, 255),
        )
        screen.blit(coordinate_text, (obj[0] + 20, obj[1] - 12))

    # Update the display with all drawing done this frame.
    pygame.display.flip()

pygame.quit()
sys.exit()
