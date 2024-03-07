
class Laptops :
    def __init__(self,brand,price,display_size):
        self.brand = brand
        self.price = price
        self.display_size = display_size

    def power(self):
        print("{} is the best laptop with pricing of rs {} and has display size of {} inch".format(self.brand,self.price,self.display_size))

lap1 = Laptops("Lenevo","80,999","16")

lap1.power()
