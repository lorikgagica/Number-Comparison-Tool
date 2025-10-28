# (Enhanced) Number Comparison Tool

def status(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

def compare_two():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("\n--- Comparison Results ----")
    if num1 == num2:
        print(f"Both numbers are equal: {num1}")
    elif num1 > num2:
        print(f"{num1} is greater than {num2}")
    else:
        print(f"{num2} is greater than {num1}")

    print(f"{num1} is {status(num1)}")
    print(f"{num2} is {status(num2)}")

    if num1 == 0 or num2 == 0:
        print("\nAt least one number is zero.")
    else:
        print("\nBoth numbers are non-zero.")

def compare_three():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))
    print("\n--- Comparison Results ---")
    if a == b == c:
        print(f"All numbers are equal: {a}")
    else:
        largest = max(a, b, c)
        print(f"The largest number is: {largest}")

    print(f"{a} is {status(a)}")
    print(f"{b} is {status(b)}")
    print(f"{c} is {status(c)}")

    if a == 0 or b == 0 or c == 0:
        print("\nAt least one number is zero.")
    else:
        print("\nNone of the numbers is zero.")

while True:
    print("\nChoose an option:")
    print("1. Compare two numbers")
    print("2. Compare three numbers")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        compare_two()
    elif choice == "2":
        compare_three()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")