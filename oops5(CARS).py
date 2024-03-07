class Cars:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    
    def accelerate(self):
        print("{} is accelerating".format(car1.brand))

car1 = Cars("Audi","Red")
car1.accelerate()
