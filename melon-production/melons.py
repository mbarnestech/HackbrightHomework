"""Melon and Squash classes."""

import robots

class Cucurbit:
    """Cucurbit superclass. """
    color = None
    stickers = []
    weight = 0.0

    def __init__(self, cucurbit_type):
        """Initialize cucurbit.

        cucurbit_type: type of cucurbit being built.
        """
        self.melon_type = cucurbit_type

    def prep(self):
        """Prepare the cucurbit."""

        robots.cleanerbot.clean(self)
        robots.stickerbot.apply_logo(self)

    def __str__(self):
        """Print out information about cucurbit."""

        if self.weight <= 0:
            return self.melon_type
        else:
            return f"{self.color} {self.weight:.2f} lbs {self.melon_type}"
        
class Melon(Cucurbit):
    """Melon Subclass."""


class Squash(Cucurbit):
    """Winter squash Subclass."""

    def prep(self):
        """Prepare the cucurbit."""

        super().prep()
        robots.painterbot.paint(self)