from diceroll import roll_the_dice
from typing import Tuple


def initialise_game() -> Tuple[list, list, list, list, list, list]:
    '''
    Initialise the default settings of the game
    Returns:
        return a Tuple containing players, positions, snakes and ladders
    '''
    players = ["Red", "Blue", "Green", "White"]
    positions = [0, 0, 0, 0]
    snake_heads = [25, 44, 65, 76, 99]
    snake_tails = [6, 23, 34, 28, 56]
    ladder_bases = [8, 26, 38, 47, 66]
    ladder_tops = [43, 39, 55, 81, 92]
    return players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops


def get_num_players() -> int:
    '''
    Get to know how many players who participate in the game.
    Returns:
        num_players(int)
    Exceptions:
        ValueError: An error occurred while input is not a numeric value,
    '''
    while True:
        try:
            # Input the number of players
            num_players = int(input("Please input the number of players: "))
            # judge whether the input is from 1 to 4
            if num_players >= 1 and num_players <= 4:
                return num_players
            else:
                print("The number of players must be between 1 and 4. Please try again.")
        except ValueError:      # When input an invalid input, rasise an exception
            print("Invalid input. Please enter a numeric value.")


def play_game(players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops) -> list:
    ''' The execution of the game
    Args:
        players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops(list): default settings of the game
    Returns:
        positions_real(list): return a list to store the final positions of four players
    '''
    # get the real number of players who participate in the game
    num_player = len(players)
    for i in range(num_player):
        players_real = players[: num_player]
        positions_real = positions[: num_player]
    while all(x < 100 for x in positions_real):
        player_order = 0  # define a flag to represent the order of players
        while player_order < num_player:
            diceroll = roll_the_dice()
            positions_real[player_order] += diceroll    # player steps to next position

            # Check if player is on a snake head
            if positions_real[player_order] in snake_heads:
                index = snake_heads.index(positions_real[player_order])
                positions_real[player_order] = snake_tails[index]
                print(f"Player {players_real[player_order]} stepped on a snake and is now in position {positions_real[player_order]}")

            # Check if player is on a ladder Base
            if positions_real[player_order] in ladder_bases:
                index = ladder_bases.index(positions_real[player_order])
                positions_real[player_order] = ladder_tops[index]
                print(f"Player {players_real[player_order]} climbed a ladder and is now in position {positions_real[player_order]}")

            if positions_real[player_order] == 100:
                # print(f"Player {players_real[player_order]} has reached 100 and is the winner!")
                break

            if positions_real[player_order] > 100:      # dismiss the position over 100
                positions_real[player_order] -= diceroll
            print(f"Player {players_real[player_order]} is in position {positions_real[player_order]}")
            player_order += 1
    return positions_real


def pick_winner(positions):
    ''' To pick the winner of the game.
    Args:
        positions(list): a list of final positions of player
    Returns:
        winner(str): return the player who reach 100 first
    '''
    if 100 in positions:
        winner = positions.index(100)
    return winner


def main():
    players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops = initialise_game()
    final_positions = play_game(players, positions, snake_heads, snake_tails, ladder_bases, ladder_tops)
    winner = pick_winner(final_positions)
    print(f"The winner is {players[winner]}!")


if __name__ == '__main__':
    main()