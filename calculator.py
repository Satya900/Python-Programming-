def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def calculator():
 

    Operation = input("Enter choice ( '+' / '-' / '*' / '/' ): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if Operation == '+':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif Operation == '-':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif Operation == '*':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif Operation == '/':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid input. Please enter a valid choice.")

if __name__ == "__main__":
    calculator()
