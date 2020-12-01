# Creating Class and Object in Python
class myBird:
    def __int__(self):
        print("myBird class constructor is executing...")

    def whatType(self):
        print("I am a Bird..")

    def canSwim(self):
        print("I can swim..")


class myParrot:
    # class attribute
    species = "bird"

    # instance attribute
    def __int__(self, name, age):
        print("myParrot class constructor is executing...")
        self.name = name
        self.age = age

    def canSing(self, thisSong):
        return "{} can sing {}....".format(self.name, thisSong)

# myPenguin class inheriting the attributes from the myBird class
class myPenguin(myBird):

    def __int__(self):
        # call super() function
        super().__int__()
        print("Penguin is ready")
    def whoisThis(self):
        print("I am Penguin")

    def canRun(self):
        print("I can run faster")

# instantiate the Parrot class
mp1 = myParrot("MyParrot1", 10)
mp2 = myParrot("MyParrot2", 15)

# access the class attributes
print("MP1 {} is a {}".format(mp1.__class__.species))
print("Mp2 {} is also a {}".format(mp2.__class__.species))

# access the instance attributes
print("{} is {} years of age".format(mp1.name, mp1.age))
print("{} is {} years of age".format(mp2.name, mp2.age))
print(mp1.canSing("Chrip"))

# Accessing the child class's attributes(Inheritance)
pg1 = myPenguin()
pg1.whoisThis()
pg1.canSwim()
pg1.canRun()

# Data Encapsulation
class personalComptuer:

    def __int__(self):
        self.maxComputerPrice = 20000

    def mySell(self):
        print("Selling Price: {}".format(self.maxComputerPrice))

    def setMaxComputerPrice(self, price):
        self.maxComputerPrice = price

pc = personalComptuer()
pc.mySell()

# Change the price
pc.maxComputerPrice = 30000
pc.mySell()

#Using setter function
pc.setMaxComputerPrice(40000)
pc.mySell()


