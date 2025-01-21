class Car:
    def __init__(self, license_plate, brand):
        self.license_plate = license_plate
        self.brand = brand

    def __str__(self):
        return f"Car [License Plate: {self.license_plate}, Brand: {self.brand}]"

    def __repr__(self):
        return f"Car({self.license_plate!r}, {self.brand!r})"

# Example usage
car1 = Car("ABC", "Toyota")
car2 = Car("123", "Tesla")

