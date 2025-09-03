# Example of use of a standard Python library

import math # imports the math module that provides access to mathematical functions

# Calculating the square root of a number

number = 122

# FUNCTION: sqrt(number) -> calculates the square root of a given number
square_root = math.sqrt(number)

if square_root.is_integer():  # removes the .0 if it's a perfect square
    print(f"The square root of {number} is {int(square_root)}")
else:
    print(f"The square root of {number} is {square_root}")