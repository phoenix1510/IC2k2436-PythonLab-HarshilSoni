""" Build a small menu driven calculator with at least 4 operations. It should keep asking for input until the user chooses to exit."""
print("\nMenu:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

while True:
    choice = input("\nEnter choice: ")

    if choice == '5':
        break

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Enter only numbers bruh!")
            continue

        if choice == '1':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Bruh dont divide by 0!")
    else:
        print("Invalid choice bruh!")