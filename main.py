print("     Welcome to the calculator")
print("     >>>>>>>>>>>>>>>>>>>>>>>>>")

print("     Choose: add, subtract, multiply, divide")
choose = input("     => ").lower()

print("\n")
print("     Enter the first number: ")
num_1 = int(input("     => "))

print("     Enter the second number: ")
num_2 = int(input("     => "))

if choose == "add":
    print(f"     >> {num_1} + {num_2} = {num_1 + num_2}")
elif choose == "subtract":
    print(f"     >> {num_1} - {num_2} = {num_1 - num_2}")
elif choose == "multiply":
    printf("     >> {num_1} x {num_2} = {num_1 * num_2}")
elif choose == "divide":
    if (num_2 == 0):
        print("Error: cannot divide by zero")
    else:
        print(f"     >> {num_1} ÷ {num_2} = {num_1 // num_2}")
