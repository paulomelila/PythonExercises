def calculate_expression():
    expression = input("Enter a math expression: ")

    try:
        # evaluate expression using eval()
        result = eval(expression)
        print(f"The result of the expression: {expression} = {result}")
    except Exception as error:
        print(f"The expression failed to evaluate: {error}")


calculate_expression()
