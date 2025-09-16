# A simple GUI application that tracks and displays mouse behavior using tkinter

import tkinter as tk

# Function to update mouse coordinates
def update_coordinates(event):
    x, y = event.x, event.y
    coord_label.config(text=f"Mouse Coordinates: X={x}, Y={y}")

# Function to capture mouse click event
def capture_click(event):
    click_label.config(text=f"Mouse clicked at: X={event.x}, Y={event.y}")

# Create the main window
mainWindow = tk.Tk()
mainWindow.title("Mouse Watcher")
mainWindow.geometry("400x300")

# Create a label to display mouse coordinates
coord_label = tk.Label(mainWindow)
coord_label.pack()

# create a label to display mouse click location
click_label = tk.Label(mainWindow)
click_label.pack()

# Bind mouse motion and click events to their respective handlers
mainWindow.bind('<Motion>', update_coordinates)
mainWindow.bind('<Button-1>', capture_click)

mainWindow.mainloop() # Start the main event loop to display the window