def add(num1, num2):
    return num1 + num2

if __name__ == "__main__":
    num1, num2 = [i for i in input("Enter 2 comma separated numbers: ").split(",")]
    print("Result is: ", add(num1, num2))