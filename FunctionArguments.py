# Function taking arguments and returing a value
def findMax(a, b):
    if a > b:
        return a
    else:
        return b


print("Max number between 10 and 20 is ", findMax(10, 20))


# Function With default parameter

def hello(name, msg=", how are ypu?"):
    print("Hello", name, msg)


hello("Agnibha", ", have a nice day.")
hello("Agnibha")


# Function with arbitrary arguments
def sumAll(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print("Sum of all the intergers between 1-5 is ", sumAll(1, 2, 3, 4, 5))
