# band.py
from musician import Musician


class Band:
    """A band consisting of multiple musicians."""

    def __init__(self, name, musicians):
        """Initialise a Band instance."""
        self.name = name
        self.musicians = musicians

    def play(self):
        """Make each musician play or notify if they need an instrument."""
        for musician in self.musicians:
            musician.play()
