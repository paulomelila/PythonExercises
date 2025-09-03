# the output of data can be formatted in many ways

hours = "10"
minutes = "23"
seconds = "38"

# using string concatenation
print(hours + ":" + minutes + ":" + seconds)

# using f-string
print(f"{hours}:{minutes}:{seconds}")

# using format()
print("{}:{}:{}".format(hours, minutes, seconds))