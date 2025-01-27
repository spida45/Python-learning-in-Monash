'''
Task 4 - Implementing Turns! (12%)
Okay! Now that you know how loops work, we can finally complete at least one whole game of Snakes and Ladders!

For this task, we are restricting where you can place the Snakes and Ladders, so please follow along:

NOTE: Please use the same variables names in this task as you did in the previous ones.

Snake Heads will be placed on: 25, 44, 65, 76, 99

Snake Tails will be placed on: 6, 23, 34, 28, 56

Ladder Bases will be placed on: 8, 26, 38, 47, 66

Ladder Tops will be placed on: 43, 39, 55, 81, 92

Your job in this task is to implement a game of Snakes and Ladders between two players until one reaches the end.

Here are the basic steps to implement the game:

1. Initialise the two players (Red and Blue), and the snakes and ladders as per the specifications provided above.

2. Commence a game of Snakes and Ladders with the Red player rolling the dice first.

3. Follow the rules of moving the player and changing their position based on the positions of the snakes and ladders. Print the position of the players after each turn separated by a \n, for example:

Player Red is in position 12
Player Blue is in position 25
4. Print statements when a player hits a snake or a ladder:

Player Red stepped on a snake and is now in position 24
Player Blue climbed a ladder and is now in position 67
5. Once one player reaches 100, the game is over and you need to save the winning player's name in a variable called winner. You should then also print out a message declaring the winner.

For example, if Red wins:

Player Red has reached 100 and is the winner!
Ensure that a player cannot CROSS 100. If the player rolls a dice number that will make them cross 100, then ignore that dice roll and move on to the second player.
For example:
Player Red is on 96
Player Blue is on 99

Player Red rolls a 5, and hence, their dice roll is ignored.
The dice is then rolled for Player Blue and they roll a 1 and win the game.

Another note is that the other player should not get to roll again if one player has already won!
For example:
Player Red is on 96
Player Blue is on 99

Player Red rolls a 4, and hence, wins the game.
The dice is not rolled for Player Blue as Red has already won the game.

There are a couple of tests given to you to check the validity of your code.
'''

# DO NOT delete this line
from diceroll import roll_the_dice
import random

# Initialise the players
p1_name = "Red"
p2_name = "Blue"

p1_position = 0
p2_position = 0

# Initialise the snakes and ladders
# Snake Positions
def generate_snake_list(length):
    heads = [random.randint(1, 100) for _ in range(length)]
    tails = [random.randint(1, heads[i]) for i in range(length)]
    return heads, tails

length_snake = 5
snake_heads, snake_tails = generate_snake_list(length_snake)

# Ladder Positions
def generate_ladder_list(length):
    bases = [random.randint(1, 100) for _ in range(length)]
    tops = [random.randint(bases[i], 100) for i in range(length)]
    return bases, tops

length_ladder = 5
ladder_bases, ladder_tops = generate_ladder_list(length_ladder)

'''
# Check if player 1 is either on a snake head or ladder Base
if p1_position in snake_heads:
    index = snake_heads.index(p1_position)
    p1_position = snake_tails[index]

if p1_position in ladder_bases:
    index = ladder_bases.index(p1_position)
    p1_position = ladder_tops[index]

# Check if player 2 is either on a snake head or ladder Base
if p2_position in snake_heads:
    index = snake_heads.index(p2_position)
    p2_position = snake_tails[index]

if p2_position in ladder_bases:
    index = ladder_bases.index(p2_position)
    p2_position = ladder_tops[index]
'''

# Commence the game & Announce the winner
while p1_position < 100 and p2_position < 100:
    # Roll the dice for the first player
    diceroll = roll_the_dice()

    # Write the logic to move the first player
    p1_position += diceroll

    # Check if player 1 is either on a snake head or ladder Base
    if p1_position in snake_heads:
        index = snake_heads.index(p1_position)
        p1_position = snake_tails[index]
        print(f"Player {p1_name} stepped on a snake and is now in position {p1_position}")

    if p1_position in ladder_bases:
        index = ladder_bases.index(p1_position)
        p1_position = ladder_tops[index]
        print(f"Player {p1_name} climbed a ladder and is now in position {p1_position}")

    '''
    if p1_position == 100:
        print(f"Player {p1_name} has reached 100 and is the winner!")
        break
    else:
        p1_position -= diceroll
    '''

    if p1_position >= 100:
        p1_position -= diceroll
    elif p1_position == 100:
        print(f"Player {p1_name} has reached 100 and is the winner!")
        break
    else:
        p1_position = p1_position

    # Roll the dice for the second player
    diceroll = roll_the_dice()

    # Write the logic to move the second player
    p2_position += diceroll

    # Check if player 2 is either on a snake head or ladder Base
    if p2_position in snake_heads:
        index = snake_heads.index(p2_position)
        p2_position = snake_tails[index]
        print(f"Player {p2_name} stepped on a snake and is now in position {p2_position}")

    if p2_position in ladder_bases:
        index = ladder_bases.index(p2_position)
        p2_position = ladder_tops[index]
        print(f"Player {p2_name} climbed a ladder and is now in position {p2_position}")

    if p2_position >= 100:
        p2_position -= diceroll
    elif p2_position == 100:
        print(f"Player {p2_name} has reached 100 and is the winner!")
        break
    else:
        p2_position = p2_position

    print(f"Player {p1_name} is in position {p1_position}\nPlayer {p2_name} is in position {p2_position}")






