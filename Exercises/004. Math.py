# Example of use of a standard Python library to perform mathematical operations

import math # imports the math module that provides access to mathematical functions

# Calculating the square root of a number
number = 122
# FUNCTION: sqrt(number) -> calculates the square root of a given number
square_root = math.sqrt(number)

if square_root.is_integer():  # removes the .0 if it's a perfect square
    print(f"The square root of {number} is {int(square_root)}")
else:
    print(f"The square root of {number} is {square_root}")

# Rounding numbers up and down
# FUNCTION: floor(n) -> returns the largest integer less than or equal to n
# FUNCTION: ceil(n) -> returns the smallest integer greater than or equal to n
n = 6.8 # example number
print(f"Rounding down {n} to its nearest integer = {math.floor(n)}") # rounds down to the nearest integer
print(f"Rounding up {n} to its nearest integer = {math.ceil(n)}") # rounds up to the nearest integer