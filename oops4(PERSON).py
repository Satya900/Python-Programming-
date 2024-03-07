class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def dance(self):
        print(self.name + " can also dance!!!")


per1 = Person("Satya", 18)

per1.dance()
