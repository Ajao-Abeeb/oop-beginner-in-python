class Car:
    def __init__(self,brand,model,price,milage):
        self.brand = brand
        self.model = model
        self.price = price
        self.milage = milage


    def start_car(self):
        print(self.brand+" car having model as "+str(self.model)+" has started")


toyota=Car('Toyato', 2004, 1300,12)
toyota.start_car()