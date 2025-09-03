# reading of data as String
age_str = "25"
height_str = "1.81"

# conversion of stypes
age = int(age_str)  # converts string to integer
height = float(height_str)  # converts string to float

print(type(age))
print(type(height))

# converting data back to String
message = "Age: " + str(age) + "\nHeight: " + str(height)
print(message)
