# Generator with a loop
def reverse_string(my_string):
    length = len(my_string)
    for i in range(length - 1, -1, -1):
        yield my_string[i]


# for loop to reverse the string

for char in reverse_string("WORLD"):
    print(char)


# A simple generator function

def my_gen():
    n = 1
    print("This is printed first")
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


a = my_gen()

next(a)
next(a)
next(a)

# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
list_ = [x ** 2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x ** 2 for x in my_list)

print(list_)
print(generator)


# Example
def PowTwoGen(max=0):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1
