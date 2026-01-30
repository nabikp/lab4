class Car:
    wheels = 4  # class variable, same for all cars

    def __init__(self, color):
        self.color = color  # instance variable, unique per car

car1 = Car("red")
car2 = Car("blue")

print(car1.wheels)  # 4
print(car2.wheels)  # 4
