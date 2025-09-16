# Exception Handling Exercises

# Exercise 1: Calculate the result of a math expression provided as a string.
# Use the eval() function to evaluate the expression and handle any exceptions that may occur.
def calculate_expression():
    expression = input("Enter a math expression: ")

    try:
        # evaluate expression using eval()
        result = eval(expression)
        print(f"The result of the expression: {expression} = {result}")
    except Exception as error:
        print(f"The expression failed to evaluate: {error}")

calculate_expression()

# Exercise 2: Create a function that takes two numbers as input and returns their division.
# Handle exceptions for invalid input (non-numeric values) and division by zero.
def divide_numbers():
    while True:
        try:
            number_1 = int(input("Enter the first number: "))
            number_2 = int(input("Enter the second number: "))
            print(f"{number_1}/{number_2} = {number_1 / number_2}")
            break
        except TypeError as error:
            print(f"Error: {error} -> Please provide two numbers.")
        except ValueError as error:
            print(f"Error: {error} -> Please provide valid numbers.")
        except ZeroDivisionError as error:
            print(f"Error: {error} -> Division by zero is not allowed.")
        except Exception as error:
            print(f"Error: {error} -> An unexpected error occurred.")

divide_numbers()
