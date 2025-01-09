from diceroll import roll_the_dice, special_roll
from helpers import generate_surprises

def reach_snakes(player: dict, play_name: str, snakes: dict):
    if str(player[play_name]) in list(snakes.keys()):
        index = list(snakes.keys()).index(str(player[play_name]))
        player[play_name] = list(snakes.values())[index]

def surprise_location(player: dict, play_name: str, surprise_location: dict, play_order: int):
    if player[play_name] in list(surprise_location):
        # print(f"{play_name} 进入了能量瓷砖")
        sproll = special_roll()
        # print("超级骰子是", sproll)
        if sproll == 0:
            play_order -= 1

        elif sproll == 1:
            # print(f"超级骰子为1,跳过下一个玩家")
            play_order += 1
            if play_order == len(player):
                play_order = 0

        else:
            # print(game['players'])
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


surprise_location(game['players'], play_name, game['surprise_location'], play_order)