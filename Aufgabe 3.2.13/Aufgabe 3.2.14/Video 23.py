class Car:
    def __init__(self):
        self.car_brand = None
        self.horse_power = None
        self.color = None

car1 = Car()
car1.car_brand = "Audi"
car1.horse_power = 250
car1.color = "Nardo Gray"

print(car1.car_brand)
print(car1.horse_power)
print(car1.color)

car2 = Car()
car2.car_brand ="BMW"
car2.horse_power =333
car2.color = "Vulcan Black"

car3 = car1

print(car1)
print(car2)
print(car3)
print(car1.horse_power)
print(car3.horse_power)
