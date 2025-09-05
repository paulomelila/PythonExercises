height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))
bmi = weight / (height ** 2)  # BMI formula

print(f"Your BMI is: {bmi:.2f}")

# BMI thresholds
if bmi < 18.5:
    print("You are underweight")
elif 18.5 <= bmi < 25:
    print("You have a normal weight")
elif 25.0 <= bmi < 30:
    print("You are overweight")
else:
    print("You are obese")