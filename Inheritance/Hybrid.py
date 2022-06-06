class Vehicle:
    def vehicle_info(self):
        print("Vehicle class")

class Car(Vehicle):
    def car_info(self):
        print("Car class")

class Truck(Vehicle):
    def truck_info(self):
        print("Truck class")

class SportsCar(Car, Vehicle):
    def sports_car_info(self):
        print("SportsCar class")