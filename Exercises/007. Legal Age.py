# a simple program to determine if someone is of legal age (+18)

age = input("How old are you? ") # ask for user's age
age = int(age) # turns the answer into an integer value

# conditional statement that analyzes if user is >= 18 years old
if age >= 18:
    print("You are of legal age.") # user's age is >= 18
else:
    print("You are not old enough.") # user's age is < 18