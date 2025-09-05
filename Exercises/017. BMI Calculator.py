# formula that calculates the Body Mass Index (BMI) based on user's weight and height.
def calculate_bmi():
    while True:
        try:
            height = float(input("Enter your height in meters: "))
            weight = float(input("Enter your weight in kg: "))

            # validate data input first to avoid division by zero or negative values
            if height <= 0 or weight <= 0:
                print("Height and weight must be positive values.")
                continue # prompt user to re-enter values

            # calculate and show BMI only if inputs are valid
            bmi = weight / (height ** 2)  # BMI formula
            print(f"Your BMI is: {bmi:.2f}")

            # determine the BMI category
            if bmi < 18.5:
                print("You are underweight")
            elif bmi < 25:
                print("You have a normal weight")
            elif bmi < 30:
                print("You are overweight")
            else:
                print("You are obese")

            break # exit the loop after successful calculation

        # handle non-numeric input
        except ValueError:
            print("Invalid input. Please enter numeric values for height and weight.")

# Run the BMI calculator
calculate_bmi()
