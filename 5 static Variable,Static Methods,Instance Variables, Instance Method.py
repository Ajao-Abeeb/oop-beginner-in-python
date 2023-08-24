class Car:
    wheels=4
    #instance
    def __init__(self,brand,model,price,milage):
        self.brand = brand
        self.model = model
        self.price = price
        self.milage = milage


    def start_car(self):
        print(self.brand+" car having model as "+str(self.model)+" has started")
    

    # static method

    @staticmethod
    def demo_method():
        print('demo static method')


    @staticmethod
    def print_car_wheels():
        print(Car.wheels) 
        Car.demo_method()
        #instance
        car =Car("honda",'amaze',1200,3)
        car.start_car()
         

toyota=Car('Toyato', 2004, 1300,12)
camry = Car('Camry','Amaze',12000,13.2)

#Ans
print(toyota.brand)
toyota.start_car()
camry.start_car()

print(Car.wheels)
toyota.print_car_wheels()