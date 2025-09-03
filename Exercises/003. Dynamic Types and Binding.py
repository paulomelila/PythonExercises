# Example of dynamic types and binding in Python

# binding of an integer value to a variable x
x = 5

# prints the current type of the variable
print("Variable type:", type(x))

# binding of a String value to the same variable x
x = "Hello"

# prints the current type of the variable x
print("Variable type:", type(x))

# binding a new value to the same variable
y = 10
print(y)
y += 2  # same as y = y + 2
y -= 2  # same as y = y - 2
y *= 2  # same as y = y * 2
y /= 2  # same as y = y / 2
y %= 2  # same as y = y % 2
print(y)

# multiple binding
a, b, c = 1, 2, 3 # binds multiple variables in the same line
print(a, b, c)
# swap values between them
a, b, c = c, a, b
print(a, b, c)