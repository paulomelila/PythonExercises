"""
    Variables in Python can be GLOBAL or LOCAL
    Global variables can be accessed from anywhere
    Local variables can't be accessed from outside the function
"""

# global scope variable
global_message = "I am a global variable"

def my_function():
    # local scope variable
    local_message = "I am a local variable"
    print(local_message)

print(global_message)
my_function()

# ERROR: trying to directly access a local variable from outside the function
# print(local_message)

# global variables can be accessed from within a function

a = 3  # this variable has global scope

def multiplicator(number):
    global a  # all references to the variable are to the global
    a = 2  # the global variable will be changed
    print(f"Inside the function the variable a is: {a}")
    return a * number

b = multiplicator(5) # the function will change the value of 'a' from 3 to 2
print(f"The variable b is: {b}")
print(f"Outside the function, the variable a is: {a}")