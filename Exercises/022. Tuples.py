"""
A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
Tuples are used to group together related data.
They are similar to lists, but unlike lists, tuples cannot be modified after their creation (they are immutable).
Tuples can contain elements of different data types, including other tuples.
Tuples are often used to represent fixed collections of items, such as coordinates, RGB color values, or database records.
You can access elements in a tuple using indexing and slicing, just like with lists.
However, since tuples are immutable, you cannot add, remove, or change elements after the tuple is created.
Tuples can be useful for ensuring that data remains constant and unchanged throughout the program.
"""
# creating a tuple
my_tuple = (1, "Hello", 3.14, [10, 20, 30], {"apple": "type of fruit"})
print("My tuple:", my_tuple)

# printing elements in a tuple and their types
for item in my_tuple:
    print(f"Element: {item}: Type: {type(item)}")

# modifying the list inside the tuple
my_tuple[3].append(40)
print("After modifying the list inside the tuple:", my_tuple)

# accessing dictionary value inside the tuple
dict_value = my_tuple[4]["apple"] # accessing the value associated with the key "apple" in the dictionary
print("Accessing the dictionary value inside the tuple:", dict_value)