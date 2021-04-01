class BetError(Exception):
    pass


class Player:
    def __init__(self, name: str, money: int, blind=0):
        self.name = name
        self.money = money
        self.blind = blind
        self.hand = ()

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name + ": " + str(self.hand[0]) + ", " + str(self.hand[1]) + \
               "\n  $" + str(self.money)

    def change_blind(self, blind: int) -> None:
        self.blind = blind

    def bet(self, amount: int) -> int:
        if amount > self.money:
            raise BetError()
        self.money -= amount
        return amount
