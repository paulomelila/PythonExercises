# creates a Person class with 5 different attributes
class Person:
    def __init__(self, name, age, height, weight, nationality):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.nationality = nationality

# creates Person variables with different attributes
john = Person('John', 45, 1.80, 78.0, 'Canadian')
alicia = Person('Alicia', 28, 1.63, 59.2, 'Peruvian')
veronica = Person('Veronica', 19, 1.71, 67.4, 'Brazilian')

# function to print a person's different attributes
def print_data(person):
    print(f"Name: {person.name}")
    print(f"Age: {person.age}")
    print(f"Height: {person.height}")
    print(f"Weight: {person.weight}")
    print(f"Nationality: {person.nationality}")

# print the result
print_data(veronica)
print('\n')
print_data(john)
print('\n')
print_data(alicia)