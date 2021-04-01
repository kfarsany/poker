from card import Card
import random


class Deck:
    def __init__(self):
        self.deck = []
        self.shuffle()

    def __repr__(self):
        result = ""
        for card in self.deck:
            result += str(card) + ' '
        return result

    def __len__(self):
        return len(self.deck)

    def deal(self) -> Card:
        return self.deck.pop()

    def shuffle(self) -> None:
        self.deck = _create_deck()
        random.shuffle(self.deck)


def _create_deck() -> [Card]:
    suits = ['C', 'S', 'D', 'H']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    result = []
    for suit in suits:
        for value in values:
            result.append(Card(value, suit))
    return result
