class Player:
    def __init__(self, name: str, money: int, blind=0):
        self.name = name
        self.money = money
        self.blind = blind
        self.last_bet = 0
        self.hand = ()

    def __repr__(self):
        return self.name

    def __str__(self):
        if self.has_folded():
            return self.name + ": FOLDED" + \
               "\n  $" + str(self.money) + "\t--> bet: $" + str(self.last_bet)
        else:
            return self.name + ": " + str(self.hand[0]) + ", " + str(self.hand[1]) + \
               "\n  $" + str(self.money) + "\t--> bet: $" + str(self.last_bet)

    def bet(self, amount: int) -> int:
        self.money -= amount
        self.last_bet += amount
        return amount

    def fold(self) -> None:
        self.hand = None

    def has_folded(self) -> bool:
        return self.hand is None
