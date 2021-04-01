from deck import Deck
from player import Player


class GameState:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.community_cards = []
        self.big_blind = 20
        self.big_blind_loc = 1

    def __str__(self):
        result = ""
        for player in self.players:
            result += str(player) + "\n"
        result += "\n\t"

        for card in self.community_cards:
            result += str(card) + "\t"
        return result + "\n\n\n"

    def add_player(self, name: str, money: int) -> None:
        self.players.append(Player(name, money))

    def deal_to_players(self) -> None:
        for player in self.players:
            player.hand = (self.deck.deal(), self.deck.deal())

    def deal_community(self) -> None:
        self.community_cards.append(self.deck.deal())

    def reshuffle(self) -> None:
        self.deck.shuffle()
        self.community_cards.clear()

    def move_blinds(self) -> None:
        self.players[self.big_blind_loc-1].change_blind(0)
        self.players[self.big_blind_loc].change_blind(self.big_blind/2)

        self.big_blind_loc += 1
        if self.big_blind_loc == len(self.players):
            self.big_blind_loc = 0
        self.players[self.big_blind_loc].change_blnd(self.big_blind)

    def init_blinds(self) -> None:
        self.players[0].change_blind(self.big_blind/2)
        self.players[1].change_blind(self.big_blind)
