from diceroll import roll_the_dice, special_roll
from helpers import generate_surprises


def initialise_game() -> dict:
    ''' Initialise the default settings of the game
    Returns:
        game(dict): return a dictionary 'game' containing players, snakes,ladders
    '''
    players = {'Red': 0, 'Blue': 0, 'Green': 0, 'White': 0}
    snakes = {'25': 6, '44': 23, '65': 34, '76': 28, '99': 56}
    ladders = {'8': 43, '26': 39, '38': 55, '47': 81, '66': 92}
    game = {'players': players, 'snakes': snakes, 'ladders': ladders}

    return game

def get_num_players() -> int:
    ''' Input a number of players
    Get to know how many players who participate in the game.
    Returns:
        num_players(int): return the correct number of players (1-4).
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

def play_game(game: dict) -> str:
    ''' The execution of the game
    Args:
        game(dict): Initial settings of the game.
    Returns:
        winner(int): The position of final winner.
    '''
    surprise_location = generate_surprises()    # call the generate_surprises function
    game['surprise_location'] = surprise_location   # add key 'surprise_location' and value into game dictionary
    print(game['surprise_location'])
    n = 4

    while all(x < 100 for x in list(game['players'].values())):
        play_order = 0      # Initial a flag of the order of players

        while play_order < len(game['players']):    # corresponding orders and players
            if play_order == 0:
                play_name = 'Red'
            elif play_order == 1:
                play_name = 'Blue'
            elif play_order == 2:
                play_name = 'Green'
            elif play_order == 3:
                play_name = 'White'
            else:
                pass

            diceroll = roll_the_dice()  # roll the dice
            players_value = game['players'][play_name]
            players_value += diceroll   # player steps to the next position

            if players_value > 100:         # dismiss the position which is better than 100
                players_value -= diceroll
            game['players'][play_name] = players_value

            if game['players'][play_name] == 100:   # jump outside the loop
                winner = play_name
                break

            # Check if player is on a snake head
            reach_snakes_or_ladders(game['players'], play_name, game['snakes'])

            # Check if player is on a ladder base
            reach_snakes_or_ladders(game['players'], play_name, game['ladders'])

            # if str(game['players'][play_name]) in list(game['snakes'].keys()):
            #     index = list(game['snakes'].keys()).index(str(game['players'][play_name]))
            #     game['players'][play_name] = list(game['snakes'].values())[index]
            #
            # if str(game['players'][play_name]) in list(game['ladders'].keys()):
            #     index = list(game['ladders'].keys()).index(str(game['players'][play_name]))
            #     game['players'][play_name] = list(game['ladders'].values())[index]


            # Check if player is on a special location
            # reach_surprise_location(game['players'], play_name, game['surprise_location'], play_order)
            if game['players'][play_name] in list(game['surprise_location']):
                sproll = special_roll()     # roll the special dice

                if sproll == 0:             # case 0: the current player gets to roll once again
                    play_order -= 1
                elif sproll == 1:           # case 1: the player after the current player loses a turn
                    play_order += 1
                    if play_order == len(game['players']):
                        play_order = 0
                else:                       # case 2: all other players on the board move back 5 spaces
                    for i in range(len(game['players'])):
                        if i != play_order:
                            if i == 0:
                                temp_name = 'Red'
                            elif i == 1:
                                temp_name = 'Blue'
                            elif i == 2:
                                temp_name = 'Green'
                            elif i == 3:
                                temp_name = 'White'
                            else:
                                pass
                            position_temp = game['players'][temp_name]
                            position_temp -= 5
                            # If moving back a player puts their position below 0, then place them back on 0
                            if position_temp < 0:
                                position_temp = 0
                            game['players'][temp_name] = position_temp
            play_order += 1

    return winner

def reach_snakes_or_ladders(player: dict, play_name: str, snakes_or_ladders: dict):
    '''
    When reach a snake or a ladder, moving from snake head to snake tail or from ladder base to ladder top
    Args:
        player(dict): The dictionary to store players
        play_name(str): The current player
        snakes_or_ladders(dict): The dictionary to store snakes and ladders
    '''
    if str(player[play_name]) in list(snakes_or_ladders.keys()):
        index = list(snakes_or_ladders.keys()).index(str(player[play_name]))
        player[play_name] = list(snakes_or_ladders.values())[index]


def reach_surprise_location(player: dict, play_name: str, surprise_location: dict, play_order: int):
    '''
    When reach the special position, according to the number of special dice to execute the different cases.
    Args:
        player(dict): The dictionary to store players
        play_name(str): The current player
        surprise_location(dict): The dictionary to store surprise locations
        play_order(int): The flag of the order of players
    '''
    if player[play_name] in list(surprise_location):
        sproll = special_roll()         # roll the special dice
        if sproll == 0:
            play_order -= 1

        elif sproll == 1:
            play_order += 1
            if play_order == len(player):
                play_order = 0

        else:
            for i in range(len(player)):
                if i != play_order:
                    if i == 0:
                        temp_name = 'Red'
                    elif i == 1:
                        temp_name = 'Blue'
                    elif i == 2:
                        temp_name = 'Green'
                    elif i == 3:
                        temp_name = 'White'
                    else:
                        pass
                    position_temp = player[temp_name]
                    position_temp -= 5
                    if position_temp < 0:
                        position_temp = 0
                    player[temp_name] = position_temp



def pick_winner(players: dict) -> str:
    ''' To pick the winner of the game.
    Args:
        players(dict): Initial the players.
    Returns:
        winner(str): return the winner in the 'players' dict.
    '''
    for k, v in players.items():
        if v == 100:
            winner = str(k)
            return winner
    else:
        return None



def turn_by_turn_gameplay():
    players = {'Red': 0, 'Blue': 0}
    snakes = {'25': 6, '44': 23, '65': 34, '76': 28, '99': 56}
    ladders = {'8': 43, '26': 39, '38': 55, '47': 81, '66': 92}
    game = {'players': players, 'snakes': snakes, 'ladders': ladders}

    surprise_location = generate_surprises()
    game['surprise_location'] = surprise_location
    print(game['surprise_location'])

    while all(x < 100 for x in list(game['players'].values())):
        play_order = 0
        while play_order < len(game['players']):
            # Roll the dice for the first player
            if play_order == 0:
                play_name = 'Red'
            elif play_order == 1:
                play_name = 'Blue'
            else:
                pass
            roll = input(f"当前是{play_name},输入roll摇骰子\n")
            while roll != 'roll' and roll != 'quit':
                roll = input(f"输入错误,请输入roll摇骰子\n")
            if roll == 'quit':
                game['players'][play_name] = 100
            diceroll = roll_the_dice()
            if roll != 'quit':
                print(f"骰子是{diceroll}")
                players_value = game['players'][play_name]
                players_value += diceroll
                if players_value > 100:
                    players_value -= diceroll
                game['players'][play_name] = players_value
            if roll != 'quit':
                print("当前玩家加骰子的值是", game['players'][play_name])

            if game['players'][play_name] == 100:
                winner = play_name
                break

            # Check if player 1 is either on a snake head or ladder Base
            if str(game['players'][play_name]) in list(game['snakes'].keys()):
                index = list(game['snakes'].keys()).index(str(game['players'][play_name]))
                game['players'][play_name] = list(game['snakes'].values())[index]
                print(f" {play_name} 踩到蛇了，现在是 {game['players'][play_name]}")

            if str(game['players'][play_name]) in list(game['ladders'].keys()):
                index = list(game['ladders'].keys()).index(str(game['players'][play_name]))
                game['players'][play_name] = list(game['ladders'].values())[index]
                print(f" {play_name} 踩到梯子了，现在是 {game['players'][play_name]}")

            if game['players'][play_name] in list(game['surprise_location']):
                print(f"{play_name} 进入了能量瓷砖")
                sproll = special_roll()
                print("超级骰子是", sproll)
                if sproll == 0:
                    play_order -= 1

                elif sproll == 1:
                    print(f"超级骰子为1,跳过下一个玩家")
                    play_order += 1
                    if play_order == len(game['players']):
                        play_order = 0

                else:
                    print(game['players'])
                    for i in range(len(game['players'])):
                        if i != play_order:
                            if i == 0:
                                temp_name = 'Red'
                            elif i == 1:
                                temp_name = 'Blue'
                            elif i == 2:
                                temp_name = 'Green'
                            elif i == 3:
                                temp_name = 'White'
                            else:
                                pass
                            position_temp = game['players'][temp_name]
                            position_temp -= 5
                            if position_temp < 0:
                                position_temp = 0
                            game['players'][temp_name] = position_temp
                    print(game['players'],"减5后的位置")

            play_order += 1

    if roll == 'quit':
        return print("游戏结束")
    else:
        return print(f"获胜的玩家是{winner}")



def main():
    '''
    The main function to run the game. Call the initialization, game execution, winner picking functions.
    '''
    game = initialise_game()
    num_players = get_num_players()
    winner = play_game(game)
    print(f"The winner is {winner}!")
    # Play a turn by turn game
    turn_by_turn_gameplay()


if __name__ == '__main__':
    main()