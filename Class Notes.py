# # Defining a class
# class CheeseBurger(object):
#     def __init__(self, patty, cheese): # Two underscores before and after
#         self.patty = patty
#         self.cheese = cheese
#         self.eaten = False
#
#     def give(self, name):
#         print(name + "is thankful")
#
#     def cut(self):
#         print("You cut the cheeseburger")
#
#     def eat(self):
#         print("You eat the cheeseburger")
#         self.eaten = True
#
#
# burger1 = CheeseBurger("Beef", "American")
# burger2 = CheeseBurger("bacon", "swiss")
#
# print(burger1.eaten)
# print(burger2.cheese)
#
# burger1.eat()
# print(burger1.eaten)
# print(burger2.eaten)
#
# class car(object):
#     def __init__(self, color, num_of_doors, hp):
#         self.color = color
#         self.doors = num_of_doors
#         self.running = False
#         self.HP = hp
#         self.passengers = 0
#         self.name = name
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# class Room(object):
#     def __init__(self, name, north):
#         self.name = name
#         self.north = north
#
#
# hdum = Room(1)
# hdum = Room(2)







class Vehicle(object):
    def _int_(self, source, material, seat, speed, passengers):
        self.power_source = source
        self.material = material
        self.seat_location = seat
        self.max_speed = speed
        self.passengers = passengers
        def move(self):
            print("you move forwards")

        def change_direction(self):
            print("you change directions")


class Car(Vehicle):
    def __init__(self, material, seat, speed, passengers, windows):
        super(Car, self)._int_ ('engine', material, seat, speed)
        self.windows = windows

    def roll_down_windows(self):
        print("you roll down the windows down")

    def turn_on(self):
        print("you turn the key and the engine starts")


test_car = Car('Aluminum', 'Driver', 140, 2, True)
test_car.change_direction()


class KeylessCar(Car):
    def __init__(self, material, seat, speed, passengers, windows):
        super(KeylessCar, self)._int_ ('engine', material, seat, speed)

        def turn_on(self):
            print("You push the button and the car turns on")

test_car.turn_on()
cool_car = keyCarLess('Aluminum', 'Driver side', 140, 2, True)
cool_car.turn_on()


class Tesla(KeylessCar):
    def _int_(self, material, seat, speed, passengers, windows):
        super(Tesla, self)._int_(material, seat, speed, passengers, windows)

        def fly(self):
            print("You launch the car into low earth orbit")

        def turn_on(self):
            Car.turn_on(self)