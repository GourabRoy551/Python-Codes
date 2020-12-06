# Demonstration
def make_decorated(func):
    def inner_function():
        print("I got decorated")
        func()

    return inner_function()


@make_decorated
def simple_func():
    print("I am a simple function")

# decor = make_decorated(simple_function)
# decor()

# simple_func()
#-----------------------------------------------------
# Another example:
def my_smart_div(func):
    def inner_func(x,y):
        print("I am dividing ", x, "and", y)
        if y == 0:
            print("Oops! Division by zero is illegal...")
            return

        return func(x, y)
    return inner_func


@my_smart_div
def go_divide(a, b):
    return a/b

print(go_divide(20, 2))
print(go_divide(20, 0))

#---------------------------------------------------------
# Example:
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")

"""
@star
@percent
def printer(msg):
    print(msg)
    
-->Here,is equivalent to

def printer(msg):
    print(msg)
printer = star(percent(printer))
"""
