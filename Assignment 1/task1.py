'''
Task 1 - Setting Up the Game Environment (8%)
In this task, we will define the game board and the 2 players that will play the game.

You will need to figure out the type of variable that will be suitable for each of the following parts of the game:

Player 1 name - We will be setting one of these 4 colors as player 1's name: Red, Blue, Green, White

Player 1 position - This will store the current position where the player sits. When the game starts, the position for all players will be 0.

Duplicate these for Player 2.

Snake-head positions - This will be a collection of positions where snake-heads are located. In this task, you will need to randomly choose 5 locations where snakes will be placed. When a player reaches this position, they will end up at the corresponding tail position.

Snake-tail positions - This will be a collection of positions where snake-tails are located. These are the places where the player ends up if they step on a snake head. Please be aware that snake tails need to be at a position less than their corresponding heads.

Ladder-base positions - This will be a collection of positions where ladder bases are located. In this task, you will need to randomly choose 5 locations where ladders will be placed. When a player reaches this position, they will end up at the corresponding ladder top position.

Ladder-top positions - This will be a collection of positions where ladder tops are located. These are the places where the player ends up if they step on a ladder base. Please be aware that ladder tops need to be at a position more than their corresponding heads.

You CANNOT have more than one item on a tile. For example - if a snake head is placed on position 5, another snake head/ snake tail/ ladder base/ ladder top CANNOT be placed on position 5.

Next, print the players' names and their corresponding positions in the following format:

Player <playername> is in position <position>
For example; if player Red is in position 0 at the start of the game, then the following string will print:

Player Red is in position 0
'''

import random
# Player 1 Name
p1_name = input("Please input Player1 name:")

# Player 1 Position
p1_position = 0

# Player 2 Name
p2_name = input("Please input Player2 name:")

# Player 2 Position
p2_position = 0

# Snake Head Positions
def generate_snake_list(length):
    heads = [random.randint(1, 100) for _ in range(length)]
    tails = [random.randint(1, heads[i]) for i in range(length)]
    return heads, tails

length_snake = 5
snake_heads, snake_tails = generate_snake_list(length_snake)

# Snake Tail Positions
#snake_tails =
print("snake_heads", snake_heads)
print("snake_tails", snake_tails)


# Ladder Base Positions
def generate_ladder_list(length):
    bases = [random.randint(1, 100) for _ in range(length)]
    tops = [random.randint(bases[i], 100) for i in range(length)]
    return bases, tops

length_ladder = 5
ladder_bases, ladder_tops = generate_ladder_list(length_ladder)

# Ladder Tops Positions
#ladder_tops =
print("ladder_bases", ladder_bases)
print("ladder_tops", ladder_tops)

# Print the position for Player 1
print("Player", p1_name, "is in position", p1_position)

# Print the position for Player 2
print("Player", p2_name, "is in position", p2_position)
