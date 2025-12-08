class Vehical:
    def startEngine(self):
        print("engine is started ")


class Car(Vehical):
    def drive(self):
        print("Car is driving ")

class Bike(Vehical):
    def ride(self):
        print("bike ia rifding ")

c1=Car()
c1.startEngine()
c1.drive()

b1=Bike()
b1.ride()