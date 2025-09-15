# exploration of tkinter module
# A simple GUI application with a button and labels
# Import the tkinter module
from tkinter import * # Import everything from the tkinter module

mainWindow = Tk() # Create the main window
mainWindow.title("My First GUI") # Set the title of the window
mainWindow.geometry("400x300") # Set the size of the window

# intro message to the user
intro_text = Label(mainWindow, text="Hello, Tkinter!") # Create a label with some text
intro_text.pack() # Pack the label to the window (default is top center)

# message related to button
btn_text = Label(mainWindow, text="Click the button below") # Create a label with some text
btn_text.pack() # Pack the label to the window (default is top center)

# button click event handler function
def on_button_click():
    btn_text.config(text="Button clicked!") # Change the label text when the button is clicked

# Create a button with some text and bind it to the click event handler function
btn = Button(mainWindow, text="Click me!", command=on_button_click)
btn.pack() # Pack the button to the window (default is top center)

mainWindow.mainloop() # Start the main event loop to display the window