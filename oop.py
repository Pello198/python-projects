class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Dog:
    def move(self):
        print("Running 🐕")

# Create instances
my_car = Car()
my_plane = Plane()
my_dog = Dog()

# Call move() on each
my_car.move()    # Driving 🚗
my_plane.move()  # Flying ✈️
my_dog.move()    # Running 🐕
