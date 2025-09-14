# creating a list with a few elements
list_of_months = ["January", "February", "March", "April", "May"]
print(list_of_months)

# accessing individual elements by index
print(f"{list_of_months[0]} is the first month of the year.") # prints first element

# adds an element to the end of the list
print("Adding June to the list of months.")
list_of_months.append("June")
print(list_of_months)

# inserting an element at a specific index
list_of_months.insert(0, "July") # inserts an element at index 0
print("Inserting July at the start of the list.")
print(list_of_months)
print(f"Now {list_of_months[0]} is the first month of the year.")

# removing an element by value
list_of_months.remove("July") # removes the element with value "July"
print("Removing July from the list.")
print(list_of_months)

# removing the last element from the list
print("Removing the last month from the list.")
last_month = list_of_months.pop()
print(f"List of months after removing {last_month}:", list_of_months) # prints the list after removing the last element

# accessing a subgroup from the list (slicing)
first_three_months = list_of_months[0:3] # gets the first three elements
print("The first three months of the year are:", first_three_months)

# sorting the list in alphabetical order
print("Sorting the list of months in alphabetical order.")
list_of_months.sort()
print(list_of_months)