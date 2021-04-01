from game_logic import GameState

STARTING_MONEY = 1000


def _run() -> None:
    game_state = GameState()
    _create_players(game_state)
    game_state.init_blinds()
    while True:
        print("Here we go...")
        game_state.reshuffle()
        game_state.deal_to_players()
        print(game_state)
        game_state.deal_community()
        game_state.deal_community()
        game_state.deal_community()
        print(game_state)
        game_state.deal_community()
        print(game_state)
        game_state.deal_community()
        print(game_state)
        break


def _get_people() -> int:
    # while True:
    #     try:
    #         result = int(input("How many players? (2 - 10): "))
    #         if result < 2 or result > 10:
    #             raise ArithmeticError()
    #         return result
    #     except ArithmeticError:
    #         print("You are a fool who does not know how to follow directions")
    return 2


def _create_players(game_state: GameState) -> None:
    users = _get_people()
    for i in range(users):
        game_state.add_player("player" + str(i+1), STARTING_MONEY)


if __name__ == "__main__":
    _run()
