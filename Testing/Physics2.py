import pygame
import sys
import copy
import json
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
save_status = None
save_status_until = 0

class Window_Border:
    def draw_border():
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, windowRect.width, 36))
    
    def draw_X():
        rect = pygame.Rect(windowRect.width - 46, 0, 46, 36)
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
    global centerPosX, centerPosY
    def __init__(self, dy, dx, mass, v, a, r):
        self.dx = centerPosX + dx
        self.dy = centerPosY + dy

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
    global centerPosX, centerPosY
    def __init__(self, dy, dx, r):
        self.dx = centerPosX + dx
        self.dy = centerPosY + dy

        self.r = r
        
    def update(self, dt):
        pygame.draw.circle(screen, (255, 255, 255), (self.dx, self.dy), self.r)
        
objects = []

dragging = False
dragOffset = (0, 0)




import tkinter as tk
from tkinter import filedialog

# Initialize tkinter and hide its root window
root = tk.Tk()
root.withdraw()
root.attributes('-topmost', True)  # Bring dialog to the front

class FileHandler:
    loaded = None
    # Open file explorer dialog
    def load():
        global objects, initial_objects, elapsedTime, save_status, save_status_until

        file_path = filedialog.askopenfilename(
            title='Select Data File',
            filetypes=[
                ('JSON files', '*.json *.JSON'),
            ],
        )

        if file_path:
            save_status = 'Loading...'
            status_surface = font.render(save_status, True, (255, 255, 255))
            screen.blit(status_surface, (10, windowRect.height - status_surface.get_height() - 10))
            pygame.display.flip()

            with open(file_path, 'r') as f:
                data = json.load(f)

            loaded_objects = []
            for item in data['objects']:
                dx = item['x'] - centerPosX
                dy = item['y'] - centerPosY
                if item['type'] == 'dynamic':
                    obj = Dynamic_Body(
                        dy, dx, item.get('mass'), item['velocity'],
                        item['acceleration'], item['radius']
                    )
                elif item['type'] == 'static':
                    obj = Static_Body(dy, dx, item['radius'])
                else:
                    raise ValueError(f"Unknown object type: {item['type']}")
                loaded_objects.append(obj)

            objects = loaded_objects
            initial_objects = copy.deepcopy(objects)
            elapsedTime = 0.0
            FileHandler.loaded = file_path
            save_status = 'Loaded!'
            save_status_until = pygame.time.get_ticks() + 1200

    def save():
        global initial_objects, save_status, save_status_until

        if FileHandler.loaded == None: 
            file_path = filedialog.asksaveasfilename(
                title='Save Data File',
                defaultextension='.JSON',
                filetypes=[
                    ('JSON files', '*.json *.JSON'),
                ],
            )
        else:
            file_path = FileHandler.loaded

        if file_path:
            save_status = 'Saving...'
            status_surface = font.render(save_status, True, (255, 255, 255))
            screen.blit(status_surface, (10, windowRect.height - status_surface.get_height() - 10))
            pygame.display.flip()

            data = {'objects': []}
            for obj in initial_objects:
                item = {
                    'type': 'dynamic' if isinstance(obj, Dynamic_Body) else 'static',
                    'x': obj.dx,
                    'y': obj.dy,
                    'radius': obj.r,
                }
                if isinstance(obj, Dynamic_Body):
                    item.update({
                        'mass': getattr(obj, 'mass', None),
                        'velocity': [obj.vx, obj.vy],
                        'acceleration': [obj.ax, obj.ay],
                    })
                data['objects'].append(item)

            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
            FileHandler.loaded = file_path
            save_status = 'Saved!'
            save_status_until = pygame.time.get_ticks() + 1200
             
             

# objects.append(Static_Body(20, 100, 10))
# objects.append(Dynamic_Body(-30, -100, None, [-10, 100], [0, -20], 10))
# objects.append(Dynamic_Body(-70, 200, None, [100, 25], [-10, -9.81], 10))

initial_objects = copy.deepcopy(objects)

           

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
                objects = copy.deepcopy(initial_objects)
                timeScale = 0.0
            elif event.key == pygame.K_l:
                FileHandler.load()
            elif event.key == pygame.K_s:
                FileHandler.save()
        elif event.type == pygame.KEYUP and event.key in (pygame.K_RIGHT, pygame.K_LEFT):
            timeScale = 0.0

    screen.fill((10, 10, 10))
    
    dt = (clock.get_time() / 1000.0) * timeScale
    elapsedTime += dt

    #if objects:
    #    label.objectValues(objects[0].vx, objects[0].vy, objects[0].ax, objects[0].ay, elapsedTime)
    #else:
    #    label.objectValues(0, 0, 0, 0, elapsedTime)

    for obj in objects:
        obj.update(dt)

    Window_Border.draw_border()
    Window_Border.draw_X()
    Window_Border.draw_fullscreen()
    if save_status:
        if save_status in ('Saved!', 'Loaded!') and pygame.time.get_ticks() >= save_status_until:
            save_status = None
        else:
            status_surface = font.render(save_status, True, (255, 255, 255))
            screen.blit(status_surface, (10, windowRect.height - status_surface.get_height() - 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()