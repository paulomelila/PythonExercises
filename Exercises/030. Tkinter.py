# exploration of tkinter module
# A simple GUI application with a button and labels
# Import the tkinter module
from email.policy import default
from tkinter import * # Import everything from the tkinter module
from tkinter import messagebox # Import the messagebox module from tkinter

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

# Adding two numbers from user input
entry_label = Label(mainWindow, text="Enter two numbers to sum: ")
entry_label.pack() # Pack the entry label to the window

entry_num1 = Entry(mainWindow) # Create the first entry widget for user input
entry_num2 = Entry(mainWindow) # Create the second entry widget for user input
entry_num1.pack() # Pack the first entry widget to the window
entry_num2.pack() # Pack the second entry widget to the window

result_label = Label(mainWindow, text="Result: ")
result_label.pack() # Pack the result label to the window

def sum_numbers():
    num1 = int(entry_num1.get()) # Get the first number from the entry widget
    num2 = int(entry_num2.get()) # Get the second number from the entry widget
    result = num1 + num2 # Calculate the sum of the two numbers
    result_label.config(text="Result: {}".format(result)) # Update the result label with the sum

btn_sum = Button(mainWindow, text="Sum numbers", command= sum_numbers)
btn_sum.pack() # Pack the sum button to the window

mainWindow.mainloop() # Start the main event loop to display the window