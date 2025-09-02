# Python supports different paradigms, like procedural and object-oriented

# Calculation the factorial of a number
number = 7

# PROCEDURAL APPROACH

# creates a function that calculates the factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# prints the result
print("(PROCEDURAL) Factorial of", number, ":", factorial(number))


# OBJECT-ORIENTED APPROACH

# creates a Factorial class
class Factorial:

    # creates a method for this class that calculates factorial
    def calculate(self, n):
        if n == 0:
            return 1
        else:
            return n * self.calculate(n - 1)

# instantiating an object f that belongs to the Factorial class
f = Factorial()

# calls the calculate() method that belongs to the Factorial class
print("(OBJECT-ORIENTED) Factorial of", number, ":", f.calculate(number))
