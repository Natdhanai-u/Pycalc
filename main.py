print("     Welcome to the calculator")
print("     >>>>>>>>>>>>>>>>>>>>>>>>>")

while True:
    print("\n")
    print("     Choose: add, subtract, multiply, divide")
    choose = input("     => ").lower().strip()

    if choose not in ("add", "subtract", "multiply", "divide"):
        print("     Error: Invalid operation. Please try again.")
        print("\n")
        continue 

    while True:
        try:
            print("\n")
            print("     Enter the first number: ")
            num_1 = int(input("     => "))
            break
        except ValueError:
            print("     Error: Invalid input!")

    while True:
        try:
            print("     Enter the second number: ")
            num_2 = int(input("     => "))
            break
        except ValueError:
            print("     Error: Invalid input!")
            print("\n")

    if choose == "add":
        print(f"     >> {num_1} + {num_2} = {num_1 + num_2}")
        print("      Calculation done! Thank you for using my calculator.")
        break
    elif choose == "subtract":
        print(f"     >> {num_1} - {num_2} = {num_1 - num_2}")
        print("      Calculation done! Thank you for using my calculator.")
        break
    elif choose == "multiply":
        print(f"     >> {num_1} x {num_2} = {num_1 * num_2}")
        print("     Calculation done! Thank you for using my calculator.")
        break
    elif choose == "divide":
        if num_2 == 0:
            print("Error: cannot divide by zero")
            continue
        else:
            print(f"     >> {num_1} ÷ {num_2} = {num_1 / num_2}")
            print("      Calculation done! Thank you for using my calculator.")
            break


