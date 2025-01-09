from diceroll import roll_the_dice
from typing import Tuple

def initialise_game() -> Tuple[list, list, list, list, list, list]:
    # DELETE the line below when you implement the function
    raise NotImplementedError

def get_num_players() -> int:
    # DELETE the line below when you implement the function
    raise NotImplementedError

def play_game(players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops) -> list:
    # DELETE the line below when you implement the function
    raise NotImplementedError

def pick_winner(positions):
    # DELETE the line below when you implement the function
    raise NotImplementedError


def main():
    players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops = initialise_game()
    final_positions = play_game(players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops)
    winner = pick_winner(final_positions)
    print(f"The winner is {players[winner]}!")

if __name__ == '__main__':
    main()