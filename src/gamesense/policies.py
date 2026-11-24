"""Beginner random policy. It deliberately does not learn."""
import random

class RandomPolicy:
    def __init__(self, seed=42):
        self.random = random.Random(seed)

    def act(self, observation):
        """Return 0 (do nothing) or 1 (flap)."""
        return self.random.randrange(2)
