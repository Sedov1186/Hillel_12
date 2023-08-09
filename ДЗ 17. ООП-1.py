class Auto:

    def __init__(self, brand, age, mark):

        self.brand = brand

        self.age = age

        self.mark = mark


    def move(self):

        print('Выводят сообщение на экран move')

    def stop(self):

        print('Выводят сообщение на экран stop')

    def birthday(self):

        self.age += 1

        print(f'Age {self.age}')

auto_1 = Auto(brand="Tesla", age=1, mark=3)

auto_1.move()

auto_1.stop()

auto_1.birthday()