# silver_service_taxi.py
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of Taxi with an additional flagfall cost and a fanciness multiplier."""

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness  # Override the price per km

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi."""
        return (f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}")

    def get_fare(self):
        """Calculate and return the fare for the current trip."""
        return round(super().get_fare(), 2)
