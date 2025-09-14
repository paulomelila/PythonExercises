"""
There are many variables in Python, the most used ones are:

Integers (int): Whole numbers, positive or negative, without a decimal point
Floats (float): Numbers with a decimal point, representing real numbers
Strings (str): Sequences of characters, enclosed in single or double quotes.
Booleans (bool): Represent truth values, either True or False.
"""

name = "Albert"  # String (str)
age = 33    # Integer (int)
height = 1.76 # Float (float)
is_of_legal_age = age >= 18 # Boolean (bool)

print(type(name))
print(type(age))
print(type(height))
print(type(is_of_legal_age))

print(name, f"is {age} years-old,", f"{height}m tall")

if is_of_legal_age:
    print(f"{name} is of legal age")
else:
    print(f"{name} is a minor")