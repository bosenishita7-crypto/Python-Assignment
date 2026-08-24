class Transport:
    def __init__(self, transport_type):
        self.type = transport_type

    def show(self):
        print("Transport Type:", self.type)

class Boat(Transport):
    def __init__(self, capacity, source, destination):
        super().__init__("Water")
        self.capacity = capacity
        self.source = source
        self.destination = destination

    def show(self):
        print(f"Boat ({self.type}) | Capacity: {self.capacity} | {self.source} to {self.destination}")

class Bus(Transport):
    def __init__(self, seat_no, source, destination):
        super().__init__("Road")
        self.seat_no = seat_no
        self.source = source
        self.destination = destination

    def show(self):
        print(f"Bus ({self.type}) | Seat No: {self.seat_no} | {self.source} to {self.destination}")

# 2 objects each
b1 = Boat(30, "Mumbai", "Goa")
b2 = Boat(15, "Kochi", "Lakshadweep")
bus1 = Bus(45, "Delhi", "Agra")
bus2 = Bus(50, "Bangalore", "Chennai")

b1.show()
b2.show()
bus1.show()
bus2.show()