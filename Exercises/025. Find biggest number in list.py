def find_biggest_number(numbers_list):
    """
    Function to find the biggest number in a list of numbers
    :param numbers_list:
    :return: the biggest number in the list
    """
    if len(numbers_list) == 0: # handle empty list case
        return None
    if len(numbers_list) == 1: # handle single element list case
        return numbers_list[0]

    biggest_number = numbers_list[0] # assume the first number is the biggest

    for number in numbers_list:
        if number > biggest_number:
            biggest_number = number # update biggest_number if a bigger number is found
    return biggest_number

# Test the function with a list of numbers
numbers = [1, 3, 7, 0, -5, 12, 4]
print(f"The biggest number in the list is: {find_biggest_number(numbers)}")