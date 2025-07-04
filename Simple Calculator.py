import math


def main():
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")    
    print("5. Power (^)")
    print("6. Factorial (!)")
    
    choice = input("Enter choice (1-6): ")

    if choice in ['1', '2', '3', '4', '5', '6']:
        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        if choice == '1':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")

        elif choice == '2':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")

        elif choice == '3':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")

        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")

        elif choice == '5':
            result = num1 ** num2
            print(f"{num1} ^ {num2} = {result}")

        elif choice == '6':
            num = int(input("Enter a non-negative integer for factorial: "))
            if num < 0:
                print("Error: Factorial is not defined for negative numbers.")
            else:
                result = math.factorial(num)
                print(f"{num}! = {result}")

    else:
        print("Invalid input: Please select a valid operation.")


if __name__ == "__main__":
    main()