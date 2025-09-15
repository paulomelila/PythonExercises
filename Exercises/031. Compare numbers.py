# A simple GUI application to compare two numbers using tkinter

import tkinter as tk # Import the tkinter module

# Function to compare two numbers
def compare_numbers(a, b):
    if a > b:
        return "{a} is greater than {b}".format(a=a, b=b)
    elif a < b:
        return "{a} is less than {b}".format(a=a, b=b)
    else:
        return "{a} is equal to {b}".format(a=a, b=b)

# Create the main window
mainWindow = tk.Tk()
mainWindow.title("Compare Two Numbers")
mainWindow.geometry("300x200")

# Label and input field for first number
label1 = tk.Label(mainWindow, text="Enter first number:")
label1.pack()
entry1 = tk.Entry(mainWindow)
entry1.pack()

# Label and input field for second number
label2 = tk.Label(mainWindow, text="Enter second number:")
label2.pack()
entry2 = tk.Entry(mainWindow)
entry2.pack()

# Result label
result_label = tk.Label(mainWindow, text=f"Result:")
result_label.pack()

# Function to handle button click and change result label text accordingly
def on_compare_click():
    first_number = int(entry1.get()) if entry1.get().isdigit() else 0 # Get and validate first number
    second_number = int(entry2.get()) if entry2.get().isdigit() else 0 # Get and validate second number
    result = compare_numbers(first_number, second_number) # Compare the two numbers
    result_label.config(text=f"Result: {result}") # Update the result label with the comparison result

# Compare button to trigger comparison
compare_button = tk.Button(mainWindow, text="Compare", command=on_compare_click) # Create the compare button
compare_button.pack() # Pack the compare button to the window

# Start the main event loop to display the window
mainWindow.mainloop()