# creating a string
text = "Hello, World!"

# accessing individual characters using indexing
first_char = text[0]  # first character
last_char = text[-1] # last character
print(f"The first character of the sentence '{text}' is '{first_char}'")
print(f"The last character of the sentence '{text}' is '{last_char}'")

# accessing a substring using slicing
substring = text[7:12]  # characters from index 7 to 11
print(f"The substring from index 7 to 11 in '{text}' is '{substring}'")

# concatenating strings
greeting = "Hello"
comma = ", "
world = "world"
exclamation = "!"
full_greeting = greeting + comma + world + exclamation
print(f"The full greeting is: '{full_greeting}'")

# dividing a string into a list of substrings using split()
list_of_words = text.split()
print(f"The list of words in the sentence '{text}' is: {list_of_words}")

# modifying a string (strings are immutable, so we create a new string)
modified_text = text.replace("World", "Python")
modified_text = modified_text.replace("!", "?!")
print(f"The modified text is: '{modified_text}'")

# converting the string to uppercase and lowercase
upper_case = text.upper()
lower_case = text.lower()
print(f"The text in uppercase is: '{upper_case}'")
print(f"The text in lowercase is: '{lower_case}'")

#removing whitespace from the beginning and end of a string
text_with_whitespace = "   Hello, World!   "
trimmed_text = text_with_whitespace.strip()
print(f"The text '{text_with_whitespace}' after trimming whitespace is: '{trimmed_text}'")

# checking if a substring exists within the string
substring = "time"
if substring in text:
    print(f"The substring '{substring}' exists in the text '{text}'.")
else:
    print(f"The substring '{substring}' does not exist in the text '{text}'.")

# formatting strings
name = "Pietro"
age = 31
location = "Italy"
# using f-strings for string formatting
print(f"My name is {name}, I am {age} years old and I live in {location}.")
# using the format() method for string formatting
print("My name is {}, I am {} years old and I live in {}.".format(name, age, location))