# While loop that increases the counter.
print("Counter loop using while:")
counter = 0 # sets counter to zero
while counter < 5: # while counter is at 0->4 the loop will run
    print("Counter is", counter)
    counter += 1 # increases the counter value for the next loop
print("\n")

# While loop that prints a message until user enters 'exit'.
print("Exit loop example:")
message = input("Type 'exit' to stop the loop: ")
while message != "exit":
    print("You typed:", message)
    message = input("Type 'exit' to stop the loop: ")
print("Loop exited.")
print("\n")

# While loop that uses break to exit the loop.
print("Break loop example:")
while True:
    print("Loop")
    word = input("Type 'exit' to exit the loop:")
    if word == "exit":
        break
print("Loop exited.")
print("\n")

# Nested while loops example.
print("Nested while loops example:")
while True:
    print("You are in the first loop.")
    option1 = input("Do you want to leave the first loop? (yes/no): ")
    if option1 == "yes":
        break
    else:
        while True:
            print("You are in the second loop.")
            option2 = input("Do you want to leave the second loop? (yes/no): ")
            if option2 == "yes":
                break
        print("Exited the second loop.")
print("Exited the first loop.")
print("Program ended.")
print("\n")

# While loop that prints a new message after 3 seconds.
import time # imports the time module to use the sleep function

message = "Hello, this message will appear after every 3 seconds. Press Ctrl+C to stop."
while True:
    print(message)
    time.sleep(3)  # pauses the loop for 3 seconds before repeating