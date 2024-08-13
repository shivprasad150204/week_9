# unreliable_car.py
import random
from car import Car


class UnreliableCar(Car):
    """A car that sometimes fails to drive based on reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a certain distance if the car is reliable enough."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
