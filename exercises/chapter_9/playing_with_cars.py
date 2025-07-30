from random import randint

from car import Car
from electric_car import ElectricCar


my_old_car = Car('audi', 'a4', 2022)
print(my_old_car.get_descriptive_name())
my_old_car.read_odometer()

my_new_car = ElectricCar('nissan', 'leaf', 2023)
print(my_new_car.get_descriptive_name())

my_old_car.odometer_reading = randint(1, 6)
my_old_car.read_odometer()
