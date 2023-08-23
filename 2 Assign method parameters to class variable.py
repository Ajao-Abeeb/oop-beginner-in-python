class Car:
    wheels = 4

    def start_car(self):
        print('Car started')

    def sample(self,brand,model,price,milage):
        self.brand = brand
        self.model = model
        self.price = price
        self.milage =  milage
        # re-assign 
        print(brand,model,price,milage)

    def sample_2(self):
        print(self.brand,self.model )


    def sample_3(self):
        # assgining parameter 
        self.brand = 'camry'
        self.model = 'Amaze'
        self.price = 15000
        self.milage = 12434
        print(self.brand,self.model) 


      # it automatic pick the last brand 
    def sample_4(self):
        print(self.wheels)
        print(self.brand, self.model)
        self.start_car()

car = Car()
# parameters
car.sample('toyota', '2004', 5000, 14)

car.sample_2()
car.sample_3()
car.sample_4()