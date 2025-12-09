from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero is not allowed."
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("Enter the first number: "))

    while True:
        print("\nAvailable operations:")
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")

        if operation_symbol not in operations:
            print("Invalid operation. Please try again.")
            continue

        num2 = float(input("Enter the next number: "))

        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)

        print(f"Result: {result}")

        proceed = input("Do you want to continue calculating with the result? Type 'y' or 'n': ").lower()

        if proceed == "y":
            num1 = result
        else:
            print("\nStarting a new calculation...\n")
            return calculator()


calculator()
