# Parent class
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def display_info(self):
        print(f"Vehicle Name: {self.name}")
        print(f"Max Speed: {self.max_speed} km/h")
        print(f"Mileage: {self.mileage} km/l")


# Child class
class Bus(Vehicle):
    pass   # Inherits everything from Vehicle


# ---------------------------
# Example usage
# ---------------------------
bus1 = Bus("School Bus", 80, 12)
bus1.display_info()
