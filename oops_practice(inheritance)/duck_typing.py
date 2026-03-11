class Car:
    def start(self):
        print("Car start ho gayi 🚗")

class Bike:
    def start(self):
        print("Bike start ho gayi 🏍️")

class Truck:
    def start(self):
        print("Truck start ho gaya 🚛")

# Alag function — class ke bahar
def ignite(vehicle):
    vehicle.start()

# Objects banao aur call karo
ignite(Car())
ignite(Bike())
ignite(Truck())
