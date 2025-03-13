
while True:
    while True:
        num1 = input("Enter the 1st Number : ")
        if num1 == "":
            print("Please enter a number ")
        else:
            break


    while True:
        operator = input("Enter a operator (+,-,/,*) : ")
        if operator == "":
            print("Please enter a operator ")
        else:
            break
    while True:
        num2 = input("Enter the 2nd Number : ")
        if num2 == "":
            print("Please enter a number ")
        else:
            break

    num1 = float(num1)
    num2 = float(num2)

    if operator == "/":
        result = num1 / num2

    elif operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    else:
        print(f"{operator} is not an operator")
        continue
    print(f"The result is : {result}")






