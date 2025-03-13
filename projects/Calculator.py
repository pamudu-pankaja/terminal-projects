while True:
    num1 = input("Enter the 1st Number: ")
    if num1 == "":
        print("Please enter a number 1")
        continue  # Restart only the number 1 input
    
    operator = input("Enter an operator (/,+,-,*): ")
    if operator == "":
        print("Please enter an operator")
        continue  # Restart only the operator input
    
    num2 = input("Enter the 2nd Number: ")
    if num2 == "":
        print("Please enter number 2")
        continue  # Restart only the number 2 input
    
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Please enter valid numbers")
        continue  # Restart the loop if input is not a valid number

    if operator == "/":
        result = num1 / num2
        print(f"Result: {result}")
    elif operator == "+":
        result = num1 + num2
        print(f"Result: {result}")
    elif operator == "-":
        result = num1 - num2
        print(f"Result: {result}")
    elif operator == "*":
        result = num1 * num2
        print(f"Result: {result}")
    else:
        print(f"{operator} is not a valid operator")
        continue  # Restart only the operator input if invalid

input("Press Enter to exit...")
