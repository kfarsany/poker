class Card:
    def __init__(self, value: str, suit: str):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return self.value + self.suit

    def __str__(self):
        return self.value + self.suit
