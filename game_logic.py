from deck import Deck
from player import Player


class GameState:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        self.turn = 0
        self.community_cards = []
        self.big_blind = 20
        self.big_blind_loc = 0
        self.pot = 0
        self.highest_bet = 0

    def __str__(self):
        result = ""
        count = 0
        for player in self.players:
            result += str(player)
            if count == self.turn:
                result += "\t ---> CURRENT MOVE"
            result += "\n"
            count += 1
        result += "\n\t"

        result += "POT:\t$" + str(self.pot) + "\n\n\t\t"

        for card in self.community_cards:
            result += str(card) + "\t"
        return result + "\n\n\n"

    def fix_first_turn(self) -> None:
        self.turn = self.big_blind_loc + 1
        if self.turn == len(self.players):
            self.turn = 0

    def change_turn(self) -> None:
        self.turn += 1
        if self.turn == len(self.players):
            self.turn = 0

    def get_current_player(self) -> Player:
        return self.players[self.turn]

    def add_to_pot(self, money: int) -> None:
        self.pot += money

    def raise_highest_bet(self, money: int) -> None:
        self.highest_bet = money

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
        self.pot = 0

    def bet_blinds(self) -> None:
        for player in self.players:
            self.add_to_pot(player.bet(player.blind))
        self.highest_bet = self.big_blind

    def clear_all_bets(self) -> None:
        for player in self.players:
            player.last_bet = 0
        self.highest_bet = 0

    def move_blinds(self) -> None:
        self.players[self.big_blind_loc-1].blind = 0
        self.players[self.big_blind_loc].blind = int(self.big_blind/2)

        self.big_blind_loc += 1
        if self.big_blind_loc == len(self.players):
            self.big_blind_loc = 0
        self.players[self.big_blind_loc].blind = self.big_blind
