# Example of use of recursion to solve the Tower of Hanoi problem
# The Tower of Hanoi is a mathematical puzzle where we have three rods and n disks.
# The objective of the puzzle is to move the entire stack to another rod, obeying the following rules:
# 1. Only one disk can be moved at a time.
# 2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
# 3. No larger disk may be placed on top of a smaller disk.
# This implementation prints the state of the towers after each move.
# Initial state: Tower A has all disks, Tower B and Tower C are empty.
# Final state: Tower C has all disks, Tower A and Tower B are empty.

# Function to move disk from source to target
def move_disk(source, target):
    disk = source.pop() # Remove the top disk from source
    target.append(disk) # Add the disk to the target

# Function to print the current state of the towers
def print_towers(tower_a, tower_b, tower_c):
    print("Tower A:", tower_a) # Print the state of Tower A
    print("Tower B:", tower_b) # Print the state of Tower B
    print("Tower C:", tower_c) # Print the state of Tower C
    print() # Print a newline for better readability

# Initialize towers
def tower_of_hanoi(number_of_disks, source, target, auxiliary):
    if number_of_disks == 1: # Base case: only one disk to move
        move_disk(source, target) # Move the disk directly from source to target
        print_towers(tower_a, tower_b, tower_c) # Print the state of the towers
    else:
        tower_of_hanoi(number_of_disks - 1, source, auxiliary, target) # Move n-1 disks from source to auxiliary
        move_disk(source, target) # Move the nth disk from source to target
        print_towers(tower_a, tower_b, tower_c) # Print the state of the towers
        tower_of_hanoi(number_of_disks - 1, auxiliary, target, source) # Move n-1 disks from auxiliary to target

# Main program execution starts here
num_of_disks = 3 # Number of disks to be used
tower_a = list(range(num_of_disks, 0, -1)) # Initialize Tower A with disks [3, 2, 1]
tower_b = [] # Initialize Tower B as empty
tower_c = [] # Initialize Tower C as empty
print("Initial State:") # Print initial state message
print_towers(tower_a, tower_b, tower_c) # Print the initial state of the towers
tower_of_hanoi(num_of_disks, tower_a, tower_c, tower_b) # Solve the Tower of Hanoi problem
print("Final State:") # Print final state message
print_towers(tower_a, tower_b, tower_c) # Print the final state of the towers