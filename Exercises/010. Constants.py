# There is no native constant type variable in Python,
# but the convention is to name a variable that is supposed to
# have a fixed value in all uppercase with underscores

PI_NUMBER = 3.14159

# using Pi constant in a calculation
radius = 5
area = PI_NUMBER * (radius ** 2)
print(f"The area of the circle is: {area}")
