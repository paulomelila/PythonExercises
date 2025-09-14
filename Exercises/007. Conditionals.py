# a simple program analyzes user's age and prints a message based on the age group
age = int(input("How old are you? ")) # ask for user's age and turn it into an integer value

# conditional statement that prints different messages based on age
if age <= 12:
    print("You are a child.")
elif age <= 19:
    print("You are a teenager.")
elif age <= 65:
    print("You are an adult.")
else:
    print("You are an elder.")