import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox

class CustomWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")
        
        # 1. Remove the native OS window border/title bar
        self.root.overrideredirect(True)
        
        # Trackers for dragging the frameless window
        self.drag_x = 0
        self.drag_y = 0
        self.is_fullscreen = False
        self.windowed_geometry = None
        
        # Build the custom window layout
        self.create_custom_border()
        self.create_window_content()
        self.toggle_fullscreen()

    def create_custom_border(self):
        # 2. Create a Frame to act as your custom window border/title bar
        self.title_bar = tk.Frame(self.root, bg="#ffffff", height=35)
        self.title_bar.pack(fill="x", side="top")
        self.title_bar.pack_propagate(False) # Keep the strict 35px height
        
        # 3. Add the "File" button directly onto your custom border
        self.file_button = tk.Button(
            self.title_bar, 
            text="File", 
            bg="#ffffff", 
            fg="black", 
            bd=0, 
            activebackground="#dadada", 
            activeforeground="black",
            padx=10,
            command=self.open_file_dialog
        )
        self.file_button.pack(side="left", fill="y")

        self.minimize_button = tk.Button(
            self.title_bar, 
            text="—",
            bg="#ffffff",
            fg="black",
            bd=0,
            activebackground="#dadada",
            activeforeground="black",
            width=6,
            command=self.minimize_window
        )
        self.minimize_button.pack(side="right", fill="y")

        self.fullscreen_button = tk.Button(
            self.title_bar,
            text="□",
            font=("TkDefaultFont", 16),
            bg="#ffffff",
            fg="black",
            bd=0,
            activebackground="#dadada",
            activeforeground="black",
            width=6,
            command=self.toggle_fullscreen
        )
        self.fullscreen_button.pack(side="right", fill="y")
        
        # Add a standard Close (X) button on the far right of the border
        self.close_button = tk.Button(
            self.title_bar, 
            text=" ✕ ", 
            font=("TkDefaultFont", 12),
            bg="#ffffff", 
            fg="black", 
            bd=0, 
            activebackground="#c0392b", 
            activeforeground="white",
            width=6,
            command=self.root.destroy
        )
        self.close_button.pack(side="right", fill="y")

        # Pack in reverse order so the buttons appear left-to-right as: minimize, fullscreen, close
        self.minimize_button.pack_forget()
        self.fullscreen_button.pack_forget()
        self.close_button.pack_forget()

        self.close_button.pack(side="right", fill="y")
        self.fullscreen_button.pack(side="right", fill="y")
        self.minimize_button.pack(side="right", fill="y")

        
        
        # 4. Bind mouse dragging events to the custom title bar
        self.title_bar.bind("<Button-1>", self.start_move)
        self.title_bar.bind("<B1-Motion>", self.do_move)

    def create_window_content(self):
        # Main application body area
        self.content_area = tk.Frame(self.root, bg="#ecf0f1", bd=2, relief="solid")
        self.content_area.pack(fill="both", expand=True)
        
        lbl = tk.Label(self.content_area, text="Main Application Window", bg="#ecf0f1")
        lbl.pack(pady=50)

    # --- Window Dragging Logic ---
    def start_move(self, event):
        self.drag_x = event.x
        self.drag_y = event.y

    def do_move(self, event):
        # Calculate new window position relative to the mouse drag
        x = self.root.winfo_x() + (event.x - self.drag_x)
        y = self.root.winfo_y() + (event.y - self.drag_y)
        self.root.geometry(f"+{x}+{y}")

    def toggle_fullscreen(self):
        if self.is_fullscreen:
            self.root.geometry(self.windowed_geometry)
            self.fullscreen_button.config(text="□")
            self.fullscreen_button.config(font=("TkDefaultFont", 16))
            self.is_fullscreen = False
        else:
            self.windowed_geometry = self.root.geometry()
            self.root.geometry(
                f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0"
            )
            self.fullscreen_button.config(text="❐")
            self.fullscreen_button.config(font=("TkDefaultFont", 12))
            self.is_fullscreen = True

    def minimize_window(self):
        # Turn off override-redirect so the window manager can minimize it.
        self.root.overrideredirect(False)
        self.root.iconify()
        self.root.bind("<Map>", self.restore_frameless_window, add="+")

    def restore_frameless_window(self, event=None):
        if self.root.state() != "iconic":
            self.root.after_idle(lambda: self.root.overrideredirect(True))

    # --- Button Functionality ---
    def open_file_dialog(self):
        # Simple file picker triggered by the title bar button
        filename = fd.askopenfilename(
            title="Open a file",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
        )
        if filename:
            messagebox.showinfo("Selected File", f"You chose:\n{filename}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = CustomWindow()
    app.run()