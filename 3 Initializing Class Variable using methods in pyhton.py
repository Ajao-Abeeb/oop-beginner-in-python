class Car:
    def initialization_method(self,brand, model, price,milage):
        self.brand= brand
        self.model = model
        self.price =price
        self.millage = milage


    def start_car(self):
        print(self.brand+" car having model as "+str(self.model),"has started")

    def stop_car(self):
        print(self.brand+" car having model as "+str(self.model)," has stopped")
    
    def print_car_details(self):
        print("Brand of the car is: " +self.brand)
        print("Model of the car is: " +str(self.model))
        print("Price of the car is: " +str(self.price))
        print("Millage of the car is: " +str(self.millage))
        print("---------------------------------------------")
         

toyota = Car()
toyota.initialization_method('Toyota', 2005, 15000, 30)

camry = Car()
camry.initialization_method('Camry', 2018, 15000000, 3)

toyota.start_car()
toyota.stop_car()
toyota.print_car_details()

camry.start_car()
camry.stop_car()
camry.print_car_details()