class Car:


    def __init__(self,doors,wheels,motor):
        self.doors = doors
        self.wheels = wheels
        self.motor = motor


def four_wheeled_car(func):
    def wrapper(car, *args):
        if car.wheels == 4:
            print(f"\nThis car has {car.wheels} wheels")
            print(f"\nThis car also has {car.doors} doors and {car.motor} motor")
        else:
            raise ValueError("\nThis car is not four wheeled")
        func(car,args)
        print(f"\nAdding {args[0]} more wheels to your car.....")
        print(f"\nThis car has now {car.wheels} wheels")
    return wrapper


@four_wheeled_car
def upgrade_wheel_number(car,wheels):
    if car.wheels == 4:
        car.wheels = car.wheels + wheels[0]
        
my_car = Car(4,4,1)
upgrade_wheel_number(my_car,3)