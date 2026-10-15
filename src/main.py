from function import add, subtract, multiply, divide 

def main():
    print("     Welcome to the calculator")
    print("     >>>>>>>>>>>>>>>>>>>>>>>>>")

    operation = {
            "add": add, 
            "subtract": subtract,
            "multiply": multiply,
            "divide": divide
            }

    while True:
        print("     Choose: add, subtract, multiply, divide")
        choose = input("     => ").lower().strip()

        if choose not in operation:
            print("     Error: Invalid operation. Please try again.")
            print("\n")
            continue 

        while True:
            try:
                print("\n")
                print("     Enter the first number: ")
                num_1 = float(input("     => "))
                break
            except ValueError:
                print("     Error: Please enter a valid number.")
                print("\n")

        while True:
            try:
                print("     Enter the second number: ")
                num_2 = float(input("     => "))
                break
            except ValueError:
                print("     Error: Please enter a valid number.")
                print("\n")

        try:
            result = operation[choose](num_1, num_2)
        except ValueError as error:
            print(f"     Error: {error}")
            print("\n")
            continue

        print(f"     >> Result: {result}")
        print(f"     Calculation complete! Thank you for using my calculator.")
        break


if __name__ == "__main__":
    main()

