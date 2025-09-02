"""
Loop that prints numbers in range of 10.
loops start at zero and go to one less than the range size
so a range (10) would start at 0 and stop at 9.
to print 1 -> 10, we have to add +1
"""

print("0 -> 9:")
for i in range (10):

    # prints 0->9
    print(i)

print("1 -> 10:")
for i in range(10):

    # prints 1->10
    print(i + 1)

print("1 -> 10: (same line)")
for i in range(10):

    # prints 1->10 in the same line
    print(i+1, end=" ")