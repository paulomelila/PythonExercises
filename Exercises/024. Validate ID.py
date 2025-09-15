# Function to validate a national identification number
# The ID number must have 11 digits and follow specific rules for check digits
# The function returns True if the ID number is valid, otherwise False
# Example of a valid ID number: "123.456.789-09"

def validate_id(id_number):
    # Remove any non-digit characters from the ID number
    id_number = ''.join(filter(str.isdigit, id_number))

    # Check if the ID number has exactly 11 digits
    if len(id_number) != 11:
        return False

    # Check if all digits are the same
    if id_number == id_number[0] * 11:
        return False

    # Calculate the first check digit
    sum1 = sum(int(id_number[i]) * (10 - i) for i in range (9))
    rest = sum1 % 11

    if rest < 2:
        check_digit1 = 0
    else:
        check_digit1 = 11 - rest

    # verify the first check digit
    if int(id_number[9]) != check_digit1:
        return False

    # Calculate the second check digit
    sum2 = sum(int(id_number[i]) * (11 - i) for i in range(10))
    rest = sum2 % 11
    if rest < 2:
        check_digit2 = 0
    else:
        check_digit2 = 11 - rest

    # verify the second check digit
    if int(id_number[10]) != check_digit2:
        return False

    # If all checks passed, the ID number is valid
    return True

# Test the function with a valid ID number
test_id = "123.456.789-09"

if validate_id(test_id):
    print(f"The ID number {test_id} is valid.")
else:
    print(f"The ID number {test_id} is invalid.")