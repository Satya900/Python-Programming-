class Person :
    country = "India"
    def __init__(self, name, age):
        self.name = name
        self.age = age

per1 = Person("Satyabrata", 18)
per2 = Person("Mohanty",21)

print("The Name of the perosn is {}, his age is {} and belongs to {}".format(per1.name,per1.age,per1.country))

