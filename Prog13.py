class car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.odometer = 0
 
    def drive(self, distance):
        self.odometer += distance
        print(f"You drove {distance} miles")
 
 
 
my_car = car("Ford", "blue")
print("Name of your car is: ",my_car.name)
print("Color of your car is: ",my_car.color)
# print(my_car.)
 
my_car.drive(100)
print()
# print(my_car.odometer)