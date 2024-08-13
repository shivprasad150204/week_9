# musician.py
from guitar import Guitar


class Musician:
    """A musician who has a list of instruments."""

    def __init__(self, name):
        """Initialise a Musician instance."""
        self.name = name
        self.instruments = []

    def add_instrument(self, instrument):
        """Add an instrument to the musician's collection."""
        self.instruments.append(instrument)

    def play(self):
        """Make the musician play an instrument if they have one."""
        if self.instruments:
            instrument = self.instruments[0]  # Assume the musician plays the first instrument
            print(f"{self.name} is playing: {instrument}")
        else:
            print(f"{self.name} needs an instrument!")
