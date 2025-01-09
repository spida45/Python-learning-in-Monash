'''
Task 3 - Handling Chutes and Ladders (12%)
In this task, we are going to handle the player landing on snakes or ladders.

You are going to need conditional statements to figure out where a player needs to land and how to update their position.

Here are the steps to follow:

Copy and paste all the code from Task 2 (except the print statements at the end).

While checking the final position after the dice roll, check if the player lands on either a snake head or a ladder base.

If they do, change their position to the corresponding snake tail or ladder top.

Save the new position as the p1_position or p2_position as appropriate.

Run the tests to make sure your logic is airtight.
'''

# Copy and paste everything from Task2
# DO NOT delete this line
from diceroll import roll_the_dice
import random

# Copy and paste the work from Task 1 here
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


# Task 2 begins here

# Roll the dice for the first player
diceroll = roll_the_dice()

# Write the logic to move the first player
p1_position += diceroll

# Roll the dice for the second player
diceroll = roll_the_dice()

# Write the logic to move the second player
p2_position += diceroll



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

# Update the positions if required


# Print the position of player 1
print("Player", p1_name, "is in position", p1_position)

# Print the position of player 2
print("Player", p2_name, "is in position", p2_position)