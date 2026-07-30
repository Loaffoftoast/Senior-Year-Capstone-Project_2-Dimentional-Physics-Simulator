#https://stackoverflow.com/questions/64543449/update-during-resize-in-pygame

import ctypes as ct
from ctypes import wintypes as w

import pygame

# ===== Windows API Constants and Type Definitions =====
# LPARAM is typedef'ed as LONG_PTR in winuser.h, so it can be used
# for LRESULT and LONG_PTR which are missing from wintypes.
LRESULT = LONG_PTR = w.LPARAM
# WNDPROC is a callback function type for window procedures
WNDPROC = ct.WINFUNCTYPE(LRESULT, w.HWND, w.UINT, w.WPARAM, w.LPARAM)
# WM_SIZE: Windows message identifier for window resize events
WM_SIZE = 0x0005
# RDW_INVALIDATE: Flag to invalidate the window region
RDW_INVALIDATE = 0x0001
# RDW_ERASE: Flag to erase the background before repainting
RDW_ERASE = 0x0004
# GWL_WNDPROC: Index for getting/setting the window procedure
GWL_WNDPROC = -4

# ===== Load and Define Windows user32 DLL Functions =====
# ctypes.windll.user32 is a cached, shared version of user32.dll.
# Get our own copy and meticulously define argtypes/restype according
# to MSDN documentation of the C prototypes.
user32 = ct.WinDLL('user32')

# GetWindowLongPtrA: Retrieves information about the specified window
user32.GetWindowLongPtrA.argtypes = w.HWND, ct.c_int
user32.GetWindowLongPtrA.restype = LONG_PTR

# GetForegroundWindow: Gets the currently active window handle
user32.GetForegroundWindow.argtypes = ()
user32.GetForegroundWindow.restype = w.HWND

# RedrawWindow: Redraws the specified window region
user32.RedrawWindow.argtypes = w.HWND, w.LPRECT, w.HRGN, w.UINT
user32.RedrawWindow.restype = w.BOOL

# CallWindowProcA: Calls the original window procedure with the message
user32.CallWindowProcA.argtypes = WNDPROC, w.HWND, w.UINT, w.WPARAM, w.LPARAM
user32.CallWindowProcA.restype = LRESULT

# SetWindowLongPtrA: Sets information about the specified window
user32.SetWindowLongPtrA.argtypes = w.HWND, ct.c_int, LONG_PTR
user32.SetWindowLongPtrA.restype = LONG_PTR

pygame.init()

font = pygame.font.SysFont("Arial", 36)
text_surface = 0

# Create a resizable pygame window with double buffering
screen = pygame.display.set_mode((320, 240), pygame.RESIZABLE | pygame.DOUBLEBUF)

monitor_info = pygame.display.Info()

resWidth, resHeight = pygame.display.get_desktop_sizes()[0]


def draw_game():
    
    global text_surface
    global resHeight
    
    scalemult = (monitor_info.current_h / screen.get_height())

    width = (f"Width: {screen.get_width()}")
    height = (f"Height: {screen.get_height()}")
    moniter_height = (f"mon height: {resHeight}")
    scale = (f"Scale: {(resHeight // screen.get_height())}")
    
    text_width = font.render(width, True, (255, 255, 255))
    text_height = font.render(height, True, (255, 255, 255))
    text_monitor_height = font.render(moniter_height, True, (255, 255, 255))
    text_scale = font.render(scale, True, (255, 255, 255))
    
    screen.fill(pygame.Color('black'))
    
        # Clears screen with black background
    # Draws a red rectangle with 10-pixel margin
    pygame.draw.rect(screen, pygame.Color('red'), pygame.Rect(0,0,screen.get_width(),screen.get_height()).inflate(-10, -10))
    pygame.draw.circle(screen, pygame.Color(0, 0, 0), (screen.get_width() // 2, screen.get_height() // 2), (50 // scalemult))
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), pygame.Rect(screen.get_width() // 2,screen.get_height() // 2, 5, 5))
    
    screen.blit(text_width, (10, 10))
    screen.blit(text_height, (10, 40))
    screen.blit(text_monitor_height, (10, 70))
    screen.blit(text_scale, (10, 100))
    
    # Updates the display to show the drawn content
    pygame.display.flip()

# Get the original window procedure to preserve it
old_window_proc = user32.GetWindowLongPtrA(user32.GetForegroundWindow(), GWL_WNDPROC)

def new_window_proc(hwnd, msg, wparam, lparam):
    # Intercept WM_SIZE messages (window resize events)
    if msg == WM_SIZE:
        draw_game()
        # Force the window to redraw
        user32.RedrawWindow(hwnd, None, None, RDW_INVALIDATE | RDW_ERASE)
    # LONG_PTR is the same bit width as WNDPROC, but
    # need cast to use it here.
    # Pass the message to the original window procedure
    return user32.CallWindowProcA(ct.cast(old_window_proc, WNDPROC), hwnd, msg, wparam, lparam)

# Create a callback wrapper for the new window procedure
new_window_proc_cb = WNDPROC(new_window_proc)

# Can't cast a WNDPROC (pointer) to a LONG_PTR directly, but can cast to void*.
# The .value of a c_void_p instance is its integer address.
# Hook the new window procedure to intercept Windows messages
user32.SetWindowLongPtrA(user32.GetForegroundWindow(), GWL_WNDPROC, ct.cast(new_window_proc_cb, ct.c_void_p).value)

# Main event loop
while True:
    # Process pygame events
    for event in pygame.event.get():
        # Exit on window close
        if event.type == pygame.QUIT:
            pygame.quit()
        # Handle window resize events
        elif event.type == pygame.VIDEORESIZE:
            pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE| pygame.DOUBLEBUF)
    # Redraw the game on each frame
    draw_game()
    