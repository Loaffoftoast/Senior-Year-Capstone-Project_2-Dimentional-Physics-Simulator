import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize tkinter and hide its root window
root = tk.Tk()
root.withdraw()
root.attributes('-topmost', True)  # Bring dialog to the front

# Open file explorer dialog
file_path = filedialog.askopenfilename(
    title='Select Data File',
    filetypes=[
        ('JSON files', '*.JSON'),
    ],
)

if file_path:
  print(f'Selected file: {file_path}')
  # Now open and read the file using Python
  with open(file_path, 'r') as f:
    data = f.read()
  print(data)