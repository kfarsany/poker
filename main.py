from game_logic import GameState

STARTING_MONEY = 1000


def _run() -> None:
    game_state = GameState()
    _create_players(game_state)
    while True:
        print("Initializing hand...")
        _start_new_hand(game_state)
        print(game_state)
        _do_round(game_state)
        game_state.deal_community()
        game_state.deal_community()
        game_state.deal_community()
        print(game_state)
        _do_round(game_state)
        game_state.deal_community()
        _do_round(game_state)
        game_state.deal_community()
        break


def _start_new_hand(game_state: GameState) -> None:
    game_state.reshuffle()
    game_state.deal_to_players()
    game_state.clear_all_bets()
    game_state.move_blinds()
    game_state.bet_blinds()
    game_state.fix_first_turn()


def _do_round(game_state: GameState) -> None:
    player = game_state.get_current_player()
    while True:
        betting_result = _get_user_input(game_state)
        game_state.add_to_pot(betting_result)
        game_state.change_turn()
        print(game_state)
        if player.last_bet == game_state.highest_bet and betting_result == 0:
            game_state.clear_all_bets()
            return


def _get_user_input(game_state: GameState) -> int:
    player = game_state.get_current_player()
    if player.last_bet < game_state.highest_bet:
        return _forced_input(game_state)
    else:
        return _free_input(game_state)


def _forced_input(game_state: GameState) -> int:
    player = game_state.get_current_player()
    price_to_call = game_state.highest_bet - player.last_bet
    can_afford_raise = price_to_call < player.money
    input_prompt = "(c)all: ${}{}\n(f)old\n"
    if not can_afford_raise:
        input_prompt = input_prompt.format(player.money, "\t---> ALL IN")
    else:
        input_prompt = input_prompt.format(price_to_call, "")
        input_prompt += "(r)aise\n"
    input_prompt += player.name + "'s turn: "

    while True:
        user_input = input(input_prompt).lower()
        if user_input == 'c':
            if not can_afford_raise:
                return player.bet(player.money)
            else:
                return player.bet(price_to_call)
        elif user_input == 'f':
            player.fold()
            return 0
        elif user_input == 'r':
            if not can_afford_raise:
                print("YOU HAVE NOT ENOUGH DUCATS, GOOD LAD")
                continue
            return _raise_input(game_state)
        else:
            print("\nYOU FOOL! TRY AGAIN!")
            continue


def _free_input(game_state: GameState) -> int:
    player = game_state.get_current_player()
    while True:
        user_input = input("(c)heck\n(r)aise\n" + player.name + "'s turn: ")
        if user_input == 'c':
            return 0
        elif user_input == 'r':
            return _raise_input(game_state)
        else:
            print("\nYOU FOOL! TRY AGAIN!")
            continue


def _raise_input(game_state: GameState) -> int:
    player = game_state.get_current_player()
    while True:
        try:
            user_input = int(input("Enter amount to raise to: "))
            if user_input > player.money:
                raise ArithmeticError
            game_state.raise_highest_bet(user_input)
            return player.bet(user_input - player.last_bet)
        except ValueError:
            print("YOU FOOL! TRY AGAIN!")
            continue
        except ArithmeticError:
            print("YOU HAVE NOT ENOUGH DUCATS, GOOD LAD")
            continue


def _get_people() -> int:
    # while True:
    #     try:
    #         result = int(input("How many players? (2 - 10): "))
    #         if result < 2 or result > 10:
    #             raise ArithmeticError()
    #         return result
    #     except ArithmeticError:
    #         print("You are a fool who does not know how to follow directions")
    return 4


def _create_players(game_state: GameState) -> None:
    users = _get_people()
    for i in range(users):
        game_state.add_player("player" + str(i+1), STARTING_MONEY)


if __name__ == "__main__":
    _run()
