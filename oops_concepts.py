class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
       

    def show_info(self):
       print(f"Brand: {self.brand}, Speed: {self.speed}")

class Truck(Vehicle):
    def carry_load(self,weight):
        self.weight=weight
        print(f"the weight carried by truck is{self.weight}")
    

    def turbo_speed(self):
        self.speed += 200
        print(f"Turbo speed is {self.speed}")

d=Vehicle("maruti",90)
d.show_info()
t=Truck("omni",70)
t.carry_load("70kg")
t.speed=200
t.turbo_speed()
