class vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self): 
        print(f"brand name = {self.brand}")

class car(vehicle):
        def drive(self):
             print("THE CAR IS DRIVING")

Car = car("TOYOTA")
Car.show_brand()
Car.drive()


