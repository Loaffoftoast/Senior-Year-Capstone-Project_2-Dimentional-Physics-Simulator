import tkinter as tk


class AppWindow:

  def __init__(self, width=600, height=400, title="Pygame in Tkinter"):
    self.root = tk.Tk()
    self.root.title(title)
    self.running = True

    # Handle the window close button cleanly
    self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    # Create a Tkinter frame to hold the Pygame display
    self.embed_frame = tk.Frame(self.root, width=width, height=height)
    self.embed_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Example Tkinter widget below the Pygame screen
    self.status_label = tk.Label(self.root, text="Tkinter UI Active")
    self.status_label.pack(side=tk.BOTTOM, pady=5)

    # Force Tkinter to draw the window so winfo_id() returns a valid ID
    self.root.update()

  def get_embed_id(self):
    return str(self.embed_frame.winfo_id())

  def on_close(self):
    self.running = False

  def update(self):
    if self.running:
      self.root.update()

  def destroy(self):
    self.root.destroy()