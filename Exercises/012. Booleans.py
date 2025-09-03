person = "Alex"
age = 68

isOfLegalAge = age >= 18 # boolean value to see if a person is of legal age
isAnElder = age >= 65

if isOfLegalAge and isAnElder:  # Checks if both statements are true at the same time
    print(f"{person} is of legal age and also an elder")
else:
    if isOfLegalAge:  # print when only isOfLegalAge is true
        print(f"{person} is of legal age and not an elder")
    else:  # print when both booleans are false
        print(f"{person} is not of legal age")