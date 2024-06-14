print("The Basic Calculator\n")

while True:
    num1 = int(input("Enter the Number 1: "))
    num2 = int(input("Enter the Number 2: "))
    symbol = input("Enter the Symbol (+,-,*,/): ")
    

    match symbol:
        case "+":
            print("\nResult: ", num1 + num2)
        case "-":
            print("\nResult: ", num1 - num2)
        case "*":
            print("\nResult: ", num1 * num2)
        case "/":
            print("\nResult: ", num1 / num2)
        case _:
            print("\nInalid Input")

    option = input("\nCan You Try This Calculator Again (Yes/No): ")

    if option == "Yes" or option == "Y" or option == "y":
        continue
    else:
        print("\nYou Successfully Exit the Calculator")
        break