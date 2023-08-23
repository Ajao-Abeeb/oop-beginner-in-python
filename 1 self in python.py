class Car:
    wheels = 4
    def start_car(self):
        print("Car started")

    def example_one(self):
            print(self.wheels)
            self.start_car()

# using object reference we can access the property of the Class, outside the class
car = Car()
print(Car.wheels)
car.start_car()
car.example_one()
 
 


