def calculator():
    print("Simple Calculator")
    print("Operations Available:")
    print("+  -> Addition")
    print("-  -> Subtraction")
    print("*  -> Multiplication")
    print("/  -> Division")

    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator entered.")
                continue

            print("Result:", result)

        except ValueError:
            print("Invalid input. Please enter numbers only.")

        choice = input("\nDo you want to calculate again? (yes/no): ").lower()
        if choice != "yes":
            print("Calculator Closed.")
            break


calculator()