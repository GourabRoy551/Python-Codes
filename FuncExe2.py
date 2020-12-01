def myAddition(x, y):
    print("Performing the addition operation...")
    return x + y


def mySubtraction(x, y):
    print("Performing the Subtraction operation...")
    return x - y


def myMultiplication(x, y):
    print("Performing the Multiplication operation...")
    return x * y


def myDivision(x, y):
    print("Performing the Division operation...")
    return x / y


def myMenu():
    print("Main Menu..")
    print("1 > Addition operation....")
    print("2 > Subtraction operation....")
    print("3 > Multiplication operation....")
    print("4 >Division operation....")
    ch = int(input("Please enter your option number = "))
    return ch


def calculation():
    global result
    ch = myMenu()
    num1 = int(input("Please enter the first number = "))
    num2 = int(input("Please enter the second number = "))
    if ch == 1:
        result = myAddition(num1, num2)
    elif ch == 2:
        result = mySubtraction(num1, num2)
    elif ch == 3:
        result = myMultiplication(num1, num2)
    elif ch == 4:
        result = myDivision(num1, num2)

    print("So result = ", result)


calculation()
