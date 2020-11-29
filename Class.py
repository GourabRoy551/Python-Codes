class Myclass:
    x = 5


p1 = Myclass()
print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("Jhon", 35)
p1.myfunc()

print(p1.name)
print(p1.age)

#del p1.age
#print(p1.age)
