# reading of data as String
age_str = "25"
height_str = "1.81"

# conversion of types
age = int(age_str)  # converts string to integer
height = float(height_str)  # converts string to float

print(type(age))
print(type(height))

# converting data back to string
message = "Age: " + str(age) + "\nHeight: " + str(height)

print(message + "\n")

#-----------------------------------------------------------------------------------

# converts user input (string) to float
grade1 = float(input("Grade 1: "))
grade2 = float(input("Grade 2: "))
grade3 = float(input("Grade 3: "))

# generates the average
average = (grade1 + grade2 + grade3) / 3

# average:.2f -> adds 2 floating points to display the average
print(f"Your average grade is: {average:.2f}")

#-----------------------------------------------------------------------------------

# converts user inputs to int, float and bool
integer = int (input("Type an integer number: "))
floating = float (input("Type a floating number: "))
boolean = input("Type a boolean value (True/False): ").lower()  # lowers all cases

boolean = (boolean == "true")  # checks if the input was "true"

print(f"Integer: {integer}:", type(integer).__name__)
print(f"Floating: {floating}:", type(floating).__name__)
print(f"Boolean: {boolean}:", type(boolean).__name__)