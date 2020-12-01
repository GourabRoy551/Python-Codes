#Catching Specific exception

try:
    a = int(input("Please enter the first number = "))
    b = int(input("Please enter the second number = "))

    if (a < 0):
        raise TypeError
    c = a / b
    print("{} / {} = {}".format(a,b,c))

except ZeroDivisionError:
    print("Division by Zero is not possible")
except ValueError:
    print("The data types are not proper")
except TypeError:
    print("The data is not in range")
except NameError:
    print("The data items are not defined")