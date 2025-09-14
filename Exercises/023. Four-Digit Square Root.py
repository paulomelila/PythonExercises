import math

# Find all four-digit numbers which can be split into two parts such that
# the sum of the two parts equals the square root of the original number.

print("Costly approach - iterating through all four-digit numbers: 1000 -> 9999\n")
for number in range (1000, 10000):
    first_two_numbers = number // 100 # integer division to get the first two digits
    last_two_numbers = number % 100 # modulus to get the last two digits
    sum = first_two_numbers + last_two_numbers # sum of the two parts

    # check if the sum of the two parts equals the square root of the original number
    if math.sqrt(number) == sum:
        print(f"The square root of {number} is equal to {first_two_numbers} + {last_two_numbers} = {sum}.")

# different approach, iterating through possible square roots,
# this saves some computation only checking 32 to 99 instead of checking from 1000 to 9999
print("\nMore efficient approach - iterating through possible square roots: 32 -> 99\n")
for num in range (32, 100): # the square root of a four-digit number is between 32 and 99
    square = num ** 2
    first_two_numbers = square // 100
    last_two_numbers = square % 100
    sum = first_two_numbers + last_two_numbers

    if num == sum:
        print(f"The square root of {square} is equal to {first_two_numbers} + {last_two_numbers} = {sum}.")