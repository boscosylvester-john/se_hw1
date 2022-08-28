def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


if __name__ == "__main__":
    num1, num2 = [int(i) for i in input("Enter 2 comma separated numbers: ").split(",")]
    print("Result is: ", add(num1, num2))