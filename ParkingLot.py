from Car import Car

class ParkingLot:
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.occupied_spots = set()  # Tracks occupied spot numbers
        self.spot_map = {}  # Maps spot numbers to Car objects

    def park_vehicle(self, spot, car):
        # Validate spot range
        if spot < 1 or spot > self.total_spots:
            return "Invalid spot. Please choose a spot between 1 and total spots."
        # Check if spot is already occupied
        if spot in self.occupied_spots:
            return f"Spot {spot} is already occupied."
        # Park the car
        self.occupied_spots.add(spot)
        self.spot_map[spot] = car
        return f"{car} parked in spot {spot}."

    def remove_vehicle(self, spot):
        # Check if spot is currently occupied
        if spot not in self.occupied_spots:
            return f"Spot {spot} is not currently occupied."
        # Remove the car
        car = self.spot_map.pop(spot)
        self.occupied_spots.remove(spot)
        return f"{car} removed from spot {spot}. Spot is now free."

    def get_available_spots(self):
        # Return all unoccupied spots
        return [spot for spot in range(1, self.total_spots + 1) if spot not in self.occupied_spots]

# Create cars
car1 = Car("ABC123", "Toyota")
car2 = Car("XYZ456", "Tesla")

# Create parking lot with 5 spots
parking_lot = ParkingLot(5)

# Park vehicles
print(parking_lot.park_vehicle(3, car1))  # Car [License Plate: ABC123, Brand: Toyota] parked in spot 3.
print(parking_lot.park_vehicle(4, car2))  # Car [License Plate: XYZ456, Brand: Tesla] parked in spot 4.
print(parking_lot.park_vehicle(3, car2))  # Spot 3 is already occupied.

# Remove vehicles
print(parking_lot.remove_vehicle(3))  # Car [License Plate: ABC123, Brand: Toyota] removed from spot 3. Spot is now free.
print(parking_lot.remove_vehicle(3))  # Spot 3 is not currently occupied.

# Check available spots
print(parking_lot.get_available_spots())  # [1, 2, 3, 5]

# Try parking in an invalid spot
print(parking_lot.park_vehicle(6, car1))  # Invalid spot. Please choose a spot between 1 and total spots.
