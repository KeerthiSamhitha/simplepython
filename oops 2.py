class animals():
    def __init__(self, x, y, z):
        self.species = x
        self.legs = y
        self.wings = z
    def updateheight(self, val):
        self.height =  val
    def getheight(self):
        return self.height
    def speak(self):
     print("The animal is a {}".format(self.species))
     print("The animal has {} legs".format(self.legs))
     print("The animal has {} wings".format(self.wings))


x = animals("Parrot", 2, 2)
x.speak()
x.updateheight('5 km')
h = x.getheight()print(h)


# Python code to demonstrate how parent constructors
# are called.

# parent class
class Person(object):

    # __init__ is known as the constructor
    def __init__(self, x, y):
        self.name = x
        self.idnumber = y

    def display(self):
        print(self.name)
        print(self.idnumber)



# child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post


        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display
