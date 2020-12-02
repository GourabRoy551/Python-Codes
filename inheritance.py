'''
Inheritance is a way of creating a new class for using details for using details
of an existing class without modifing it.
'''
# Example 1
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)


p1 = Person("Jhon","Doe")

print(p1.fname, p1.lname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname,lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.fname, self.lname, "to the class of", self.graduationyear )

p2 = Student("Mike", "Olsen" ,2022)
p2.welcome()


# Example 2

# parent class
class Bird:
    def __int__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")
# child class
class Penguin(Bird):
    def __int__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")
    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()

b1 = Bird()
b1.whoisThis()

'''Use of the super() function inside the __init__() method
 allows us to run the __init__() method of the parent class 
 inside the child class.'''