def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def get_input(val):
    return [int(i) for i in val.split(",")]
    

def get_operator(val):
    if val in ("+", "-", "*", "/", "^"):
        return val
    raise ValueError


if __name__ == "__main__":
    while True:
        try:
            [num1, num2] = get_input(input("Enter 2 comma separated numbers: "))
            break
        except ValueError:
            print("Enter 2 comma separated numbers only.")
    while True:
        try:
            operator = get_operator(input("Enter operator (+,-,*,/): "))
            break
        except ValueError:
            print("Enter a valid operator.")
    if operator == "+":
        print("Result is ", add(num1, num2))
    elif operator == "-":
        print("Result is ", subtract(num1, num2))
    elif operator == "*":
        print("Result is ", multiply(num1, num2))
    elif operator == "/":
        print("Result is ", divide(num1, num2))
    