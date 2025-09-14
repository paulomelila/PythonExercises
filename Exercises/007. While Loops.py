"""
While loop that increases the counter.
"""
print("Counter loop using while:")
counter = 0 # sets counter to zero
while counter < 5: # while counter is at 0->4 the loop will run
    print("Counter is", counter)
    counter += 1 # increases the counter value for the next loop

"""
While loop that prints a message until user enters 'exit'.
"""
message = input("Type 'exit' to stop the loop:")
while message != "exit":
    print("You typed:", message)
    message = input("Type 'exit' to stop the loop:")
print("Loop exited.")
print("\n")