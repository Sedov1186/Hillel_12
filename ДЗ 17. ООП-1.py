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

if __name__ == "__main__":
    my_auto = Auto(brand="Tesla", age=1, mark="3", color="Red", weight="1500 kg")

    print(f"Brand: {my_auto.brand}")
    print(f"Age: {my_auto.age}")
    print(f"Color: {my_auto.color}")
    print(f"Mark: {my_auto.mark}")


    my_auto.move()
    my_auto.birthday()
    print(f"New age after birthday: {my_auto.age}")
    my_auto.stop()