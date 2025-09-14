"""
Ask for user's name and print each letter on a new line.
Strings in Python are iterable, meaning we can loop through each character in the string.
"""
print("Print each letter of your name on a new line:")
name = input("What is your name? ")
for letter in name:
    print(letter)
print("\n")

"""
Loop that counts occurrences of a specific letter in a word.
"""
print("Count occurrences of a specific letter in a word:")
text = "programming"
letter_to_find = "r"
counter = 0

for letter in text:
    if letter == letter_to_find:
        counter += 1

print(f"The letter '{letter_to_find}' appears {counter} times in the word '{text}'.")
print("\n")

"""
Loop that prints each name in a list.
Lists in Python are iterable, meaning we can loop through each item in the list.
"""
print("Print each name in a list:")
name_list = ["Albert", "Beth", "Charlie", "Diana"]
for name in name_list:
    print(name)
print("\n")

"""
Loop that prints the square of each number in a list.
Also calculates the sum of the numbers in the list.
"""
print("Print the square of each number in a list:")
number_list = [1, 2, 3, 4, 5]
print("Number list:", number_list, sep=" ")
for number in number_list:
    print(f"The square of {number} is {number ** 2}")
sum = 0
for number in number_list:
    sum += number
print("The sum of the numbers in the list is", sum)
print("\n")

"""
Loop that prints numbers in range of 10.
Range loops start at zero and go to one less than the range size
so a range (10) would start at 0 and stop at 9.
to print 1 -> 10, we have to add +1
"""
print("0 -> 9:")

for i in range (10):

    # prints 0->9
    print(i)

print("\n")

print("1 -> 10:")
for i in range(10):

    # prints 1->10
    print(i + 1)

print("\n")

print("1 -> 10: (same line)")
for i in range(10):

    # prints 1->10 in the same line
    print(i+1, end=" ")

print("\n")

"""
The initial and final values of the range can be manually set.
The range function can take a third argument that sets the step/increment value.
The final value is exclusive, so the loop stops before reaching it.
"""
print("1 -> 9 (step: 2):")
for item in range(1, 9, 2):  # for loop that starts at 1, ends before 10, and increases by 2
    print(item)
print("\n")

"""
Loop that prints the multiplication table of a number.
"""
number = int(input("Enter a number to find its multiplication table: "))
print(f"Multiplication table of {number}:")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
print("\n")

"""
Loop that increases the counter.
"""
print("Counter loop using while:")
counter = 0 # sets counter to zero
while counter < 5: # while counter is at 0->4 the loop will run
    print("Counter is", counter)
    counter += 1 # increases the counter value for the next loop