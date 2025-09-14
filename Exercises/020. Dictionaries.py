# creating a dictionary with a few key-value pairs
my_dictionary = {
    "Name": "Alice",
    "Age": 30,
    "City": "New York"
}

print(my_dictionary)

# accessing individual values by key
name = my_dictionary["Name"]
age = my_dictionary["Age"]
city = my_dictionary["City"]
print(f"Name: {name}")  # prints the value associated with the key "name"
print(f"Age: {age}")  # prints the value associated with the key "age"
print(f"City: {city}")  # prints the value associated with the key "city"

# adding a new key-value pair to the dictionary
my_dictionary["Occupation"] = "Engineer"
print("After adding occupation:", my_dictionary)

# updating the value of an existing key
my_dictionary["Age"] = 31 # updates the value associated with the key "age"
print("After updating age:", my_dictionary)

# removing a key-value pair by key
del my_dictionary["City"] # removes the key-value pair with key "city"
print("After removing city:", my_dictionary)

# accessing all keys and values in the dictionary
keys = my_dictionary.keys()
values = my_dictionary.values()

# printing all keys and values
print("Keys in the dictionary:", keys)
print("Values in the dictionary:", values)

# iterating through the dictionary and printing each key-value pair
for key, value in my_dictionary.items():
    print(f"{key}: {value}")

# checking if a key exists in the dictionary
key_search = input("Enter the key you want to search: ").lower().capitalize()  # normalize input to match key format
if key_search in my_dictionary:
    print(f"The key '{key_search}' exists in the dictionary. Its value is:", my_dictionary[key_search])
else:
    print(f"The key '{key_search}' does not exist in the dictionary.")

# using get() method to access a value safely
city = my_dictionary.get("City", "Not Found") # returns "Not Found" if the key doesn't exist
print(f"City: {city}") # city was removed earlier, so it should print "Not Found"

# clearing all key-value pairs from the dictionary
my_dictionary.clear()
print("After clearing the dictionary:", my_dictionary)