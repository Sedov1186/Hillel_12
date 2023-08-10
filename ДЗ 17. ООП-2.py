import time

class Auto:
    def __init__(self, brand, age, mark, color='', weight=''):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print("move")

    def birthday(self):
        self.age += 1

    def stop(self):
        print("stop")

class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color='', weight=''):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        super().move()
        print("attention")

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)

class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color='', weight=''):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'max speed is {self.max_speed}')

# Пример использования классов Truck и Car
if __name__ == '__main__':
    truck1 = Truck(brand='Renault', age=3, mark='Duster', max_load=20000, color='white', weight='8000 kg')
    truck2 = Truck(brand='Mazda', age=2, mark='R500', max_load=18000, color='blue', weight='7500 kg')

    car1 = Car(brand='Tesla', age=1, mark='3', max_speed=225, color='Red', weight='1200 kg')
    car2 = Car(brand='Honda', age=2, mark='Civic', max_speed=200, color='red', weight='1300 kg')

    truck1.move()
    truck1.birthday()
    truck1.load()
    print(f'Truck1 Age: {truck1.age}')
    print(f'Truck1 Max Load: {truck1.max_load}')
    truck1.stop()

    truck2.move()
    truck2.birthday()
    truck2.load()
    print(f'Truck2 Age: {truck2.age}')
    print(f'Truck2 Max Load: {truck2.max_load}')
    truck2.stop()

    car1.move()
    car1.birthday()
    print(f'Car1 Age: {car1.age}')
    print(f'Car1 Max Speed: {car1.max_speed}')
    car1.stop()

    car2.move()
    car2.birthday()
    print(f'Car2 Age: {car2.age}')
    print(f'Car2 Max Speed: {car2.max_speed}')
    car2.stop()