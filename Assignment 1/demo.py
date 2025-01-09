from diceroll import roll_the_dice, special_roll
from helpers import generate_surprises

game = {
        'p_name': ["Red", "Blue", "Green", "White"],
        'p_position': [0, 0, 0, 0],
        'snake_heads': [25, 44, 65, 76, 99],
        'snake_tails':[6, 23, 34, 28, 56],
        'ladder_bases': [8, 26, 38, 47, 66],
        'ladder_tops': [43, 39, 55, 81, 92]
    }

# call the function of generating surprise
special_tiles = generate_surprises()

# add special_tiles into dict game
game.update({'special_tiles': special_tiles})

print(game)