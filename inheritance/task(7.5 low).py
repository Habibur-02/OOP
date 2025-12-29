class Vehicle:
    def __init__(self, make, model, year, energy_level):
        self._make = make
        self._model = model
        self._year = year
        self._energy_level = energy_level

    def start_engine(self):
        print("Engine starting...")

    def refill(self, amount):
        self._energy_level += amount
        print(f"Energy level now at {self._energy_level}")

class ElectricCar(Vehicle):
    def __init__(self, make, model, year, battery_capacity):
        # Electric cars use battery, not fuel
        super().__init__(make, model, year, energy_level=100)
        self._battery_capacity = battery_capacity

    def start_engine(self):
        print("Starting silent electric motor...")

    def charge(self): # Added self
        print("Charging battery...")

class Truck(Vehicle):
    def __init__(self, make, model, year, max_cargo_weight, fuel_level):
        super().__init__(make, model, year, fuel_level)
        self._max_cargo_weight = max_cargo_weight

    def start_engine(self):
        print("Starting heavy-duty diesel engine...")

# Use descriptive names, avoid 'list'
fleet = [
    Truck("Volvo", "FH16", 2022, 20000, 100),
    ElectricCar("Tesla", "Model S", 2023, 100)
]

for vehicle in fleet:
    vehicle.start_engine()
