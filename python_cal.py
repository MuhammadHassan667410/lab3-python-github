number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

def add_numbers(num1, num2):
    return num1 + num2
def subtract_numbers(num1, num2):
    return num1 - num2
def multiply_numbers(num1, num2):
    return num1 * num2
def divide_numbers(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
def calculate_percentage(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return (num1 / num2) * 100

while True:
    print("\nWelcome to the Python Calculator!")
    print("\nSelect an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Check Even/Odd")
    print("6. Calculate Percentage")
    print("7. Exit")

    choice = int(input("Enter your choice (1-7): "))

    if choice == 1:
        result = add_numbers(number_1, number_2)
        print(f"The sum is: {result}")
    elif choice == 2:
        result = subtract_numbers(number_1, number_2)
        print(f"The difference is: {result}")
    elif choice == 3:
        result = multiply_numbers(number_1, number_2)
        print(f"The product is: {result}")
    elif choice == 4:
        result = divide_numbers(number_1, number_2)
        print(f"The quotient is: {result}")
    elif choice == 5:
        result1 = check_even_odd(number_1)
        result2 = check_even_odd(number_2)
        print(f"{number_1} is {result1} and {number_2} is {result2}.")
    elif choice == 6:
        result = calculate_percentage(number_1, number_2)
        print(f"{number_1} is {result}% of {number_2}.")
    elif choice == 7:
        print("Exiting the calculator.")
        print("Thank you for using the Python Calculator!")
        break
    else:
        print("Invalid input. Please try again.")