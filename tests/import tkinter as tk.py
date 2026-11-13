import tkinter as tk
import os
import pygame

root = tk.Tk()
root.title("Display")

screen_frame = tk.Frame(root, width=800, height=600)
screen_frame.pack()
screen_frame.pack_propagate(False)
root.update()

# Embed Pygame's display surface in the Tkinter frame (supported on Windows).
os.environ["SDL_WINDOWID"] = str(screen_frame.winfo_id())
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()


def update_pygame():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			root.destroy()
			return

	screen.fill((30, 30, 30))
	pygame.display.flip()
	clock.tick(60)
	root.after(16, update_pygame)


root.after(0, update_pygame)
root.mainloop()
pygame.quit()
