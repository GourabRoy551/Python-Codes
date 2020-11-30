#Function without a return statement
def hello1():
    print("Hello!")


#function with a return statement
def hello2():

    '''
    This is 
    a multiline 
    text.
    '''

    return "Hello!"

hello1()
print(hello2())
print(hello2.__doc__)