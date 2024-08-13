# trees.py
import random


class Tree:
    """A tree with a trunk and leaves."""

    def __init__(self, trunk_height, number_of_leaves):
        """Initialise a Tree instance."""
        self.trunk_height = trunk_height
        self.number_of_leaves = number_of_leaves

    def __str__(self):
        """Return a string representation of the Tree."""
        leaves = '#' * self.number_of_leaves
        trunk = '|' * self.trunk_height
        return f"{leaves}\n{trunk}"

    def grow(self, sunlight, water):
        """
