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

#-------------------------------------------------------

# printing sequences
seq = [1, 2, 3]
print(seq)

# printing substrings
text = "Python"
print(text[0])
print(text[0:3])    # prints index 0->2, not 3
print(text[3:6])    # prints index 3->5, not 6
print(text[::-1])   # inverts the word