# defining a function that returns the result of the sum between two given numbers
def sum_of_two_numbers(a, b):
    return a + b
# defining a function that returns the result of the substraction between two given numbers
def substraction_of_two_numbers(a, b):
    return a - b

# asking the user for two numbers
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

# asking the user for an option to choose between sum or substraction
option = int(input("Enter '1' for sum or '2' for substraction: "))

# printing the result
if option == 1: # if user chose option 1, perform sum
    print("{} + {} =".format(first_number, second_number), sum_of_two_numbers(first_number, second_number))
elif option == 2: # if user chose option 2, perform substraction
    print(f"{first_number} - {second_number} =", substraction_of_two_numbers(first_number, second_number))
else:
    print("Invalid option")

# use of default parameters in functions
def greet(name="Guest"): # default value is "Guest" if no name is provided
    print(f"Hello, {name}!")
greet() # calls the function without an argument, uses default value
greet("Paulo") # calls the function with an argument, overrides default value

# example of a recursive function that prints numbers from x down to 1
def regressive(x):
    if x <= 0:
        return
    else:
        print(x)
        regressive(x - 1)
regressive(5) # calls the recursive function starting from 5