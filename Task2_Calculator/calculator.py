print("==============================")
print("          CALCULATOR          ")
print("==============================")

while True:

    # Safe input handling
    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("\nInvalid input! Please enter numbers only.")
        continue

    print("\nSelect Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    print("\nYou can perform multiple operations at a time..!!")
    print("Example: 1,2 or 1,2,3,4")

    # Take operation input
    choices = input("\nEnter your choice (1/2/3/4): ")

    # Handle empty input
    if choices.strip() == "":
        print("\nNo operation selected!")
        continue

    # Split multiple inputs
    choices_list = [choice.strip() for choice in choices.split(",")]

    valid = False

    if '1' in choices_list:
        print("Addition Result =", num1 + num2)
        valid = True

    if '2' in choices_list:
        print("Subtraction Result =", num1 - num2)
        valid = True

    if '3' in choices_list:
        print("Multiplication Result =", num1 * num2)
        valid = True

    if '4' in choices_list:
        if num2 == 0:
            print("Division Result = Error! Division by zero not allowed.")
        else:
            print("Division Result =", num1 / num2)
        valid = True

    # Invalid selection message
    if not valid:
        print("\nInvalid operation number chosen..!!")
        print("Please select a valid operation number among 1, 2, 3, 4.")

    # Continue or exit
    again = input("\nDo you want to perform new calculation? (y/n): ").lower()

    if again != 'y':
        print("\nThank you for using the calculator! 😊")
        break
